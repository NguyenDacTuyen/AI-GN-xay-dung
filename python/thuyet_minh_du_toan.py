# -*- coding: utf-8 -*-
"""
Lập THUYẾT MINH DỰ TOÁN theo mẫu công ty template/du-toan/tong-hop/thuyet-minh-du-toan.docx
(chép ra bản mới, không sửa mẫu), cho dự án một hoặc nhiều hạng mục.

- Tên dự án, hạng mục, văn bản riêng của dự án, người ký, đường dẫn file: lấy từ FILE KHAI BÁO DỰ ÁN
  (mẫu: python/mau-khai-bao-du-an.ini).
- Số liệu chi phí đọc từ file TỔNG HỢP (lập bằng python/tong_hop_du_toan.py), Excel tính lại trước khi đọc,
  nên thuyết minh luôn khớp file tổng hợp. Có kiểm tra chi phí xây dựng file tổng hợp khớp tổng các file hạng mục.
  Trình tự khi sửa dự toán: chạy lại tong_hop_du_toan.py rồi chạy chương trình này.
- Giữ định dạng của mẫu: mỗi đoạn được thay chữ nhưng giữ nguyên định dạng đoạn và định dạng chữ của mẫu.
- Chỗ chưa có thông tin (khai báo để trống) ghi "......" và TÔ VÀNG.

Chạy:  python python/thuyet_minh_du_toan.py <file khai báo>
  ví dụ: python python/thuyet_minh_du_toan.py ket-qua/be-tu-hoai-10m3/khai-bao-du-an.ini
"""
import os, re, sys, tempfile, zipfile

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAU = os.path.join(GOC, "template", "du-toan", "tong-hop", "thuyet-minh-du-toan.docx")
sys.path.insert(0, os.path.join(GOC, "python"))
import khai_bao
from khai_bao import CHO_TRONG
from chuyen_f1_ve_mau import bang_chu             # đọc số thành chữ (dùng chung)
from tong_hop_du_toan import loai_cong_trinh, TEN_TH_HM  # loại công trình tra TT38; tên sheet tổng hợp

VANG = "VANG"   # đánh dấu đoạn chữ cần tô vàng
CONG_TY = "Công ty cổ phần Tư vấn Đầu tư Xây dựng Gia Nguyễn"


# ------------------------------------------------------------------ số liệu từ file dự toán
def mo_excel(path, sheet):
    """Mở bằng Excel (chỉ đọc), tính lại, trả về sheet giá trị (sheet: tên, hoặc danh sách tên để chọn tên có trong file)."""
    import win32com.client
    import openpyxl
    tam = os.path.join(tempfile.gettempdir(), "tm_" + os.path.basename(path))
    if os.path.exists(tam):
        os.remove(tam)
    xl = win32com.client.DispatchEx("Excel.Application")
    xl.Visible = False
    xl.DisplayAlerts = False
    try:
        wb = xl.Workbooks.Open(path, 0, True)
        xl.CalculateFull()
        wb.SaveAs(tam, 51)
        wb.Close(False)
    finally:
        xl.Quit()
    wb = openpyxl.load_workbook(tam, data_only=True)
    return wb[sheet if isinstance(sheet, str) else next(t for t in sheet if t in wb.sheetnames)]


def doc_hang_muc(path):
    ws = mo_excel(path, TEN_TH_HM)
    return {ws[f"C{r}"].value: ws[f"E{r}"].value for r in range(6, ws.max_row + 1) if ws[f"C{r}"].value}


def doc_tong_hop(path):
    """Giá trị sau thuế (cột I) theo ký hiệu (cột C) của bảng tổng hợp, thêm tổng làm tròn và tỷ lệ dự phòng."""
    ws = mo_excel(path, "TH TMDT")
    v = {}
    for r in range(7, ws.max_row + 1):
        kh, ten = ws[f"C{r}"].value, str(ws[f"B{r}"].value or "")
        if kh:
            v[kh] = ws[f"I{r}"].value or 0
            if kh == "GDP1":
                v["TL_DP"] = ws[f"D{r}"].value
        if ten.startswith("Tổng cộng (làm tròn)"):
            v["LAM"] = ws[f"I{r}"].value
    return v


def so(x):
    return f"{round(x):,}".replace(",", ".")


def pct(x):
    return f"{x * 100:g}".replace(".", ",") + "%"


def ty_le_hang_muc(v):
    """Tỷ lệ chi phí chung, không xác định khối lượng, thu nhập chịu thuế, VAT, nhà tạm suy từ số liệu hạng mục."""
    vat = round(v["GTGT"] / v["G"], 4)
    return (round(v["C"] / v["T"], 4), round(v["TT"] / v["T"], 4), round(v["TL"] / (v["T"] + v["GT"]), 4),
            vat, round(v["LT"] / (v["G"] * (1 + vat)), 4))


# ------------------------------------------------------------------ sửa XML theo đoạn
def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def to_vang(rpr):
    if "<w:highlight" in rpr:
        return rpr
    if "</w:szCs>" in rpr or "<w:szCs " in rpr:
        return re.sub(r"(<w:szCs [^>]*/>)", r'\1<w:highlight w:val="yellow"/>', rpr, count=1)
    if "<w:lang " in rpr:
        return rpr.replace("<w:lang ", "<w:highlight w:val=\"yellow\"/><w:lang ", 1)
    return rpr.replace("</w:rPr>", "<w:highlight w:val=\"yellow\"/></w:rPr>")


def runs_rpr(p):
    """Danh sách rPr của các run có chữ trong đoạn."""
    out = []
    for r in re.findall(r"<w:r[ >].*?</w:r>", p, re.S):
        m = re.search(r"<w:rPr>.*?</w:rPr>", r, re.S)
        out.append(m.group(0) if m else "<w:rPr></w:rPr>")
    return out


def dat_chu(p, doan):
    """Thay nội dung đoạn p. doan = list các phần: (chữ, chỉ số run mẫu lấy định dạng[, VANG]) hoặc 'BR'."""
    mo = re.match(r"<w:p[ >][^>]*>|<w:p>", p).group(0)
    ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S)
    ppr = ppr.group(0) if ppr else ""
    rp = runs_rpr(p) or ["<w:rPr></w:rPr>"]
    ra = []
    for d in doan:
        if d == "BR":
            ra.append(f"<w:r>{rp[0]}<w:br/></w:r>")
            continue
        chu, i = d[0], min(d[1], len(rp) - 1)
        r = rp[i]
        if len(d) > 2 and d[2] == VANG:
            r = to_vang(r)
        ra.append(f'<w:r>{r}<w:t xml:space="preserve">{esc(chu)}</w:t></w:r>')
    return mo + ppr + "".join(ra) + "</w:p>"


def hoac(gia_tri, cho_trong, i=0):
    """Phần chữ: có thông tin thì ghi bình thường, chưa có thì ghi chỗ trống và tô vàng."""
    return (gia_tri, i) if gia_tri else (cho_trong, i, VANG)


def can_cu(gia_tri):
    """Bỏ chữ "Căn cứ" anh đã gõ sẵn ở đầu (chương trình tự thêm)."""
    return re.sub(r"^căn cứ\s+", "", gia_tri.strip(), flags=re.I).rstrip(";.")


def main():
    kb = khai_bao.doc()
    KQ = kb.file_thuyet_minh
    if os.path.exists(KQ):
        raise SystemExit(f"File đã có, không ghi đè: {KQ}")
    ds_hm = [(h, doc_hang_muc(h.file_du_toan)) for h in kb.hang_muc]
    v = doc_tong_hop(kb.file_tong_hop)
    loai = loai_cong_trinh(ds_hm)[0].lower()    # theo hạng mục có chi phí xây dựng trước thuế lớn nhất
    GXD, QLDA, TV, CK, DP, TMDT, LAM = v["GXD"], v["GQLDA"], v["GTV"], v["GK"], v["GDP"], v["TMĐT"], v["LAM"]
    GDD = v.get("GDD", 0)                # chi phí di dời (nếu có khai báo)
    giao_thong = any(h.linh_vuc == "giao-thong" for h in kb.hang_muc)
    tong_hm = sum(x["Tdt"] for _, x in ds_hm)
    assert abs(GXD - tong_hm) < 1, f"Chi phí xây dựng file tổng hợp ({GXD}) khác tổng các file hạng mục ({tong_hm})"
    assert abs(GXD + QLDA + TV + CK + DP + GDD - TMDT) < 2, "số liệu tổng hợp không cộng khớp"
    tl_dp = pct(v["TL_DP"])
    ten_hm = "; ".join(h.ten for h, _ in ds_hm)
    hm_ban_ve = "; ".join(f"{h.ten}" + (f" (bản vẽ {h.ky_hieu})" if h.ky_hieu else "") for h, _ in ds_hm)

    z = zipfile.ZipFile(MAU)
    x = z.read("word/document.xml").decode("utf-8")
    hd = z.read("word/header1.xml").decode("utf-8")

    vt = [(m.start(), m.end()) for m in re.finditer(r"<w:p[ >].*?</w:p>", x, re.S)]
    P = [x[a:b] for a, b in vt]
    assert len(P) == 131, len(P)
    txt = lambda i: "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", P[i]))
    # Kiểm tra đúng mẫu (tránh sửa nhầm khi mẫu đổi)
    for i, s in ((8, "CÁC CỨN CỨ"), (60, "4570"), (90, "TỔNG MỨC ĐẦU TƯ"), (130, "TRẦN PHÚ THẠNH")):
        assert s in txt(i), (i, txt(i))

    moi = {}            # chỉ số đoạn -> XML mới (None = xóa)
    them_sau = {}       # chỉ số đoạn -> list XML chèn sau

    moi[2] = dat_chu(P[2], [("Số: ", 0), hoac(kb.so_van_ban, CHO_TRONG), (f"/TMDT.GN_{kb.nam}", 0)])
    moi[5] = dat_chu(P[5], [("THUYẾT MINH DỰ TOÁN", 0), "BR", ("Công trình: ", 2),
                            hoac(kb.ten_du_an, CHO_TRONG * 6 + " (anh bổ sung)", 2)])
    moi[6] = dat_chu(P[6], [(f"Hạng mục: {ten_hm}", 0)])
    them_sau[6] = [dat_chu(P[6], [("Địa điểm: ", 0), hoac(kb.dia_diem, CHO_TRONG * 4), (f" – {kb.tinh_thanh}", 0)])]
    moi[8] = dat_chu(P[8], [("CÁC CĂN CỨ LẬP DỰ TOÁN:", 0)])
    moi[9] = dat_chu(P[9], [("Khối lượng: ", 0), (
        f"Theo bảng chi tiết khối lượng lập từ hồ sơ thiết kế bản vẽ thi công hạng mục {hm_ban_ve} "
        f"do {CONG_TY} lập.", 1)])
    # Bộ đơn giá cũ (QĐ 2966/2023, 1491/2024, 959/2025): luôn bỏ, vì đơn giá lập trực tiếp trên F1.
    # Văn bản riêng ngành đường bộ (NĐ 165/2024, QĐ 38/QĐ-GT, CV 2424/SGTVT, QĐ 1762/QĐ-SGTVT):
    # giữ khi dự án có hạng mục giao thông, bỏ khi chỉ có hạ tầng kỹ thuật.
    for i in (57, 58, 59) + (() if giao_thong else (32, 51, 53, 54)):
        moi[i] = None
    # Quy hoạch, chủ trương, hợp đồng: riêng của từng dự án (mẫu là của dự án KP8-15)
    moi[62] = dat_chu(P[62], [(f"Căn cứ {can_cu(kb.van_ban_quy_hoach)};", 0)] if kb.van_ban_quy_hoach else
                      [("Căn cứ ...... (văn bản quy hoạch liên quan, nếu có - anh bổ sung);", 0, VANG)])
    moi[64] = dat_chu(P[64], [(f"Căn cứ {can_cu(kb.van_ban_chu_truong)};", 0)] if kb.van_ban_chu_truong else
                      [("Căn cứ ...... (quyết định phê duyệt chủ trương đầu tư / phê duyệt dự án - anh bổ sung);", 0, VANG)])
    moi[65] = dat_chu(P[65], [(f"Căn cứ {can_cu(kb.hop_dong_tu_van)};", 0)] if kb.hop_dong_tu_van else
                      [(f"Căn cứ hợp đồng tư vấn số ...... ngày ...... giữa ...... và {CONG_TY} (anh bổ sung);", 0, VANG)])
    for i in range(66, 74):
        moi[i] = None
    moi[75] = dat_chu(P[75], [(f"Hồ sơ thiết kế bản vẽ thi công hạng mục {hm_ban_ve} do {CONG_TY} lập;", 0)])
    moi[76] = dat_chu(P[76], [(f"{kb.ho_so_khao_sat.rstrip(';.')};", 0)] if kb.ho_so_khao_sat else
                      [("Hồ sơ khảo sát địa chất khu vực xây dựng ...... (anh bổ sung, nếu có);", 0, VANG)])
    cuoc = (f"; vật liệu lấy tại mỏ (đá, cát) cộng cước vận chuyển bằng ô tô tự đổ 10 tấn, cự ly {kb.cu_ly_km} km;"
            if kb.cu_ly_km else ";")
    moi[77] = dat_chu(P[77], [
        ("Giá vật liệu theo công bố giá vật liệu xây dựng ", 0), hoac(kb.thoi_diem_gia_vl, CHO_TRONG),
        (f" của Sở Xây dựng {kb.tinh_thanh} (Thông báo số ", 0),
        hoac(kb.so_thong_bao_gia, "...... - anh kiểm tra đúng số thông báo giá"),
        ("), lấy mức giá cao nhất trong công bố" + cuoc, 0)])
    moi[78] = dat_chu(P[78], [("Giá nhiên liệu theo dữ liệu phần mềm Dự toán F1 ", 0),
                              ("(anh kiểm tra ngày công bố giá nhiên liệu Petrolimex áp dụng)", 0, VANG), (";", 0)])
    moi[82] = dat_chu(P[82], [
        ("Đơn giá xây dựng chi tiết lập theo phương pháp tính trực tiếp trên phần mềm Dự toán F1: định mức theo ", 0),
        hoac(kb.dinh_muc, CHO_TRONG), ("; giá nhân công theo ", 0), hoac(kb.gia_nhan_cong, CHO_TRONG),
        ("; giá ca máy xác định theo phương pháp tại ", 0), hoac(kb.gia_ca_may, CHO_TRONG),
        ("; giá vật liệu theo công bố giá ", 0), hoac(kb.thoi_diem_gia_vl, CHO_TRONG),
        (" (giá cao nhất)" + (" cộng cước vận chuyển." if kb.cu_ly_km else ".") +
         (f" {kb.cong_tac_tuong_tu}" if kb.cong_tac_tuong_tu else ""), 0)])
    moi[85] = dat_chu(P[85], [("Tổng dự toán được lập theo hướng dẫn của Thông tư 36/2026/TT-BXD. Cụ thể như sau:", 0)])
    tl = {ty_le_hang_muc(x) for _, x in ds_hm}
    if len(tl) == 1:                     # các hạng mục cùng tỷ lệ: ghi cụ thể
        C, TT, TL, VAT, LT = tl.pop()
        ty_le = (f"chi phí chung bằng {pct(C)} và chi phí một số công việc không xác định được khối lượng từ thiết kế "
                 f"bằng {pct(TT)} chi phí trực tiếp; thu nhập chịu thuế tính trước bằng {pct(TL)} (chi phí trực tiếp + "
                 f"chi phí gián tiếp); thuế giá trị gia tăng {pct(VAT)}. Chi phí nhà tạm để ở và điều hành thi công "
                 f"bằng {pct(LT)} chi phí xây dựng trước thuế, đã gồm thuế giá trị gia tăng.")
    else:
        ty_le = ("chi phí chung và chi phí một số công việc không xác định được khối lượng từ thiết kế tính bằng tỷ lệ % "
                 "chi phí trực tiếp; thu nhập chịu thuế tính trước, thuế giá trị gia tăng, chi phí nhà tạm để ở và điều "
                 "hành thi công theo tỷ lệ của từng hạng mục (xem dự toán hạng mục).")
    moi[86] = dat_chu(P[86], [("Chi phí xây dựng gồm: chi phí trực tiếp (vật liệu, nhân công, máy thi công); "
                               "chi phí gián tiếp gồm " + ty_le, 0)])
    them_sau[86] = [dat_chu(P[86], [(
        "Chi phí quản lý dự án, chi phí tư vấn đầu tư xây dựng, chi phí khác tính theo tỷ lệ % trên chi phí xây dựng "
        f"theo Thông tư 38/2026/TT-BXD ({loai}, loại công trình của hạng mục có chi phí xây dựng lớn nhất; tỷ lệ nội suy "
        "theo tổng chi phí xây dựng trước thuế của dự án); chi phí thẩm định hồ sơ mời thầu, kết quả lựa chọn nhà thầu theo Nghị định 214/2025/NĐ-CP; phí "
        "thẩm định dự án theo Thông tư 28/2023/TT-BTC; chi phí bảo hiểm công trình theo Nghị định 67/2023/NĐ-CP, Nghị "
        "định 220/2026/NĐ-CP; phí thẩm định dự toán xây dựng theo Thông tư 27/2023/TT-BTC, Thông tư 64/2025/TT-BTC; "
        "chi phí kiểm toán độc lập, thẩm tra phê duyệt quyết toán theo "
        "Nghị định 193/2026/NĐ-CP; chi phí kiểm tra công tác nghiệm thu theo Thông tư 10/2021/TT-BXD. "
        "Chi tiết xem bảng tổng hợp dự toán đính kèm.", 0)])]
    # Khoản tạm tính anh khai báo (đảm bảo giao thông, di dời): ghi rõ là tạm tính, tô vàng phần căn cứ chờ bổ sung
    tam_tinh = ([f"chi phí đảm bảo an toàn giao thông phục vụ thi công {so(kb.dam_bao_giao_thong)} đồng (trước thuế)"]
                if kb.dam_bao_giao_thong else []) + ([f"{kb.ten_di_doi.lower()} {so(GDD)} đồng"] if GDD else [])
    if tam_tinh:
        them_sau[86].append(dat_chu(P[86], [("Các khoản tạm tính: " + "; ".join(tam_tinh) + " ", 0),
                                            ("(anh bổ sung căn cứ)", 0, VANG), (".", 0)]))
    moi[88] = dat_chu(P[88], [(
        f"Dự phòng cho yếu tố phát sinh khối lượng công việc được tính bằng {tl_dp} tổng chi phí xây dựng, chi phí "
        "quản lý dự án, chi phí tư vấn đầu tư xây dựng và chi phí khác.", 0)])
    them_sau[88] = [dat_chu(P[88], [("Dự phòng cho yếu tố trượt giá: không tính, ", 0),
                                    hoac(f"do {kb.ly_do_truot_gia}" if kb.ly_do_truot_gia else "",
                                         "do ...... (anh xác nhận lý do)"), (".", 0)])]
    moi[92] = dat_chu(P[92], [("Xem bảng chi tiết khối lượng công tác xây dựng đính kèm", 0)])
    moi[94] = dat_chu(P[94], [("Tổng mức đầu tư: ", 0), (f"{so(LAM)} đồng", 0),
                              (" (đã làm tròn; xem bảng tổng hợp dự toán đính kèm)", 0)])
    moi[95] = dat_chu(P[95], [(f"(Bằng chữ: {bang_chu(LAM).replace('./.', '')}).", 0)])
    # Bảng chi tiết mẫu: 6 dòng x (tên, ":", số tiền, "đồng") ở các đoạn 97..120.
    # Điền lần lượt các khoản dự án có; dòng thừa xóa (chưa hỗ trợ chi phí bồi thường, hỗ trợ và tái định cư).
    dong = [("Chi phí xây dựng", GXD), ("Chi phí quản lý dự án", QLDA), ("Chi phí tư vấn đầu tư xây dựng", TV),
            ("Chi phí khác", CK), ("Chi phí dự phòng", DP)]
    if GDD:
        dong.append((f"{kb.ten_di_doi} (tạm tính)", GDD))
    for k in range(6):
        if k < len(dong):
            moi[97 + 4 * k] = dat_chu(P[97 + 4 * k], [(dong[k][0], 0)])
            moi[99 + 4 * k] = dat_chu(P[99 + 4 * k], [(f" {so(dong[k][1])} ", 0)])
        else:
            for i in range(97 + 4 * k, 101 + 4 * k):
                moi[i] = "XOA_DONG_BANG"
    moi[130] = dat_chu(P[130], [("                              ", 0), hoac(kb.nguoi_lap, "(Họ tên người lập)"),
                                ("                                                                                     ", 0),
                                hoac(kb.giam_doc, "(Họ tên Giám đốc)")])

    # Ghép lại
    out, cuoi = [], 0
    for i, (a, b) in enumerate(vt):
        out.append(x[cuoi:a])
        if i in moi:
            if moi[i] is not None:
                out.append(moi[i])
        else:
            out.append(P[i])
        out.extend(them_sau.get(i, []))
        cuoi = b
    out.append(x[cuoi:])
    x2 = "".join(out)
    # Xóa cả dòng bảng có đánh dấu (ô bảng không được để trống đoạn nên xóa cả dòng <w:tr>)
    x2 = re.sub(r"<w:tr[ >](?:(?!</w:tr>).)*XOA_DONG_BANG(?:(?!</w:tr>).)*</w:tr>", "", x2, flags=re.S)
    assert "XOA_DONG_BANG" not in x2

    # Đầu trang: tên ngắn (nếu khai báo), không thì tên dự án; chưa có tên dự án mà chỉ 1 hạng mục thì ghi tên hạng mục
    if kb.ten_dau_trang:
        nhan, ten_dau = ("Dự án: " if kb.ten_du_an or len(ds_hm) > 1 else "Hạng mục: "), kb.ten_dau_trang
    elif kb.ten_du_an:
        nhan, ten_dau = "Dự án: ", kb.ten_du_an
    elif len(ds_hm) == 1:
        nhan, ten_dau = "Hạng mục: ", ds_hm[0][0].ten
    else:
        nhan, ten_dau = "Dự án: ", CHO_TRONG
    hd2 = hd.replace(">Dự án: <", f">{esc(nhan)}<", 1).replace(
        ">Nâng cấp, mở rộng đường KP18-15<", f">{esc(ten_dau)}<", 1)

    with zipfile.ZipFile(KQ, "w", zipfile.ZIP_DEFLATED) as zo:
        for it in z.infolist():
            if it.filename == "word/document.xml":
                zo.writestr(it, x2.encode("utf-8"))
            elif it.filename == "word/header1.xml":
                zo.writestr(it, hd2.encode("utf-8"))
            else:
                zo.writestr(it, z.read(it.filename))
    print("Đã lập:", KQ)
    print(f"GXD={so(GXD)} QLDA={so(QLDA)} TV={so(TV)} K={so(CK)} DP={so(DP)} TMĐT={so(TMDT)} Làm tròn={so(LAM)}")
    print(bang_chu(LAM))


if __name__ == "__main__":
    main()

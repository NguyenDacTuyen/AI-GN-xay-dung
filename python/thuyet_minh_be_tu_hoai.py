# -*- coding: utf-8 -*-
"""
Lập THUYẾT MINH DỰ TOÁN dự án có hạng mục Bể tự hoại 10 m³ (GN2026-HT-01) theo mẫu công ty
template/du-toan/tong-hop/thuyet-minh-du-toan.docx (chép ra bản mới, không sửa mẫu).

- Số liệu chi phí đọc từ file TỔNG HỢP ket-qua/be-tu-hoai-10m3/du-toan_tong-hop.xlsx (lập bằng
  python/tong_hop_be_tu_hoai.py), Excel tính lại trước khi đọc, nên thuyết minh luôn khớp file tổng hợp.
  Có kiểm tra chi phí xây dựng trong file tổng hợp khớp file dự toán hạng mục.
  Trình tự khi sửa dự toán: chạy lại tong_hop_be_tu_hoai.py rồi chạy chương trình này.
- Giữ định dạng của mẫu: mỗi đoạn được thay chữ nhưng giữ nguyên định dạng đoạn và định dạng chữ của mẫu.
- Chỗ chưa có thông tin (tên công trình, văn bản pháp lý riêng của dự án, người ký...) để "......" và TÔ VÀNG.

Chạy:  python python/thuyet_minh_be_tu_hoai.py
"""
import os, re, shutil, sys, tempfile, zipfile

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAU = os.path.join(GOC, "template", "du-toan", "tong-hop", "thuyet-minh-du-toan.docx")
DT = os.path.join(GOC, "ket-qua", "be-tu-hoai-10m3", "du-toan_be-tu-hoai-10m3_TT38-HCM.xlsx")
TH = os.path.join(GOC, "ket-qua", "be-tu-hoai-10m3", "du-toan_tong-hop.xlsx")
KQ = os.path.join(GOC, "ket-qua", "be-tu-hoai-10m3", "thuyet-minh-du-toan_tong-hop.docx")
sys.path.insert(0, os.path.join(GOC, "python"))
from chuyen_f1_ve_mau_ha_tang import bang_chu      # đọc số thành chữ (dùng chung)

HANG_MUC = "Bể tự hoại BTCT 3 ngăn, dung tích hữu ích 10 m³"
VANG = "VANG"   # đánh dấu đoạn chữ cần tô vàng


# ------------------------------------------------------------------ số liệu từ file dự toán
def mo_excel(path, sheet):
    """Mở bằng Excel (chỉ đọc), tính lại, trả về sheet giá trị."""
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
    return openpyxl.load_workbook(tam, data_only=True)[sheet]


def doc_hang_muc():
    ws = mo_excel(DT, "Tổng hợp dự toán")
    return {ws[f"C{r}"].value: ws[f"E{r}"].value for r in range(6, ws.max_row + 1) if ws[f"C{r}"].value}


def doc_tong_hop():
    """Giá trị sau thuế (cột I) theo ký hiệu (cột C) của bảng tổng hợp, thêm tổng làm tròn và tỷ lệ dự phòng."""
    ws = mo_excel(TH, "TH TMDT")
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


def main():
    if os.path.exists(KQ):
        raise SystemExit(f"File đã có, không ghi đè: {KQ}")
    hm = doc_hang_muc()
    v = doc_tong_hop()
    GXD, QLDA, TV, CK, DP, TMDT, LAM = v["GXD"], v["GQLDA"], v["GTV"], v["GK"], v["GDP"], v["TMĐT"], v["LAM"]
    assert abs(GXD - hm["Tdt"]) < 1, f"Chi phí xây dựng file tổng hợp ({GXD}) khác file hạng mục ({hm['Tdt']})"
    assert abs(GXD + QLDA + TV + CK + DP - TMDT) < 2, "số liệu tổng hợp không cộng khớp"
    tl_dp = f"{v['TL_DP'] * 100:g}".replace(".", ",") + "%"

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

    moi[2] = dat_chu(P[2], [("Số: ", 0), ("......", 0, VANG), ("/TMDT.GN_2026", 0)])
    moi[5] = dat_chu(P[5], [("THUYẾT MINH DỰ TOÁN", 0), "BR", ("Công trình: ", 2),
                            ("...................................... (anh bổ sung)", 2, VANG)])
    moi[6] = dat_chu(P[6], [(f"Hạng mục: {HANG_MUC}", 0)])
    them_sau[6] = [dat_chu(P[6], [("Địa điểm: ", 0), ("......................", 0, VANG),
                                  (" – Thành phố Hồ Chí Minh", 0)])]
    moi[8] = dat_chu(P[8], [("CÁC CĂN CỨ LẬP DỰ TOÁN:", 0)])
    moi[9] = dat_chu(P[9], [("Khối lượng: ", 0), (
        f"Theo bảng chi tiết khối lượng lập từ hồ sơ thiết kế bản vẽ thi công hạng mục {HANG_MUC} "
        "(bản vẽ GN2026-HT-01) do Công ty cổ phần Tư vấn Đầu tư Xây dựng Gia Nguyễn lập.", 1)])
    # Văn bản riêng của đường giao thông và bộ đơn giá cũ: không áp dụng cho dự toán này
    for i in (32, 51, 53, 54, 57, 58, 59):
        moi[i] = None
    # Quy hoạch, chủ trương, hợp đồng: của dự án khác (KP8-15) -> để trống cho anh bổ sung
    moi[62] = dat_chu(P[62], [("Căn cứ ...... (văn bản quy hoạch liên quan, nếu có - anh bổ sung);", 0, VANG)])
    moi[64] = dat_chu(P[64], [("Căn cứ ...... (quyết định phê duyệt chủ trương đầu tư / phê duyệt dự án - anh bổ sung);", 0, VANG)])
    moi[65] = dat_chu(P[65], [("Căn cứ hợp đồng tư vấn số ...... ngày ...... giữa ...... và Công ty cổ phần Tư vấn Đầu tư Xây dựng Gia Nguyễn (anh bổ sung);", 0, VANG)])
    for i in range(66, 74):
        moi[i] = None
    moi[75] = dat_chu(P[75], [(f"Hồ sơ thiết kế bản vẽ thi công hạng mục {HANG_MUC} (bản vẽ GN2026-HT-01) "
                               "do Công ty cổ phần Tư vấn Đầu tư Xây dựng Gia Nguyễn lập;", 0)])
    moi[76] = dat_chu(P[76], [("Hồ sơ khảo sát địa chất khu vực xây dựng ...... (anh bổ sung, nếu có);", 0, VANG)])
    moi[77] = dat_chu(P[77], [
        ("Giá vật liệu theo công bố giá vật liệu xây dựng tháng 8 năm 2026 của Sở Xây dựng Thành phố Hồ Chí Minh "
         "(Thông báo số ", 0), ("28977/TB-SXD-KT&VLXD ngày 10/8/2026 - anh kiểm tra đúng số thông báo giá tháng 8/2026", 0, VANG),
        ("), lấy mức giá cao nhất trong công bố; vật liệu lấy tại mỏ (đá, cát) cộng cước vận chuyển bằng ô tô tự đổ 10 tấn, cự ly 30 km;", 0)])
    moi[78] = dat_chu(P[78], [("Giá nhiên liệu theo dữ liệu phần mềm Dự toán F1 ", 0),
                              ("(anh kiểm tra ngày công bố giá nhiên liệu Petrolimex áp dụng)", 0, VANG), (";", 0)])
    moi[82] = dat_chu(P[82], [(
        "Đơn giá xây dựng chi tiết lập theo phương pháp tính trực tiếp trên phần mềm Dự toán F1: định mức theo "
        "Thông tư 38/2026/TT-BXD; giá nhân công theo Quyết định số 4570/QĐ-UBND ngày 24/7/2026 của UBND Thành phố "
        "Hồ Chí Minh (Vùng I); giá ca máy xác định theo phương pháp tại Thông tư 37/2026/TT-BXD; giá vật liệu theo "
        "công bố giá tháng 8/2026 (giá cao nhất) cộng cước vận chuyển. Các công tác không có định mức riêng cho bể "
        "chứa (bê tông, cốt thép, ván khuôn đáy, thành, nắp bể; lắp đặt ống, phụ kiện uPVC D114, D60) được áp dụng "
        "định mức của công tác tương tự (bê tông, cốt thép, ván khuôn móng, tường, sàn mái; lắp ống, phụ kiện nhựa).", 0)])
    moi[85] = dat_chu(P[85], [("Tổng dự toán được lập theo hướng dẫn của Thông tư 36/2026/TT-BXD. Cụ thể như sau:", 0)])
    moi[86] = dat_chu(P[86], [(
        "Chi phí xây dựng gồm: chi phí trực tiếp (vật liệu, nhân công, máy thi công); chi phí gián tiếp gồm chi phí "
        "chung bằng 7,3% và chi phí một số công việc không xác định được khối lượng từ thiết kế bằng 2,5% chi phí "
        "trực tiếp; thu nhập chịu thuế tính trước bằng 5,5% (chi phí trực tiếp + chi phí gián tiếp); thuế giá trị "
        "gia tăng 8%. Chi phí nhà tạm để ở và điều hành thi công bằng 1,1% chi phí xây dựng trước thuế, "
        "đã gồm thuế giá trị gia tăng.", 0)])
    them_sau[86] = [dat_chu(P[86], [(
        "Chi phí quản lý dự án, chi phí tư vấn đầu tư xây dựng, chi phí khác tính theo tỷ lệ % trên chi phí xây dựng "
        "theo Thông tư 38/2026/TT-BXD (công trình hạ tầng kỹ thuật, cấp IV, thiết kế 1 bước; tỷ lệ tra trên phần mềm "
        "Dự toán F1); chi phí thẩm định hồ sơ mời thầu, kết quả lựa chọn nhà thầu theo Nghị định 214/2025/NĐ-CP; phí "
        "thẩm định dự án theo Thông tư 28/2023/TT-BTC; chi phí kiểm toán độc lập, thẩm tra phê duyệt quyết toán theo "
        "Nghị định 193/2026/NĐ-CP; chi phí kiểm tra công tác nghiệm thu theo Thông tư 10/2021/TT-BXD. "
        "Chi tiết xem bảng tổng hợp dự toán đính kèm.", 0)])]
    moi[88] = dat_chu(P[88], [(
        f"Dự phòng cho yếu tố phát sinh khối lượng công việc được tính bằng {tl_dp} tổng chi phí xây dựng, chi phí "
        "quản lý dự án, chi phí tư vấn đầu tư xây dựng và chi phí khác.", 0)])
    them_sau[88] = [dat_chu(P[88], [("Dự phòng cho yếu tố trượt giá: không tính, ", 0),
                                    ("do thời gian thực hiện dự án dưới 1 năm (anh xác nhận)", 0, VANG), (".", 0)])]
    moi[92] = dat_chu(P[92], [("Xem bảng chi tiết khối lượng công tác xây dựng đính kèm", 0)])
    moi[94] = dat_chu(P[94], [("Tổng mức đầu tư: ", 0), (f"{so(LAM)} đồng", 0),
                              (" (đã làm tròn; xem bảng tổng hợp dự toán đính kèm)", 0)])
    moi[95] = dat_chu(P[95], [(f"(Bằng chữ: {bang_chu(LAM).replace('./.', '')}).", 0)])
    # Bảng chi tiết mẫu: 6 dòng x (tên, ":", số tiền, "đồng") ở các đoạn 97..120.
    # Dự án không có chi phí bồi thường, hỗ trợ và tái định cư: bỏ dòng thứ nhất.
    for i in range(97, 101):
        moi[i] = "XOA_DONG_BANG"
    dong = [("Chi phí xây dựng", GXD), ("Chi phí quản lý dự án", QLDA), ("Chi phí tư vấn đầu tư xây dựng", TV),
            ("Chi phí khác", CK), ("Chi phí dự phòng", DP)]
    for k, (ten, tien) in enumerate(dong, start=1):
        moi[97 + 4 * k] = dat_chu(P[97 + 4 * k], [(ten, 0)])
        moi[99 + 4 * k] = dat_chu(P[99 + 4 * k], [(f" {so(tien)} ", 0)])
    moi[130] = dat_chu(P[130], [("                              ", 0), ("(Họ tên người lập)", 0, VANG),
                                ("                                                                                     ", 0),
                                ("(Họ tên Giám đốc)", 0, VANG)])

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

    hd2 = hd.replace(">Dự án: <", ">Hạng mục: <", 1).replace(
        ">Nâng cấp, mở rộng đường KP18-15<", ">Bể tự hoại BTCT 3 ngăn 10 m³<", 1)

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

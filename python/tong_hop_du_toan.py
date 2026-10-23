# -*- coding: utf-8 -*-
"""
Lập BẢNG TỔNG HỢP DỰ TOÁN XÂY DỰNG CÔNG TRÌNH (theo mẫu công ty template/du-toan/tong-hop/bang-du-toan-tong-hop.xlsx)
cho dự án một hoặc nhiều hạng mục (cách A: file hạng mục dừng ở chi phí xây dựng, file này tính các chi phí còn lại).

Nguồn số liệu (khai báo trong FILE KHAI BÁO DỰ ÁN, mẫu: python/mau-khai-bao-du-an.ini):
  - Chi phí xây dựng: sheet "Tổng hợp dự toán" của file dự toán từng hạng mục (ký hiệu G, GTGT, LT).
    Trước thuế, thuế: chỉ cộng hạng mục; sau thuế: cộng thêm nhà tạm (đã gồm VAT).
  - Tỷ lệ chi phí QLDA, lập BCKTKT, thẩm tra, giám sát, lập HSMT: sheet "TT38" của mẫu tổng hợp (anh đã nhập bảng
    TT 38/2026/TT-BXD). Loại công trình lấy theo hạng mục có chi phí xây dựng trước thuế lớn nhất; tỷ lệ nội suy theo
    TỔNG chi phí xây dựng trước thuế của dự án (ô C4 sheet TT38). Sheet TT38 giữ lại trong file kết quả để kiểm tra.
  - Phí thẩm định dự án, kiểm toán, quyết toán: sheet TT38 còn bảng văn bản cũ, nên lấy từ sheet "TMĐT" của file F1
    xuất ra nếu có khai báo file_f1_tmdt; không có thì để trống, tô vàng "cần tra cứu".
  - Thẩm định HSMT, kết quả LCNT (0,1%), kiểm tra nghiệm thu (20% giám sát), dự phòng khối lượng (5%): theo mẫu.
  - Danh mục khoản chi phí: theo mẫu công ty; khoản nào dự án không có thì bỏ.

Chạy:  python python/tong_hop_du_toan.py <file khai báo>
  ví dụ: python python/tong_hop_du_toan.py ket-qua/be-tu-hoai-10m3/khai-bao-du-an.ini
"""
import os, re, sys, tempfile
from copy import copy

import openpyxl
from openpyxl.cell.cell import MergedCell
from openpyxl.styles import Alignment, Border, Font, PatternFill
from openpyxl.worksheet.pagebreak import RowBreak

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAU = os.path.join(GOC, "template", "du-toan", "tong-hop", "bang-du-toan-tong-hop.xlsx")
sys.path.insert(0, os.path.join(GOC, "python"))
import khai_bao
from khai_bao import CHO_TRONG, chu_hoa, dia_diem_day_du
from chuyen_f1_ve_mau import bang_chu

TEN_TH_HM = ("Tong hop du toan", "Tổng hợp dự toán")   # tên sheet tổng hợp của file hạng mục (mẫu mới, bản cũ)


def mo_excel(path):
    """Mở bằng Excel (chỉ đọc, tắt macro), tính lại, trả về workbook giá trị."""
    import win32com.client
    tam = os.path.join(tempfile.gettempdir(), "th_" + os.path.basename(path).rsplit(".", 1)[0] + ".xlsx")
    if os.path.exists(tam):
        os.remove(tam)
    xl = win32com.client.DispatchEx("Excel.Application")
    xl.Visible = False
    xl.DisplayAlerts = False
    xl.AutomationSecurity = 3
    try:
        wb = xl.Workbooks.Open(path, 0, True)
        xl.CalculateFull()
        wb.SaveAs(tam, 51)
        wb.Close(False)
    finally:
        xl.Quit()
    return openpyxl.load_workbook(tam, data_only=True)


def doc_hang_muc(path):
    wb = mo_excel(path)
    ws = wb[next(t for t in TEN_TH_HM if t in wb.sheetnames)]
    v = {ws[f"C{r}"].value: ws[f"E{r}"].value for r in range(6, ws.max_row + 1) if ws[f"C{r}"].value}
    return v


def doc_ty_le(path):
    """Tỷ lệ (cột E) trong sheet TMĐT của F1, tìm dòng theo nội dung.
    Một khoản có thể có nhiều dòng (ví dụ lập BCKTKT có Bảng 2.4, 2.5, 2.6 theo loại công trình): lấy dòng F1
    đang tính (cột H có tiền); các dòng còn lại F1 nhân 0.
    Trả về (loai, t, bang): loai = chữ "công trình hạ tầng kỹ thuật, thiết kế 1 bước, cấp IV" theo lựa chọn trên F1,
    t = tỷ lệ từng khoản, bang = số bảng tra ghi trong tên dòng F1 (ví dụ "Bảng 2.5"), không có thì để trống."""
    wsv = mo_excel(path)["TMĐT"]
    ten = {r: str(wsv[f"B{r}"].value or "") for r in range(10, 80)}
    loai = ", ".join(x[0].lower() + x[1:] for x in (str(wsv[f"E{r}"].value or "") for r in (5, 6, 7)) if x)

    tim = {
        "QLDA": ("Chi phí quản lý dự án",),
        "BCKTKT": ("lập báo cáo kinh tế - kỹ thuật",),
        "TT_TK": ("thẩm tra thiết kế xây dựng",),
        "TT_DT": ("thẩm tra dự toán công trình",),
        "GS": ("giám sát thi công xây dựng",),
        "HSMT": ("lập hồ sơ mời thầu, đánh giá hồ sơ dự thầu thi công xây dựng",),
        "TD_HSMT": ("thẩm định hồ sơ mời thầu, hồ sơ yêu cầu",),
        "TD_KQ": ("thẩm định kết quả lựa chọn nhà thầu",),
        "TD_DA": ("Phí thẩm định dự án đầu tư",),
        "KTOAN": ("kiểm toán độc lập",),
        "QTOAN": ("thẩm tra, phê duyệt quyết toán",),
        "NTHU": ("kiểm tra công tác nghiệm thu",),
        "DP": ("Dự phòng cho yếu tố khối lượng",),
    }
    t, bang = {}, {}
    for k, tu in tim.items():
        ds = [r for r, x in ten.items() if all(y in x for y in tu)]
        if not ds:
            raise SystemExit(f"Sheet TMĐT của F1 không có dòng '{tu[0]}'")
        r = next((r for r in ds if (wsv[f"H{r}"].value or 0) > 0), ds[0])
        t[k] = wsv[f"E{r}"].value
        m = re.search(r"Bảng \d+\.\d+", ten[r])
        bang[k] = m.group(0) if m else ""
    return loai, t, bang


LOAI_CT = {"dan-dung": "Công trình dân dụng", "cong-nghiep": "Công trình công nghiệp",
           "giao-thong": "Công trình giao thông", "ha-tang-ky-thuat": "Công trình hạ tầng kỹ thuật"}


def loai_cong_trinh(ds_hm):
    """Loại công trình để tra tỷ lệ: theo hạng mục có chi phí xây dựng trước thuế (ký hiệu G) lớn nhất.
    ds_hm = [(hạng mục khai báo, số liệu đọc từ file hạng mục)]. Trả về (tên loại như trong sheet TT38, hạng mục đó)."""
    h, _ = max(ds_hm, key=lambda x: x[1].get("G") or 0)
    if h.linh_vuc not in LOAI_CT:
        raise SystemExit(f"Hạng mục '{h.ten}': lĩnh vực '{h.linh_vuc}' chưa có trong bảng tra TT38")
    return LOAI_CT[h.linh_vuc], h


def o_tt38(ws, ma, loai):
    """Địa chỉ ô "Giá trị" (tỷ lệ %, Excel đã nội suy) của dòng loại công trình trong bảng có mã `ma`
    của sheet TT38 (bảng nằm giữa 2 dòng mốc ở cột A: ma^ ... ma$)."""
    dau = cuoi = None
    for r in range(1, ws.max_row + 1):
        a = ws[f"A{r}"].value
        if a == ma + "^":
            dau = r
        elif a == ma + "$" and dau:
            cuoi = r
            break
    if not cuoi:
        raise SystemExit(f"Sheet TT38 không có bảng {ma} (dòng mốc {ma}^ ... {ma}$)")
    cot = next((c.column_letter for hang in ws.iter_rows(min_row=dau, max_row=cuoi) for c in hang
                if c.value == "Giá trị"), None)
    dong = next((r for r in range(dau, cuoi) if str(ws[f"B{r}"].value or "").strip() == loai), None)
    if not cot or not dong:
        raise SystemExit(f"Sheet TT38, bảng {ma}: không thấy cột 'Giá trị' hoặc dòng '{loai}'")
    return f"TT38!{cot}{dong}"


def sua_loi_bang_bcktkt(ws):
    """Bảng lập BCKTKT (mã LBC79) của mẫu: các dòng dân dụng, công nghiệp, nông nghiệp, hạ tầng so cận với 7 và 15,
    trong khi hàng mốc là 1, 3, 20, 40 tỷ (dòng giao thông đúng) -> chi phí 3 đến 40 tỷ nội suy ra sai.
    Chỉ sửa trong FILE KẾT QUẢ, không sửa mẫu. Trả về danh sách ô đã sửa."""
    da_sua = []
    for r in range(1, ws.max_row + 1):
        if ws[f"A{r}"].value != "LBC79^":
            continue
        moc = next(rr for rr in range(r, r + 5) if ws[f"G{rr}"].value == "Giá trị") + 1
        for rr in range(moc + 1, moc + 6):
            for c in "HI":
                f = ws[f"{c}{rr}"].value
                if isinstance(f, str) and f"${moc}=7," in f:
                    ws[f"{c}{rr}"] = f.replace(f"${moc}=7,", f"${moc}=20,").replace(f"${moc}=15,", f"${moc}=40,")
                    da_sua.append(f"{c}{rr}")
    return da_sua


def pct(x):
    return f"{x * 100:.3f}".rstrip("0").rstrip(".").replace(".", ",") + "%"


def main():
    kb = khai_bao.doc()
    KQ = kb.file_tong_hop
    if os.path.exists(KQ):
        raise SystemExit(f"File đã có, không ghi đè: {KQ}")
    if kb.truot_gia != "khong":
        raise SystemExit("Dự phòng trượt giá: chương trình hiện chỉ hỗ trợ 'khong' (không tính)")
    for path in [h.file_du_toan for h in kb.hang_muc] + ([kb.f1_tmdt] if kb.f1_tmdt else []):
        if not os.path.exists(path):
            raise SystemExit(f"Chưa có file: {path}")
    ds_hm = [(h, doc_hang_muc(h.file_du_toan)) for h in kb.hang_muc]
    loai, h_lon = loai_cong_trinh(ds_hm)
    t = doc_ty_le(kb.f1_tmdt)[1] if kb.f1_tmdt else {}   # chỉ dùng cho phí thẩm định dự án, kiểm toán, quyết toán

    def cc(k):
        """Căn cứ: số bảng TT 38/2026 theo mẫu tổng hợp công ty."""
        bang = {"QLDA": "Bảng 1.1", "BCKTKT": "Bảng 2.5", "TT_TK": "Bảng 2.19", "TT_DT": "Bảng 2.20",
                "GS": "Bảng 2.24", "HSMT": "Bảng 2.22"}
        return f"{bang[k]} TT 38/2026/TT-BXD"
    VAT = kb.vat

    import shutil
    shutil.copy(MAU, KQ)
    wb = openpyxl.load_workbook(KQ)
    for ws in list(wb.worksheets):
        if ws.title not in ("TH TMDT", "TT38"):
            wb.remove(ws)                      # bỏ các sheet khác (kể cả sheet ẩn) mà không đọc
    wt = wb["TT38"]
    wt.defined_names.clear()
    wt.sheet_view.tabSelected = False          # tránh Excel mở ra 2 sheet bị chọn chung (nhóm sheet)
    loi_bcktkt = sua_loi_bang_bcktkt(wt)
    # Tỷ lệ (%) Excel nội suy trong sheet TT38, theo loại công trình của hạng mục lớn nhất
    tl = {k: f"={o_tt38(wt, ma, loai)}/100" for k, ma in
          (("QLDA", "QLDA79"), ("BCKTKT", "LBC79"), ("TT_TK", "TTTKXD79"), ("TT_DT", "TTDT79"),
           ("GS", "GSTC79"), ("HSMT", "LXL79"))}
    wb._external_links = []
    wb.defined_names.clear()
    wb.active = 0
    for v in wb.views:                         # mẫu đặt firstSheet=2, còn 1 sheet thì Excel không mở được
        v.firstSheet = v.activeTab = 0
    ws = wb["TH TMDT"]
    ws.defined_names.clear()
    ws.sheet_view.pane = None                  # bỏ cố định khung (mẫu để lại pane hỏng)
    ws.sheet_view.selection = []
    ws.row_breaks = RowBreak()                 # bỏ ngắt trang cũ của mẫu
    cols = list("ABCDEFGHIJ")
    st = {k: {c: copy(ws[f"{c}{r}"]._style) for c in cols}
          for k, r in (("nhom", 8), ("con", 9), ("nhom2", 13), ("muc", 18), ("con3", 20),
                       ("dp", 47), ("tong", 51), ("tron", 52), ("chu", 53), ("ky", 54))}
    for m in list(ws.merged_cells.ranges):
        if m.min_row >= 7:
            ws.unmerge_cells(str(m))
    ws.delete_rows(7, ws.max_row)
    for k in [k for k in ws.row_dimensions if k >= 7]:   # bỏ dòng ẩn, chiều cao dòng cũ của mẫu
        del ws.row_dimensions[k]
    for row in ws.iter_rows(min_row=1, max_row=6, min_col=11, max_col=20):   # vùng nháp ngoài vùng in
        for c in row:
            if not isinstance(c, MergedCell):
                c.value = None
    ws["A2"] = "DỰ ÁN: " + (chu_hoa(kb.ten_du_an) or CHO_TRONG * 9 + " (ANH BỔ SUNG)")
    ws["A3"] = "ĐỊA ĐIỂM: " + chu_hoa(dia_diem_day_du(kb))
    ws["L4"], ws["M4"] = "Thuế suất GTGT:", VAT          # ô tham số VAT duy nhất
    ws["M4"].number_format = "0%"
    V = "$M$4"

    dong = []   # (kiểu, A, B, C, D, E(cách tính), G, H, I, J)
    r0 = 7

    def them(*a):
        dong.append(a)
        return r0 + len(dong) - 1

    n = len(ds_hm)
    ky_hieu = " + ".join(f"GXD{i}" for i in range(1, n + 2))
    rI = them("nhom", "I", "Chi phí xây dựng", "GXD", None, f'="{ky_hieu} (nhà tạm chỉ cộng sau thuế)"', "SUMG", None, None, None)
    r_hms = [them("muc", None, f"- Chi phí xây dựng hạng mục {h.ten}", f"GXD{i}", None,
                  "Theo bảng tổng hợp dự toán hạng mục (*)", v["G"], v["GTGT"], "GH",
                  f"Dự toán hạng mục {h.ky_hieu}".strip())
             for i, (h, v) in enumerate(ds_hm, start=1)]
    r_lt = them("muc", None, "- Chi phí nhà tạm để ở và điều hành thi công", f"GXD{n + 1}", None,
                "Theo bảng tổng hợp dự toán hạng mục, đã gồm VAT (*)", None, None,
                sum(v["LT"] for _, v in ds_hm), "TT 36/2026/TT-BXD")
    B = f"$G${rI}"           # GXD trước thuế (không gồm nhà tạm) - cơ sở tính các tỷ lệ, giống F1
    rII = them("nhom", "II", "Chi phí quản lý dự án", "GQLDA", tl["QLDA"], '="GXD trước thuế x "&D{r}',
               f"=ROUND({B}*D{{r}},0)", f"=ROUND(G{{r}}*{V},0)", "GH", cc("QLDA"))
    rIII = them("nhom2", "III", "Chi phí tư vấn đầu tư xây dựng", "GTV", None, None, "SUBG", "SUBH", "SUBI", None)
    tv = [
        them("muc", 1, "- Chi phí lập Báo cáo kinh tế - kỹ thuật", "GTV1", tl["BCKTKT"], '="GXD trước thuế x "&D{r}&" (tối thiểu 5 triệu)"',
             f"=ROUND(MAX({B}*D{{r}},5000000),0)", f"=ROUND(G{{r}}*{V},0)", "GH", cc("BCKTKT")),
        them("muc", 2, "- Chi phí thẩm tra thiết kế bản vẽ thi công", "GTV2", tl["TT_TK"], '="GXD trước thuế x "&D{r}&" (tối thiểu 2 triệu)"',
             f"=ROUND(MAX({B}*D{{r}},2000000),0)", f"=ROUND(G{{r}}*{V},0)", "GH", cc("TT_TK")),
        them("muc", 3, "- Chi phí thẩm tra dự toán xây dựng", "GTV3", tl["TT_DT"], '="GXD trước thuế x "&D{r}&" (tối thiểu 2 triệu)"',
             f"=ROUND(MAX({B}*D{{r}},2000000),0)", f"=ROUND(G{{r}}*{V},0)", "GH", cc("TT_DT")),
        them("muc", 4, "- Chi phí giám sát thi công xây dựng", "GTV4", tl["GS"], '="GXD trước thuế x "&D{r}',
             f"=ROUND({B}*D{{r}},0)", f"=ROUND(G{{r}}*{V},0)", "GH", cc("GS")),
        them("muc", 5, "- Chi phí lập HSMT và đánh giá HSDT thi công xây dựng", "GTV5", tl["HSMT"], '="GXD trước thuế x "&D{r}',
             f"=ROUND({B}*D{{r}},0)", f"=ROUND(G{{r}}*{V},0)", "GH", cc("HSMT")),
        them("muc", 6, "- Chi phí thẩm định hồ sơ mời thầu gói thầu thi công xây dựng", "GTV6", 0.001,   # 0,1% theo mẫu
             '="GXD sau thuế x "&D{r}&" (tối thiểu 2 triệu, tối đa 60 triệu)"',
             f"=ROUND(MIN(MAX($I${rI}*D{{r}},2000000),60000000),0)", 0, "GH", "NĐ 214/2025/NĐ-CP"),
        them("muc", 7, "- Chi phí thẩm định kết quả lựa chọn nhà thầu gói thầu thi công xây dựng", "GTV7", 0.001,
             '="GXD sau thuế x "&D{r}&" (tối thiểu 3 triệu, tối đa 60 triệu)"',
             f"=ROUND(MIN(MAX($I${rI}*D{{r}},3000000),60000000),0)", 0, "GH", "NĐ 214/2025/NĐ-CP"),
    ]
    rIV = them("nhom2", "IV", "Chi phí khác", "GK", None, None, "SUBG", "SUBH", "SUBI", None)
    base_tm = f"($I${rI}+$I${rII}+$I${rIII})"     # tổng mức tạm tính để tính phí thẩm định, kiểm toán, quyết toán
    can_tra = []      # dòng chưa có tỷ lệ (không khai báo file F1): tô vàng, anh tra cứu

    def phi(stt, ten, ky, k, cach, g, h, can_cu):
        """Khoản phí tính trên tổng mức: tỷ lệ lấy từ F1 nếu có; không có thì để trống, công thức ra 0."""
        if k in t:
            return them("muc", stt, ten, ky, t[k], cach, g, h, "GH", can_cu)
        r = them("muc", stt, ten, ky, None, "Cần tra cứu tỷ lệ (sheet TT38 còn bảng văn bản cũ)",
                 g.replace("=", '=IF(D{r}="",0,', 1) + ")", h, "GH", can_cu + " - cần tra cứu")
        can_tra.append(r)
        return r
    ck = [
        phi(1, "- Phí thẩm định dự án đầu tư xây dựng", "K1", "TD_DA",
            '="(GXD + GQLDA + GTV) x "&D{r}&" (tối thiểu 500.000, tối đa 150 triệu)"',
            f"=ROUND(MIN(MAX({base_tm}*D{{r}},500000),150000000),0)", 0, "TT 28/2023/TT-BTC"),
        phi(2, "- Chi phí kiểm toán độc lập", "K2", "KTOAN",
            '="(GXD + GQLDA + GTV) x "&D{r}&" (tối thiểu 1 triệu)"',
            f"=ROUND(MAX({base_tm}*D{{r}},1000000),0)", f"=ROUND(G{{r}}*{V},0)", "NĐ 193/2026/NĐ-CP"),
        phi(3, "- Chi phí thẩm tra, phê duyệt quyết toán", "K3", "QTOAN",
            '="(GXD + GQLDA + GTV) x "&D{r}&" (tối thiểu 500.000)"',
            f"=ROUND(MAX({base_tm}*D{{r}},500000),0)", 0, "NĐ 193/2026/NĐ-CP"),
        them("muc", 4, "- Chi phí kiểm tra công tác nghiệm thu công trình", "K4", 0.2,   # 20% giám sát, theo mẫu
             '="GTV4 trước thuế x "&D{r}', f"=ROUND($G${tv[3]}*D{{r}},0)", f"=ROUND(G{{r}}*{V},0)", "GH", "TT 10/2021/TT-BXD"),
    ]
    if kb.dam_bao_giao_thong:            # khoản riêng của giao thông, anh khai báo (tạm tính, trước thuế)
        ck.append(them("muc", len(ck) + 1, "- Chi phí đảm bảo an toàn giao thông phục vụ thi công", f"K{len(ck) + 1}",
                       None, "Tạm tính (theo khai báo)", kb.dam_bao_giao_thong, f"=ROUND(G{{r}}*{V},0)", "GH",
                       "Tạm tính - anh bổ sung căn cứ"))
    rV = them("nhom2", "V", "Chi phí dự phòng", "GDP", None, '="GDP1 + GDP2"', None, None, "DP", None)
    rdp1 = them("dp", "5.1", " - Chi phí dự phòng cho yếu tố khối lượng", "GDP1", 0.05,   # 5% theo mẫu
                '="(GXD + GQLDA + GTV + GK) x "&D{r}', None, None,
                f"=ROUND((I{rI}+I{rII}+I{rIII}+I{rIV})*D{{r}},0)", "TT 38/2026/TT-BXD")
    rdp2 = them("dp", "5.2", " - Chi phí dự phòng cho yếu tố trượt giá", "GDP2", None,
                f"Không tính ({kb.ly_do_truot_gia or 'anh xác nhận lý do'})", None, None, 0, None)
    if kb.di_doi:                        # chi phí di dời hạ tầng kỹ thuật, anh khai báo (tạm tính, đã gồm thuế)
        rVI = them("nhom2", "VI", f"{kb.ten_di_doi} (tạm tính)", "GDD", None, "Tạm tính (theo khai báo), đã gồm thuế",
                   None, None, kb.di_doi, "Tạm tính - anh bổ sung căn cứ")
        rT = them("tong", None, "Tổng cộng (I+II+III+IV+V+VI)", "TMĐT", None, '="GXD + GQLDA + GTV + GK + GDP + GDD"',
                  None, None, f"=I{rI}+I{rII}+I{rIII}+I{rIV}+I{rV}+I{rVI}", None)
    else:
        rT = them("tong", None, "Tổng cộng (I+II+III+IV+V)", "TMĐT", None, '="GXD + GQLDA + GTV + GK + GDP"', None, None,
                  f"=I{rI}+I{rII}+I{rIII}+I{rIV}+I{rV}", None)
    rR = them("tron", None, "Tổng cộng (làm tròn)", None, None, None, None, None, f"=ROUND(I{rT},-6)", None)

    for i, d in enumerate(dong):
        r = r0 + i
        kieu, a, b, c, dm, e, g, h, iv, j = d
        for col in cols:
            ws[f"{col}{r}"]._style = copy(st[kieu][col])
        ws[f"A{r}"], ws[f"B{r}"], ws[f"C{r}"], ws[f"J{r}"] = a, b, c, j
        if dm is not None:
            ws[f"D{r}"] = dm
            ws[f"D{r}"].number_format = "0.000%"
        if e:
            ws[f"E{r}"] = e.format(r=r)
        ws.merge_cells(f"E{r}:F{r}")
        if g == "SUMG":
            # trước thuế và thuế: chỉ hạng mục; sau thuế: cộng thêm nhà tạm (đã gồm VAT), giống THDT hạng mục
            g = "=" + "+".join(f"G{x}" for x in r_hms)
            h = "=" + "+".join(f"H{x}" for x in r_hms)
            iv = "=" + "+".join(f"I{x}" for x in r_hms + [r_lt])
        if g == "SUBG":
            ds = tv if r == rIII else ck
            g = "=" + "+".join(f"G{x}" for x in ds)
            h = "=" + "+".join(f"H{x}" for x in ds)
            iv = "=" + "+".join(f"I{x}" for x in ds)
        if iv == "DP":
            iv = f"=I{rdp1}+I{rdp2}"
        for col, val in (("G", g), ("H", h)):
            if val is not None:
                ws[f"{col}{r}"] = val.format(r=r) if isinstance(val, str) else val
        if iv == "GH":
            iv = f"=G{r}+H{r}"
        if iv is not None:
            ws[f"I{r}"] = iv.format(r=r) if isinstance(iv, str) else iv
        for col in "BEJ":
            ws[f"{col}{r}"].alignment = ws[f"{col}{r}"].alignment.copy(wrap_text=True, vertical="center")
        if kieu == "tong":
            ws[f"I{r}"].fill = PatternFill(fill_type=None)       # bỏ tô vàng của mẫu cũ
        ws.row_dimensions[r].height = 36 if len(str(b)) > 48 or len(str(e or "")) > 40 or len(str(j or "")) > 22 else 26
        if r in can_tra:
            for col in "DEJ":
                ws[f"{col}{r}"].fill = PatternFill("solid", fgColor="FFFF00")
    # Sheet TT38 nội suy theo tổng chi phí xây dựng trước thuế của dự án (tỷ đồng), không có thiết bị, GPMB, khảo sát
    wt["C4"] = f"='TH TMDT'!G{rI}/10^9"
    wt["C6"], wt["C11"] = 0, 0
    wt["C9"] = f"='TH TMDT'!I{rT}/10^9"
    # Bằng chữ: tính lại đúng như công thức để viết chữ
    r = rR + 1
    for col in cols:
        ws[f"{col}{r}"]._style = copy(st["chu"][col])
    ws.merge_cells(f"A{r}:J{r}")
    ws[f"A{r}"] = "Bằng chữ: (xem dòng dưới, chương trình điền sau khi tính)"
    r_chu = r
    r += 1
    file_hm = ", ".join(os.path.basename(h.file_du_toan) for h in kb.hang_muc)
    ws[f"A{r}"] = (f"(*) Chi phí xây dựng lấy từ file {file_hm}, sheet \"Tổng hợp dự toán\" (ký hiệu G, GTGT, LT). "
                   f"Tỷ lệ QLDA, tư vấn: sheet TT38 (TT 38/2026/TT-BXD), {loai.lower()} theo hạng mục {h_lon.ten} "
                   f"(chi phí xây dựng trước thuế lớn nhất), nội suy theo tổng chi phí xây dựng trước thuế của dự án."
                   + (" Phí thẩm định dự án, kiểm toán, quyết toán: tỷ lệ theo phần mềm Dự toán F1." if t else
                      " Ô tô vàng: chưa có tỷ lệ, anh tra cứu theo văn bản hiện hành."))
    ws[f"A{r}"].font = Font(name="Times New Roman", size=11, italic=True)
    ws[f"A{r}"].alignment = Alignment(vertical="top")
    r += 2
    for txt_l, txt_r in (("NGƯỜI LẬP", "NGƯỜI CHỦ TRÌ"), (None, None), (None, None), (None, None),
                         ("(Họ tên - anh bổ sung)", "(Họ tên, chứng chỉ định giá XD - anh bổ sung)")):
        if txt_l:
            for col, txt in (("B", txt_l), ("I", txt_r)):
                ws[f"{col}{r}"] = txt
                ws[f"{col}{r}"].font = Font(name="Times New Roman", size=13, bold=txt.isupper(), italic=not txt.isupper())
                ws[f"{col}{r}"].alignment = Alignment(horizontal="center")
        r += 1
    for rr in range(r_chu + 1, r + 1):          # cột J của mẫu có sẵn khung viền, bỏ ở phần chữ ký
        for col in cols:
            ws[f"{col}{rr}"].border = Border()
    ws.print_area = f"A1:J{r}"
    wb.save(KQ)

    # Tính lại bằng Excel để lấy tổng và viết bằng chữ
    wv = mo_excel(KQ)["TH TMDT"]
    tong = wv[f"I{rR}"].value
    wb = openpyxl.load_workbook(KQ)
    wb["TH TMDT"][f"A{r_chu}"] = "Bằng chữ: " + bang_chu(tong)
    wb.save(KQ)
    print("Đã lập:", KQ)
    print(f"Loại công trình tra sheet TT38: {loai} (theo hạng mục {h_lon.ten})")
    if loi_bcktkt:
        print("Đã sửa lỗi công thức bảng lập BCKTKT trong sheet TT38 của file kết quả (mẫu giữ nguyên):",
              ", ".join(loi_bcktkt))
    if can_tra:
        print("Chưa có file F1 TMĐT: phí thẩm định dự án, kiểm toán, quyết toán để trống, tô vàng - anh tra cứu.")
    for k_, rr in (("GXD", rI), ("GQLDA", rII), ("GTV", rIII), ("GK", rIV), ("GDP", rV), ("TMĐT", rT), ("Làm tròn", rR)):
        print(f"{k_:9} {wv[f'G{rr}'].value or 0:>14,.0f} {wv[f'H{rr}'].value or 0:>12,.0f} {wv[f'I{rr}'].value or 0:>14,.0f}")
    print(bang_chu(tong))


if __name__ == "__main__":
    main()

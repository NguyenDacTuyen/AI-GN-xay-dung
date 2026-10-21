# -*- coding: utf-8 -*-
"""
Chuyển file Excel xuất từ phần mềm Dự toán F1 về MẪU DỰ TOÁN HẠ TẦNG KỸ THUẬT của công ty Gia Nguyễn.

Việc chương trình làm:
  1. Mở file F1 xuất ra (.xlsm) bằng Excel ở chế độ CHỈ ĐỌC, tắt macro, lưu một bản .xlsx tạm để đọc.
  2. Chép file mẫu template/du-toan/ha-tang-ky-thuat/du-toan-ha-tang.xlsx sang thư mục kết quả (không sửa file mẫu).
  3. Đổ số liệu F1 vào các sheet theo đúng bố cục mẫu:
       Công trình (chi tiết khối lượng, có dòng diễn giải) - Hao phí vật tư - Vật liệu - Nhân công - Máy thi công
       - Tổng hợp dự toán - Bìa dự toán.
     Giữ chuỗi công thức: Công trình -> Hao phí vật tư -> Vật liệu / Nhân công / Máy thi công -> Tổng hợp dự toán.
  4. Không ghi đè file kết quả đã có.

Chạy:  python python/chuyen_f1_ve_mau_ha_tang.py
"""
import math, os, re, shutil, sys, tempfile
from copy import copy

import openpyxl
from openpyxl.cell.cell import MergedCell
from openpyxl.styles import Alignment, Font

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THU_MUC = os.path.join(GOC, "ket-qua", "be-tu-hoai-10m3")
F1_XUAT = os.path.join(THU_MUC, "F1-xuat_be-tu-hoai-10m3.xlsm")
MAU = os.path.join(GOC, "template", "du-toan", "ha-tang-ky-thuat", "du-toan-ha-tang.xlsx")
KQ = os.path.join(THU_MUC, "du-toan_be-tu-hoai-10m3_TT38-HCM.xlsx")

CONG_TRINH = "CÔNG TRÌNH: ................................................ (ANH BỔ SUNG TÊN CÔNG TRÌNH)"
HANG_MUC = "HẠNG MỤC: BỂ TỰ HOẠI BTCT 3 NGĂN, DUNG TÍCH HỮU ÍCH 10 m³ (BẢN VẼ GN2026-HT-01)"
DIA_DIEM = "ĐỊA ĐIỂM: ................................................, THÀNH PHỐ HỒ CHÍ MINH"
TNR = "Times New Roman"


# ------------------------------------------------------------------ đọc file F1
def doc_f1():
    """Mở file F1 bằng Excel (chỉ đọc, tắt macro), tính lại, lưu bản .xlsx tạm. Trả về (wb công thức, wb giá trị)."""
    import win32com.client
    tam = os.path.join(tempfile.gettempdir(), "f1_xuat_tam.xlsx")
    if os.path.exists(tam):
        os.remove(tam)
    xl = win32com.client.DispatchEx("Excel.Application")
    xl.Visible = False
    xl.DisplayAlerts = False
    xl.AutomationSecurity = 3          # tắt macro
    try:
        wb = xl.Workbooks.Open(F1_XUAT, 0, True)
        xl.CalculateFull()
        wb.SaveAs(tam, 51)
        wb.Close(False)
    finally:
        xl.Quit()
    return openpyxl.load_workbook(tam), openpyxl.load_workbook(tam, data_only=True)


# ------------------------------------------------------------------ đổi tham chiếu công thức
REF = re.compile(r"'(Công trình|Hao phí VT|Vật liệu|Nhân công|Máy thi công)'!\$?([A-Z]{1,3})\$?(\d+)")
HP_COT = {"K": "I", "L": "I", "M": "I", "G": "G", "H": "G", "I": "G"}   # cột hao phí F1 -> cột mẫu


def doi_ref(f):
    """Đổi tham chiếu sang sheet của mẫu: Công trình lùi 1 dòng (mẫu có thêm dòng địa điểm),
    'Hao phí VT' -> 'Hao phí vật tư' (gộp 3 cột VL/NC/M thành 1 cột)."""
    if not isinstance(f, str) or not f.startswith("="):
        return f

    def thay(m):
        sh, col, row = m.group(1), m.group(2), int(m.group(3))
        if sh == "Công trình":
            return f"'Công trình'!{col}{row + 1}"
        if sh == "Hao phí VT":
            return f"'Hao phí vật tư'!{HP_COT.get(col, col)}{row}"
        return f"'{sh}'!{col}{row}"
    return REF.sub(thay, f)


def chep_kieu(dst, src):
    """Chép định dạng giữa 2 file khác nhau."""
    dst.font = copy(src.font)
    dst.border = copy(src.border)
    dst.fill = copy(src.fill)
    dst.number_format = src.number_format
    dst.alignment = copy(src.alignment)
    dst.protection = copy(src.protection)


def bo_gop(ws, tu_dong):
    for m in list(ws.merged_cells.ranges):
        if m.min_row >= tu_dong:
            ws.unmerge_cells(str(m))


def xoa_tu(ws, tu_dong):
    bo_gop(ws, tu_dong)
    if ws.max_row >= tu_dong:
        ws.delete_rows(tu_dong, ws.max_row - tu_dong + 1)


# ------------------------------------------------------------------ đọc số thành chữ
DV = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]


def doc3(n, day_du):
    tr, ch, dv = n // 100, n // 10 % 10, n % 10
    s = []
    if day_du or tr:
        s.append(DV[tr] + " trăm")
    if ch == 0:
        if dv and (day_du or tr):
            s.append("lẻ")
    elif ch == 1:
        s.append("mười")
    else:
        s.append(DV[ch] + " mươi")
    if dv:
        if dv == 1 and ch > 1:
            s.append("mốt")
        elif dv == 5 and ch > 0:
            s.append("lăm")
        elif dv == 4 and ch > 1:
            s.append("tư")
        else:
            s.append(DV[dv])
    return " ".join(s)


def bang_chu(so):
    so = int(round(so))
    if so == 0:
        return "Không đồng"
    nhom = []
    while so:
        nhom.append(so % 1000)
        so //= 1000
    ten = ["", " nghìn", " triệu", " tỷ"]
    s = []
    for i in range(len(nhom) - 1, -1, -1):
        if nhom[i]:
            s.append(doc3(nhom[i], i != len(nhom) - 1) + ten[i % 4 if i < 4 else 3])
    t = " ".join(s)
    return t[0].upper() + t[1:] + " đồng./."


# ------------------------------------------------------------------ chương trình chính
def main():
    if os.path.exists(KQ):
        raise SystemExit(f"File đã có, không ghi đè: {KQ}")
    f1, f1v = doc_f1()
    shutil.copy(MAU, KQ)
    wb = openpyxl.load_workbook(KQ)
    giu = ("Công trình", "Hao phí vật tư", "Vật liệu", "Tổng hợp du toan (2)", "Bìa du toan (2)")
    for ws in list(wb.worksheets):
        if ws.title not in giu:
            wb.remove(ws)
    wb._external_links = []
    wb.defined_names.clear()
    for ws in wb.worksheets:
        ws.defined_names.clear()

    # ============================== 1. CÔNG TRÌNH (chi tiết khối lượng)
    ws, src, srv = wb["Công trình"], f1["Công trình"], f1v["Công trình"]
    cols = [openpyxl.utils.get_column_letter(i) for i in range(1, 26)]
    st = {k: {c: copy(ws[f"{c}{r}"]._style) for c in cols} for k, r in (("cv", 11), ("dg", 12), ("tong", 248))}
    st_hdr4 = {c: copy(ws[f"{c}4"]._style) for c in cols}
    xoa_tu(ws, 8)
    ws["A2"] = src["A2"].value
    ws["A3"], ws["A4"] = CONG_TRINH, HANG_MUC
    for c in cols:
        ws[f"{c}5"]._style = copy(st_hdr4[c])
    ws.merge_cells("A5:W5")
    ws["A5"] = DIA_DIEM
    ws.row_dimensions[5].height = ws.row_dimensions[4].height

    r_thm = next(r for r in range(7, src.max_row + 1) if src[f"C{r}"].value == "THM")
    dong_cv, dau = [], None
    for r in range(7, r_thm):
        n = r + 1
        if src[f"A{r}"].value is not None:                       # dòng công tác
            for c in cols:
                ws[f"{c}{n}"]._style = copy(st["cv"][c])
            for c in "ACDEMNOPXY":
                ws[f"{c}{n}"] = src[f"{c}{r}"].value
            for a, b in (("Q", "M"), ("R", "N"), ("S", "O"), ("T", "P")):
                ws[f"{a}{n}"] = f"=ROUND(L{n}*{b}{n},0)"
            ws[f"B{n}"] = "GN2026-HT-01"
            dong_cv.append(n)
        elif src[f"D{r}"].value is not None:                     # dòng diễn giải
            for c in cols:
                ws[f"{c}{n}"]._style = copy(st["dg"][c])
            txt = str(src[f"D{r}"].value)
            ws[f"D{n}"] = txt
            kq = srv[f"K{r}"].value
            # lấy biểu thức trong chữ diễn giải làm công thức (nếu tính ra đúng số F1)
            bt = txt.rsplit(" = ", 1)[0]
            bt = bt.rsplit(": ", 1)[-1].strip().replace(",", ".")
            try:
                if re.fullmatch(r"[\d.+\-*/() ]+", bt) and abs(eval(bt) - kq) < 5e-4:
                    ws[f"K{n}"] = f"=ROUND({bt},4)"      # F1 làm tròn mỗi dòng diễn giải 4 số lẻ
                else:
                    ws[f"K{n}"] = kq
            except Exception:
                ws[f"K{n}"] = kq
        ws.row_dimensions[n].height = src.row_dimensions[r].height
    # khối lượng = tổng các dòng diễn giải bên dưới
    for i, n in enumerate(dong_cv):
        cuoi = (dong_cv[i + 1] if i + 1 < len(dong_cv) else r_thm + 1) - 1
        ws[f"L{n}"] = f"=ROUND(SUM(K{n + 1}:K{cuoi}),4)"
    n_thm = r_thm + 1
    for c in cols:
        ws[f"{c}{n_thm}"]._style = copy(st["tong"][c])
    ws[f"C{n_thm}"], ws[f"D{n_thm}"] = "THM", "TỔNG HẠNG MỤC"
    for c in "QRST":
        ws[f"{c}{n_thm}"] = f"=SUM({c}8:{c}{n_thm - 1})"
    k = n_thm + 2
    for o, t in ((f"D{k}", "NGƯỜI THỰC HIỆN"), (f"O{k}", "NGƯỜI CHỦ TRÌ")):
        ws[o] = t
        ws[o].font = Font(name=TNR, size=11, bold=True)
        ws[o].alignment = Alignment(horizontal="center")
    for o in (f"D{k + 4}", f"O{k + 4}"):
        ws[o] = "(Họ tên, chứng chỉ hành nghề định giá XD - anh bổ sung)"
        ws[o].font = Font(name=TNR, size=11, italic=True)
        ws[o].alignment = Alignment(horizontal="center")
    ws.print_area = f"A1:W{k + 4}"
    for n in dong_cv:                                    # khối lượng hiện đủ 4 số lẻ như F1
        ws[f"L{n}"].number_format = "#,##0.0000"
    ws.row_dimensions[7].height = 32                     # tiêu đề "Nhân công" không bị cắt
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0

    # ============================== 2. HAO PHÍ VẬT TƯ (gộp VL/NC/M thành 1 cột "Vật tư")
    ws, src = wb["Hao phí vật tư"], f1["Hao phí VT"]
    hcols = list("ABCDEFGHI")
    sth = {k: {c: copy(ws[f"{c}{r}"]._style) for c in hcols} for k, r in (("cv", 10), ("nhom", 11), ("ct", 12))}
    xoa_tu(ws, 7)
    dong_cv_hp = None
    for r in range(7, src.max_row + 1):
        a, d = src[f"A{r}"].value, src[f"D{r}"].value
        if a is None and d is None and src[f"B{r}"].value is None:
            continue
        if isinstance(a, str) and "'Công trình'" in a:              # dòng công tác
            kieu, dong_cv_hp = "cv", r
            for c in "ABDEF":
                ws[f"{c}{r}"] = doi_ref(src[f"{c}{r}"].value)
        elif d in ("Vật liệu", "Nhân công", "Máy thi công"):        # nhóm
            kieu = "nhom"
            ws[f"D{r}"] = d
        else:                                                        # hao phí
            kieu = "ct"
            for c in "BCDE":
                ws[f"{c}{r}"] = doi_ref(src[f"{c}{r}"].value)
            dm = next((src[f"{c}{r}"].value for c in "GHI" if src[f"{c}{r}"].value is not None), None)
            ws[f"G{r}"] = dm
            ws[f"H{r}"] = src[f"J{r}"].value
            if any(src[f"{c}{r}"].value is not None for c in "KLM"):
                ws[f"I{r}"] = f"=ROUND(F{dong_cv_hp}*G{r}*H{r},6)"
        for c in hcols:
            ws[f"{c}{r}"]._style = copy(sth[kieu][c])
    ws["A1"] = "BẢNG PHÂN TÍCH VẬT TƯ"
    ws["A2"], ws["A3"] = "='Công trình'!A3", "='Công trình'!A4"
    ws.print_area = f"A1:I{src.max_row}"

    # ============================== 3. VẬT LIỆU (cùng bố cục cột với F1)
    ws, src, srv = wb["Vật liệu"], f1["Vật liệu"], f1v["Vật liệu"]
    vcols = [openpyxl.utils.get_column_letter(i) for i in range(1, 31)]
    stv = {k: {c: copy(ws[f"{c}{r}"]._style) for c in vcols}
           for k, r in (("chinh", 8), ("con", 9), ("t1", 210), ("t2", 211), ("t3", 212))}
    xoa_tu(ws, 8)
    r_tong = next(r for r in range(8, src.max_row + 1) if src[f"E{r}"].value == "Tổng vật liệu:")
    for r in range(8, r_tong + 1):
        if src[f"E{r}"].value == "Cộng vật liệu chính:":
            kieu = "t1"
        elif src[f"E{r}"].value == "Cộng vật liệu phụ:":
            kieu = "t2"
        elif r == r_tong:
            kieu = "t3"
        else:
            kieu = "chinh" if src[f"A{r}"].value is not None else "con"
        for c in vcols:
            v = src[f"{c}{r}"].value
            if v is not None:
                ws[f"{c}{r}"] = doi_ref(v)
            ws[f"{c}{r}"]._style = copy(stv[kieu][c])
        # ghi rõ cước vận chuyển vào cột nguồn mua
        cuoc = srv[f"P{r}"].value
        if kieu == "chinh" and cuoc:
            ws[f"H{r}"] = ((src[f"H{r}"].value or "Giá tại nguồn") +
                           f"; cộng cước ô tô tự đổ 10T, cự ly 30 km: {cuoc:,.0f} đ/{src[f'F{r}'].value}"
                           .replace(",", "."))
        ws.row_dimensions[r].height = max(src.row_dimensions[r].height or 15, 15)
    ws["A2"] = "(Theo thông báo giá vật liệu xây dựng tháng 8 năm 2026 của Sở Xây dựng TP. Hồ Chí Minh; giá cao nhất trong thông báo)"
    ws.print_area = f"A1:AD{r_tong}"
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0

    # ============================== 4. NHÂN CÔNG, MÁY THI CÔNG (chép từ F1, giữ định dạng F1)
    for ten in ("Nhân công", "Máy thi công"):
        s = f1[ten]
        ws = wb.create_sheet(ten, index=wb.sheetnames.index("Vật liệu") + 1 if ten == "Nhân công"
                             else wb.sheetnames.index("Nhân công") + 1)
        for row in s.iter_rows():
            for c in row:
                d = ws.cell(row=c.row, column=c.column, value=doi_ref(c.value))
                if c.has_style:
                    chep_kieu(d, c)
        for k_, dim in s.column_dimensions.items():
            ws.column_dimensions[k_].width = dim.width
            ws.column_dimensions[k_].hidden = dim.hidden
        for k_, dim in s.row_dimensions.items():
            ws.row_dimensions[k_].height = dim.height
        for m in s.merged_cells.ranges:
            ws.merge_cells(str(m))
        ws.page_setup.orientation, ws.page_setup.paperSize = "landscape", 9
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
        ws.oddFooter.center.text = "Trang &P/&N"
    q_nc = next(r for r in range(7, f1["Nhân công"].max_row + 1) if f1["Nhân công"][f"E{r}"].value == "Cộng nhân công:")
    q_m = next(r for r in range(7, f1["Máy thi công"].max_row + 1) if f1["Máy thi công"][f"D{r}"].value == "Cộng Máy:")

    # ============================== 5. TỔNG HỢP DỰ TOÁN (bố cục 5 cột của mẫu, khoản mục theo F1)
    ws = wb["Tổng hợp du toan (2)"]
    ws.title = "Tổng hợp dự toán"
    hs = {f1["Hệ số"][f"B{r}"].value: f1["Hệ số"][f"C{r}"].value for r in range(2, 29)}
    C, TT, TL, VAT, LT = hs["hsC"], hs["hsTT"], hs["hsTL"], hs["hsGTGT"], hs["hsGxdnt"]
    t5 = "ABCDE"
    stt_ = {k: {c: copy(ws[f"{c}{r}"]._style) for c in t5}
            for k, r in (("nhom", 6), ("muc", 7), ("con", 8), ("cong", 13), ("muc2", 15), ("tl", 19),
                         ("gxd", 22), ("tdt", 23), ("chu", 24), ("ngay", 26))}
    ky = {r: (ws[f"A{r}"].value, copy(ws[f"A{r}"]._style), ws.row_dimensions[r].height) for r in range(27, 37)}
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=6, max_col=12):
        for c in row:
            if not isinstance(c, MergedCell):
                c.value = None
    xoa_tu(ws, 6)
    for c in t5:
        ws[f"{c}4"]._style = copy(ws[f"{c}3"]._style)
    ws.merge_cells("A4:E4")
    ws["A2"], ws["A3"], ws["A4"] = "='Công trình'!A3", "='Công trình'!A4", "='Công trình'!A5"

    def pct(x):
        return f"{x * 100:g}".replace(".", ",") + "%"

    dong = [  # (stt, nội dung, ký hiệu, cách tính (công thức chữ), thành tiền, kiểu)
        ("I", "CHI PHÍ TRỰC TIẾP", None, None, None, "nhom"),
        (1, "Chi phí vật liệu", "VL", '"Theo bảng tổng hợp vật liệu"', "=ROUND('Vật liệu'!AD{v},0)".format(v=r_tong), "muc"),
        (2, "Chi phí nhân công", "NC", '"Theo bảng tổng hợp nhân công"', f"=ROUND('Nhân công'!Q{q_nc},0)", "muc"),
        (3, "Chi phí máy thi công", "M", '"Theo bảng tổng hợp máy thi công"', f"=ROUND('Máy thi công'!Q{q_m},0)", "muc"),
        ("", "Chi phí trực tiếp", "T", '=C{a}&" + "&C{b}&" + "&C{c}', "=E{a}+E{b}+E{c}", "cong"),
        ("II", "CHI PHÍ GIÁN TIẾP", None, None, None, "nhom"),
        (1, "Chi phí chung", "C", f'=C{{t}}&" x {pct(C)}"', f"=ROUND(E{{t}}*{C},0)", "muc2"),
        (2, "Chi phí một số công việc không xác định được khối lượng từ thiết kế", "TT",
         f'=C{{t}}&" x {pct(TT)}"', f"=ROUND(E{{t}}*{TT},0)", "muc2"),
        ("", "Chi phí gián tiếp", "GT", '=C{c1}&" + "&C{c2}', "=E{c1}+E{c2}", "cong"),
        ("III", "THU NHẬP CHỊU THUẾ TÍNH TRƯỚC", "TL", f'="("&C{{t}}&" + "&C{{gt}}&") x {pct(TL)}"',
         f"=ROUND((E{{t}}+E{{gt}})*{TL},0)", "tl"),
        ("", "Chi phí xây dựng trước thuế", "G", '=C{t}&" + "&C{gt}&" + "&C{tl}', "=E{t}+E{gt}+E{tl}", "cong"),
        ("IV", "THUẾ GIÁ TRỊ GIA TĂNG", "GTGT", f'=C{{g}}&" x {pct(VAT)}"', f"=ROUND(E{{g}}*{VAT},0)", "tl"),
        ("V", "CHI PHÍ XÂY DỰNG SAU THUẾ", "Gxd", '=C{g}&" + "&C{vat}', "=E{g}+E{vat}", "gxd"),
        ("VI", "CHI PHÍ NHÀ TẠM ĐỂ Ở VÀ ĐIỀU HÀNH THI CÔNG", "LT",
         f'=C{{g}}&" x {pct(LT)} x (1 + {pct(VAT)})"', f"=ROUND(E{{g}}*{LT}*(1+{VAT}),0)", "tl"),
        ("", "TỔNG DỰ TOÁN HẠNG MỤC", "Tdt", '=C{gxd}&" + "&C{lt}', "=E{gxd}+E{lt}", "gxd"),
        ("", "Làm tròn", None, None, "=ROUND(E{tdt},-3)", "tdt"),
    ]
    r0 = 6
    rr = {}
    keys = [None, "vl", "nc", "m", "t", None, "c1", "c2", "gt", "tl", "g", "vat", "gxd", "lt", "tdt", "lam"]
    for i, k_ in enumerate(keys):
        if k_:
            rr[k_] = r0 + i
    rr.update(a=rr["vl"], b=rr["nc"], c=rr["m"])
    for i, (stt, nd, kh, ct, tt, kieu) in enumerate(dong):
        r = r0 + i
        for c in t5:
            ws[f"{c}{r}"]._style = copy(stt_[kieu][c])
        ws[f"A{r}"], ws[f"B{r}"], ws[f"C{r}"] = stt, nd, kh
        if ct:
            ws[f"D{r}"] = ct.format(**rr) if ct.startswith("=") else "=" + ct
        if tt:
            ws[f"E{r}"] = tt.format(**rr)
        ws.row_dimensions[r].height = 30 if len(nd) > 55 else 21.95
    r_lam = rr["lam"]
    # Bằng chữ: tính lại đúng như công thức trong file (để viết chữ)
    sv = f1v
    VLv = round(sv["Vật liệu"][f"AD{r_tong}"].value)
    NCv = round(sv["Nhân công"][f"Q{q_nc}"].value)
    Mv = round(sv["Máy thi công"][f"Q{q_m}"].value)
    T = VLv + NCv + Mv
    Cv, TTv = round(T * C), round(T * TT)
    GT = Cv + TTv
    TLv = round((T + GT) * TL)
    G = T + GT + TLv
    VATv = round(G * VAT)
    Gxd = G + VATv
    LTv = round(G * LT * (1 + VAT))
    lam = round(Gxd + LTv, -3)
    r = r_lam + 1
    for c in t5:
        ws[f"{c}{r}"]._style = copy(stt_["chu"][c])
    ws.merge_cells(f"A{r}:E{r}")
    ws[f"A{r}"] = "Bằng chữ: " + bang_chu(lam)
    r += 2
    ws.merge_cells(f"C{r}:E{r}")
    ws[f"C{r}"] = "TP. Hồ Chí Minh, ngày ...... tháng ...... năm 2026"
    ws[f"C{r}"]._style = copy(stt_["ngay"]["C"])
    noi = {27: "ĐƠN VỊ LẬP", 28: "CÔNG TY CỔ PHẦN TƯ VẤN ĐẦU TƯ XÂY DỰNG", 29: "GIA NGUYỄN", 30: "GIÁM ĐỐC",
           34: "(Họ tên Giám đốc - anh bổ sung)", 35: "NGƯỜI LẬP",
           36: "(Họ tên, chứng chỉ KS định giá XD hạng ... số ... - anh bổ sung)"}
    for k_, txt in noi.items():
        rr_ = r + (k_ - 26)
        ws.merge_cells(f"A{rr_}:E{rr_}")
        ws[f"A{rr_}"] = txt
        ws[f"A{rr_}"]._style = copy(ky[k_][1])
        ws.row_dimensions[rr_].height = ky[k_][2]
    ws.print_area = f"A1:E{r + 10}"
    for rr_ in range(1, r + 11):
        ws.row_dimensions[rr_].hidden = False

    # ============================== 6. BÌA
    bia = wb["Bìa du toan (2)"]
    bia.title = "Bìa dự toán"
    bia["A3"] = "(CHỦ ĐẦU TƯ / CƠ QUAN CHỦ QUẢN - anh bổ sung)"
    bia["D15"] = CONG_TRINH.split(": ", 1)[1]
    bia["D16"] = DIA_DIEM.split(": ", 1)[1]
    for m in list(bia.merged_cells.ranges):
        if m.min_row == 17:
            bia.unmerge_cells(str(m))
    bia["C17"] = "HẠNG MỤC:"
    bia["C17"]._style = copy(bia["C16"]._style)
    bia.merge_cells("D17:O17")
    bia["D17"] = HANG_MUC.split(": ", 1)[1]
    bia["D17"]._style = copy(bia["D16"]._style)
    bia["A29"] = "TP. Hồ Chí Minh, năm 2026"
    for c in ("R1", "R2"):
        bia[c] = None
    # mẫu gốc không đặt vùng in nên bìa tràn 3 trang: in vừa 1 trang A4 ngang
    bia.print_area = "A1:O31"
    bia.sheet_properties.pageSetUpPr.fitToPage = True
    bia.page_setup.fitToWidth, bia.page_setup.fitToHeight = 1, 1

    # Thứ tự sheet: Bìa, Tổng hợp, Công trình, Hao phí, Vật liệu, Nhân công, Máy
    thu_tu = ["Bìa dự toán", "Tổng hợp dự toán", "Công trình", "Hao phí vật tư", "Vật liệu", "Nhân công", "Máy thi công"]
    wb._sheets = [wb[t] for t in thu_tu]
    wb.active = 1
    wb.save(KQ)
    print("Đã lập:", KQ)
    print(f"VL={VLv:,} NC={NCv:,} M={Mv:,} T={T:,} Gxd={Gxd:,} LT={LTv:,} Làm tròn={lam:,}")
    print(bang_chu(lam))


if __name__ == "__main__":
    main()

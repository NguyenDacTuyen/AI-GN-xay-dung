# -*- coding: utf-8 -*-
"""
Lập BẢNG TỔNG HỢP DỰ TOÁN XÂY DỰNG CÔNG TRÌNH (theo mẫu công ty template/du-toan/tong-hop/bang-du-toan-tong-hop.xlsx)
cho dự án gồm hạng mục Bể tự hoại 10 m³ (cách A: file hạng mục dừng ở chi phí xây dựng, file này tính các chi phí còn lại).

Nguồn số liệu:
  - Chi phí xây dựng: ket-qua/be-tu-hoai-10m3/du-toan_be-tu-hoai-10m3_TT38-HCM.xlsx (sheet "Tổng hợp dự toán").
  - Tỷ lệ chi phí QLDA, tư vấn, chi phí khác: sheet "TMĐT" của file F1 xuất ra F1-xuat_be-tu-hoai-10m3_TMDT.xlsm
    (F1 tra bảng TT 38/2026/TT-BXD; anh chốt 23/10/2026: công trình hạ tầng kỹ thuật, cấp IV, thiết kế 1 bước, dự phòng 5%).
  - Danh mục khoản chi phí: theo mẫu công ty; khoản nào hạng mục không có thì bỏ.

Chạy:  python python/tong_hop_be_tu_hoai.py
"""
import os, sys, tempfile
from copy import copy

import openpyxl
from openpyxl.cell.cell import MergedCell
from openpyxl.styles import Alignment, Border, Font, PatternFill
from openpyxl.worksheet.pagebreak import RowBreak

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THU_MUC = os.path.join(GOC, "ket-qua", "be-tu-hoai-10m3")
MAU = os.path.join(GOC, "template", "du-toan", "tong-hop", "bang-du-toan-tong-hop.xlsx")
DT_HM = os.path.join(THU_MUC, "du-toan_be-tu-hoai-10m3_TT38-HCM.xlsx")
F1_TMDT = os.path.join(THU_MUC, "F1-xuat_be-tu-hoai-10m3_TMDT.xlsm")
KQ = os.path.join(THU_MUC, "du-toan_tong-hop.xlsx")
sys.path.insert(0, os.path.join(GOC, "python"))
from chuyen_f1_ve_mau_ha_tang import bang_chu

DU_AN = "DỰ ÁN: ...................................................... (ANH BỔ SUNG)"
DIA_DIEM = "ĐỊA ĐIỂM: ......................................, THÀNH PHỐ HỒ CHÍ MINH"
FILE_HM = os.path.basename(DT_HM)


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


def doc_hang_muc():
    ws = mo_excel(DT_HM)["Tổng hợp dự toán"]
    v = {ws[f"C{r}"].value: ws[f"E{r}"].value for r in range(6, ws.max_row + 1) if ws[f"C{r}"].value}
    return v


def doc_ty_le():
    """Tỷ lệ (cột E) và mức tối thiểu trong công thức F1, tìm dòng theo nội dung."""
    wsv = mo_excel(F1_TMDT)["TMĐT"]
    ten = {r: str(wsv[f"B{r}"].value or "") for r in range(10, 80)}
    loai = f"{wsv['E5'].value} - {wsv['E6'].value} - {wsv['E7'].value}"

    def tl(*tu):
        for r, t in ten.items():
            if all(x in t for x in tu):
                return wsv[f"E{r}"].value
        raise KeyError(tu)
    return loai, {
        "QLDA": tl("Chi phí quản lý dự án"),
        "BCKTKT": tl("lập báo cáo kinh tế - kỹ thuật", "Bảng 2.5"),
        "TT_TK": tl("thẩm tra thiết kế xây dựng"),
        "TT_DT": tl("thẩm tra dự toán công trình"),
        "GS": tl("giám sát thi công xây dựng"),
        "HSMT": tl("lập hồ sơ mời thầu, đánh giá hồ sơ dự thầu thi công xây dựng"),
        "TD_HSMT": tl("thẩm định hồ sơ mời thầu, hồ sơ yêu cầu"),
        "TD_KQ": tl("thẩm định kết quả lựa chọn nhà thầu"),
        "TD_DA": tl("Phí thẩm định dự án đầu tư"),
        "KTOAN": tl("kiểm toán độc lập"),
        "QTOAN": tl("thẩm tra, phê duyệt quyết toán"),
        "NTHU": tl("kiểm tra công tác nghiệm thu"),
        "DP": tl("Dự phòng cho yếu tố khối lượng"),
    }


def pct(x):
    return f"{x * 100:.3f}".rstrip("0").rstrip(".").replace(".", ",") + "%"


def main():
    if os.path.exists(KQ):
        raise SystemExit(f"File đã có, không ghi đè: {KQ}")
    hm = doc_hang_muc()
    loai, t = doc_ty_le()
    VAT = hm["GTGT"] / hm["G"]
    VAT = round(VAT, 4)

    import shutil
    shutil.copy(MAU, KQ)
    wb = openpyxl.load_workbook(KQ)
    for ws in list(wb.worksheets):
        if ws.title != "TH TMDT":
            wb.remove(ws)                      # bỏ các sheet khác (kể cả sheet ẩn) mà không đọc
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
    ws["A2"], ws["A3"] = DU_AN, DIA_DIEM
    ws["L4"], ws["M4"] = "Thuế suất GTGT:", VAT          # ô tham số VAT duy nhất
    ws["M4"].number_format = "0%"
    V = "$M$4"

    dong = []   # (kiểu, A, B, C, D, E(cách tính), G, H, I, J)
    r0 = 7

    def them(*a):
        dong.append(a)
        return r0 + len(dong) - 1

    rI = them("nhom", "I", "Chi phí xây dựng", "GXD", None, '="GXD1 + GXD2 (nhà tạm chỉ cộng sau thuế)"', "SUMG", None, None, None)
    r_hm = them("muc", None, "- Chi phí xây dựng hạng mục Bể tự hoại BTCT 3 ngăn 10 m³ (hạ tầng kỹ thuật)", "GXD1", None,
                "Theo bảng tổng hợp dự toán hạng mục (*)", hm["G"], hm["GTGT"], "GH", "Dự toán hạng mục GN2026-HT-01")
    r_lt = them("muc", None, "- Chi phí nhà tạm để ở và điều hành thi công", "GXD2", None,
                "Theo bảng tổng hợp dự toán hạng mục, đã gồm VAT (*)", None, None, hm["LT"], "TT 36/2026/TT-BXD")
    B = f"$G${rI}"           # GXD trước thuế (không gồm nhà tạm) - cơ sở tính các tỷ lệ, giống F1
    rII = them("nhom", "II", "Chi phí quản lý dự án", "GQLDA", t["QLDA"], '="GXD trước thuế x "&D{r}',
               f"=ROUND({B}*D{{r}},0)", f"=ROUND(G{{r}}*{V},0)", "GH", "Bảng 1.1 TT 38/2026/TT-BXD")
    rIII = them("nhom2", "III", "Chi phí tư vấn đầu tư xây dựng", "GTV", None, None, "SUBG", "SUBH", "SUBI", None)
    tv = [
        them("muc", 1, "- Chi phí lập Báo cáo kinh tế - kỹ thuật", "GTV1", t["BCKTKT"], '="GXD trước thuế x "&D{r}&" (tối thiểu 5 triệu)"',
             f"=ROUND(MAX({B}*D{{r}},5000000),0)", f"=ROUND(G{{r}}*{V},0)", "GH", "Bảng 2.5 TT 38/2026/TT-BXD"),
        them("muc", 2, "- Chi phí thẩm tra thiết kế bản vẽ thi công", "GTV2", t["TT_TK"], '="GXD trước thuế x "&D{r}&" (tối thiểu 2 triệu)"',
             f"=ROUND(MAX({B}*D{{r}},2000000),0)", f"=ROUND(G{{r}}*{V},0)", "GH", "Bảng 2.19 TT 38/2026/TT-BXD"),
        them("muc", 3, "- Chi phí thẩm tra dự toán xây dựng", "GTV3", t["TT_DT"], '="GXD trước thuế x "&D{r}&" (tối thiểu 2 triệu)"',
             f"=ROUND(MAX({B}*D{{r}},2000000),0)", f"=ROUND(G{{r}}*{V},0)", "GH", "Bảng 2.20 TT 38/2026/TT-BXD"),
        them("muc", 4, "- Chi phí giám sát thi công xây dựng", "GTV4", t["GS"], '="GXD trước thuế x "&D{r}',
             f"=ROUND({B}*D{{r}},0)", f"=ROUND(G{{r}}*{V},0)", "GH", "Bảng 2.24 TT 38/2026/TT-BXD"),
        them("muc", 5, "- Chi phí lập HSMT và đánh giá HSDT thi công xây dựng", "GTV5", t["HSMT"], '="GXD trước thuế x "&D{r}',
             f"=ROUND({B}*D{{r}},0)", f"=ROUND(G{{r}}*{V},0)", "GH", "Bảng 2.22 TT 38/2026/TT-BXD"),
        them("muc", 6, "- Chi phí thẩm định hồ sơ mời thầu gói thầu thi công xây dựng", "GTV6", t["TD_HSMT"],
             '="GXD sau thuế x "&D{r}&" (tối thiểu 2 triệu, tối đa 60 triệu)"',
             f"=ROUND(MIN(MAX($I${rI}*D{{r}},2000000),60000000),0)", 0, "GH", "NĐ 214/2025/NĐ-CP"),
        them("muc", 7, "- Chi phí thẩm định kết quả lựa chọn nhà thầu gói thầu thi công xây dựng", "GTV7", t["TD_KQ"],
             '="GXD sau thuế x "&D{r}&" (tối thiểu 3 triệu, tối đa 60 triệu)"',
             f"=ROUND(MIN(MAX($I${rI}*D{{r}},3000000),60000000),0)", 0, "GH", "NĐ 214/2025/NĐ-CP"),
    ]
    rIV = them("nhom2", "IV", "Chi phí khác", "GK", None, None, "SUBG", "SUBH", "SUBI", None)
    base_tm = f"($I${rI}+$I${rII}+$I${rIII})"     # tổng mức tạm tính để tính phí thẩm định, kiểm toán, quyết toán
    ck = [
        them("muc", 1, "- Phí thẩm định dự án đầu tư xây dựng", "K1", t["TD_DA"],
             '="(GXD + GQLDA + GTV) x "&D{r}&" (tối thiểu 500.000, tối đa 150 triệu)"',
             f"=ROUND(MIN(MAX({base_tm}*D{{r}},500000),150000000),0)", 0, "GH", "TT 28/2023/TT-BTC"),
        them("muc", 2, "- Chi phí kiểm toán độc lập", "K2", t["KTOAN"],
             '="(GXD + GQLDA + GTV) x "&D{r}&" (tối thiểu 1 triệu)"',
             f"=ROUND(MAX({base_tm}*D{{r}},1000000),0)", f"=ROUND(G{{r}}*{V},0)", "GH", "NĐ 193/2026/NĐ-CP"),
        them("muc", 3, "- Chi phí thẩm tra, phê duyệt quyết toán", "K3", t["QTOAN"],
             '="(GXD + GQLDA + GTV) x "&D{r}&" (tối thiểu 500.000)"',
             f"=ROUND(MAX({base_tm}*D{{r}},500000),0)", 0, "GH", "NĐ 193/2026/NĐ-CP"),
        them("muc", 4, "- Chi phí kiểm tra công tác nghiệm thu công trình", "K4", t["NTHU"],
             '="GTV4 trước thuế x "&D{r}', f"=ROUND($G${tv[3]}*D{{r}},0)", f"=ROUND(G{{r}}*{V},0)", "GH", "TT 10/2021/TT-BXD"),
    ]
    rV = them("nhom2", "V", "Chi phí dự phòng", "GDP", None, '="GDP1 + GDP2"', None, None, "DP", None)
    rdp1 = them("dp", "5.1", " - Chi phí dự phòng cho yếu tố khối lượng", "GDP1", t["DP"],
                '="(GXD + GQLDA + GTV + GK) x "&D{r}', None, None,
                f"=ROUND((I{rI}+I{rII}+I{rIII}+I{rIV})*D{{r}},0)", "TT 38/2026/TT-BXD")
    rdp2 = them("dp", "5.2", " - Chi phí dự phòng cho yếu tố trượt giá", "GDP2", None,
                "Không tính (thời gian thực hiện dưới 1 năm - anh xác nhận)", None, None, 0, None)
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
            g, h, iv = f"=G{r_hm}", f"=H{r_hm}", f"=I{r_hm}+I{r_lt}"
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
    # Bằng chữ: tính lại đúng như công thức để viết chữ
    r = rR + 1
    for col in cols:
        ws[f"{col}{r}"]._style = copy(st["chu"][col])
    ws.merge_cells(f"A{r}:J{r}")
    ws[f"A{r}"] = "Bằng chữ: (xem dòng dưới, chương trình điền sau khi tính)"
    r_chu = r
    r += 1
    ws[f"A{r}"] = (f"(*) Chi phí xây dựng lấy từ file {FILE_HM}, sheet \"Tổng hợp dự toán\" (ký hiệu G, GTGT, LT). "
                   "Tỷ lệ chi phí lấy từ phần mềm Dự toán F1 (TT 38/2026/TT-BXD; công trình hạ tầng kỹ thuật, cấp IV, thiết kế 1 bước).")
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
    print("Thiết lập F1:", loai)
    for k_, rr in (("GXD", rI), ("GQLDA", rII), ("GTV", rIII), ("GK", rIV), ("GDP", rV), ("TMĐT", rT), ("Làm tròn", rR)):
        print(f"{k_:9} {wv[f'G{rr}'].value or 0:>14,.0f} {wv[f'H{rr}'].value or 0:>12,.0f} {wv[f'I{rr}'].value or 0:>14,.0f}")
    print(bang_chu(tong))


if __name__ == "__main__":
    main()

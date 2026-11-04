# -*- coding: utf-8 -*-
"""
BÓC KHỐI LƯỢNG TỔNG HỢP TRÊN 1 FILE MẪU: THOÁT NƯỚC + GIAO THÔNG
------------------------------------------------------------------
Một lần chạy ra 1 file Excel đủ các sheet (theo mẫu mau-boc-khoi-luong-tong-hop.xlsx):
  - Dao dap cong, Dao dap ho ga, Moi noi-goi cong : bóc TỰ ĐỘNG từ bản vẽ DXF trắc dọc thoát nước.
  - Dao dap nen duong                              : đổ từ file CSV xuất ra từ phần mềm ADSdesign (giao thông).
  - Tong hop                                       : tự cộng, công thức tự tìm dòng TỔNG.

Công cụ này GỌI LẠI 2 chương trình có sẵn trong cùng thư mục:
  boc-ham-ga-thoat-nuoc.py  và  boc-cong-moinoi-thoat-nuoc.py
rồi: điền đúng 3 cột cuối hầm ga (VK lót=Q, BT lót=R, cừ tràm=S), dựng lại sheet giao thông
theo số công tác trong CSV, và kẻ viền ngoài cùng của mọi bảng thành nét đậm.

Cần: Python + ezdxf + openpyxl  (cài 1 lần: pip install ezdxf openpyxl)
Chạy: sửa phần CẤU HÌNH rồi chạy, hoặc nhấp đúp chay-boc-tong-hop.bat.

LƯU Ý QUAN TRỌNG (để không lệch cột):
  Các cột trong chương trình phải KHỚP TIÊU ĐỀ từng tab của file mẫu. Nếu anh sửa lại bố cục
  cột trong mẫu thì phải chỉnh lại chương trình cho khớp, nếu không số sẽ ghi sai cột.
"""
import importlib.util, openpyxl, os, csv, tempfile
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.worksheet.properties import PageSetupProperties
from openpyxl.worksheet.page import PageMargins

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)

# ================== CẤU HÌNH (anh sửa ở đây) ==================
MAU = os.path.join(PROJ, "template", "du-toan", "thoat-nuoc-giao-thong",
                   "mau-boc-khoi-luong-tong-hop.xlsx")       # file mẫu tổng hợp (không sửa file này)
DXF = r"F:/demo/Acad_BD_TD_TN Nhi Binh 5.dxf"                # bản vẽ trắc dọc thoát nước
CSV_GIAOTHONG = r"F:/demo/Bang khoi luong xuat tu phan mem addesign.csv"  # CSV giao thông; để "" nếu công trình KHÔNG có phần giao thông
OUT = os.path.join(PROJ, "ket-qua", "06_tong-hop-1-file", "KL-tong-hop_CONGTRINH.xlsx")

# Tên công tác giao thông chuẩn, theo đúng THỨ TỰ cột trong CSV ADSdesign:
CONGTAC_GIAOTHONG = ["Đắp vỉa hè", "Đắp nền đường", "Đào nền", "Đào khuôn", "Vét bùn",
                     "Đánh cấp", "Bù vênh đường cũ", "Đắp Taluy", "Đắp đất trồng cây"]
# =============================================================


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def main():
    tmp = tempfile.mkdtemp(prefix="boctonghop_")
    s1 = os.path.join(tmp, "s1.xlsx"); s2 = os.path.join(tmp, "s2.xlsx")

    # --- 1) Hầm ga -> tab "Dao dap ho ga" ---
    hg = _load("bhg", "boc-ham-ga-thoat-nuoc.py"); hg.MAU = MAU; hg.OUT = s1; hg.DXF = DXF; hg.main()
    # --- 2) Cống + mối nối/gối -> "Dao dap cong" + "Moi noi-goi cong" ---
    cm = _load("bcm", "boc-cong-moinoi-thoat-nuoc.py"); cm.MAU = s1; cm.OUT = s2; cm.DXF = DXF; cm.main()

    wb = openpyxl.load_workbook(s2)
    thin = Side(style="thin"); med = Side(style="medium"); BOX = Border(thin, thin, thin, thin)
    TN = Font(name="Times New Roman", size=11); DAM = Font(name="Times New Roman", size=11, bold=True)
    CEN = Alignment("center", "center", wrap_text=True)

    def find_tong(w):
        for rr in range(w.max_row, 1, -1):
            if w.cell(rr, 1).value == "TỔNG": return rr

    # --- 3) Hầm ga: mẫu đã có sẵn cột Q=VK lót, R=BT lót M150, S=cừ tràm -> ghi ĐÚNG cột ---
    wh = wb["Dao dap ho ga"]; tgh = find_tong(wh)
    for r in range(6, tgh):
        wh.cell(r, 17).value = f"=4*I{r}*'Thong so'!$B$14"   # Q: VK lót hầm ga (m2)
        wh.cell(r, 18).value = f"=I{r}^2*'Thong so'!$B$14"   # R: BT lót hầm ga M150 (m3)
        wh.cell(r, 19).value = f"=J{r}^2"                    # S: DT cừ tràm (m2)
        for c in (17, 18, 19):
            cc = wh.cell(r, c); cc.number_format = "0.000"; cc.border = BOX; cc.font = TN; cc.alignment = CEN
    for c in (17, 18, 19):
        L = get_column_letter(c); tc = wh.cell(tgh, c); tc.value = f"=SUM({L}6:{L}{tgh-1})"
        tc.number_format = "0.000"; tc.border = BOX; tc.font = DAM; tc.alignment = CEN

    # --- 4) Giao thông: dựng lại sheet "Dao dap nen duong" theo CSV (số cột động) ---
    if CSV_GIAOTHONG and os.path.exists(CSV_GIAOTHONG):
        _boc_giao_thong(wb, CSV_GIAOTHONG, med, thin, TN, DAM)

    # --- 5) Viền ngoài cùng mọi bảng = nét đậm (medium), giữ nguyên viền trong ---
    for sn in ("Dao dap cong", "Moi noi-goi cong", "Dao dap ho ga", "Dao dap nen duong"):
        if sn in wb.sheetnames: _vien_ngoai_dam(wb[sn], med)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    try:
        wb.save(OUT); print("XONG. File tong hop:", OUT)
    except PermissionError:
        print("!! File ket qua dang mo trong Excel. Dong file roi chay lai.")


def _boc_giao_thong(wb, csvf, med, thin, TN, DAM):
    raw = open(csvf, 'rb').read().decode('cp1258', errors='replace')
    rows = list(csv.reader(raw.splitlines(), delimiter=','))
    hdr0 = rows[0]; end = len(hdr0)
    for i, v in enumerate(hdr0):
        if 'trung' in v.lower() and i > 3: end = i; break
    nct = end - 3
    names = [CONGTAC_GIAOTHONG[i] if i < len(CONGTAC_GIAOTHONG)
             else (rows[1][3+i].strip() or "Công tác %d" % (i+1)) for i in range(nct)]
    cocs = []
    for jdx, r in enumerate(rows):
        if len(r) > 3+nct-1 and r[0].strip().isdigit():
            ten = r[1].strip(); dt = []
            for c in range(3, 3+nct):
                try: dt.append(float(r[c].replace(',', '.')))
                except: dt.append(0.0)
            kc = None
            if jdx+1 < len(rows) and len(rows[jdx+1]) > 2:
                try: kc = float(rows[jdx+1][2].strip().replace(',', '.'))
                except: kc = None
            cocs.append([ten, dt, kc])
    N = len(cocs); ncol = 3 + 2*nct

    SHN = "Dao dap nen duong"
    idx = wb.sheetnames.index(SHN); wb.remove(wb[SHN]); ws = wb.create_sheet(SHN, idx)
    T20 = Font(name="Times New Roman", size=20, bold=True); T14 = Font(name="Times New Roman", size=14, bold=True)
    T13 = Font(name="Times New Roman", size=13, bold=True); IT = Font(name="Times New Roman", size=10, italic=True)
    xam = PatternFill("solid", fgColor="DDEBF7"); xanh = PatternFill("solid", fgColor="E2EFDA")
    vang = PatternFill("solid", fgColor="FFF2CC"); C = Alignment("center", "center", wrap_text=True)
    ws.page_setup.orientation = "landscape"; ws.page_setup.paperSize = 9; ws.print_title_rows = "5:6"
    ws.cell(1, 1, "BẢNG TÍNH KHỐI LƯỢNG ĐÀO ĐẮP NỀN ĐƯỜNG").font = T20; ws.cell(1, 1).alignment = C
    ws.cell(2, 1, "CÔNG TRÌNH: ......").font = T14; ws.cell(2, 1).alignment = C
    ws.cell(3, 1, "ĐỊA ĐIỂM: ......").font = T13; ws.cell(3, 1).alignment = C
    H1, H2 = 5, 6
    for i, h in enumerate(["STT", "Tên cọc", "Khoảng cách lẻ (m)"], 1):
        cell = ws.cell(H1, i, h); cell.font = DAM; cell.alignment = C; cell.fill = xam; ws.cell(H2, i).fill = xam
    c = 4
    for nm in names:
        cell = ws.cell(H1, c, nm); cell.font = DAM; cell.alignment = C; cell.fill = xam; ws.cell(H1, c+1).fill = xam
        ws.cell(H2, c, "Diện tích (m²)").font = DAM; ws.cell(H2, c).alignment = C; ws.cell(H2, c).fill = xanh
        ws.cell(H2, c+1, "Khối lượng (m³)").font = DAM; ws.cell(H2, c+1).alignment = C; ws.cell(H2, c+1).fill = xam
        c += 2
    DSTART = 7
    for i, (ten, dt, kc) in enumerate(cocs):
        r = DSTART+i
        ws.cell(r, 1, i+1); ws.cell(r, 2, ten); ws.cell(r, 3, (0 if i == 0 else cocs[i-1][2]))
        cc = 4
        for di in range(nct):
            ws.cell(r, cc, round(dt[di], 2)); ws.cell(r, cc).number_format = "0.00"; ws.cell(r, cc).fill = vang
            X = get_column_letter(cc)
            ws.cell(r, cc+1).value = 0 if i == 0 else f"=({X}{r}+{X}{r-1})/2*C{r}"
            ws.cell(r, cc+1).number_format = "0.000"; cc += 2
        ws.cell(r, 3).number_format = "0.00"
    tong = DSTART+N
    ws.cell(tong, 1, "TỔNG"); cc = 4
    for di in range(nct):
        ws.cell(tong, cc).number_format = "0.00"; kl = get_column_letter(cc+1)
        ws.cell(tong, cc+1).value = f"=SUM({kl}{DSTART}:{kl}{tong-1})"; ws.cell(tong, cc+1).number_format = "0.000"; cc += 2
    for r in range(H1, tong+1):
        for cc in range(1, ncol+1):
            cell = ws.cell(r, cc)
            cell.border = Border(left=med if cc == 1 else thin, right=med if cc == ncol else thin,
                                 top=med if r == H1 else thin, bottom=med if r == tong else thin)
            cell.font = DAM if (r in (H1, H2) or r == tong or cc == 2) else TN
            cell.alignment = C
    for r in (1, 2, 3): ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=ncol)
    for i in (1, 2, 3): ws.merge_cells(start_row=H1, start_column=i, end_row=H2, end_column=i)
    c = 4
    for _ in names: ws.merge_cells(start_row=H1, start_column=c, end_row=H1, end_column=c+1); c += 2
    ws.merge_cells(start_row=tong, start_column=1, end_row=tong, end_column=3)
    ws.cell(4, 1, "Phương pháp mặt cắt: KL = (DT mặt cắt này + DT mặt cắt trước)/2 × khoảng cách lẻ. Số liệu từ bảng khối lượng ADSdesign.").font = IT
    ws.column_dimensions["A"].width = 5.140625; ws.column_dimensions["B"].width = 6.7109375; ws.column_dimensions["C"].width = 7.5
    cc = 4
    for di in range(nct):
        ws.column_dimensions[get_column_letter(cc)].width = 6.42578125
        ws.column_dimensions[get_column_letter(cc+1)].width = 8.7109375; cc += 2
    ws.row_dimensions[1].height = 35.1; ws.row_dimensions[2].height = 24.95; ws.row_dimensions[3].height = 24.95
    ws.row_dimensions[4].height = 15.75; ws.row_dimensions[5].height = 35.1; ws.row_dimensions[6].height = 53.25
    for r in range(7, tong+1): ws.row_dimensions[r].height = 24.95
    ws.page_margins = PageMargins(left=0.492126, right=0.03937, top=0.511811, bottom=0.669291)
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
    # chot canh phai cho o tieu de gop cuoi cung (o gop hay bi bo sot)
    for r in (5, 6):
        cc = ws.cell(r, ncol); b = cc.border
        cc.border = Border(left=b.left, right=med, top=med if r == 5 else b.top, bottom=b.bottom)
    print("   Giao thong: so cong tac", nct, "| so coc", N)


def _vien_ngoai_dam(w, med):
    rmin = rmax = cmin = cmax = None
    for row in w.iter_rows():
        for cell in row:
            b = cell.border
            if b and any(s and s.style for s in (b.left, b.right, b.top, b.bottom)):
                r, c = cell.row, cell.column
                rmin = r if rmin is None else min(rmin, r); rmax = r if rmax is None else max(rmax, r)
                cmin = c if cmin is None else min(cmin, c); cmax = c if cmax is None else max(cmax, c)
    if rmin is None: return
    for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
            if not (r in (rmin, rmax) or c in (cmin, cmax)): continue
            cell = w.cell(r, c); b = cell.border
            try:
                cell.border = Border(left=med if c == cmin else b.left, right=med if c == cmax else b.right,
                                     top=med if r == rmin else b.top, bottom=med if r == rmax else b.bottom)
            except Exception: pass


if __name__ == "__main__":
    main()

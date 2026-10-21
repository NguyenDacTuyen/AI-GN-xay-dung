# -*- coding: utf-8 -*-
"""
BỂ TỰ HOẠI BTCT 3 NGĂN, DUNG TÍCH HỮU ÍCH 10 m³ – dự án GN2026, bản vẽ GN2026-HT-01

Chương trình này là "nguồn số liệu duy nhất" cho bể:
  1. Khai báo kích thước, cao độ, cốt thép (phương án anh Tuyên đã duyệt ngày 20/10/2026).
  2. Tính bảng thống kê cốt thép và khối lượng các công tác (dùng cho dự toán).
  3. Sinh file AutoLISP  lisp/be-tu-hoai-10m3.lsp  để AutoCAD vẽ bản vẽ (tỷ lệ 1/50, đơn vị mm),
     đúng layer, text style, dim style của template ISO_CTY.dwt.
  4. Ghi số liệu ra  ket-qua/be-tu-hoai-10m3/so-lieu.json  để lập dự toán.

Cách chạy:  python python/be_tu_hoai_10m3.py
"""
import json, math, os

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # thư mục AI_Cad_K1

# ============================================================== 1. THÔNG SỐ (mm)
L1, L2, L3 = 2000, 1000, 1000      # chiều dài thông thủy: ngăn chứa, ngăn lắng, ngăn lọc
B = 1700                           # chiều rộng thông thủy
HN, HK = 1500, 300                 # chiều cao nước, khoảng khí
TW, TV, TD, TN = 200, 150, 250, 150  # dày thành, vách, đáy, nắp
MO = 200                           # đáy mở rộng mỗi bên (chống đẩy nổi)
LOT, CAT = 100, 200                # dày bê tông lót, cát đệm
LOT_RONG, CAT_RONG = 100, 100      # lót rộng hơn đáy, cát rộng hơn lót (mỗi bên)
CU_DAI, CU_MAT_DO = 4500, 25       # cừ tràm: dài (mm), mật độ (cây/m²)
C_DAY, C_THANH, C_NAP = 40, 35, 25 # lớp bê tông bảo vệ
LO_THAM = 600                      # ô nắp thăm 600x600, mỗi ngăn 1 ô
DAN_DAY = 80                       # đan nắp thăm, đan lọc dày 80
DA_LOC = 300                       # lớp đá 1x2 ngăn lọc
CAO_DAN_LOC = 300                  # đan lọc đặt cách đáy lòng bể

LT = L1 + L2 + L3 + 2 * TV         # dài lòng trong = 4300
HT = HN + HK                       # cao lòng trong = 1800
LO, BO, HO = LT + 2 * TW, B + 2 * TW, TD + HT + TN   # ngoài: 4700 x 2100 x 2200
LD, BD = LO + 2 * MO, BO + 2 * MO  # đáy mở rộng: 5100 x 2500

# Cao độ (m), mặt sân hoàn thiện = ±0.000 = mặt nắp
CD = {"nap": 0.0, "mn": -0.450, "ong_vao": -0.400, "day_long": -(TN + HT) / 1000,
      "day_kc": -HO / 1000, "day_lot": -(HO + LOT) / 1000, "day_cat": -(HO + LOT + CAT) / 1000}

# ============================================================== 2. THỐNG KÊ CỐT THÉP
def kg_m(d):                       # kg/m = 0,00617 x d²
    return 0.00617 * d * d

def so_thanh(chieu_dai, buoc):     # số thanh trên một chiều dài, bước a
    return math.floor(chieu_dai / buoc) + 1

THEP = []                          # [cấu kiện, số hiệu, hình dạng, d, dài 1 thanh, số lượng]
def them(ck, sh, hd, d, l, n):
    THEP.append({"cau_kien": ck, "so_hieu": sh, "hinh_dang": hd, "d": d, "l": l, "n": n})

them("Đáy bể", 1, "Bẻ 2 đầu 150", 12, LD - 2 * C_DAY + 300, so_thanh(BD - 2 * C_DAY, 200))
them("Đáy bể", 2, "Bẻ 2 đầu 150", 12, BD - 2 * C_DAY + 300, so_thanh(LD - 2 * C_DAY, 200))
them("Đáy bể", 3, "Bẻ 2 đầu 150", 12, LD - 2 * C_DAY + 300, so_thanh(BD - 2 * C_DAY, 200))
them("Đáy bể", 4, "Bẻ 2 đầu 150", 12, BD - 2 * C_DAY + 300, so_thanh(LD - 2 * C_DAY, 200))
n_dung = 2 * 2 * so_thanh(LO - 2 * C_THANH, 200) + 2 * 2 * so_thanh(BO - 2 * C_THANH, 200)
them("Thành bể", 5, "Chữ L, chân 200", 10, HO - C_DAY - C_NAP + 200, n_dung)
them("Thành bể", 6, "Vòng kín, nối 400", 10, 2 * ((LO - 2 * C_THANH) + (BO - 2 * C_THANH)) + 400,
     so_thanh(HO - C_DAY - C_NAP, 200))
them("Thành bể", 7, "Vòng kín, nối 400", 10, 2 * ((LT + 2 * C_THANH) + (B + 2 * C_THANH)) + 400,
     so_thanh(HT, 200))
them("Vách ngăn", 8, "Bẻ 2 đầu 150", 8, HT + 300, 2 * so_thanh(B, 200))
them("Vách ngăn", 9, "Bẻ 2 đầu 150", 8, B + 300, 2 * so_thanh(HT, 200))
them("Nắp bể", 10, "Bẻ 2 đầu 100", 10, LO - 2 * C_NAP + 200, so_thanh(BO - 2 * C_NAP, 200))
them("Nắp bể", 11, "Bẻ 2 đầu 100", 10, BO - 2 * C_NAP + 200, so_thanh(LO - 2 * C_NAP, 200))
them("Nắp bể", 12, "Bẻ 2 đầu 100", 8, LO - 2 * C_NAP + 200, so_thanh(BO - 2 * C_NAP, 200))
them("Nắp bể", 13, "Bẻ 2 đầu 100", 8, BO - 2 * C_NAP + 200, so_thanh(LO - 2 * C_NAP, 200))
them("Lỗ thăm", 14, "Thẳng", 12, LO_THAM + 2 * 400, 3 * 4 * 2)
them("Đan thăm", 15, "Thẳng", 6, LO_THAM - 30, 3 * 2 * so_thanh(LO_THAM - 30, 150))
them("Đan lọc", 16, "Thẳng", 6, B - 30, so_thanh(L3 - 30, 150))
them("Đan lọc", 17, "Thẳng", 6, L3 - 30, so_thanh(B - 30, 150))
for t in THEP:
    t["tong_m"] = round(t["l"] * t["n"] / 1000, 2)
    t["kg"] = round(t["tong_m"] * kg_m(t["d"]), 2)
TONG_D = {}
for t in THEP:
    TONG_D[t["d"]] = round(TONG_D.get(t["d"], 0) + t["kg"], 2)
TONG_KG = round(sum(TONG_D.values()), 2)

# ============================================================== 3. KHỐI LƯỢNG (cho dự toán)
m = 1 / 1000
V_LO_THAM = 3 * LO_THAM * LO_THAM * TN * m ** 3
KL = {
    "be_tong_day": round(LD * BD * TD * m ** 3, 3),
    "be_tong_thanh": round((2 * LO * TW * HT + 2 * B * TW * HT) * m ** 3, 3),
    "be_tong_vach": round(2 * B * TV * HT * m ** 3, 3),
    "be_tong_nap": round(LO * BO * TN * m ** 3 - V_LO_THAM, 3),
    "be_tong_dan_tham": round(3 * LO_THAM * LO_THAM * DAN_DAY * m ** 3, 3),
    "be_tong_dan_loc": round(L3 * B * DAN_DAY * m ** 3, 3),
    "be_tong_lot": round((LD + 2 * LOT_RONG) * (BD + 2 * LOT_RONG) * LOT * m ** 3, 3),
    "cat_dem": round((LD + 2 * LOT_RONG + 2 * CAT_RONG) * (BD + 2 * LOT_RONG + 2 * CAT_RONG) * CAT * m ** 3, 3),
    "dien_tich_cu": round((LD + 2 * LOT_RONG + 2 * CAT_RONG) * (BD + 2 * LOT_RONG + 2 * CAT_RONG) * m ** 2, 3),
    "da_loc": round(L3 * B * DA_LOC * m ** 3, 3),
    "trat_trong": round((2 * (LT + B) * HT + LT * B) * m ** 2 + 2 * 2 * B * HT * m ** 2, 3),
    "bitum_ngoai": round((2 * (LO + BO) * (HO - TD) + (LD * BD - LO * BO) + 2 * (LD + BD) * TD) * m ** 2, 3),
    "thep_kg": TONG_D, "thep_tong_kg": TONG_KG,
}
DUNG_TICH = (L1 + L2 + L3) * B * HN * m ** 3

# ============================================================== 4. SINH FILE LISP
def S(s):
    """Chuỗi LISP: thoát dấu \\ và ", chữ có dấu đổi sang mã \\U+XXXX (AutoCAD hiển thị Unicode)."""
    out = []
    for ch in s:
        if ch == "\\":
            out.append("\\\\")
        elif ch == '"':
            out.append('\\"')
        elif ord(ch) > 127:
            out.append("\\\\U+%04X" % ord(ch))
        else:
            out.append(ch)
    return '"' + "".join(out) + '"'

def N(v):
    return f"{float(v):.1f}"

LAY = {"bt": "56.Tp_net betong", "thay": "5.TP_net thay", "dut": "4.Tp_Net dut", "truc": "9.Tp_Truc",
       "cat": "2.Tp_Cat", "hatch": "3.TP_Hatch", "thep": "10.TP_Thep chu", "thep2": "11.TP_Thep dai",
       "coc": "14.TP_Coc", "ong": "25.TP_Duong TNT", "dat": "16.TP_hientrang", "txt": "6.TP_Tex tNote",
       "title": "8.TP_Text Title", "dim": "1.Tp_dim", "leader": "42.Tp_M learder", "bang": "13.TP_bangTK"}
ST_NOTE, H_NOTE = "08.TP_1-50 Note", 125.0
ST_TITLE, H_TITLE = "07.TP_1-50 Title", 175.0
DIMST = "03.TP_1-50"

PARTS = {}                          # tên hàm LISP -> danh sách dòng lệnh
cur = None
def part(name):
    global cur
    cur = name
    PARTS[name] = []
def emit(s):
    PARTS[cur].append("  " + s)

def line(lay, x1, y1, x2, y2):
    emit(f'(L {S(LAY[lay])} {N(x1)} {N(y1)} {N(x2)} {N(y2)})')
def rect(lay, x1, y1, x2, y2, var=None):
    pts = f"(list (list {N(x1)} {N(y1)}) (list {N(x2)} {N(y1)}) (list {N(x2)} {N(y2)}) (list {N(x1)} {N(y2)}))"
    cmd = f'(PL {S(LAY[lay])} {pts} 1)'
    emit(f'(setq {var} {cmd})' if var else cmd)
def circle(lay, x, y, r):
    emit(f'(CI {S(LAY[lay])} {N(x)} {N(y)} {N(r)})')
def text(s, x, y, kind="note", just="L", lay=None):
    st, h = (ST_TITLE, H_TITLE) if kind == "title" else (ST_NOTE, H_NOTE)
    lay = lay or ("title" if kind == "title" else "txt")
    emit(f'(TX {S(LAY[lay])} {S(st)} {N(h)} {N(x)} {N(y)} {S(s)} {S(just)})')
def hatch(pat, sc, *vars_):
    emit(f'(HT {S(pat)} {sc} (list {" ".join(vars_)}))')
def dim(x1, y1, x2, y2, xd, yd):
    emit(f'(DM {N(x1)} {N(y1)} {N(x2)} {N(y2)} {N(xd)} {N(yd)})')
def chain_h(xs, y_obj, y_dim):      # chuỗi kích thước ngang
    for a, b in zip(xs, xs[1:]):
        dim(a, y_obj, b, y_obj, (a + b) / 2, y_dim)
def chain_v(ys, x_obj, x_dim):      # chuỗi kích thước đứng
    for a, b in zip(ys, ys[1:]):
        dim(x_obj, a, x_obj, b, x_dim, (a + b) / 2)
def cao_do(x, y, s):
    """Ký hiệu cao độ theo mẫu công ty (anh Tuyên gửi 20/10/2026): đỉnh tam giác tại (x,y) trên đường cao độ."""
    emit(f'(CDO {N(x)} {N(y)} {S(s)})')
def bubble(x, y, so, ghi, xt, yt, ben=0):
    """Số hiệu thép (mẫu anh Tuyên 20/10/2026): mũi tên tại thanh thép (x,y), gãy, đường ngang có chữ thép
    phía trên, vòng tròn số hiệu ở cuối đường ngang.
    ben=0: tự chọn, (xt,yt) là vị trí vòng tròn của bố cục.
    ben=1 / -1: (xt,yt) là điểm gãy; vòng tròn nằm bên phải (1) hoặc bên trái (-1) điểm gãy."""
    emit(f'(BB {N(x)} {N(y)} {N(xt)} {N(yt)} {S(str(so))} {S(ghi)} {ben})')
def note(xo, yo, xk, yk, s, huong=1):
    """Ghi chú có đường dẫn: mũi tên chỉ vào đối tượng (xo,yo), gãy tại (xk,yk), kẻ đường ngang
    sang phải (huong=1) hoặc trái (-1), chữ nằm trên đường ngang.
    Multileader chữ tự chọn hướng theo vị trí điểm gãy: điểm gãy phải nằm ĐÚNG PHÍA chữ đi
    (huong=1 thì xk > xo, huong=-1 thì xk < xo), nếu không chữ sẽ quay ngược."""
    if (xk - xo) * huong < 0:
        raise ValueError(f"note '{s}': điểm gãy nằm ngược phía với hướng chữ")
    emit(f'(NOTE {N(xo)} {N(yo)} {N(xk)} {N(yk)} {S(s)} {huong})')
def section_marker(x, y, letter, horizontal):
    if horizontal:
        line("cat", x - 150, y, x + 150, y)
    else:
        line("cat", x, y - 100, x, y + 100)
    text(letter, x + (0 if horizontal else 120), y + (120 if horizontal else 0), kind="title", just="M")

# ---------------- Vị trí các hình trong Model (mm)
XP, YP = 1500, 12000               # mặt bằng bể: góc dưới trái thân bể
XN = XP + 8200                     # mặt bằng nắp
XA, YA = 1500, 9300                # mặt cắt A-A: góc trái thân bể, cao độ ±0.000
XB = 10400                         # mặt cắt B-B: góc trái thân bể
x_vach1 = TW + L1                  # vị trí vách (tính từ mép ngoài trái)
x_vach2 = x_vach1 + TV + L2
x_ngan = [TW + L1 / 2, x_vach1 + TV + L2 / 2, x_vach2 + TV + L3 / 2]   # tâm 3 ngăn

def plan(x0, y0, nap):
    """Mặt bằng: nap=False là bỏ nắp (thấy thành, vách), nap=True là mặt bằng nắp."""
    rect("dut", x0 - MO, y0 - MO, x0 + LO + MO, y0 + BO + MO)               # đáy mở rộng (khuất)
    rect("bt", x0, y0, x0 + LO, y0 + BO, "pO")
    if not nap:
        rect("bt", x0 + TW, y0 + TW, x0 + LO - TW, y0 + BO - TW, "pIn")
        rect("bt", x0 + x_vach1, y0 + TW, x0 + x_vach1 + TV, y0 + BO - TW, "pV1")
        rect("bt", x0 + x_vach2, y0 + TW, x0 + x_vach2 + TV, y0 + BO - TW, "pV2")
        hatch("AR-CONC", 0.6, "pO", "pIn"); hatch("AR-CONC", 0.6, "pV1"); hatch("AR-CONC", 0.6, "pV2")
        yc = y0 + BO / 2
        for xa, xb in ((x0 - 1000, x0 + TW + 200), (x0 + LO - TW - 200, x0 + LO + 800)):   # ống vào, ra
            line("ong", xa, yc - 57, xb, yc - 57); line("ong", xa, yc + 57, xb, yc + 57)
        for xv in (x_vach1, x_vach2):                                       # lỗ thông qua vách
            for yy in (y0 + TW + 400, y0 + BO - TW - 400):
                line("ong", x0 + xv - 100, yy - 57, x0 + xv + TV + 100, yy - 57)
                line("ong", x0 + xv - 100, yy + 57, x0 + xv + TV + 100, yy + 57)
        for i, ten in enumerate(("CHỨA", "LẮNG", "LỌC")):                   # tên ngăn, 2 dòng
            text("NGĂN", x0 + x_ngan[i], y0 + TW + 420, just="M")
            text(ten, x0 + x_ngan[i], y0 + TW + 220, just="M")
        note(x0 - 250, yc + 57, x0 - 400, yc + 350, "ỐNG VÀO", -1)
        note(x0 + LO + 400, yc + 57, x0 + LO + 550, yc + 350, "ỐNG RA", 1)
        note(x0 + LO + MO, y0 + BO - 100, x0 + LO + MO + 300, y0 + BO + 100, "ĐÁY MỞ RỘNG 200", 1)
    for xc in x_ngan:                                                       # ô thăm 600x600
        rect("dut" if not nap else "bt", x0 + xc - LO_THAM / 2, y0 + BO / 2 - LO_THAM / 2,
             x0 + xc + LO_THAM / 2, y0 + BO / 2 + LO_THAM / 2)
    xo, yo = x0 + LO - TW - 100, y0 + BO - TW - 100
    circle("ong", xo, yo, 30)                                               # ống thông hơi D60
    if nap:
        note(x0 + x_ngan[0] - 200, y0 + BO / 2 + LO_THAM / 2, x0 + x_ngan[0] - 100, y0 + BO + 250,
             "NẮP THĂM 600x600 (ĐAN BTCT DÀY 80)", 1)
        note(xo, yo, x0 + LO + 300, y0 + BO + 250, "THÔNG HƠI D60", 1)
        hatch("AR-CONC", 0.6, "pO")

part("bth-matbang")
plan(XP, YP, nap=False)
section_marker(XP - 1300, YP + BO / 2, "A", True); section_marker(XP + LO + 1300, YP + BO / 2, "A", True)
section_marker(XP + x_ngan[0], YP - 1080, "B", False); section_marker(XP + x_ngan[0], YP + BO + 380, "B", False)
text("%%uMẶT BẰNG BỂ (ĐÃ BỎ NẮP)", XP + LO / 2, YP - 1450, kind="title", just="M")
text("TỶ LỆ 1/50", XP + LO / 2, YP - 1700, just="M")

part("bth-matbangnap")
plan(XN, YP, nap=True)
text("%%uMẶT BẰNG NẮP BỂ", XN + LO / 2, YP - 1450, kind="title", just="M")
text("TỶ LỆ 1/50", XN + LO / 2, YP - 1700, just="M")

def section(x0, y0, length, inner, walls_x, nap_holes, ten, along):
    """Vẽ mặt cắt. along=True: mặt cắt dọc A-A (có vách, ống); False: mặt cắt ngang B-B."""
    yb = y0 - HO                                   # đáy kết cấu
    # Cừ tràm, cát, lót
    xl, xr = x0 - MO - LOT_RONG - CAT_RONG, x0 + length + MO + LOT_RONG + CAT_RONG
    rect("thay", xl, yb - LOT - CAT, xr, yb - LOT, "pCat")
    rect("thay", x0 - MO - LOT_RONG, yb - LOT, x0 + length + MO + LOT_RONG, yb, "pLot")
    hatch("AR-SAND", 0.6, "pCat"); hatch("AR-CONC", 0.4, "pLot")
    xx = xl + 100
    while xx < xr:
        line("coc", xx, yb - LOT - CAT, xx, yb - LOT - CAT - 400)
        xx += 200
    yz = yb - LOT - CAT - 450                      # đường cắt lìa cừ
    line("thay", xl - 100, yz + 60, (xl + xr) / 2 - 80, yz + 60)
    line("thay", (xl + xr) / 2 - 80, yz + 60, (xl + xr) / 2, yz - 60)
    line("thay", (xl + xr) / 2, yz - 60, (xl + xr) / 2 + 80, yz + 60)
    line("thay", (xl + xr) / 2 + 80, yz + 60, xr + 100, yz + 60)
    # Bê tông: đáy, thành, vách, nắp
    rect("bt", x0 - MO, yb, x0 + length + MO, yb + TD, "pD"); hatch("AR-CONC", 0.6, "pD")
    rect("bt", x0, yb + TD, x0 + TW, y0 - TN, "pT1"); hatch("AR-CONC", 0.6, "pT1")
    rect("bt", x0 + length - TW, yb + TD, x0 + length, y0 - TN, "pT2"); hatch("AR-CONC", 0.6, "pT2")
    for i, xv in enumerate(walls_x):
        rect("bt", x0 + xv, yb + TD, x0 + xv + TV, y0 - TN, f"pV{i}"); hatch("AR-CONC", 0.6, f"pV{i}")
    edges = [0] + [e for h in nap_holes for e in (h - LO_THAM / 2, h + LO_THAM / 2)] + [length]
    for i in range(0, len(edges), 2):
        rect("bt", x0 + edges[i], y0 - TN, x0 + edges[i + 1], y0, f"pN{i}"); hatch("AR-CONC", 0.6, f"pN{i}")
    for h in nap_holes:                            # đan nắp thăm
        rect("thay", x0 + h - LO_THAM / 2 + 10, y0 - DAN_DAY, x0 + h + LO_THAM / 2 - 10, y0)
    # Mặt đất, mực nước
    line("dat", xl - 800, y0, xl, y0); line("dat", xr, y0, xr + 800, y0)
    yn = y0 + CD["mn"] * 1000
    line("dut", x0 + TW, yn, x0 + length - TW, yn)
    # Cốt thép
    yd1, yd2 = yb + C_DAY, yb + TD - C_DAY
    line("thep", x0 - MO + C_DAY, yd1 + 150, x0 - MO + C_DAY, yd1)
    line("thep", x0 - MO + C_DAY, yd1, x0 + length + MO - C_DAY, yd1)
    line("thep", x0 + length + MO - C_DAY, yd1, x0 + length + MO - C_DAY, yd1 + 150)
    line("thep", x0 - MO + C_DAY, yd2 - 150, x0 - MO + C_DAY, yd2)
    line("thep", x0 - MO + C_DAY, yd2, x0 + length + MO - C_DAY, yd2)
    line("thep", x0 + length + MO - C_DAY, yd2, x0 + length + MO - C_DAY, yd2 - 150)
    xx = x0 - MO + C_DAY
    while xx <= x0 + length + MO - C_DAY + 1:
        circle("thep2", xx, yd1 + 30, 22); circle("thep2", xx, yd2 - 30, 22)
        xx += 200
    for xw, s in ((x0 + C_THANH, 1), (x0 + TW - C_THANH, 1), (x0 + length - C_THANH, -1), (x0 + length - TW + C_THANH, -1)):
        line("thep", xw, yd1 + 20, xw, y0 - C_NAP)
        line("thep", xw, yd1 + 20, xw + s * 200, yd1 + 20)
        yy = yb + TD
        while yy <= y0 - TN:
            circle("thep2", xw + (25 if xw in (x0 + C_THANH, x0 + length - TW + C_THANH) else -25), yy, 22)
            yy += 200
    for xv in walls_x:
        xc = x0 + xv + TV / 2
        line("thep", xc, yb + TD - 150, xc, y0 - TN + 100)
        yy = yb + TD + 100
        while yy <= y0 - TN:
            circle("thep2", xc + 30, yy, 18); yy += 200
    yn1, yn2 = y0 - TN + C_NAP, y0 - C_NAP
    for i in range(0, len(edges), 2):
        a, b = x0 + edges[i] + C_NAP, x0 + edges[i + 1] - C_NAP
        line("thep", a, yn1, b, yn1); line("thep", a, yn2, b, yn2)
        xx = a
        while xx <= b:
            circle("thep2", xx, yn1 + 30, 22); xx += 200
    # Ghi chú thép (số hiệu như bảng thống kê)
    if along:
        bubble(x0 + 1200, yd1, 1, "Ø12a200", x0 + 1250, yb - 1000, ben=-1)
        bubble(x0 + 2600, yd2, 3, "Ø12a200", x0 + 2650, yb - 1000, ben=1)
        bubble(x0 + C_THANH, y0 - 900, 5, "Ø10a200", x0 - 1200, y0 - 600)
        bubble(x0 + x_vach1 + TV / 2, y0 - 1200, 8, "Ø8a200", x0 + x_vach1 - 900, y0 - 1500)
        bubble(x0 + 650, yn1, 10, "Ø10a200", x0 + 650, y0 + 650, ben=-1)
        bubble(x0 + 1600, yn2, 12, "Ø8a200", x0 + 1500, y0 + 650)
    else:
        bubble(x0 + 600, yd1, 2, "Ø12a200", x0 - 700, yb - 1000)
        bubble(x0 + 950, yd2, 4, "Ø12a200", x0 + 500, yb + 650, ben=1)   # đặt trong lòng bể (B-B hẹp)
        bubble(x0 + C_THANH, y0 - 900, 6, "Ø10a200", x0 - 1300, y0 - 900)
        bubble(x0 + length - C_THANH, y0 - 1300, 7, "Ø10a200", x0 + length + 400, y0 - 1000)
        bubble(x0 + 400, yn1, 11, "Ø10a200", x0 - 300, y0 + 650)
        bubble(x0 + length - 400, yn2, 13, "Ø8a200", x0 + length - 300, y0 + 650)
    # Ghi chú vật liệu: đường dẫn xuống góc dưới bên phải, chữ xếp chồng
    for i, (y_obj, s) in enumerate(((yb - LOT / 2, "BT LÓT B7,5 DÀY 100"), (yb - LOT - CAT / 2, "CÁT ĐỆM DÀY 200"),
                                    (yb - LOT - CAT - 250, f"CỪ TRÀM L=4,5m, {CU_MAT_DO} CÂY/m²"))):
        note(xr - 150 - i * 100, y_obj, xr + 250, yb - 650 - i * 300, s, 1)
    # Cao độ
    xe = x0 + length + MO + 2300                   # cột ký hiệu cao độ, cách mặt cắt để chừa chỗ ghi chú
    cot_y = {}                                     # cao độ thấp nhất đã vẽ ở mỗi cột
    for k, s in (("nap", "±0.000"), ("mn", "-0.450 (MN)"), ("day_long", f"{CD['day_long']:.3f}"),
                 ("day_kc", f"{CD['day_kc']:.3f}"), ("day_cat", f"{CD['day_cat']:.3f}")):
        yk = y0 + CD[k] * 1000
        cot = 0                                    # ký hiệu cao 375: nếu sát ký hiệu trên < 420 thì lùi sang cột bên trái
        while cot in cot_y and cot_y[cot] - yk < 420:
            cot -= 1
        cot_y[cot] = yk
        line("dim", x0 + length + MO + 50, yk, xe + cot * 900 - 120, yk)     # đường dóng cao độ
        cao_do(xe + cot * 900, yk, s)
    text(f"%%u{ten}", x0 + length / 2, yz - 500, kind="title", just="M")
    text("TỶ LỆ 1/50", x0 + length / 2, yz - 750, just="M")

part("bth-matcat-a")
section(XA, YA, LO, None, (x_vach1, x_vach2), x_ngan, "MẶT CẮT A-A", along=True)
# Ống vào, ống ra, lỗ thông vách, ống thông hơi, ngăn lọc (riêng mặt cắt A-A)
yv = YA + CD["ong_vao"] * 1000
line("ong", XA - 1000, yv, XA + TW + 250, yv); line("ong", XA - 1000, yv + 114, XA + TW + 250, yv + 114)
line("ong", XA + TW + 193, yv, XA + TW + 193, yv - 500); line("ong", XA + TW + 307, yv, XA + TW + 307, yv - 500)
yr = YA + CD["mn"] * 1000
line("ong", XA + LO - TW - 250, yr, XA + LO + 1000, yr); line("ong", XA + LO - TW - 250, yr + 114, XA + LO + 1000, yr + 114)
line("ong", XA + LO - TW - 307, yr, XA + LO - TW - 307, yr - 500); line("ong", XA + LO - TW - 193, yr, XA + LO - TW - 193, yr - 500)
for xv in (x_vach1, x_vach2):
    yl = YA - 1200
    line("ong", XA + xv - 100, yl - 57, XA + xv + TV + 100, yl - 57); line("ong", XA + xv - 100, yl + 57, XA + xv + TV + 100, yl + 57)
xth = XA + LO - TW - 100
line("ong", xth - 30, YA, xth - 30, YA + 700); line("ong", xth + 30, YA, xth + 30, YA + 700)
line("ong", xth - 80, YA + 700, xth + 80, YA + 700)
yfl = YA - HO + TD + CAO_DAN_LOC
rect("thay", XA + x_vach2 + TV, yfl, XA + LO - TW, yfl + DAN_DAY, "pDL"); hatch("AR-CONC", 0.4, "pDL")
rect("thay", XA + x_vach2 + TV, yfl + DAN_DAY, XA + LO - TW, yfl + DAN_DAY + DA_LOC, "pDa"); hatch("GRAVEL", 0.6, "pDa")
note(XA + LO - TW - 200, yfl + DAN_DAY + 150, XA + LO + 200, yfl + DAN_DAY + 250, "ĐÁ 1x2 DÀY 300", 1)
note(XA + LO - TW - 200, yfl + 40, XA + LO + 200, yfl - 100, "ĐAN LỌC BTCT DÀY 80", 1)
note(xth + 30, YA + 550, xth + 300, YA + 700, "ỐNG THÔNG HƠI uPVC D60", 1)

part("bth-matcat-b")
section(XB, YA, BO, None, (), (BO / 2,), "MẶT CẮT B-B", along=False)

part("bth-kichthuoc")
emit('(DIMSET)')
xs_p = [XP, XP + TW, XP + x_vach1, XP + x_vach1 + TV, XP + x_vach2, XP + x_vach2 + TV, XP + LO - TW, XP + LO]
chain_h(xs_p, YP, YP - 450); dim(XP, YP, XP + LO, YP, XP + LO / 2, YP - 800)
chain_v([YP, YP + TW, YP + BO - TW, YP + BO], XP, XP - 450); dim(XP, YP, XP, YP + BO, XP - 800, YP + BO / 2)
xs_n = [XN] + [XN + c + s * LO_THAM / 2 for c in x_ngan for s in (-1, 1)] + [XN + LO]
chain_h(xs_n, YP, YP - 450); dim(XN, YP, XN + LO, YP, XN + LO / 2, YP - 800)
chain_v([YP, YP + BO / 2 - LO_THAM / 2, YP + BO / 2 + LO_THAM / 2, YP + BO], XN, XN - 450)
yb = YA - HO
chain_h(xs_p, YA, YA + 350)
chain_v([yb - LOT - CAT, yb - LOT, yb, yb + TD, YA - TN, YA], XA - MO - LOT_RONG - CAT_RONG, XA - 900)
dim(XA, yb, XA, YA, XA - 1250, YA - HO / 2)
chain_h([XB, XB + TW, XB + BO - TW, XB + BO], YA, YA + 350)
emit('(DIMRESTORE)')

# ---------------- Bảng thống kê cốt thép
part("bth-bang")
cols = [("Cấu kiện", 1500), ("Số|hiệu", 450), ("Hình dạng", 1500), ("Ø|(mm)", 450),
        ("Dài 1|thanh (mm)", 800), ("Số|lượng", 550), ("Tổng|dài (m)", 850), ("Khối|lượng (kg)", 850)]
X0T, Y0T, RH, HH = 600, 5050, 220, 480
WT = sum(w for _, w in cols)
text("%%uBẢNG THỐNG KÊ CỐT THÉP BỂ TỰ HOẠI", X0T + WT / 2, Y0T + 230, kind="title", just="M")
rows = []
prev = None
for t in THEP:
    rows.append([t["cau_kien"] if t["cau_kien"] != prev else "", str(t["so_hieu"]), t["hinh_dang"],
                 str(t["d"]), f"{t['l']:,}".replace(",", "."), str(t["n"]),
                 f"{t['tong_m']:.2f}".replace(".", ","), f"{t['kg']:.2f}".replace(".", ",")])
    prev = t["cau_kien"]
rows.append(["Tổng theo đường kính: " + "; ".join(f"Ø{d} = {v:.2f} kg".replace(".", ",") for d, v in sorted(TONG_D.items())), "", "", "", "", "", "", ""])
rows.append(["TỔNG CỘNG", "", "", "", "", "", "", f"{TONG_KG:.2f}".replace(".", ",")])
H = HH + RH * len(rows)
x = X0T
xs = [X0T]
for _, w in cols:
    x += w; xs.append(x)
for xx in xs:
    line("bang", xx, Y0T, xx, Y0T - HH if xx not in (xs[1], xs[2], xs[3], xs[4], xs[5], xs[6]) else Y0T - H + 2 * RH)
for xx in (xs[0], xs[-2], xs[-1]):
    line("bang", xx, Y0T - HH, xx, Y0T - H)
line("bang", X0T, Y0T, X0T + WT, Y0T)
line("bang", X0T, Y0T - HH, X0T + WT, Y0T - HH)
for i in range(1, len(rows) + 1):
    line("bang", X0T, Y0T - HH - RH * i, X0T + WT, Y0T - HH - RH * i)
for (ten, w), xa in zip(cols, xs):
    parts_ = ten.split("|")
    if len(parts_) == 1:
        text(parts_[0], xa + w / 2, Y0T - HH / 2, just="M")
    else:
        text(parts_[0], xa + w / 2, Y0T - HH / 2 + 95, just="M")
        text(parts_[1], xa + w / 2, Y0T - HH / 2 - 95, just="M")
for i, r in enumerate(rows):
    yc = Y0T - HH - RH * i - RH / 2
    if i >= len(rows) - 2:
        text(r[0], X0T + 80, yc, just="ML")
        if r[7]:
            text(r[7], xs[-1] - 60, yc, just="MR")
        continue
    for j, v in enumerate(r):
        if not v:
            continue
        if j in (0, 2):
            text(v, xs[j] + 60, yc, just="ML")
        elif j >= 4:
            text(v, xs[j + 1] - 60, yc, just="MR")
        else:
            text(v, xs[j] + cols[j][1] / 2, yc, just="M")

# ---------------- Ghi chú
part("bth-ghichu")
GC = ["GHI CHÚ:",
      "1. Kích thước ghi bằng mm, cao độ ghi bằng m. Cao độ ±0.000 là mặt sân hoàn thiện (mặt nắp bể).",
      "2. Dung tích hữu ích V = (2,0 + 1,0 + 1,0) x 1,7 x 1,5 = " + f"{DUNG_TICH:.1f}".replace(".", ",") + " m³.",
      "3. Bê tông bể B20 (M250) đá 1x2; bê tông lót B7,5 (M100) dày 100.",
      "4. Cốt thép Ø ≥ 10 dùng CB300-V; Ø < 10 dùng CB240-T. Lớp bảo vệ: đáy 40, thành 35, nắp 25.",
      "5. Xử lý nền: cừ tràm L = 4,5 m, Ø gốc ≥ 8-10 cm, mật độ 25 cây/m²; cát đệm dày 200 đầm chặt.",
      "6. Chống thấm: trong lòng trát 2 lớp vữa XM M100 dày 20 có phụ gia chống thấm, đánh màu;",
      "    mặt ngoài quét bitum chống thấm 2 lớp.",
      "7. Ống vào, ống ra, lỗ thông qua vách: uPVC D114; ống thông hơi uPVC D60 cao hơn mặt sân 700.",
      "8. Đáy mở rộng 200 mỗi bên để chống đẩy nổi. Thi công hố đào có bơm hạ mực nước ngầm;",
      "    không hút cạn bể khi mực nước ngầm cao.",
      "9. Ngăn lọc: đan BTCT dày 80 đục lỗ D30 a100, trên rải đá 1x2 dày 300.",
      "10. Thép trong bảng thống kê chưa trừ phần cắt tại lỗ thăm.",
      "11. Kích thước, cốt thép là đề xuất theo cấu tạo; kỹ sư thiết kế kiểm tra trước khi phát hành."]
for i, s in enumerate(GC):
    text(s, 8600, 5050 - i * 300, kind="title" if i == 0 else "note")

# ---------------- Ghép file LISP
HEAD = r''';;; ============================================================
;;; Lệnh: BTH10 – Vẽ bể tự hoại BTCT 3 ngăn, hữu ích 10 m3 (GN2026-HT-01)
;;; File SINH TỰ ĐỘNG bởi python/be_tu_hoai_10m3.py – sửa thông số trong file Python rồi chạy lại.
;;; Vẽ trong Model, tỷ lệ 1/50, đơn vị mm, theo layer/style của template ISO_CTY.dwt.
;;; ============================================================
(vl-load-com)
;; Đường thẳng
(defun L (lay x1 y1 x2 y2)
  (entmake (list '(0 . "LINE") (cons 8 lay) (list 10 x1 y1 0.0) (list 11 x2 y2 0.0))))
;; Đa tuyến (pts: danh sách điểm, cl=1 khép kín) – trả về tên đối tượng
(defun PL (lay pts cl)
  (entmake (append (list '(0 . "LWPOLYLINE") '(100 . "AcDbEntity") (cons 8 lay)
                         '(100 . "AcDbPolyline") (cons 90 (length pts)) (cons 70 cl))
                   (mapcar '(lambda (p) (cons 10 p)) pts)))
  (entlast))
;; Đường tròn
(defun CI (lay x y r)
  (entmake (list '(0 . "CIRCLE") (cons 8 lay) (list 10 x y 0.0) (cons 40 r))))
;; Chữ: just = "L" trái, "M" giữa, "ML" giữa-trái, "MR" giữa-phải
(defun TX (lay sty h x y s just / h72 v73)
  (cond ((= just "M") (setq h72 1 v73 2))
        ((= just "ML") (setq h72 0 v73 2))
        ((= just "MR") (setq h72 2 v73 2))
        (t (setq h72 0 v73 0)))
  (entmake (list '(0 . "TEXT") (cons 8 lay) (cons 7 sty) (list 10 x y 0.0) (cons 40 h)
                 (cons 1 s) (cons 72 h72) (cons 73 v73) (list 11 x y 0.0))))
;; Mặt cắt vật liệu (hatch) theo biến hệ thống HPNAME/HPSCALE
(defun HT (pat sc ents / ss)
  (setq ss (ssadd))
  (foreach e ents (ssadd e ss))
  (setvar "CLAYER" "3.TP_Hatch")
  (setvar "HPNAME" pat) (setvar "HPSCALE" sc) (setvar "HPANG" 0.0)
  (command "_.-HATCH" "_S" ss "" ""))
;; Kích thước thẳng
(defun DM (x1 y1 x2 y2 xd yd)
  (command "_.DIMLINEAR" (list x1 y1) (list x2 y2) (list xd yd)))
(defun DIMSET ()
  (setq *bth-os* (getvar "OSMODE"))
  (setvar "OSMODE" 0)
  (command "_.-DIMSTYLE" "_R" "03.TP_1-50")
  (setvar "CLAYER" "1.Tp_dim"))
(defun DIMRESTORE () (if *bth-os* (setvar "OSMODE" *bth-os*)))
;; ---- Ghi chú theo mẫu công ty: Multileader và block mẫu (lisp/gn-mau-iso.lsp, lệnh GNMAU) ----
;; Bản vẽ chưa có mẫu thì nạp và chạy GNMAU (thêm block GN_*, kiểu Multileader TP_1-xx GhiChu/SoHieuThep)
(if (not (and (tblsearch "BLOCK" "GN_CaoDo") (tblsearch "BLOCK" "GN_SoHieuThep_T")))
  (progn (load "__MAU_ISO__") (c:GNMAU)))
(defun MSP () (vla-get-modelspace (vla-get-activedocument (vlax-get-acad-object))))
;; Bề rộng một dòng chữ ghi chú 1/50
(defun TW (s / tb) (setq tb (textbox (list (cons 1 s) (cons 7 "08.TP_1-50 Note") (cons 40 125.0))))
  (- (car (cadr tb)) (car (car tb))))
;; ObjectID của ô chữ (ATTDEF) trong block
(defun ATTID (blk tag / id)
  (vlax-for o (vla-item (vla-get-blocks (vla-get-activedocument (vlax-get-acad-object))) blk)
    (if (and (= (vla-get-ObjectName o) "AcDbAttributeDefinition") (= (vla-get-TagString o) tag))
      (setq id (vla-get-ObjectID o))))
  id)
;; Tạo Multileader: mũi tên (ax,ay), điểm gãy (lx,ly), kiểu sty, layer 42.Tp_M learder
(defun MLNEW (ax ay lx ly sty / ml)
  (setq ml (vlax-invoke (MSP) 'AddMLeader (mapcar 'float (list ax ay 0 lx ly 0)) 0))
  (vla-put-Layer ml "42.Tp_M learder")
  (vla-put-StyleName ml sty)
  ml)
;; Đổi hướng đường ngang làm ghi chú dịch đi: dời về đúng điểm gãy rồi đặt lại đường dẫn
(defun MLFIX (ml ax ay lx ly / v)
  (setq v (vlax-invoke ml 'GetLeaderLineVertices 0))
  (vla-Move ml (vlax-3d-point (nth 3 v) (nth 4 v) 0.0) (vlax-3d-point (float lx) (float ly) 0.0))
  (vlax-invoke ml 'SetLeaderLineVertices 0 (mapcar 'float (list ax ay 0 lx ly 0))))
;; Ghi chú có đường dẫn: mũi tên tại đối tượng (xo,yo), gãy tại (xk,yk), chữ trên đường ngang
(defun NOTE (xo yo xk yk s dir / ml)
  (setq ml (MLNEW xo yo xk yk "TP_1-50 GhiChu"))
  (vla-put-TextString ml s)
  (vl-catch-all-apply 'vla-SetDoglegDirection (list ml 0 (vlax-3d-point (float dir) 0.0 0.0)))
  (MLFIX ml xo yo xk yk))
;; Ký hiệu cao độ: chèn block GN_CaoDo hệ số 50, đỉnh tam giác tại (x,y).
;; Chữ dài hơn đường đỡ chữ của block thì kẻ nối thêm đường đỡ chữ.
(defun CDO (x y s / bl w)
  (setq bl (vla-InsertBlock (MSP) (vlax-3d-point (float x) (float y) 0.0) "GN_CaoDo" 50.0 50.0 50.0 0.0))
  (vla-put-Layer bl "1.Tp_dim")
  (foreach a (vlax-invoke bl 'GetAttributes) (vla-put-TextString a s))
  (setq w (TW s))
  (if (> (+ 50.0 w 50.0) 450.0)
    (L "1.Tp_dim" (+ x 450.0) (+ y 172.0) (+ x 50.0 w 50.0) (+ y 172.0))))
;; Số hiệu thép (mẫu anh gửi): mũi tên tại thanh thép (xo,yo), gãy rồi kẻ đường ngang, chữ thép trên
;; đường ngang, vòng tròn số hiệu ở CUỐI đường ngang. (xc,yc) = vị trí vòng tròn của bố cục.
;; Thép nằm bên phải vòng tròn thì dùng block GN_SoHieuThep_T (vòng tròn bên trái, đường ngang sang trái).
;; Đường ngang dài vừa chữ thép + 150. ben = 1 / -1: (xc,yc) là điểm gãy, vòng tròn bên phải / trái.
(defun BB (xo yo xc yc n s ben / dl lft lx blk ml)
  (setq dl (+ (TW s) 150.0))
  (cond ((= ben 1) (setq lft nil lx xc))
        ((= ben -1) (setq lft T lx xc))
        ((> xo xc) (setq lft T lx (+ xc 125.0 dl)))
        (T (setq lft nil lx (- xc 125.0))))
  (setq blk (if lft "GN_SoHieuThep_T" "GN_SoHieuThep"))
  (setq ml (MLNEW xo yo lx yc "TP_1-50 SoHieuThep"))
  (vla-put-ContentType ml 1)
  (vla-put-ContentBlockName ml blk)
  (vla-put-DoglegLength ml dl)
  (vla-SetDoglegDirection ml 0 (vlax-3d-point (if lft -1.0 1.0) 0.0 0.0))
  (vla-SetBlockAttributeValue ml (ATTID blk "SO_HIEU") n)
  (vla-SetBlockAttributeValue ml (ATTID blk "THEP") s)
  (MLFIX ml xo yo lx yc))
'''.replace("__MAU_ISO__", os.path.join(GOC, "lisp", "gn-mau-iso.lsp").replace("\\", "/"))
out = [HEAD]
for name, body in PARTS.items():
    out.append(f"(defun {name} ( / pO pIn pV1 pV2 pV0 pD pT1 pT2 pN0 pN2 pN4 pN6 pCat pLot pDL pDa os)")
    out.append('  (setvar "CTAB" "Model") (setq os (getvar "OSMODE")) (setvar "OSMODE" 0) (setvar "CMDECHO" 0)')
    out.extend(body)
    out.append('  (setvar "OSMODE" os)')
    out.append(f'  "{name} OK")')
out.append('(defun c:BTH10 () (foreach f (list bth-matbang bth-matbangnap bth-matcat-a bth-matcat-b bth-kichthuoc bth-bang bth-ghichu) (f)) (princ))')
lisp_path = os.path.join(GOC, "lisp", "be-tu-hoai-10m3.lsp")
os.makedirs(os.path.dirname(lisp_path), exist_ok=True)
with open(lisp_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")

kq_dir = os.path.join(GOC, "ket-qua", "be-tu-hoai-10m3")
os.makedirs(kq_dir, exist_ok=True)
with open(os.path.join(kq_dir, "so-lieu.json"), "w", encoding="utf-8") as f:
    json.dump({"kich_thuoc_mm": {"L1": L1, "L2": L2, "L3": L3, "B": B, "HN": HN, "HK": HK, "TW": TW, "TV": TV,
                                 "TD": TD, "TN": TN, "MO": MO, "LO": LO, "BO": BO, "HO": HO, "LD": LD, "BD": BD},
               "cao_do_m": CD, "dung_tich_m3": DUNG_TICH, "thep": THEP, "khoi_luong": KL}, f, ensure_ascii=False, indent=1)

print(f"Dung tich huu ich: {DUNG_TICH:.2f} m3 | ngoai than {LO}x{BO}x{HO} | day {LD}x{BD}")
print("Thong ke thep:")
for t in THEP:
    print(f"  {t['so_hieu']:2} {t['cau_kien']:10} D{t['d']:<2} L={t['l']:5} n={t['n']:3} tong={t['tong_m']:7.2f} m  {t['kg']:7.2f} kg")
print("  Tong theo duong kinh:", TONG_D, "| Tong:", TONG_KG, "kg")
print("Khoi luong:", {k: v for k, v in KL.items() if not k.startswith("thep")})
print("So dong lenh LISP:", sum(len(v) for v in PARTS.values()), "->", lisp_path)

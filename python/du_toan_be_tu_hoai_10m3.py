# -*- coding: utf-8 -*-
"""
Lập bảng chi tiết khối lượng + bảng tổng hợp kinh phí hạng mục BỂ TỰ HOẠI 10 m³ (GN2026-HT-01)
theo mẫu dự toán hạ tầng kỹ thuật của công ty.

- Đọc số liệu bản vẽ từ ket-qua/be-tu-hoai-10m3/so-lieu.json (kích thước, bảng thống kê thép).
- Chép file mẫu template/du-toan/ha-tang-ky-thuat/du-toan-ha-tang.xlsx sang thư mục kết quả rồi thay nội dung
  (không sửa file mẫu).
- Đơn giá, định mức hao phí: anh Tuyên lập trên phần mềm F1 (định mức nhà nước, đơn giá TP.HCM).
  File này chỉ ghi khối lượng, mã hiệu ĐỀ XUẤT (cần đối chiếu) và để trống các ô đơn giá.

Chạy:  python python/du_toan_be_tu_hoai_10m3.py
"""
import json, math, os, shutil
from copy import copy

import openpyxl
from openpyxl.cell.cell import MergedCell
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAU = os.path.join(GOC, "template", "du-toan", "ha-tang-ky-thuat", "du-toan-ha-tang.xlsx")
THU_MUC = os.path.join(GOC, "ket-qua", "be-tu-hoai-10m3")
KQ = os.path.join(THU_MUC, "du-toan_be-tu-hoai-10m3.xlsx")
SL = json.load(open(os.path.join(THU_MUC, "so-lieu.json"), encoding="utf-8"))

# ============================================================== 1. THÔNG SỐ (m)
k = {kk: v / 1000 for kk, v in SL["kich_thuoc_mm"].items()}
LO, BO, HO = k["LO"], k["BO"], k["HO"]          # kích thước ngoài bể 4,7 x 2,1 x 2,2
LD, BD = k["LD"], k["BD"]                      # đáy mở rộng 5,1 x 2,5
TD, TW, TV, TN, B, MO = k["TD"], k["TW"], k["TV"], k["TN"], k["B"], k["MO"]
L3 = k["L3"]
HT = k["HN"] + k["HK"]                          # cao lòng trong 1,8
LT = k["L1"] + k["L2"] + k["L3"] + 2 * TV       # dài lòng trong 4,3
LOT, CAT = 0.1, 0.2                             # bê tông lót, cát đệm (bản vẽ)
L_LOT, B_LOT = LD + 0.2, BD + 0.2               # lót rộng hơn đáy 100 mỗi bên: 5,3 x 2,7
L_CAT, B_CAT = L_LOT + 0.2, B_LOT + 0.2         # cát rộng hơn lót 100 mỗi bên: 5,5 x 2,9
O_THAM, DAN, DA_LOC = 0.6, 0.08, 0.3            # ô thăm 600x600, đan dày 80, đá lọc dày 300
CU_DAI, CU_MAT_DO = 4.5, 25                     # cừ tràm
SAU_DAO = -SL["cao_do_m"]["day_cat"]            # 2,5 m: từ ±0.000 tới đáy cát đệm

# --- GIẢ ĐỊNH (chưa có trên bản vẽ, cần anh xác nhận) ---
MO_DAO = 0.3      # đáy hố đào rộng hơn mép cát đệm mỗi bên (m), chỗ thao tác
MAI = 0.5         # mái dốc hố đào 1:0,5
TY_LE_MAY = 0.9   # đào máy 90%, thủ công sửa hố 10%

a_d, b_d = L_CAT + 2 * MO_DAO, B_CAT + 2 * MO_DAO          # đáy hố đào
A_m, B_m = a_d + 2 * MAI * SAU_DAO, b_d + 2 * MAI * SAU_DAO  # miệng hố đào


def g(x):
    """Số gọn cho công thức Excel: 6.1, 0.25, 4 (không đuôi 0)."""
    s = ("%.4f" % x).rstrip("0").rstrip(".")
    return s if s != "-0" else "0"


def vn(x, nd=3):
    """Số kiểu Việt Nam trong diễn giải: 88,583"""
    return ("%.*f" % (nd, x)).replace(".", ",")


V_DAO = f"{g(SAU_DAO)}/6*({g(a_d)}*{g(b_d)}+{g(A_m)}*{g(B_m)}+({g(a_d)}+{g(A_m)})*({g(b_d)}+{g(B_m)}))"
CHIEM_CHO = [  # (tên, biểu thức m3) phần hố đào bị chiếm chỗ
    ("Cát đệm", f"{g(L_CAT)}*{g(B_CAT)}*{g(CAT)}"),
    ("Bê tông lót", f"{g(L_LOT)}*{g(B_LOT)}*{g(LOT)}"),
    ("Đáy bể", f"{g(LD)}*{g(BD)}*{g(TD)}"),
    ("Thân bể (từ mặt đáy -1,950 lên ±0,000)", f"{g(LO)}*{g(BO)}*{g(HO - TD)}"),
]

# ============================================================== 2. DANH MỤC CÔNG TÁC
# Mỗi dòng diễn giải: (nhãn, biểu thức) -> chữ "nhãn: bt = kq", cột K = "=bt"
# hoặc dict(text=..., f=..., v=...) khi cần ghi riêng.
CAN_TRA = "Cần tra"


def thep(ds_sh):
    """Dòng diễn giải thép lấy đúng bảng thống kê trên bản vẽ (kg), đổi ra tấn."""
    rows = []
    for t in SL["thep"]:
        if t["so_hieu"] in ds_sh:
            l = t["l"] / 1000
            rows.append(dict(
                text=f"SH{t['so_hieu']} Ø{t['d']} ({t['cau_kien'].lower()}, {t['hinh_dang'].lower()}): "
                     f"{vn(l, 2)}m x {t['n']} thanh x {vn(0.00617 * t['d'] ** 2, 3)} kg/m = {vn(t['kg'], 2)} kg",
                f=f"=ROUND(ROUND({g(l)}*{t['n']},2)*0.00617*{t['d']}^2,2)/1000",
                v=t["kg"] / 1000))
    return rows


NHOM = [
    ("A. PHẦN ĐÀO ĐẮP, XỬ LÝ NỀN", [
        dict(ma="AB.25111", ten="Đào móng bể bằng máy đào ≤0,8 m³, chiều rộng móng ≤6 m, đất cấp I (90% khối lượng đào)",
             dv="100m3", gc="Đề xuất, cần đối chiếu (cấp đất giả định cấp I)",
             rows=[(f"Hố đào: đáy {vn(a_d, 1)}x{vn(b_d, 1)}, miệng {vn(A_m, 1)}x{vn(B_m, 1)}, sâu {vn(SAU_DAO, 1)}, "
                    f"mái 1:{vn(MAI, 1)}; x {vn(TY_LE_MAY, 1)} /100", f"{V_DAO}*{g(TY_LE_MAY)}/100")]),
        dict(ma=CAN_TRA, ten="Đào móng bể bằng thủ công, sửa hố móng, đất cấp I (10% khối lượng đào)",
             dv="m3", gc="Nhóm AB.1 - đào móng thủ công",
             rows=[(f"Hố đào x {vn(1 - TY_LE_MAY, 1)}", f"{V_DAO}*{g(1 - TY_LE_MAY)}")]),
        dict(ma=CAN_TRA, ten=f"Đóng cừ tràm L={vn(CU_DAI, 1)} m, Ø gốc 8-10 cm, mật độ {CU_MAT_DO} cây/m², đất cấp I",
             dv="100m", gc="Nhóm AC.1 - đóng cọc tre, cọc tràm",
             rows=[dict(text=f"Diện tích đóng cừ {vn(L_CAT, 1)}*{vn(B_CAT, 1)} = {vn(L_CAT * B_CAT, 2)} m²; "
                             f"số cây = {vn(L_CAT * B_CAT, 2)}*{CU_MAT_DO} = {math.ceil(L_CAT * B_CAT * CU_MAT_DO)} cây; "
                             f"{math.ceil(L_CAT * B_CAT * CU_MAT_DO)}*{vn(CU_DAI, 1)}/100",
                        f=f"=ROUNDUP({g(L_CAT)}*{g(B_CAT)}*{CU_MAT_DO},0)*{g(CU_DAI)}/100",
                        v=math.ceil(L_CAT * B_CAT * CU_MAT_DO) * CU_DAI / 100)]),
        dict(ma=CAN_TRA, ten="Đắp cát đệm móng dày 200, đầm chặt", dv="m3",
             gc="Nhóm AB.13 - đắp cát công trình; độ chặt K cần anh xác định",
             rows=[("Cát đệm", f"{g(L_CAT)}*{g(B_CAT)}*{g(CAT)}")]),
        dict(ma="AF.11121", ten="Bê tông lót móng đá 4x6, B7,5 (M100), dày 100, chiều rộng >250 cm", dv="m3",
             gc="Đề xuất, cần đối chiếu (bản vẽ chưa ghi cỡ đá lót, giả định 4x6)",
             rows=[("Lót đáy bể", f"{g(L_LOT)}*{g(B_LOT)}*{g(LOT)}")]),
        dict(ma=CAN_TRA, ten="Đắp đất hoàn trả hố móng bằng đất đào, đầm chặt K=0,90", dv="m3",
             gc="Nhóm AB.13 - đắp đất nền móng công trình",
             rows=[("Thể tích hố đào", V_DAO)] + [(f"Trừ {t.lower()}", f"-{e}") for t, e in CHIEM_CHO]),
        dict(ma=CAN_TRA, ten="Vận chuyển đất thừa bằng ô tô tự đổ (cự ly cần xác định)", dv="100m3",
             gc="Nhóm AB.41/AB.42 - vận chuyển đất; chọn theo loại xe, cự ly",
             rows=[(f"{t} /100", f"{e}/100") for t, e in CHIEM_CHO]),
    ]),
    ("B. PHẦN BÊ TÔNG CỐT THÉP ĐỔ TẠI CHỖ", [
        dict(ma=CAN_TRA, ten="Bê tông đáy bể đá 1x2, B20 (M250), dày 250", dv="m3",
             gc="Nhóm AF - bê tông móng / đáy bể chứa; chọn trộn tại chỗ hay thương phẩm",
             rows=[("Đáy bể (mở rộng 200 mỗi bên)", f"{g(LD)}*{g(BD)}*{g(TD)}")]),
        dict(ma=CAN_TRA, ten="Bê tông thành bể đá 1x2, B20 (M250), dày 200, chiều cao ≤4 m", dv="m3",
             gc="Nhóm AF - bê tông tường / thành bể chứa",
             rows=[("Thành dọc", f"2*{g(LO)}*{g(TW)}*{g(HT)}"), ("Thành ngang", f"2*{g(B)}*{g(TW)}*{g(HT)}")]),
        dict(ma=CAN_TRA, ten="Bê tông vách ngăn đá 1x2, B20 (M250), dày 150, chiều cao ≤4 m", dv="m3",
             gc="Nhóm AF - bê tông tường / vách bể chứa",
             rows=[("2 vách ngăn", f"2*{g(B)}*{g(TV)}*{g(HT)}")]),
        dict(ma=CAN_TRA, ten="Bê tông nắp bể đá 1x2, B20 (M250), dày 150", dv="m3",
             gc="Nhóm AF - bê tông sàn / nắp bể chứa",
             rows=[("Nắp bể", f"{g(LO)}*{g(BO)}*{g(TN)}"), ("Trừ 3 ô thăm 600x600", f"-3*{g(O_THAM)}*{g(O_THAM)}*{g(TN)}")]),
        dict(ma="AF.61120", ten="Sản xuất, lắp dựng cốt thép đáy bể, đường kính ≤18 mm (Ø12, CB300-V)", dv="tấn",
             gc="Đề xuất (cốt thép móng Ø≤18), cần đối chiếu", rows=thep([1, 2, 3, 4])),
        dict(ma=CAN_TRA, ten="Sản xuất, lắp dựng cốt thép thành, vách bể, đường kính ≤10 mm, cao ≤4 m (Ø10 CB300-V, Ø8 CB240-T)",
             dv="tấn", gc="Nhóm AF.61 - cốt thép tường", rows=thep([5, 6, 7, 8, 9])),
        dict(ma=CAN_TRA, ten="Sản xuất, lắp dựng cốt thép nắp bể, đường kính ≤10 mm (Ø10 CB300-V, Ø8 CB240-T)",
             dv="tấn", gc="Nhóm AF.61 - cốt thép sàn mái", rows=thep([10, 11, 12, 13])),
        dict(ma=CAN_TRA, ten="Sản xuất, lắp dựng cốt thép nắp bể, đường kính ≤18 mm (Ø12 gia cường ô thăm, CB300-V)",
             dv="tấn", gc="Nhóm AF.61 - cốt thép sàn mái", rows=thep([14])),
        dict(ma=CAN_TRA, ten="Ván khuôn gỗ đáy bể (móng)", dv="100m2", gc="Nhóm AF.81 - ván khuôn gỗ; loại ván khuôn cần xác định",
             rows=[("Cạnh đáy", f"2*({g(LD)}+{g(BD)})*{g(TD)}/100")]),
        dict(ma=CAN_TRA, ten="Ván khuôn gỗ thành, vách bể, chiều cao ≤4 m", dv="100m2", gc="Nhóm AF.81 - ván khuôn gỗ tường",
             rows=[("Thành ngoài", f"2*({g(LO)}+{g(BO)})*{g(HT)}/100"),
                   ("Thành trong", f"2*({g(LT)}+{g(B)})*{g(HT)}/100"),
                   ("Trừ chỗ vách giáp thành", f"-4*{g(TV)}*{g(HT)}/100"),
                   ("Vách ngăn 2 mặt", f"2*2*{g(B)}*{g(HT)}/100")]),
        dict(ma=CAN_TRA, ten="Ván khuôn gỗ nắp bể", dv="100m2", gc="Nhóm AF.81 - ván khuôn gỗ sàn",
             rows=[("Mặt dưới nắp", f"{g(LT)}*{g(B)}/100"),
                   ("Trừ đầu vách", f"-2*{g(TV)}*{g(B)}/100"),
                   ("Trừ 3 ô thăm", f"-3*{g(O_THAM)}*{g(O_THAM)}/100"),
                   ("Cạnh ngoài nắp", f"2*({g(LO)}+{g(BO)})*{g(TN)}/100"),
                   ("Cạnh 3 ô thăm", f"3*4*{g(O_THAM)}*{g(TN)}/100")]),
    ]),
    ("C. CẤU KIỆN BÊ TÔNG ĐÚC SẴN", [
        dict(ma=CAN_TRA, ten="Bê tông đan đúc sẵn đá 1x2, B20 (M250), dày 80 (đan nắp thăm, đan lọc)", dv="m3",
             gc="Nhóm AG.1 - bê tông cấu kiện đúc sẵn",
             rows=[("Đan nắp thăm 600x600", f"3*{g(O_THAM)}*{g(O_THAM)}*{g(DAN)}"),
                   ("Đan lọc (chưa trừ lỗ D30)", f"{g(L3)}*{g(B)}*{g(DAN)}")]),
        dict(ma=CAN_TRA, ten="Sản xuất cốt thép đan đúc sẵn, đường kính ≤10 mm (Ø6, CB240-T)", dv="tấn",
             gc="Nhóm AG.1 - cốt thép cấu kiện đúc sẵn", rows=thep([15, 16, 17])),
        dict(ma=CAN_TRA, ten="Ván khuôn gỗ đan đúc sẵn (chỉ tính ván cạnh)", dv="100m2", gc="Nhóm AG.3 - ván khuôn cấu kiện đúc sẵn",
             rows=[("Cạnh đan nắp thăm", f"3*4*{g(O_THAM)}*{g(DAN)}/100"),
                   ("Cạnh đan lọc", f"2*({g(L3)}+{g(B)})*{g(DAN)}/100")]),
        dict(ma=CAN_TRA, ten="Lắp đặt đan nắp thăm BTCT đúc sẵn (khoảng 72 kg/tấm)", dv="cái", gc="Nhóm AG.4 - lắp cấu kiện đúc sẵn",
             rows=[("3 ngăn x 1 tấm", "3")]),
        dict(ma=CAN_TRA, ten="Lắp đặt đan lọc BTCT đúc sẵn (khoảng 340 kg/tấm)", dv="cái", gc="Nhóm AG.4 - lắp cấu kiện đúc sẵn",
             rows=[("Ngăn lọc", "1")]),
    ]),
    ("D. HOÀN THIỆN, CHỐNG THẤM", [
        dict(ma=CAN_TRA, ten="Trát thành, vách trong lòng bể 2 lớp, dày 20, vữa XM M100 có phụ gia chống thấm", dv="m2",
             gc="Nhóm AK.2 - trát tường; phụ gia chống thấm tính thêm vật liệu",
             rows=[("Thành trong", f"2*({g(LT)}+{g(B)})*{g(HT)}"),
                   ("Trừ chỗ vách giáp thành", f"-4*{g(TV)}*{g(HT)}"),
                   ("Vách ngăn 2 mặt", f"2*2*{g(B)}*{g(HT)}")], ten_id="trat"),
        dict(ma=CAN_TRA, ten="Láng đáy bể dày 20, vữa XM M100 có phụ gia chống thấm, có đánh màu", dv="m2",
             gc="Nhóm AK.4 - láng nền có đánh màu",
             rows=[("Đáy lòng bể", f"{g(LT)}*{g(B)}"), ("Trừ chân vách", f"-2*{g(TV)}*{g(B)}")]),
        dict(ma=CAN_TRA, ten="Đánh màu thành, vách trong lòng bể", dv="m2", gc="Cần tra mã đánh màu",
             rows=[dict(text="Bằng diện tích trát thành, vách", f="=L{trat}", v=None)]),
        dict(ma=CAN_TRA, ten="Quét bitum chống thấm mặt ngoài bể, 2 lớp", dv="m2", gc="Nhóm AK - quét chống thấm",
             rows=[("Thành ngoài", f"2*({g(LO)}+{g(BO)})*{g(HO - TD)}"),
                   ("Mặt trên đáy mở rộng", f"{g(LD)}*{g(BD)}-{g(LO)}*{g(BO)}"),
                   ("Cạnh đáy", f"2*({g(LD)}+{g(BD)})*{g(TD)}")]),
        dict(ma=CAN_TRA, ten="Rải đá 1x2 làm lớp lọc ngăn lọc, dày 300", dv="m3", gc="Cần tra mã rải vật liệu lọc",
             rows=[("Ngăn lọc", f"{g(L3)}*{g(B)}*{g(DA_LOC)}")]),
    ]),
    ("E. ỐNG, PHỤ KIỆN uPVC", [
        dict(ma=CAN_TRA, ten="Lắp đặt ống uPVC D114 nối dán keo (ống vào, ống ra, ống qua vách)", dv="100m",
             gc="Nhóm BB - lắp đặt ống nhựa; 1 m ống chờ ngoài bể mỗi đầu đã tính",
             rows=[("Ống vào: 1,0 ngoài + 0,2 thành + 0,25 trong + 0,5 ống đứng", "(1+0.2+0.25+0.5)/100"),
                   ("Ống ra: 1,0 ngoài + 0,2 thành + 0,25 trong + 0,5 ống đứng", "(1+0.2+0.25+0.5)/100"),
                   ("Ống qua vách: 2 vách x 2 lỗ x (0,15 + 0,2)", "4*(0.15+0.2)/100")]),
        dict(ma=CAN_TRA, ten="Lắp đặt tê uPVC D114 nối dán keo", dv="cái", gc="Nhóm BB - lắp đặt phụ tùng ống nhựa",
             rows=[("Ống vào, ống ra", "2")]),
        dict(ma=CAN_TRA, ten="Lắp đặt ống uPVC D60 thông hơi nối dán keo", dv="100m", gc="Nhóm BB - lắp đặt ống nhựa",
             rows=[("Qua nắp 0,15 + cao hơn mặt sân 0,7", "(0.15+0.7)/100")]),
        dict(ma=CAN_TRA, ten="Lắp đặt chụp thông hơi uPVC D60", dv="cái", gc="Nhóm BB - lắp đặt phụ tùng ống nhựa",
             rows=[("Đầu ống thông hơi", "1")]),
    ]),
]

CONG_TRINH = "CÔNG TRÌNH: ................................................ (ANH BỔ SUNG TÊN CÔNG TRÌNH)"
HANG_MUC = "HẠNG MỤC: BỂ TỰ HOẠI BTCT 3 NGĂN, DUNG TÍCH HỮU ÍCH 10 m³ (BẢN VẼ GN2026-HT-01)"
DIA_DIEM = "ĐỊA ĐIỂM: ................................................, THÀNH PHỐ HỒ CHÍ MINH"

VANG = PatternFill("solid", fgColor="FFFF99")       # ô cần anh nhập / đối chiếu
VANG_NHAT = PatternFill("solid", fgColor="FFF2CC")
TNR = "Times New Roman"


# ============================================================== 3. LẬP FILE
def chep_style(dst, src):
    dst._style = copy(src._style)


def so_dong(s, rong=58):
    return max(1, math.ceil(len(s) / rong))


def main():
    if os.path.exists(KQ):
        raise SystemExit(f"File đã có, không ghi đè: {KQ}")
    shutil.copy(MAU, KQ)
    wb = openpyxl.load_workbook(KQ)

    # Chỉ giữ sheet chi tiết khối lượng và sheet tổng hợp; các sheet khác F1 sẽ xuất (không đọc nội dung sheet ẩn)
    for ws in list(wb.worksheets):
        if ws.title not in ("Công trình", "Tổng hợp du toan (2)"):
            wb.remove(ws)
    # Xóa liên kết rác sang file ngoài và các tên vùng lỗi của file mẫu
    wb._external_links = []
    wb.defined_names.clear()
    for ws in wb.worksheets:
        ws.defined_names.clear()

    # ---------------------------------------------------------------- Sheet 1: Công trình
    ws = wb["Công trình"]
    cols = [openpyxl.utils.get_column_letter(i) for i in range(1, 26)]   # A..Y
    st = {kind: {c: copy(ws[f"{c}{r}"]._style) for c in cols}
          for kind, r in (("nhom", 8), ("cv", 11), ("dg", 12), ("tong", 248))}
    st_hdr4 = {c: copy(ws[f"{c}4"]._style) for c in cols}
    st_nhom_font = copy(ws["D8"].font)
    ws.delete_rows(8, ws.max_row)

    ws["A3"] = CONG_TRINH
    ws["A4"] = HANG_MUC
    for c in cols:
        ws[f"{c}5"]._style = copy(st_hdr4[c])
    ws.merge_cells("A5:W5")
    ws["A5"] = DIA_DIEM
    ws.row_dimensions[5].height = ws.row_dimensions[4].height
    ws["A2"] = "(Ban hành kèm theo Thông tư số 13/2021/TT-BXD ngày 31/08/2021 của Bộ Xây dựng - anh kiểm tra hiệu lực)"
    ws["Y6"] = "Ghi chú mã hiệu"
    ws.column_dimensions["Y"].width = 48
    # Hiện cột đơn giá, thành tiền vật liệu (đơn giá lấy từ F1)
    for c in ("M", "Q"):
        ws.column_dimensions[c].hidden = False

    r = 8
    stt = 0
    dong_cv = []          # (dòng, item)
    ten_id = {}
    for ten_nhom, items in NHOM:
        for c in cols:                     # dòng nhóm: kiểu dòng công tác, chữ đậm (kiểu dòng nhóm của mẫu có gạch chéo)
            ws[f"{c}{r}"]._style = copy(st["cv"][c])
        ws[f"D{r}"] = ten_nhom
        ws[f"D{r}"].font = copy(st_nhom_font)
        r += 1
        for it in items:
            stt += 1
            rc = r
            for c in cols:
                ws[f"{c}{r}"]._style = copy(st["cv"][c])
            ws[f"A{r}"] = stt
            ws[f"B{r}"] = "GN2026-HT-01"
            ws[f"C{r}"] = it["ma"]
            ws[f"C{r}"].fill = VANG if it["ma"] == CAN_TRA else VANG_NHAT
            ws[f"D{r}"] = it["ten"]
            ws[f"E{r}"] = it["dv"]
            ws[f"X{r}"] = "Đơn giá TP.HCM trên F1 (anh chọn bộ đơn giá hiện hành)"
            ws[f"Y{r}"] = it["gc"]
            for c in ("M", "O", "P"):
                ws[f"{c}{r}"].fill = VANG_NHAT
            for a, b in (("Q", "M"), ("R", "N"), ("S", "O"), ("T", "P")):
                ws[f"{a}{r}"] = f"=ROUND(L{r}*{b}{r},0)"
            ws.row_dimensions[r].height = max(21.95, 17.5 * so_dong(it["ten"]))
            if "ten_id" in it:
                ten_id[it["ten_id"]] = r
            r += 1
            r0 = r
            for row in it["rows"]:
                for c in cols:
                    ws[f"{c}{r}"]._style = copy(st["dg"][c])
                if isinstance(row, dict):
                    text, f = row["text"], row["f"].format(**ten_id) if "{" in row["f"] else row["f"]
                else:
                    nhan, bt = row
                    val = eval(bt)
                    text = f"{nhan}: {bt.replace('.', ',')} = {vn(val, 3)}"
                    f = "=" + bt
                ws[f"D{r}"] = text
                ws[f"K{r}"] = f
                ws.row_dimensions[r].height = max(21.95, 17.5 * so_dong(text))
                r += 1
            ws[f"L{rc}"] = f"=ROUND(SUM(K{r0}:K{r - 1}),4)"
            dong_cv.append((rc, it))
    # Dòng tổng
    for c in cols:
        ws[f"{c}{r}"]._style = copy(st["tong"][c])
    ws[f"C{r}"] = "THM"
    ws[f"D{r}"] = "TỔNG HẠNG MỤC"
    for c in ("Q", "R", "S", "T"):
        ws[f"{c}{r}"] = f"=SUM({c}8:{c}{r - 1})"
    r_tong = r
    # Phần ký
    r += 2
    f_ky = Font(name=TNR, size=11, bold=True)
    ws[f"D{r}"] = "NGƯỜI THỰC HIỆN"
    ws[f"O{r}"] = "NGƯỜI CHỦ TRÌ"
    ws[f"D{r + 4}"] = "(Họ tên, chứng chỉ hành nghề định giá XD - anh bổ sung)"
    ws[f"O{r + 4}"] = "(Họ tên, chứng chỉ hành nghề định giá XD - anh bổ sung)"
    for cc in (f"D{r}", f"O{r}"):
        ws[cc].font = f_ky
        ws[cc].alignment = Alignment(horizontal="center")
    for cc in (f"D{r + 4}", f"O{r + 4}"):
        ws[cc].font = Font(name=TNR, size=11, italic=True)
        ws[cc].alignment = Alignment(horizontal="center")
    ws.print_area = f"A1:W{r + 4}"
    # In vừa 1 trang ngang (đã hiện thêm cột vật liệu), tiêu đề cột đủ cao cho chữ "Nhân công"
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.row_dimensions[7].height = 32

    # ---------------------------------------------------------------- Sheet: Tổng hợp dự toán
    th = wb["Tổng hợp du toan (2)"]
    th.title = "Tổng hợp dự toán"
    for row in th.iter_rows(min_row=1, max_row=th.max_row, min_col=6, max_col=12):   # cột F..L: số nháp của mẫu
        for c in row:
            if not isinstance(c, MergedCell):
                c.value = None
    th["A2"] = "='Công trình'!A3"
    th["A3"] = "='Công trình'!A4"
    for c in "ABCDE":
        th[f"{c}4"]._style = copy(th[f"{c}3"]._style)
    th.merge_cells("A4:E4")
    th["A4"] = "='Công trình'!A5"
    th.row_dimensions[4].height = th.row_dimensions[3].height
    th["D8"] = "Lấy ở bảng chi tiết khối lượng"
    th["E8"] = f"='Công trình'!Q{r_tong}+'Công trình'!R{r_tong}"
    th["E10"] = f"='Công trình'!S{r_tong}"
    th["E12"] = f"='Công trình'!T{r_tong}"
    th["D10"] = th["D12"] = "Lấy ở bảng chi tiết khối lượng"
    th["D18"] = '=C15&" + "&C16&" + "&C17'          # mẫu ghi nhầm C + LT + TL
    th["A24"] = "Bằng chữ: (ghi sau khi có giá trị Gxd từ phần mềm F1)"
    th["C26"] = "TP. Hồ Chí Minh, ngày ...... tháng ...... năm 2026"
    th["A34"] = "(Họ tên Giám đốc - anh bổ sung)"
    th["A36"] = "(Chứng chỉ KS định giá XD hạng ... số ... - anh bổ sung)"
    th["A42"] = "(Họ tên người lập - anh bổ sung)"
    for rr in range(25, 43):                   # mẫu ẩn sẵn phần ký tên
        th.row_dimensions[rr].hidden = False

    # ---------------------------------------------------------------- Sheet: Nhập F1
    nf = wb.create_sheet("Nhập F1")
    tieu_de = ["STT", "Mã hiệu", "Tên công tác", "Đơn vị", "Khối lượng", "Ghi chú mã hiệu"]
    rong = [6, 12, 70, 9, 12, 50]
    vien = Border(*(Side(style="thin"),) * 4)
    nf["A1"] = "DANH MỤC CÔNG TÁC VÀ KHỐI LƯỢNG ĐỂ NHẬP VÀO PHẦN MỀM F1"
    nf["A1"].font = Font(name=TNR, size=14, bold=True)
    nf["A2"] = "Khối lượng lấy tự động từ sheet 'Công trình'. Ô mã hiệu tô vàng: cần tra hoặc đối chiếu trên F1."
    nf["A2"].font = Font(name=TNR, size=11, italic=True)
    for i, (t, w) in enumerate(zip(tieu_de, rong)):
        c = nf.cell(row=4, column=i + 1, value=t)
        c.font = Font(name=TNR, size=11, bold=True)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = vien
        c.fill = PatternFill("solid", fgColor="EFEFF2")
        nf.column_dimensions[openpyxl.utils.get_column_letter(i + 1)].width = w
    for j, (rc, it) in enumerate(dong_cv):
        rr = 5 + j
        vals = [f"='Công trình'!A{rc}", f"='Công trình'!C{rc}", f"='Công trình'!D{rc}",
                f"='Công trình'!E{rc}", f"='Công trình'!L{rc}", f"='Công trình'!Y{rc}"]
        for i, v in enumerate(vals):
            c = nf.cell(row=rr, column=i + 1, value=v)
            c.font = Font(name=TNR, size=11)
            c.border = vien
            c.alignment = Alignment(vertical="center", wrap_text=True,
                                    horizontal="center" if i in (0, 3) else None)
        nf.cell(row=rr, column=5).number_format = "#,##0.0000"
        nf.cell(row=rr, column=2).fill = VANG if it["ma"] == CAN_TRA else VANG_NHAT
        nf.row_dimensions[rr].height = max(18, 16 * so_dong(it["ten"], 75))
    nf.page_setup.orientation = "landscape"
    nf.page_setup.paperSize = 9
    nf.print_title_rows = "4:4"
    for s in (nf,):
        s.sheet_properties.pageSetUpPr.fitToPage = True
        s.page_setup.fitToWidth, s.page_setup.fitToHeight = 1, 0

    # ---------------------------------------------------------------- Sheet: Căn cứ, giả định
    cc = wb.create_sheet("Căn cứ, giả định")
    cc.column_dimensions["A"].width = 6
    cc.column_dimensions["B"].width = 120
    noi_dung = [
        ("CĂN CỨ (anh kiểm tra văn bản còn hiệu lực trước khi dùng)", None),
        ("1", "Bản vẽ GN2026-HT-01 Bể tự hoại BTCT 3 ngăn 10 m³ (bản PDF v14) và bảng thống kê cốt thép trên bản vẽ (tổng 799,06 kg)."),
        ("2", "Phương pháp đo bóc khối lượng: Thông tư 13/2021/TT-BXD."),
        ("3", "Định mức: Thông tư 12/2021/TT-BXD và các văn bản sửa đổi, bổ sung (ví dụ Thông tư 09/2024/TT-BXD). Em không chắc danh mục văn bản sửa đổi đến tháng 10/2026, anh kiểm tra trên F1."),
        ("4", "Chi phí gián tiếp, thu nhập chịu thuế tính trước: Thông tư 11/2021/TT-BXD. Tỷ lệ trong sheet tổng hợp (C 5,5%; LT 1,1%; TT 2,0%; TL 5,5%) là tỷ lệ của file mẫu (công trình hạ tầng kỹ thuật), anh xác định lại theo quy mô và văn bản hiện hành."),
        ("5", "Thuế GTGT để 10%: anh kiểm tra chính sách giảm thuế GTGT đang áp dụng tại thời điểm lập."),
        ("6", "Đơn giá: bộ đơn giá xây dựng TP.HCM và công bố giá vật liệu của Sở Xây dựng TP.HCM tháng 9/2026, anh chọn trên F1. Từ 2025 địa giới đã sắp xếp lại, cần đúng bộ đơn giá hiện hành."),
        ("", None),
        ("MÃ HIỆU", None),
        ("-", "Cột 'Mã hiệu' tô vàng đậm 'Cần tra': em không có mã chính xác, cột 'Ghi chú mã hiệu' ghi nhóm định mức để anh tra trên F1."),
        ("-", "Mã tô vàng nhạt (AB.25111, AF.11121, AF.61120): là ĐỀ XUẤT, cần đối chiếu nội dung và điều kiện áp dụng trên F1 trước khi dùng."),
        ("", None),
        ("GIẢ ĐỊNH (bản vẽ chưa thể hiện, cần anh xác nhận)", None),
        ("G1", "Mặt đất tự nhiên tại vị trí bể = cao độ ±0.000 (mặt nắp bể). Chiều sâu đào 2,5 m tới đáy cát đệm."),
        ("G2", "Đất cấp I (nền đất yếu)."),
        ("G3", f"Đáy hố đào rộng hơn mép cát đệm {vn(MO_DAO, 1)} m mỗi bên; mái dốc 1:{vn(MAI, 1)}; đào máy {int(TY_LE_MAY * 100)}%, thủ công {int(round((1 - TY_LE_MAY) * 100))}%. Muốn đổi thì sửa thông số đầu file python/du_toan_be_tu_hoai_10m3.py rồi chạy lại."),
        ("G4", "Đắp hoàn trả hố móng bằng đất đào tại chỗ, K=0,90; đất thừa (bằng phần bể và lớp lót, cát chiếm chỗ) chở đi đổ."),
        ("G5", "Bê tông lót dùng đá 4x6. Ván khuôn gỗ. Đan nắp thăm và đan lọc đúc sẵn rồi lắp đặt (đan lọc 1 tấm, khoảng 340 kg)."),
        ("G6", "Ống uPVC: đã tính 1 m ống chờ ngoài bể ở mỗi đầu ống vào, ống ra."),
        ("G7", "Trát, láng trong lòng bể tính theo diện tích thực (đã trừ chỗ vách giáp thành, chân vách). File so-lieu.json ghi 41,15 m² là chưa trừ các phần này."),
        ("", None),
        ("CHƯA TÍNH, CẦN ANH QUYẾT ĐỊNH", None),
        ("C1", "Bơm nước hố móng (mực nước ngầm cao): số ca máy bơm theo biện pháp thi công."),
        ("C2", "Chống vách hố đào (cừ ván, cừ Larsen) nếu không đào được mái dốc."),
        ("C3", "Cự ly vận chuyển đất thừa, vị trí bãi đổ."),
        ("C4", "Tên công trình, chủ đầu tư, địa điểm cụ thể, người lập, người chủ trì và số chứng chỉ."),
    ]
    rr = 1
    for a, b in noi_dung:
        ca, cb = cc.cell(row=rr, column=1, value=a), cc.cell(row=rr, column=2, value=b)
        if b is None:
            ca.font = Font(name=TNR, size=12, bold=True)
        else:
            ca.font = cb.font = Font(name=TNR, size=11)
            cb.alignment = Alignment(wrap_text=True, vertical="top")
            ca.alignment = Alignment(horizontal="center", vertical="top")
            cc.row_dimensions[rr].height = 16 * so_dong(b, 130)
        rr += 1
    cc.page_setup.orientation = "landscape"
    cc.page_setup.paperSize = 9

    wb.active = 0
    wb.save(KQ)
    print("Đã lập:", KQ)
    print("Số công tác:", len(dong_cv), "| dòng tổng hạng mục:", r_tong)


if __name__ == "__main__":
    main()

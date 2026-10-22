# -*- coding: utf-8 -*-
"""
Tạo file Excel để NHẬP THẲNG vào phần mềm Dự toán F1 (nút "Nhập Excel"), lấy khối lượng từ số liệu bản vẽ
bể tự hoại GN2026-HT-01 (python/du_toan_be_tu_hoai_10m3.py đọc ket-qua/be-tu-hoai-10m3/so-lieu.json).

Mỗi công tác: 1 dòng chính (STT, mã hiệu, tên, đơn vị, khối lượng = tổng diễn giải)
              + các dòng diễn giải bên dưới (tên bộ phận: biểu thức, khối lượng từng dòng).
Mã hiệu: bảng mã TT38/2026 anh Tuyên đã duyệt ngày 21/10/2026 (áp dụng công tác tương tự).

Chạy:  python python/f1_nhap_be_tu_hoai.py
"""
import importlib.util, os, re

import openpyxl
from openpyxl.styles import Font

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KQ = os.path.join(GOC, "ket-qua", "be-tu-hoai-10m3", "F1-nhap_be-tu-hoai-10m3.xlsx")

spec = importlib.util.spec_from_file_location("dt", os.path.join(GOC, "python", "du_toan_be_tu_hoai_10m3.py"))
dt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dt)

# Bảng mã đã duyệt, theo thứ tự công tác trong du_toan_be_tu_hoai_10m3.py (bỏ "Đánh màu").
# (mã, đơn vị F1, hệ số đổi khối lượng)  - hệ số: /100 khi định mức tính theo 100m3, x2 khi quét 2 lớp
MA = [
    ("AB.25111", "100m3", 1), ("AB.11371", "m3", 1), ("AC.11221", "100m", 1), ("AB.66143", "100m3", 0.01),
    ("AF.11121A", "m3", 1), ("AB.65120", "100m3", 0.01), ("AB.41431", "100m3", 1),
    ("AF.11224A", "m3", 1), ("AF.12114A", "m3", 1), ("AF.12114A", "m3", 1), ("AF.12414A", "m3", 1),
    ("AF.61120", "tấn", 1), ("AF.61411", "tấn", 1), ("AF.61511", "tấn", 1), ("AF.61521", "tấn", 1),
    ("AF.81111", "100m2", 1), ("AF.81311", "100m2", 1), ("AF.81151", "100m2", 1),
    ("AG.11414A", "m3", 1), ("AG.13231", "tấn", 1), ("AF.81152", "100m2", 1), ("AG.41411", "cái", 1),
    ("AG.41411", "cái", 1), ("AK.21234", "m2", 1), ("AK.41214", "m2", 1), ("AK.94121", "m2", 2),
    ("AK.98110", "m3", 1), ("BB.41108", "100m", 1), ("BB.75106", "cái", 1), ("BB.41106", "100m", 1),
    ("BB.75104", "cái", 1),
]


def tron(x, nd=4):
    """Làm tròn như hàm ROUND của Excel và F1 (5 làm tròn lên)."""
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal(f"{x:.15g}").quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP))


def vn(x, nd=4):
    s = ("%.*f" % (nd, x)).rstrip("0").rstrip(".")
    return s.replace(".", ",")


def main():
    items = [it for _, its in dt.NHOM for it in its if not it["ten"].startswith("Đánh màu")]
    assert len(items) == len(MA), (len(items), len(MA))
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Cong trinh"
    ws.append(["STT", "Mã hiệu", "Tên công tác / diễn giải", "Đơn vị", "Khối lượng"])
    tong = []
    for stt, (it, (ma, dv, hs)) in enumerate(zip(items, MA), 1):
        dong = []
        for row in it["rows"]:
            if isinstance(row, dict):
                if "Bằng diện tích" in row["text"]:
                    continue
                if "ROUNDUP" in row["f"]:
                    so_cay = round(row["v"] * 100 / dt.CU_DAI)
                    bt = f"{so_cay}*{dt.g(dt.CU_DAI)}/100"
                    nhan = f"Diện tích {vn(dt.L_CAT, 1)}x{vn(dt.B_CAT, 1)}, {dt.CU_MAT_DO} cây/m² = {so_cay} cây, dài {vn(dt.CU_DAI, 1)}m"
                else:                                        # dòng thép theo số hiệu
                    l, n, d = re.findall(r"ROUND\(([\d.]+)\*(\d+),2\)\*0\.00617\*(\d+)", row["f"])[0]
                    bt = f"{l}*{n}*{round(0.00617 * int(d) ** 2, 5)}/1000"
                    nhan = row["text"].split(":")[0] + f", L={vn(float(l), 3)}m x {n} thanh"
            else:
                nhan, bt = row
            if hs != 1:
                bt = f"({bt})*{dt.g(hs)}"
                nhan += " (đổi ra 100m3)" if hs < 1 else " (2 lớp)"
            kl = tron(eval(bt))
            dong.append((f"{nhan}: {bt.replace('.', ',')}", kl))
        kl_cv = tron(sum(k for _, k in dong))
        ws.append([stt, ma, it["ten"], dv, kl_cv])
        for txt, kl in dong:
            ws.append([None, None, txt, None, kl])
        tong.append((stt, ma, kl_cv))
    for c, w in zip("ABCDE", (6, 12, 90, 9, 12)):
        ws.column_dimensions[c].width = w
    for row in ws.iter_rows():
        for c in row:
            c.font = Font(name="Times New Roman", size=11, bold=(c.row == 1),
                          italic=(c.row > 1 and row[0].value is None))
    wb.save(KQ)
    print("Đã tạo:", KQ, "| số dòng:", ws.max_row)
    for t in tong:
        print(*t)


if __name__ == "__main__":
    main()

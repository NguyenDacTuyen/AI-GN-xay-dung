# -*- coding: utf-8 -*-
"""
Đọc FILE KHAI BÁO DỰ ÁN (.ini) dùng chung cho 3 chương trình:
  - python/chuyen_f1_ve_mau.py  (file F1 xuất ra -> dự toán hạng mục theo mẫu công ty)
  - python/tong_hop_du_toan.py          (các hạng mục -> bảng tổng hợp dự toán)
  - python/thuyet_minh_du_toan.py       (bảng tổng hợp -> thuyết minh dự toán Word)

File khai báo mẫu (có giải thích từng dòng): python/mau-khai-bao-du-an.ini
Mỗi dự án chép mẫu đó vào thư mục kết quả của dự án, điền thông tin, rồi chạy:
  python python/<tên chương trình>.py <đường dẫn file khai báo>
"""
import configparser, os, sys
from types import SimpleNamespace

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHO_TRONG = "......"     # chỗ chưa có thông tin: chương trình ghi dấu này và tô vàng


def doc(path=None):
    """Đọc file khai báo. Không truyền đường dẫn thì lấy tham số đầu tiên khi chạy chương trình."""
    if path is None:
        if len(sys.argv) < 2:
            raise SystemExit("Thiếu file khai báo dự án. Cách chạy, ví dụ:\n"
                             "  python python/tong_hop_du_toan.py ket-qua/be-tu-hoai-10m3/khai-bao-du-an.ini")
        path = sys.argv[1]
    path = os.path.abspath(path)
    if not os.path.isfile(path):
        raise SystemExit(f"Không thấy file khai báo: {path}")

    cp = configparser.ConfigParser(interpolation=None, comment_prefixes=("#", ";"), inline_comment_prefixes=None)
    cp.optionxform = str                                   # giữ nguyên chữ hoa, chữ thường của tên mục
    cp.read(path, encoding="utf-8-sig")                    # utf-8-sig: đọc được cả file lưu bằng Notepad

    def g(muc, ten, mac_dinh=""):
        return cp.get(muc, ten, fallback=mac_dinh).strip()

    thu_muc = g("du_an", "thu_muc") or os.path.dirname(path)
    if not os.path.isabs(thu_muc):
        thu_muc = os.path.join(os.path.dirname(path), thu_muc)

    def f(ten_file):
        """Tên file trong khai báo -> đường dẫn đầy đủ (file nằm trong thư mục dự án nếu chỉ ghi tên)."""
        if not ten_file:
            return ""
        return ten_file if os.path.isabs(ten_file) else os.path.normpath(os.path.join(thu_muc, ten_file))

    hang_muc = []
    for muc in sorted((m for m in cp.sections() if m.startswith("hang_muc")),
                      key=lambda m: int("".join(c for c in m if c.isdigit()) or 0)):
        hm = SimpleNamespace(
            muc=muc,
            ten=g(muc, "ten"),
            ky_hieu=g(muc, "ky_hieu_ban_ve"),
            linh_vuc=g(muc, "linh_vuc", "ha-tang-ky-thuat"),
            file_f1_xuat=f(g(muc, "file_f1_xuat")),
            file_du_toan=f(g(muc, "file_du_toan")),
        )
        for ten in ("ten", "file_du_toan"):
            if not getattr(hm, ten):
                raise SystemExit(f"File khai báo, mục [{muc}]: chưa ghi '{ten}'")
        hang_muc.append(hm)
    if not hang_muc:
        raise SystemExit("File khai báo chưa có mục [hang_muc_1]")

    try:
        vat = float(g("tong_hop", "thue_gtgt", "8").replace(",", ".")) / 100
    except ValueError:
        raise SystemExit("File khai báo: thuế suất GTGT phải là số, ví dụ: thue_gtgt = 8")

    def tien(muc, ten):
        """Số tiền (đồng), cho phép ghi 50.000.000 hoặc 50000000; để trống = 0 (không tính)."""
        x = g(muc, ten).replace(".", "").replace(",", "").replace(" ", "")
        if not x:
            return 0
        if not x.isdigit():
            raise SystemExit(f"File khai báo, mục [{muc}], dòng '{ten}': phải là số tiền, ví dụ 50.000.000")
        return int(x)

    return SimpleNamespace(
        file=path,
        thu_muc=thu_muc,
        ten_du_an=g("du_an", "ten_du_an"),
        ten_dau_trang=g("du_an", "ten_dau_trang"),
        dia_diem=g("du_an", "dia_diem"),
        tinh_thanh=g("du_an", "tinh_thanh", "Thành phố Hồ Chí Minh"),
        chu_dau_tu=g("du_an", "chu_dau_tu"),
        nam=g("du_an", "nam", "2026"),
        dinh_muc=g("can_cu", "dinh_muc"),
        gia_nhan_cong=g("can_cu", "gia_nhan_cong"),
        gia_ca_may=g("can_cu", "gia_ca_may"),
        thoi_diem_gia_vl=g("gia", "thoi_diem_gia_vat_lieu"),
        so_thong_bao_gia=g("gia", "so_thong_bao_gia"),
        cu_ly_km=g("gia", "cu_ly_van_chuyen_km"),
        hang_muc=hang_muc,
        f1_tmdt=f(g("tong_hop", "file_f1_tmdt")),
        file_tong_hop=f(g("tong_hop", "file_ket_qua", "du-toan_tong-hop.xlsx")),
        vat=vat,
        truot_gia=g("tong_hop", "du_phong_truot_gia", "khong").lower(),
        ly_do_truot_gia=g("tong_hop", "ly_do_khong_tinh_truot_gia"),
        dam_bao_giao_thong=tien("tong_hop", "dam_bao_giao_thong"),
        di_doi=tien("tong_hop", "di_doi_ha_tang"),
        ten_di_doi=g("tong_hop", "ten_di_doi", "Chi phí di dời hạ tầng kỹ thuật"),
        file_thuyet_minh=f(g("thuyet_minh", "file_ket_qua", "thuyet-minh-du-toan_tong-hop.docx")),
        so_van_ban=g("thuyet_minh", "so_van_ban"),
        van_ban_quy_hoach=g("thuyet_minh", "van_ban_quy_hoach"),
        van_ban_chu_truong=g("thuyet_minh", "van_ban_chu_truong"),
        hop_dong_tu_van=g("thuyet_minh", "hop_dong_tu_van"),
        ho_so_khao_sat=g("thuyet_minh", "ho_so_khao_sat"),
        cong_tac_tuong_tu=g("thuyet_minh", "ghi_chu_cong_tac_tuong_tu"),
        nguoi_lap=g("thuyet_minh", "nguoi_lap"),
        giam_doc=g("thuyet_minh", "giam_doc"),
    )


def dia_diem_day_du(kb):
    """'Xã ..., Thành phố Hồ Chí Minh' (chưa có địa điểm chi tiết thì để '......')."""
    return f"{kb.dia_diem or CHO_TRONG}, {kb.tinh_thanh}"


def chu_hoa(s):
    """Viết hoa nhưng giữ đơn vị m², m³."""
    return s.upper().replace("M²", "m²").replace("M³", "m³")

# 00 — Kế hoạch (điều phối) — DEMO đội agent

## 1. Việc được giao
- Demo luồng đội agent trên file `F:\demo\Acad_BD_TD_TN Nhi Binh 5.dxf` (hạ tầng khu Nhị Bình, TP.HCM).
- Phạm vi: 1 hạng mục nhỏ — **hệ thống thoát nước (giếng thu + cống dọc)**. Chạy đủ: bóc khối lượng → kiểm tra.

## 2. Đầu vào đã đọc
- `F:\demo\Acad_BD_TD_TN Nhi Binh 5.dxf` (DXF AC1021, đơn vị mm, 14.576 đối tượng, 258 layer).

## 3. Kết quả (bảng phân việc)
| Lĩnh vực | Agent | Đầu vào | Sản phẩm | Phụ thuộc |
|---|---|---|---|---|
| Bóc khối lượng | ky-su-boc-khoi-luong | DXF trên | Bảng KL thoát nước (Excel) + `02_khoi-luong.md` | (bản vẽ đã có) |
| Soát số học KL | kiem-tra-khoi-luong | Excel KL | nhận xét | cần 02 |
| Soát hồ sơ tổng | ky-su-kiem-tra | 00, 02 + DXF | `07_kiem-tra-ho-so.md` | cần 02 |

Ghi chú hướng dẫn cho ky-su-boc-khoi-luong:
- Giếng thu: đếm block mặt bằng `KHGMBGiengThu` (mỗi giếng 1 block). Số mốc tham khảo điều phối đã dò: **30 cái**.
- Cống dọc: các layer hình cống (`TP15_BD_MB_Cong`, `TP16_BD_Timcong`, `51/52/53.TP_...cong`) trống trong modelspace; hình cống nằm trong đối tượng proxy (ACAD_PROXY_ENTITY) của phần mềm chuyên dụng. Không bóc trực tiếp chiều dài/kích thước cống được → ghi `[Chờ bổ sung]`, chỉ nguồn thay thế (bảng thống kê cống, trắc dọc TNuoc).

## 4. Giả định đã dùng
- Mỗi block `KHGMBGiengThu` = 1 giếng thu.
- Đơn vị bản vẽ mm (INSUNITS=4).

## 5. Chỗ chưa chắc (Cần xác nhận lại)
- Loại/kết cấu giếng thu (giếng hàm ếch, giếng thu đơn/đôi) cần bản vẽ chi tiết.

## 6. Việc người sau cần làm
- ky-su-boc-khoi-luong bóc KL theo hướng dẫn trên; sau đó 2 agent kiểm tra soát.

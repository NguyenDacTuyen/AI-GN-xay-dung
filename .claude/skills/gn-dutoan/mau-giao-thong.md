# Mẫu dự toán giao thông (tài liệu tra cứu của skill gn-dutoan)

File mẫu: `template/du-toan/giao-thong/du-toan-giao-thong.xlsx` (đọc ngày 20/10/2026). Mẫu lấy từ dự toán cải tạo, nâng cấp hệ thống đường giao thông nội bộ kho nguyên liệu.

**Đọc `mau-hang-muc-chung.md` trước.** File này chỉ ghi phần riêng.

## Các sheet đang hiện (theo thứ tự)
| Sheet | Nội dung |
|---|---|
| `Công trình` | Bảng chi tiết khối lượng công tác xây dựng (tiêu đề cột ở dòng 6–7, nhóm đầu ví dụ "I) PHẦN MẶT ĐƯỜNG") |
| `Hao phí vật tư` | Bảng phân tích vật tư |
| `Vật liệu` | Bảng tổng hợp vật liệu, dòng 2 ghi "(Theo thông báo giá VLXD tháng ... năm ... của Sở Xây dựng ...)" |
| `Bìa du toan` | Trang bìa dự toán (bố cục giống trang bìa mẫu hạ tầng) |
| `Tong hop du toan` | Bảng tổng hợp kinh phí hạng mục |
| `Dự thầu` | **Bảng giá dự thầu** |

## Riêng của mẫu này
- Sheet chi tiết khối lượng có 2 dòng đầu: CÔNG TRÌNH, ĐỊA ĐIỂM.
- **Trang bìa:** "BÁO CÁO KINH TẾ KỸ THUẬT XÂY DỰNG CÔNG TRÌNH" / "(PHẦN DỰ TOÁN)", CÔNG TRÌNH, ĐỊA ĐIỂM XD, ĐƠN VỊ LẬP: CÔNG TY CỔ PHẦN TƯ VẤN ĐẦU TƯ XÂY DỰNG GIA NGUYỄN, "TP. Hồ Chí Minh, năm ...".
- **Bảng giá dự thầu** (sheet `Dự thầu`):
  - Dòng 1: **BẢNG GIÁ DỰ THẦU**. Dòng 2–3 lấy tên công trình, địa điểm từ sheet `Công trình`.
  - Cột: **STT | Mã hiệu | Tên công tác | Đơn vị | Khối lượng | Đơn giá | Thành tiền**.
  - Mỗi dòng lấy STT, mã, tên, đơn vị, khối lượng từ sheet `Công trình`. Đơn giá lấy từ bảng đơn giá chi tiết (sheet ẩn). `Thành tiền = ROUND(Khối lượng*Đơn giá,0)`.
  - Cuối bảng: "Tổng cộng", "Làm tròn" (`ROUND(...,-3)`, tròn nghìn đồng), dòng bằng chữ.
  - Phần ký: "... , ngày ... tháng ... năm ...", "Đại diện hợp pháp của nhà thầu", "[ghi tên, chức danh, ký tên và đóng dấu]".
- Tỷ lệ trong mẫu (của dự án cũ, **phải xác định lại cho từng dự án**):

  | Khoản | Tỷ lệ trong mẫu |
  |---|---|
  | Chi phí chung (C) | 6,2% × T |
  | Nhà tạm (LT) | 1,1% × T |
  | Công tác không xác định khối lượng (TT) | 2,0% × T |
  | Thu nhập chịu thuế tính trước (TL) | 6,0% × (T + GT) |
  | VAT | 10% × G |

- Có thêm dòng **TỔNG DỰ TOÁN (Tdt) = Gxd**.

## Lỗi, điểm lạ trong file mẫu (Claude không tự sửa file mẫu; khi lập file mới thì làm đúng)
1. Cột "Cách tính" dòng **Chi phí gián tiếp** ghi ra "C + LT + TL", đúng ra phải là "C + LT + TT".
2. Bảng giá dự thầu viết số tiền bằng chữ bằng hàm **`TienBangChu()`**. Hàm này không có sẵn trong Excel (cần add-in riêng). Mở trên máy không có add-in sẽ báo lỗi `#NAME?`. Khi lập file mới, **ghi bằng chữ thành văn bản** (Claude tự đổi số ra chữ), không dùng hàm này.
3. Đơn giá của bảng dự thầu lấy từ sheet ẩn "Đơn giá chi tiết". File mới phải giữ đúng liên kết đó, hoặc lấy đơn giá tổng hợp theo cách anh chỉ định.
4. Trang bìa ghi cơ quan chủ quản "SỞ KẾ HOẠCH VÀ ĐẦU TƯ THÀNH PHỐ HỒ CHÍ MINH" và năm 2023. Đổi theo dự án mới.
5. Thông báo giá vật liệu trong mẫu là của tháng 04/2023. Cập nhật theo thời điểm lập.

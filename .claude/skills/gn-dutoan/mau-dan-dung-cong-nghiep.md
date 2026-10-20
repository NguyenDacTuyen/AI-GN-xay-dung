# Mẫu dự toán dân dụng, công nghiệp (tài liệu tra cứu của skill gn-dutoan)

File mẫu: `template/du-toan/dan-dung-cong-nghiep/du-toan-dd-cn.xlsx` (đọc ngày 20/10/2026). Mẫu lấy từ dự toán phần xây dựng hệ thống lạnh 03 kho nguyên liệu tại Đồng Nai.

**Đọc `mau-hang-muc-chung.md` trước.** File này chỉ ghi phần riêng.

## Các sheet đang hiện (theo thứ tự)
| Sheet | Nội dung |
|---|---|
| `cong trinh` | Bảng chi tiết khối lượng công tác xây dựng (tiêu đề cột ở dòng 7–8, dữ liệu từ dòng 9) |
| `Phan tich vat tu` | Bảng phân tích vật tư |
| `vat tu` | Bảng tổng hợp vật liệu (cột H ghi nguồn giá, ví dụ "Giá vật liệu tháng 6/2025 - Đồng Nai") |
| `Tong hop du toan` | Bảng tổng hợp kinh phí hạng mục |

Tên sheet viết **không dấu, chữ thường** (khác 2 mẫu kia).

## Riêng của mẫu này
- Sheet chi tiết khối lượng có đủ 3 dòng đầu: CÔNG TRÌNH, **HẠNG MỤC**, ĐỊA ĐIỂM.
- Tỷ lệ trong mẫu (của dự án cũ, **phải xác định lại cho từng dự án**):

  | Khoản | Tỷ lệ trong mẫu |
  |---|---|
  | Chi phí chung (C) | 6,2% × T |
  | Nhà tạm (LT) | 1,1% × T |
  | Công tác không xác định khối lượng (TT) | 2,0% × T |
  | Thu nhập chịu thuế tính trước (TL) | 6,0% × (T + GT) |
  | VAT | **8%** × G |

- Không có dòng TỔNG DỰ TOÁN (Tdt). Bảng dừng ở **V. CHI PHÍ XÂY DỰNG (Gxd)**, rồi đến dòng bằng chữ.
- Phần ký: ĐƠN VỊ LẬP, GIÁM ĐỐC và NGƯỜI LẬP, kèm số chứng chỉ kỹ sư định giá xây dựng.

## Lỗi, điểm lạ trong file mẫu (Claude không tự sửa file mẫu; khi lập file mới thì làm đúng)
1. Sheet `Tong hop du toan`, ô A2–A4 lấy tên công trình bằng **liên kết sang một file Excel khác** (`'[1]cong trinh'!A3`), không phải sheet trong chính file. File mới phải trỏ về sheet `cong trinh` của chính nó.
2. Cột "Cách tính" của dòng **Chi phí gián tiếp** ghi chữ ra "C + LT + TL" (trỏ nhầm ô ký hiệu TL), trong khi công thức tiền đúng là C + LT + TT. File mới phải ghi "C + LT + TT".
3. VAT trong mẫu là **8%** (theo chính sách giảm thuế có thời hạn), khác 2 mẫu kia (10%). Kiểm tra thuế suất tại thời điểm lập.
4. Dòng "Bằng chữ" là chữ gõ tay của dự án cũ.
5. Các cột ẩn F–L của sheet tổng hợp còn số nháp (tính tay của dự án cũ). Không dùng.

# Mẫu dự toán hạ tầng kỹ thuật (tài liệu tra cứu của skill gn-dutoan)

File mẫu: `template/du-toan/ha-tang-ky-thuat/du-toan-ha-tang.xlsx` (đọc ngày 20/10/2026). Mẫu lấy từ dự toán cải tạo, nâng cấp hệ thống thoát nước kho nguyên liệu (mương BTCT, cống D400, hố ga).

**Đọc `mau-hang-muc-chung.md` trước.** File này chỉ ghi phần riêng.

## Các sheet đang hiện (theo thứ tự)
| Sheet | Nội dung |
|---|---|
| `Công trình` | Bảng chi tiết khối lượng công tác xây dựng (tiêu đề cột ở dòng 6–7, dữ liệu từ dòng 8) |
| `Hao phí vật tư` | Bảng phân tích vật tư |
| `Vật liệu` | Bảng tổng hợp vật liệu, dòng 2 ghi "(Theo thông báo giá vật liệu xây dựng tháng ... năm ... của Sở Xây dựng ...)" |
| `HO GA CONG D400 _OK` | **Bảng tính khối lượng đào đất, đổ bê tông hố ga** theo cao độ |
| `CONG D400_ok` | **Bảng tính khối lượng đào, lấp đất phui cống** theo cao độ |
| `Tổng hợp du toan (2)` | Bảng tổng hợp kinh phí hạng mục |
| `Bìa du toan (2)` | Trang bìa dự toán |

## Riêng của mẫu này
- Sheet chi tiết khối lượng chỉ có 2 dòng đầu: CÔNG TRÌNH, ĐỊA ĐIỂM (không có dòng HẠNG MỤC).
- **Bảng tính khối lượng hố ga và cống** (khổ A4 ngang, font Times New Roman 11):
  - Hố ga, các cột: tên hố ga, loại, cao độ đỉnh, cao độ đáy cống, cao độ đáy hố ga, thép thân và thang hố ga (kg), chiều sâu, rộng, dài phui đào, thể tích đào, chiều cao và thể tích đổ bê tông, thể tích hố ga chiếm chỗ, thể tích đắp trả, ván khuôn.
  - Cống, các cột: hố ga đầu, hố ga cuối, khoảng cách 2 hố ga, cao độ thiết kế tại 2 hố ga, cao độ đáy cống, chiều sâu đào trung bình, bề rộng đáy và miệng phui, số đốt cống, thể tích đào, đắp, chiếm chỗ.
  - Tính bằng **công thức theo cao độ**, ví dụ chiều sâu đào `=F9-((G9+H9)/2)+0.05+0.2`. Khối lượng ở đây là nguồn cho các dòng diễn giải trong sheet `Công trình`.
- **Trang bìa:**
  - Góc trái là cơ quan chủ quản, dòng dưới là tên đơn vị lập "CTY CP TƯ VẤN ĐẦU TƯ XÂY DỰNG GIA NGUYỄN". Góc phải là quốc hiệu, tiêu ngữ.
  - Giữa trang: "BÁO CÁO KINH TẾ KỸ THUẬT XÂY DỰNG CÔNG TRÌNH" / "(PHẦN DỰ TOÁN)", CÔNG TRÌNH, ĐỊA ĐIỂM XD.
  - Cuối trang: ĐƠN VỊ LẬP, rồi "TP. Hồ Chí Minh, năm ...".
  - Font Times New Roman, tên báo cáo cỡ 26.
- Tỷ lệ trong mẫu (của dự án cũ, **phải xác định lại cho từng dự án**):

  | Khoản | Tỷ lệ trong mẫu |
  |---|---|
  | Chi phí chung (C) | **5,5%** × T |
  | Nhà tạm (LT) | 1,1% × T |
  | Công tác không xác định khối lượng (TT) | 2,0% × T |
  | Thu nhập chịu thuế tính trước (TL) | **5,5%** × (T + GT) |
  | VAT | 10% × G |

- Có thêm dòng **TỔNG DỰ TOÁN (Tdt) = Gxd** sau dòng chi phí xây dựng.

## Lỗi, điểm lạ trong file mẫu (Claude không tự sửa file mẫu; khi lập file mới thì làm đúng)
1. Cột "Cách tính" dòng **Chi phí gián tiếp** ghi ra "C + LT + TL", đúng ra phải là "C + LT + TT" (công thức tiền thì đúng).
2. Hai sheet tính khối lượng hố ga và cống có **tiêu đề dùng font VNI-Times** (bảng mã cũ, hiện chữ lỗi khi máy không cài font VNI), và dòng 2–3 **liên kết sang file Excel khác** (`'[146]CA SAU CONG D400'`). File mới dùng Times New Roman Unicode và lấy tên công trình từ sheet `Công trình`.
3. Trang bìa ghi cơ quan chủ quản là "SỞ KẾ HOẠCH VÀ ĐẦU TƯ THÀNH PHỐ HỒ CHÍ MINH" và năm cũ. Đổi theo chủ đầu tư, cơ quan quản lý của dự án mới (từ năm 2025 các sở đã sắp xếp lại, cần kiểm tra tên cơ quan).
4. Tên sheet tổng hợp và bìa có đuôi "(2)" (bản sao của sheet khác). File mới nên đặt tên gọn: `Tổng hợp dự toán`, `Bìa dự toán`.
5. Thông báo giá vật liệu trong mẫu là của tháng 04/2023. Cập nhật theo thời điểm lập.

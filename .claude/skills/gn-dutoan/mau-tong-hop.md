# Mẫu tổng hợp dự toán xây dựng công trình (tài liệu tra cứu của skill gn-dutoan)

File mẫu: `template/du-toan/tong-hop/bang-du-toan-tong-hop.xlsx` (đọc ngày 20/10/2026, **chỉ đọc các sheet đang hiện**). Mẫu lấy từ dự án nâng cấp mặt đường, lắp đặt hệ thống thoát nước tại TP.HCM.

Đây là **file tổng hợp riêng** theo cách A: lấy chi phí xây dựng (Gxd) của các file hạng mục cộng lại, rồi mới tính chi phí quản lý dự án, tư vấn, chi phí khác, dự phòng.

## Các sheet đang hiện
| Sheet | Nội dung |
|---|---|
| `TH TMDT` | **Tổng hợp dự toán xây dựng công trình** (sheet chính) |
| `Du_phong_truot_gia` | Bảng tính dự phòng phí do trượt giá theo thời gian |

Sheet **`TT38`** (anh để hiện và cập nhật ngày 24/10/2026): bảng định mức chi phí QLDA và tư vấn theo TT 38/2026/TT-BXD, có công thức nội suy theo ô C4 (chi phí xây dựng, tỷ đồng). Mỗi bảng nằm giữa 2 dòng mốc ở cột A (`QLDA79^` ... `QLDA79$`), cột "Giá trị" là tỷ lệ đã nội suy. Anh xác nhận bảng lập BCKTKT (5,8% hạ tầng dưới 1 tỷ) là đúng; 4,37% trên F1 là tỷ lệ cho dự án bảo trì nhóm C, không dùng.

**Lỗi đã biết của sheet TT38 (24/10/2026):**
- Bảng lập BCKTKT (`LBC79`): dòng dân dụng, công nghiệp, nông nghiệp, hạ tầng so cận với 7 và 15 (mốc thật là 1, 3, 20, 40 tỷ) nên 3 đến 40 tỷ nội suy sai. Chương trình tổng hợp sửa trong file kết quả, mẫu giữ nguyên.
- Các bảng phí thẩm định dự án, thẩm định TK/dự toán, quyết toán, kiểm toán, PCCC còn theo văn bản cũ (TT 176/2011, 209/2016, 210/2016, 75/2014, 150/2014, NĐ 99/2021): chương trình không dùng.
- Trong `TH TMDT` của mẫu: D37 (bảo hiểm) trỏ vào bảng phí thẩm định dự án; D38, D39 trỏ dòng giao thông.

## Định dạng sheet `TH TMDT`
- Khổ **A4 ngang**, tỷ lệ in 73%, vừa 1 trang theo chiều ngang. Lề trái, phải 0,5 cm, lề trên 1,3 cm, lề dưới 1,7 cm. Chân trang "Trang x/y".
- Font **Times New Roman 13**. Dòng tiêu đề nhóm (I, II, III...) in đậm. Tên bảng cỡ 20 đậm.
- Dòng 1: **TỔNG HỢP DỰ TOÁN XÂY DỰNG CÔNG TRÌNH**. Dòng 2: DỰ ÁN. Dòng 3: ĐỊA ĐIỂM. Góc phải: "Đơn vị tính: Đồng".
- Cột: **TT | NỘI DUNG CHI PHÍ | KÝ HIỆU | ĐỊNH MỨC | CÁCH TÍNH (gộp 2 cột E:F) | GIÁ TRỊ TRƯỚC THUẾ | THUẾ GTGT | GIÁ TRỊ SAU THUẾ | CĂN CỨ**.
- Số tiền định dạng kế toán không số lẻ: `_(* #,##0_)`.
- Cột "Cách tính" ghi bằng công thức nối chữ, ví dụ `="GXD trước thuế x "&D18&" x 1,08"`.

## Bố cục khoản mục
| TT | Nội dung | Ký hiệu | Cách tính trong mẫu | Căn cứ trong mẫu |
|---|---|---|---|---|
| **I** | **Chi phí xây dựng** | GXD | Tổng các dòng bên dưới | |
| | Chi phí hạ tầng kỹ thuật | | Lấy từ file tổng hợp hạng mục phần hạ tầng | |
| | Chi phí đường giao thông | | Lấy từ file tổng hợp hạng mục phần giao thông | |
| | Chi phí phần dân dụng và công nghiệp | | Lấy từ file tổng hợp hạng mục phần dân dụng | |
| **II** | **Chi phí quản lý dự án** | GQLDA | GXD trước thuế × % | Bảng 1.1 TT 38/2026/TT-BXD |
| **III** | **Chi phí tư vấn đầu tư xây dựng** | GTV | Tổng các mục 1–7 | |
| 1 | Khảo sát địa hình bước BCKTKT | GTV1 | Tạm tính (nhập giá trị sau thuế) | |
| 2 | Lập BCKTKT | GTV2 | GXD trước thuế × % × 1,08 | Bảng 2.5 TT 38/2026/TT-BXD |
| 3 | Thẩm tra TKBVTC và dự toán, gồm 3.1 thẩm tra thiết kế, 3.2 thẩm tra dự toán | GTV3 | GXD trước thuế × % | Bảng 2.19 và 2.20 |
| 4 | Giám sát thi công xây dựng | GTV4 | GXD trước thuế × % | Bảng 2.24 |
| 5 | Lập HSMT và đánh giá HSDT thi công | GTV5 | GXD trước thuế × % | Bảng 2.22 |
| 6 | Thẩm định HSMT gói thầu thi công | GTV6 | GXD × 0,1% (tối thiểu 2 triệu, tối đa 60 triệu) | NĐ 214/2025/NĐ-CP |
| 7 | Thẩm định kết quả lựa chọn nhà thầu | GTV7 | GXD × 0,1% (tối thiểu 2 triệu, tối đa 60 triệu) | NĐ 214/2025/NĐ-CP |
| **IV** | **Chi phí khác** | GK | Tổng các mục | |
| 1 | Phí thẩm định dự án đầu tư | K1 | TMĐT × % (tối thiểu 500.000, tối đa 150 triệu) | TT 28/2023/TT-BTC |
| 2 | Bảo hiểm công trình | K2 | GXD trước thuế × % × 1,08 | NĐ 67/2023/NĐ-CP |
| 3 | Phí thẩm định thiết kế BVTC | K3 | GXD trước thuế × % × 50% | TT 27/2023/TT-BTC và TT 64/2025/TT-BTC |
| 4 | Phí thẩm định dự toán | K4 | GXD trước thuế × % × 50% | như trên |
| 5 | Kiểm toán độc lập | K5 | TMĐT × % × 1,08 | NĐ 254/2025/NĐ-CP |
| 6 | Thẩm tra, phê duyệt quyết toán | K6 | TMĐT × % × 50% | |
| 7 | Kiểm tra nghiệm thu công trình trước khi đưa vào sử dụng | K7 | 20% × chi phí giám sát trước thuế × 1,08 | TT 10/2021/TT-BXD |
| 8 | Đảm bảo giao thông trong quá trình thi công | K8 | Tạm tính | |
| **V** | **Chi phí dự phòng** | GDP | GDP1 + GDP2 | |
| 5.1 | Dự phòng cho yếu tố khối lượng | GDP1 | 5% × (GXD + GQLDA + GTV + GK) | TT 38/2026/TT-BXD |
| 5.2 | Dự phòng cho yếu tố trượt giá | GDP2 | Lấy từ sheet `Du_phong_truot_gia` | |
| **VI** | **Chi phí di dời hạ tầng kỹ thuật** | GDD | Tạm tính (ví dụ di dời trụ điện) | |
| | **Tổng cộng** | TMĐT | GXD + GQLDA + GTV + GK + GDP + GDD, **làm tròn triệu đồng** (`ROUND(...,-6)`) | |

- Các khoản tư vấn, chi phí khác tính thuế GTGT ở cột riêng. Các khoản phí, lệ phí (thẩm định) không chịu VAT.
- Mục nào dự án không có thì bỏ dòng, đánh lại số thứ tự. Dự án có thiết bị, bồi thường giải phóng mặt bằng thì thêm khoản tương ứng.

## Sheet `Du_phong_truot_gia`
1. **Thông tin đầu vào:** tên dự án; tổng chi phí thực hiện dự án (chưa gồm lãi vay, chưa dự phòng); năm gốc; tiến độ thực hiện.
2. **Bảng chỉ số giá xây dựng** từng năm của địa phương (mẫu dùng chỉ số giá TP.HCM 2020–2025):
   - Quy về năm gốc.
   - Tính chỉ số liên hoàn.
   - Lấy **chỉ số liên hoàn bình quân** `IXDCTbq = AVERAGE(...)`.
3. **Tính trượt giá:**
   - Phân bổ chi phí theo tỷ lệ % từng năm thực hiện.
   - Chỉ số trượt giá lũy tích `kt = IXDCTbq^t`.
   - Trượt giá từng năm = chi phí đã trượt giá − chi phí chưa trượt giá.
   - `GDP2` = tổng các năm.

## Lỗi, điểm lạ trong file mẫu (Claude không tự sửa file mẫu; khi lập file mới thì làm đúng)
1. **Vùng nháp ngoài vùng in** (cột M–T và các dòng 57–78) còn nhiều số tính tay, ô lỗi `#REF!` và liên kết sang file Excel khác (`[675]`, `[676]`). File mới **không chép vùng nháp này**.
2. Dòng "Chi phí phần dân dụng và công nghiệp" gõ thừa chữ ("Chi phí **đ**phần..."), và cột cách tính ghi nhầm "phần giao thông".
3. Giá trị chi phí xây dựng từng phần (dòng 9–11) không liên kết tới file hạng mục. File mới phải **ghi rõ nguồn** (tên file hạng mục) và số phải khớp đúng Gxd của từng file.
4. Thuế GTGT chỗ thì gõ thẳng `0.08`, chỗ thì lấy từ ô tham số (M4 = 8). File mới dùng **một ô tham số VAT duy nhất**, và kiểm tra thuế suất tại thời điểm lập.
5. Định mức "0,1%" (thẩm định HSMT, kết quả lựa chọn nhà thầu) nhập dạng chữ. Công thức nhân với chữ có thể lỗi `#VALUE!` tùy cài đặt Excel. Công thức mới chặn tối đa 60 triệu nhưng **chưa chặn tối thiểu 2 triệu**, dù ghi chú có ghi.
6. Dòng kiểm tra nghiệm thu: chuỗi cách tính thiếu chữ " x " trước 1,08.
7. Sheet trượt giá: tổng chi phí thực hiện dự án (ô E6) **gõ tay**, không liên kết với tổng GXD + GQLDA + GTV + GK của sheet chính. Chỉ số giá là của TP.HCM, cần đổi theo địa phương và năm.
8. Phí thẩm định tính × 50% theo chính sách giảm phí có thời hạn (TT 64/2025/TT-BTC). Kiểm tra còn hiệu lực trước khi dùng.
9. Mẫu lưu `firstSheet=2`, có dòng ẩn (GPMB, khảo sát BCNCKT...) và ô cố định khung hỏng. Khi chép chỉ giữ sheet `TH TMDT`, phải đưa `firstSheet` về 0, bỏ chiều cao, ẩn dòng cũ, bỏ ngắt trang cũ; nếu không, Excel **không mở được file** hoặc mất dòng khi in.
10. Cột J có sẵn khung viền ở cả vùng dưới bảng. Phần chữ ký phải bỏ viền.

## Chương trình lập file tổng hợp (anh chốt 23/10/2026, chạy thử với bể tự hoại GN2026-HT-01)
Trình tự: dự toán hạng mục trên F1 (tới chi phí xây dựng) → **file tổng hợp** → **thuyết minh** lấy số từ file tổng hợp.

1. (Không bắt buộc) File F1 xuất ra sau khi chọn loại công trình, số bước, cấp ở sheet **TMĐT**: chỉ dùng để lấy tỷ lệ phí thẩm định dự án, kiểm toán, quyết toán (F1 theo TT 28/2023, NĐ 193/2026). Không khai báo thì 3 khoản này để trống, tô vàng "cần tra cứu".
2. Chạy `python/tong_hop_du_toan.py <file khai báo>` (xem mục File khai báo dự án trong SKILL.md). Chương trình:
   - Lấy chi phí xây dựng (G, GTGT, LT) từ sheet "Tổng hợp dự toán" của file hạng mục.
   - **Tỷ lệ QLDA, lập BCKTKT, thẩm tra TK, thẩm tra DT, giám sát, lập HSMT** (anh chốt 24/10/2026): công thức trỏ sang sheet `TT38` giữ lại trong file kết quả. Loại công trình theo **hạng mục có chi phí xây dựng trước thuế lớn nhất** (`linh_vuc` của hạng mục đó); tỷ lệ nội suy theo **tổng** chi phí xây dựng trước thuế cả dự án (TT38!C4 = GXD trước thuế). Thẩm định HSMT, KQLCNT 0,1%; nghiệm thu 20% giám sát; dự phòng khối lượng 5%: theo mẫu.
   - Ghi ra `du-toan_tong-hop.xlsx`, mọi số tiền đều là công thức, có một ô thuế suất VAT duy nhất (M4).
3. Chạy `python/thuyet_minh_du_toan.py <file khai báo>` (mẫu thuyết minh, xem `mau-thuyet-minh.md`).

Danh mục khoản theo mẫu công ty, chỉ giữ khoản dự án có. **F1 có thêm** một số khoản mẫu công ty không có (thẩm tra, thẩm định BCKTKT, giám sát đánh giá đầu tư, lập kế hoạch tổng thể LCNT, PCCC...): **không tự đưa vào**, báo anh quyết định.

Phí thẩm định dự án, kiểm toán, quyết toán trên F1 tính theo tổng mức đầu tư (F1 tính vòng lặp). File tổng hợp tạm lấy cơ sở **GXD + GQLDA + GTV (sau thuế)** để tránh công thức vòng tròn; báo anh nếu cần đổi.

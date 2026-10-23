# Mẫu thuyết minh dự toán (tài liệu tra cứu của skill gn-dutoan)

File mẫu: `template/du-toan/tong-hop/thuyet-minh-du-toan.docx` (anh chép vào ngày 23/10/2026; mẫu lấy từ dự án Nâng cấp, mở rộng đường KP8-15). Bìa đi kèm: `template/du-toan/tong-hop/bia-du-toan.docx`.

## Định dạng
- Khổ **Letter nằm ngang**, khung viền trang, Times New Roman 13.
- Đầu trang: "Dự án: <tên> ... Thuyết minh Dự toán". Chân trang: tên công ty và "Trang: x/y" (trường tự động).
- Đầu văn bản là bảng 2 cột: công ty / quốc hiệu, "Số: 02/TMDT.GN_2026", "TP. Hồ Chí Minh, ngày ... tháng ... năm ...".

## Bố cục
1. **THUYẾT MINH DỰ TOÁN**, dự án, địa điểm.
2. **I. CÁC CĂN CỨ LẬP DỰ TOÁN:** khối lượng; định mức, đơn giá, văn bản pháp lý gồm:
   a. Văn bản Luật; b. Nghị định – Thông tư; c. Văn bản của Sở, ban ngành TP.HCM (đơn giá, nhân công); văn bản quy hoạch; văn bản chủ trương, quyết định, hợp đồng của dự án; d. tài liệu khác (khảo sát, công bố giá vật liệu, giá nhiên liệu).
3. **II. PHƯƠNG PHÁP TÍNH TOÁN VÀ GIÁ TRỊ DỰ TOÁN:** phương pháp lập đơn giá; các chi phí tổng hợp (TT 36/2026); dự phòng.
4. **III. TỔNG MỨC ĐẦU TƯ:** khối lượng (xem bảng), kinh phí (tổng, bằng chữ, bảng 6 dòng: bồi thường, xây dựng, QLDA, tư vấn, khác, dự phòng).
5. Ghi chú, chữ ký Người lập, Giám đốc.

## Khi lập cho một hạng mục (cách A)
- Mục III đổi thành **GIÁ TRỊ DỰ TOÁN HẠNG MỤC**. Bảng kinh phí ghi T, GT, TL, GTGT, LT (không ghi QLDA, tư vấn, chi phí khác, dự phòng; các khoản này thuộc file tổng hợp).
- Bỏ văn bản không áp dụng (ví dụ văn bản riêng ngành đường bộ, bộ đơn giá cũ khi dùng đơn giá trực tiếp TT38/2026). Báo anh danh sách đã bỏ.
- Văn bản quy hoạch, chủ trương, hợp đồng, khảo sát là **riêng của từng dự án**: không chép của dự án cũ; để "......" và tô vàng.
- Số liệu lấy thẳng từ file dự toán (chương trình: `python/thuyet_minh_du_toan.py <file khai báo>`).

## Khi lập cho cả dự án (cách A, anh chốt 23/10/2026)
- Số liệu lấy từ **file tổng hợp** `du-toan_tong-hop.xlsx` (xem `mau-tong-hop.md`), không lấy từ file hạng mục. Chương trình kiểm tra GXD file tổng hợp khớp file hạng mục rồi mới viết.
- Mục II thêm đoạn cách tính QLDA, tư vấn, chi phí khác (căn cứ từng khoản) và dự phòng (khối lượng %, trượt giá).
- Mục III giữ **TỔNG MỨC ĐẦU TƯ**: tổng làm tròn, bằng chữ, bảng chi phí. Khoản dự án không có (ví dụ bồi thường) thì bỏ dòng.

## Lỗi, điểm lạ trong mẫu (làm đúng khi lập file mới)
1. "CÁC **CỨN** CỨ" → "CÁC **CĂN** CỨ".
2. Đầu trang ghi "KP**18**-15", trong khi thân văn bản ghi "KP8-15".
3. Một số dòng thiếu chữ "Căn cứ" ở đầu (NĐ 214/2025, NĐ 08/2022, TT 32/2026, TT 34/2026), có lỗi gõ "40/2026/T-BXD", "41/2026/TT-BD", "Chính phu".
4. Người ký trong mẫu (Trần Phú Thạnh, Đào Duy Sang) là của dự án cũ: hỏi anh trước khi ghi.
5. Các văn bản 2026 trong mẫu mới hơn kiến thức của Claude: **nhắc anh kiểm tra hiệu lực**, không tự khẳng định.

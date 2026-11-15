---
name: gn-dutoan
description: Bóc tách khối lượng từ bản vẽ (DWG, DXF, PDF) và lập dự toán, tổng mức đầu tư, bảng khối lượng mời thầu, bảng so sánh giá thầu vật tư theo định mức, đơn giá Việt Nam, xuất file Excel. Dùng khi anh Tuyên yêu cầu bóc khối lượng, tính khối lượng, thống kê vật tư, lập dự toán, áp mã hiệu định mức, tra đơn giá, giá vật liệu, so sánh báo giá vật tư, lập dự toán theo mẫu công ty cho dân dụng, công nghiệp, hạ tầng kỹ thuật, giao thông, bảng tổng hợp dự toán nhiều hạng mục.
---

# Bóc khối lượng và dự toán

Phạm vi:
- **Bóc khối lượng:** đọc bản vẽ DWG/DXF để bóc tách khối lượng và vật tư.
- **Dự toán, tổng mức đầu tư:** lập dự toán, tổng mức, bảng so sánh giá thầu vật tư.

Luôn tuân thủ mục **"Định mức, đơn giá và văn bản pháp lý"** trong CLAUDE.md global: ghi rõ nguồn, kiểm tra hiệu lực văn bản, không tự bịa mã hiệu định mức hay đơn giá.

Nếu cần đọc bản vẽ CAD bằng code thì dùng thêm skill `gn-banvecad-isocty` để biết layer và đơn vị của template công ty. Nếu việc là **thẩm tra** dự toán của người khác thì dùng skill `tham-tra`.

## Quy tắc bóc khối lượng và dự toán

- Kết quả xuất ra **file Excel** (.xlsx), gồm các cột:
  `STT | Mã hiệu định mức | Tên công việc / vật tư | Đơn vị | Diễn giải cách tính | Khối lượng | Ghi chú`
- Phần **diễn giải cách tính** phải ghi rõ để anh kiểm tra lại được, ví dụ: `2 x (10,5 x 0,3 x 0,5)`.
- Trong Excel, dùng **công thức** thay vì nhập sẵn con số, để anh dễ kiểm tra và sửa.
- Đơn vị dùng theo thông lệ dự toán: m, m², m³, tấn, kg, cái, bộ...
- Sắp xếp theo hạng mục công trình, giống bảng khối lượng mời thầu thông thường.
- Nếu bản vẽ thiếu số liệu hoặc không rõ thì **liệt kê ra để hỏi**, không tự đoán.

## Các việc có file tra cứu riêng (đọc đúng file khi gặp việc đó)

- **Bóc đào đắp + bê tông hầm ga, cống, mối nối từ trắc dọc thoát nước; bóc tổng hợp thoát nước + giao thông 1 file Excel:** đọc `boc-tu-trac-doc.md`. Nguyên tắc: tính động từ DXF theo tên layer, lấy chính file Excel mẫu làm nền, chỉ thêm/bớt số hàng. Không dựng bảng từ đầu rồi tự định dạng.
- **Từ bản vẽ đến phần mềm F1** (bóc khối lượng, gán mã, tạo file nhập F1, tính giá, xuất Excel): đọc `quy-trinh-f1.md`. Anh lập dự toán trên F1, Claude lo khối lượng và chuyển mẫu.
- **File khai báo dự án `.ini` và 3 chương trình** (`chuyen_f1_ve_mau.py`, `tong_hop_du_toan.py`, `thuyet_minh_du_toan.py`, chạy bằng `python/chay-du-toan.bat`): đọc `khai-bao-du-an.md`.

## Mẫu dự toán của công ty theo lĩnh vực

Anh chốt ngày 20/10/2026. Mỗi lĩnh vực có mẫu Excel riêng, file mẫu để trong `template/du-toan/<lĩnh vực>/`. Cách trình bày của từng mẫu ghi trong file tra cứu cùng thư mục với skill này (đọc ngày 20/10/2026, chỉ đọc các sheet đang hiện).

**Trước khi lập dự toán hạng mục, đọc 2 file:**
1. `mau-hang-muc-chung.md`: bố cục 4 sheet chung, định dạng, công thức, bảng tổng hợp kinh phí hạng mục, quy tắc lập file mới.
2. File của đúng lĩnh vực trong bảng dưới: sheet riêng, tỷ lệ chi phí trong mẫu, lỗi đã biết.

**Lập file tổng hợp dự toán chung:** đọc `mau-tong-hop.md`.

**Viết thuyết minh dự toán (Word):** đọc `mau-thuyet-minh.md` (mẫu `template/du-toan/tong-hop/thuyet-minh-du-toan.docx`).

| Lĩnh vực | Ví dụ công trình, hạng mục | File mẫu | File tra cứu |
|---|---|---|---|
| Dân dụng, công nghiệp | Nhà xưởng, nhà văn phòng, nhà hội quán, nhà bơm | `template/du-toan/dan-dung-cong-nghiep/du-toan-dd-cn.xlsx` | `mau-dan-dung-cong-nghiep.md` |
| Hạ tầng kỹ thuật | San nền, cấp thoát nước, bể tự hoại, xử lý nước thải, điện chiếu sáng | `template/du-toan/ha-tang-ky-thuat/du-toan-ha-tang.xlsx` | `mau-ha-tang-ky-thuat.md` |
| Giao thông | Đường, vỉa hè, cầu, cống qua đường, tổ chức giao thông | `template/du-toan/giao-thong/du-toan-giao-thong.xlsx` | `mau-giao-thong.md` |
| **Tổng hợp dự toán chung** | Bảng tổng hợp cả dự án nhiều hạng mục | `template/du-toan/tong-hop/bang-du-toan-tong-hop.xlsx` | `mau-tong-hop.md` |

Cột "Ví dụ" là đề xuất ban đầu. Hạng mục nào xếp nhóm nào chưa chắc (ví dụ nhà bơm, bể tự hoại) thì hỏi anh.

**Lưu ý chung cho cả 4 mẫu:**
- Tỷ lệ chi phí chung, thu nhập chịu thuế, VAT, định mức tư vấn trong mẫu **là của dự án cũ**. Phải xác định lại cho từng dự án, ghi căn cứ.
- Mỗi file tra cứu có mục "Lỗi, điểm lạ trong file mẫu". Khi lập file mới thì **làm đúng**, không chép theo lỗi.
- **Không sửa file mẫu.** Luôn chép ra thư mục kết quả rồi mới làm.

### Cách chọn mẫu
1. Anh **nói rõ lĩnh vực** (ví dụ "dự toán giao thông", "theo mẫu hạ tầng") thì dùng đúng mẫu đó.
2. Anh không nói thì tự xác định theo loại công trình, **báo anh mẫu đã chọn trước khi lập**.
3. Không xác định được thì **hỏi anh**, không tự đoán.

### Dự án nhiều hạng mục khác lĩnh vực (cách A)
Ví dụ Công viên I.22: nhà hội quán là dân dụng, san nền giao thông là giao thông, cấp thoát nước là hạ tầng kỹ thuật.

1. **Mỗi hạng mục một file Excel**, dùng mẫu của lĩnh vực hạng mục đó. File hạng mục **chỉ tính tới chi phí xây dựng** của hạng mục: chi phí trực tiếp, chi phí gián tiếp, thu nhập chịu thuế tính trước, VAT. **Không tính** chi phí QLDA, tư vấn, chi phí khác, dự phòng trong file hạng mục.
2. **Một file Excel tổng hợp dự toán chung riêng**, theo mẫu tổng hợp:
   - Lấy chi phí xây dựng của từng hạng mục, cộng thành **tổng chi phí xây dựng** của dự án.
   - Trên tổng đó mới tính **chi phí quản lý dự án, chi phí tư vấn đầu tư xây dựng, chi phí khác, chi phí dự phòng** (và chi phí thiết bị, bồi thường nếu có).
3. Giá trị chi phí xây dựng trong file tổng hợp phải **khớp đúng** với dòng chi phí xây dựng cuối cùng của từng file hạng mục. Ghi rõ nguồn từng dòng (tên file hạng mục).
4. Tên file, ví dụ:
   - `du-toan_01-nha-hoi-quan.xlsx`, `du-toan_03-san-nen-giao-thong.xlsx`...
   - `du-toan_tong-hop.xlsx`
   - Đánh số theo danh mục hạng mục của dự án.

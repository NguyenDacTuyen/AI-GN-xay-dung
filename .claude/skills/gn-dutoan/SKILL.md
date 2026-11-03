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

## Bóc khối lượng tự động từ trắc dọc thoát nước, xuất theo mẫu (đọc `boc-tu-trac-doc.md`)

Khi bóc **đào đắp + bê tông hầm ga (giếng thu)** hạ tầng thoát nước: làm theo file tra cứu **`boc-tu-trac-doc.md`** (cùng thư mục skill). Nguyên tắc 2 bước:
1. **Tính động** từ DXF trắc dọc theo tên layer (bao nhiêu giếng cũng được), khối lượng dùng công thức.
2. **Lấy chính file Excel mẫu làm nền**, chỉ thêm/bớt số hàng cho khớp số giếng → giữ nguyên 100% định dạng mẫu (in ngang, lề, hàng, cột, số lẻ, ô gộp).
Không dựng bảng từ đầu rồi tự định dạng; không mở mẫu điền tay vào số hàng cố định.

Hai bộ công cụ (cùng file mẫu `mau hamga.xlsx`, cùng sheet "DINH HINH CONG" để tra):
- **Hầm ga (giếng thu):** `python/boc-ham-ga-thoat-nuoc.py` (`chay-boc-ham-ga.bat`) → tab "Dao dap ho ga".
- **Cống + mối nối/gối cống:** `python/boc-cong-moinoi-thoat-nuoc.py` (`chay-boc-cong-moinoi.bat`) → tab "Dao dap cong" + "Moi noi-goi cong", mỗi đoạn ghép 2 giếng đầu/sau, tra VLOOKUP vào "DINH HINH CONG".

Tên layer, cột, công thức, thông số, bảng định hình: xem **`boc-tu-trac-doc.md`**. Bản vẽ khác chuẩn layer thì sửa CẤU HÌNH đầu chương trình (tự in danh sách layer nếu sai tên). Số cột trong chương trình phải khớp header tab của file mẫu, nếu không sẽ lệch cột.

## Trình tự bản vẽ → phần mềm Dự toán F1 (anh chốt 22/10/2026, đã chạy thử khớp 100% với bể tự hoại GN2026-HT-01)

Anh lập dự toán trên **phần mềm F1** (cài ở `C:\Program Files (x86)\DuToanF1`; sau bản cập nhật 22/10/2026 cửa sổ F1 chạy bằng `dutoanf1.exe`, khi điều khiển màn hình phải xin quyền đúng tên này). Không cần anh làm bảng khối lượng Excel:

1. **Vẽ** theo ISO_CTY, anh duyệt bản vẽ.
2. **Bóc khối lượng** từ số liệu bản vẽ, mỗi công tác có các dòng diễn giải `tên bộ phận: biểu thức`.
3. **Gán mã** theo định mức đang dùng (TT 38/2026), chọn công tác tương tự theo tên, đưa anh **duyệt một bảng duy nhất**. Đổi đơn vị theo định mức (ví dụ m3 → 100m3 thì nhân 0,01; quét 2 lớp thì nhân 2).
4. **Tạo file nhập F1** bằng chương trình (mẫu: `python/f1_nhap_be_tu_hoai.py`). Sheet gồm cột A STT, B mã hiệu, C tên công tác / diễn giải, D đơn vị, E khối lượng, dữ liệu từ dòng 2. Dòng diễn giải để trống STT và mã. Khối lượng từng dòng làm tròn 4 số lẻ **kiểu Excel** (làm tròn ở 15 chữ số có nghĩa, rồi 5 làm tròn lên).
5. **Trên F1, tạo công trình mới** (không đè file `.ctr` có sẵn), bấm **Nhập Excel** (nút cạnh biểu tượng in, *không* bấm nhầm Xuất Excel), chọn file, khai báo: Cột mã công tác = B, Tên = C, Đơn vị = D, Khối lượng = E, lấy từ dòng 2, rồi bấm **Đồng ý** và chọn **Tra lại công tác**. Trong hộp tra lại, để **trống ô "Tên công tác"** (giữ tên của mình), tích đơn vị và định mức VL, NC, máy.
6. **Giá:**
   - **Nhân công:** sheet Nhân công, bấm Tính lương, chọn QĐ 4570 Vùng I, rồi Áp giá hiện tại.
   - **Máy:** sheet Máy thi công, bấm Tính giá ca máy (TT 37/2026), rồi Áp giá hiện tại.
   - **Vật liệu:** sheet Vật liệu, chuột phải, chọn "Lấp giá vật liệu từ cơ sở dữ liệu – tất cả vật liệu", chọn bảng giá TP.HCM mới nhất, bấm **Chọn giá cao nhất**.
   - **Vật tư lấy tại mỏ (đá, cát):** bấm Cước ô tô; nhập cự ly, chọn xe tự đổ 10 tấn, nhập giá ca máy xe (lấy ở sheet Máy thi công); dòng nào chưa có loại hàng thì chọn loại hàng (ví dụ "đá dăm (10m3)") và quy đổi 10. Nhập bằng phím **Tab** (phím Enter làm bảng cuộn, dễ nhập nhầm dòng). Cuối cùng bấm Áp cước ô tô.
7. **Tính:** sheet Công trình, tích "Tính đơn giá trực tiếp cho VL, NC, Máy", chọn Yes, rồi "Có, thay đổi mẫu" (THDT theo TT 36/2026).
8. **Giá vật tư ngoài công bố** (ví dụ côn, cút nhựa) do anh nhập; có thể chuột phải chọn "Lưu giá vật liệu vào cơ sở dữ liệu" để lần sau F1 tự lấy.
9. **Xuất Excel** từ F1 ra tên mới. Màn hình F1 có thể **chưa cập nhật** tổng vật liệu sau khi áp cước; con số đúng là số trong file xuất sau khi Excel tính lại. Sau đó chạy `python/chuyen_f1_ve_mau.py <file khai báo>` để ra file theo mẫu công ty của đúng lĩnh vực (xem mục File khai báo dự án).

Không ghi trực tiếp vào file `.ctr` của F1 (định dạng riêng). Hộp thoại cập nhật phần mềm F1 do chương trình khác mở, phải nhờ anh bấm.

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

## File khai báo dự án (anh chốt 23/10/2026, dùng chung cho hạ tầng kỹ thuật và giao thông)
Ba chương trình `python/chuyen_f1_ve_mau.py` (F1 → dự toán hạng mục theo mẫu), `python/tong_hop_du_toan.py` (tổng hợp), `python/thuyet_minh_du_toan.py` (thuyết minh) **không sửa code cho từng dự án**. Mọi thông tin riêng của dự án (tên dự án, địa điểm, chủ đầu tư, các hạng mục và lĩnh vực, ký hiệu bản vẽ, tên file, cự ly vận chuyển, số thông báo giá, khoản tạm tính, văn bản riêng, người ký) ghi trong **một file khai báo `.ini`**:
1. Chép `python/mau-khai-bao-du-an.ini` vào thư mục kết quả của dự án (`ket-qua/<du-an>/khai-bao-du-an.ini`), điền thông tin. Ô chưa có để trống, chương trình ghi "......" và tô vàng. Mẫu đã có giải thích từng dòng.
2. Mỗi hạng mục ghi `linh_vuc = ha-tang-ky-thuat` hoặc `linh_vuc = giao-thong`. Chương trình chuyển mẫu chọn file mẫu và tên sheet theo dòng này (bảng `MAU_LV` trong chương trình), tự dò các dòng mẫu định dạng.
3. Chạy lần lượt 3 chương trình, mỗi lệnh kèm đường dẫn file khai báo. Ví dụ đã chạy: `ket-qua/be-tu-hoai-10m3/khai-bao-du-an.ini`.
   **Cách anh dùng (chốt 24/10/2026):** thư mục dự án đặt ở đâu cũng được (ngoài AI_Cad_K1), chỉ cần chép vào đó: file khai báo `khai-bao-du-an.ini`, file `python/chay-du-toan.bat` và các file F1 xuất ra; **không chép chương trình, không chép mẫu**. Nhấp đúp `chay-du-toan.bat` là chạy đủ 3 bước, dừng và báo rõ khi bước nào lỗi (ví dụ file kết quả đã có). Trong `.bat`, dòng `CT=` trỏ tới `AI_Cad_K1\python`; dời thư mục AI_Cad_K1 hoặc sang máy khác thì sửa dòng này (máy khác phải chép giữ cấu trúc `python\` và `template\du-toan\`). Chữ trong `.bat` viết không dấu, xuống dòng kiểu Windows (CRLF).
4. Dự án nhiều hạng mục: thêm mục `[hang_muc_2]`, `[hang_muc_3]`... (có thể khác lĩnh vực). File tổng hợp cộng chi phí xây dựng các hạng mục.
5. Chương trình đọc file khai báo: `python/khai_bao.py`. Thêm thông tin mới thì thêm vào cả file đó và file mẫu `.ini`.

Theo lĩnh vực:
- **File dự toán hạng mục:** 6 sheet theo mẫu (tổng hợp, chi tiết khối lượng, phân tích vật tư, vật liệu, nhân công, máy). Mẫu chỉ hiện 4 sheet; sheet ẩn (bìa, dự thầu, đơn giá chi tiết...) **không đọc, không chép**. Bìa dùng file Word `template/du-toan/tong-hop/bia-du-toan.docx`.
- **Tổng hợp (chốt 24/10/2026):** tỷ lệ QLDA và tư vấn tra **sheet TT38 của mẫu tổng hợp**, loại công trình theo hạng mục có chi phí xây dựng trước thuế lớn nhất, nội suy theo tổng chi phí xây dựng trước thuế cả dự án; **không cần file F1 TMĐT** (phí thẩm định dự án, kiểm toán, quyết toán cũng tra sheet TT38). Chi tiết và lỗi đã biết của sheet TT38: `mau-tong-hop.md`. Khoản tạm tính khai báo: `dam_bao_giao_thong` (trước thuế, cộng vào chi phí khác), `di_doi_ha_tang` (đã gồm thuế, mục VI riêng, không tính dự phòng).
- **Thuyết minh:** bộ đơn giá cũ (QĐ 2966/2023, 1491/2024, 959/2025) luôn bỏ. Văn bản ngành đường bộ (NĐ 165/2024, QĐ 38/QĐ-GT, CV 2424/SGTVT, QĐ 1762/QĐ-SGTVT) giữ khi dự án có hạng mục giao thông, bỏ khi chỉ có hạ tầng. Văn bản của Sở Giao thông vận tải cũ: nhắc anh kiểm tra hiệu lực (các sở đã sắp xếp lại từ 2025).

Giới hạn hiện tại: chỉ có mẫu **hạ tầng kỹ thuật** và **giao thông** (chưa có dân dụng, công nghiệp). Anh sửa mẫu lần nữa thì kiểm tra lại chương trình; chương trình báo lỗi rõ khi không thấy sheet hoặc dòng mốc. Dự phòng trượt giá chỉ hỗ trợ "không tính". Chi phí bồi thường chưa hỗ trợ. Giao thông mới chạy thử bằng số liệu F1 của bể tự hoại; dự án giao thông thật đầu tiên cần đối chiếu kỹ.

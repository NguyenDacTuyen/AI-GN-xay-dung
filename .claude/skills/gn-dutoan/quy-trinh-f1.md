# Trình tự bản vẽ → phần mềm Dự toán F1 (anh chốt 22/10/2026, đã chạy thử khớp 100% với bể tự hoại GN2026-HT-01)

Anh lập dự toán trên **phần mềm F1** (cài ở `C:\Program Files (x86)\DuToanF1`; sau bản cập nhật 22/10/2026 cửa sổ F1 chạy bằng `dutoanf1.exe`, khi điều khiển màn hình phải xin quyền đúng tên này). Không cần anh làm bảng khối lượng Excel:

1. **Vẽ** theo ISO_CTY, anh duyệt bản vẽ.
2. **Bóc khối lượng** từ số liệu bản vẽ, mỗi công tác có các dòng diễn giải `tên bộ phận: biểu thức`.
3. **Gán mã** theo định mức đang dùng (TT 38/2026), chọn công tác tương tự theo tên, đưa anh **duyệt một bảng duy nhất**. Đổi đơn vị theo định mức (ví dụ m3 → 100m3 thì nhân 0,01; quét 2 lớp thì nhân 2).
4. **Tạo file nhập F1** bằng chương trình (mẫu: `python/f1_nhap_be_tu_hoai.py`). Sheet gồm cột A STT, B mã hiệu, C tên công tác / diễn giải, D đơn vị, E khối lượng, dữ liệu từ dòng 2. Dòng diễn giải để trống STT và mã. Khối lượng từng dòng làm tròn 4 số lẻ **kiểu Excel** (làm tròn ở 15 chữ số có nghĩa, rồi 5 làm tròn lên).
5. **Trên F1, tạo công trình mới** (không đè file `.ctr` có sẵn), bấm **Nhập Excel** (nút cạnh biểu tượng in, *không* bấm nhầm Xuất Excel), chọn file, khai báo: Cột mã công tác = B, Tên = C, Đơn vị = D, Khối lượng = E, lấy từ dòng 2, rồi bấm **Đồng ý** và chọn **Tra lại công tác**. Trong hộp tra lại, để **trống ô "Tên công tác"** (giữ tên của mình), tích đơn vị và định mức VL, NC, máy.
6. **Giá:**
   - **Nhân công:** sheet Nhân công, bấm Tính lương, chọn QĐ 4570 Vùng I, rồi Áp giá hiện tại.
   - **Máy:** sheet Máy thi công, bấm Tính giá ca máy (TT 37/2026, `Cần xác nhận lại`: số hiệu thông tư giá ca máy), rồi Áp giá hiện tại.
   - **Vật liệu:** sheet Vật liệu, chuột phải, chọn "Lấp giá vật liệu từ cơ sở dữ liệu – tất cả vật liệu", chọn bảng giá TP.HCM mới nhất, bấm **Chọn giá cao nhất**.
   - **Vật tư lấy tại mỏ (đá, cát):** bấm Cước ô tô; nhập cự ly, chọn xe tự đổ 10 tấn, nhập giá ca máy xe (lấy ở sheet Máy thi công); dòng nào chưa có loại hàng thì chọn loại hàng (ví dụ "đá dăm (10m3)") và quy đổi 10. Nhập bằng phím **Tab** (phím Enter làm bảng cuộn, dễ nhập nhầm dòng). Cuối cùng bấm Áp cước ô tô.
7. **Tính:** sheet Công trình, tích "Tính đơn giá trực tiếp cho VL, NC, Máy", chọn Yes, rồi "Có, thay đổi mẫu" (THDT theo TT 36/2026).
8. **Giá vật tư ngoài công bố** (ví dụ côn, cút nhựa) do anh nhập; có thể chuột phải chọn "Lưu giá vật liệu vào cơ sở dữ liệu" để lần sau F1 tự lấy.
9. **Xuất Excel** từ F1 ra tên mới. Màn hình F1 có thể **chưa cập nhật** tổng vật liệu sau khi áp cước; con số đúng là số trong file xuất sau khi Excel tính lại. Sau đó chạy `python/chuyen_f1_ve_mau.py <file khai báo>` để ra file theo mẫu công ty của đúng lĩnh vực (xem `khai-bao-du-an.md`).

Không ghi trực tiếp vào file `.ctr` của F1 (định dạng riêng). Hộp thoại cập nhật phần mềm F1 do chương trình khác mở, phải nhờ anh bấm.

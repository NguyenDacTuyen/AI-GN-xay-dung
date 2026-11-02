# 07 — Kiểm tra hồ sơ (ky-su-kiem-tra) — DEMO

> Agent chính ghi nguyên văn báo cáo của ky-su-kiem-tra (agent chỉ đọc, không có quyền Write). Phần "Soát số học Excel" ở cuối do agent chính đứng ra làm thay kiem-tra-khoi-luong, vì subagent ở máy này không chạy được Python để mở .xlsx.

## Kết luận: CẦN SỬA

Phạm vi đã đối chiếu với DXF (bằng Grep, chỉ đọc):
- Số giếng thu 30 khả tín: `KHGMBGiengThu` xuất hiện 33 lần (30 INSERT + 1 BLOCK_RECORD + 2 dòng BLOCK); có HG01..HG30, không có HG31+.
- `DeMatCatGiengThu` 30 cái, `MatCatGiengThu` 29 cái (khớp điểm lệch 29/30 mà 02 đã tự nêu).
- `TP15_BD_MB_Cong`, `TP16_BD_Timcong` chỉ xuất hiện ở bảng layer và tên STYLE chữ → khớp nhận định "layer cống trống".
- 1.212 dòng `ACAD_PROXY_ENTITY` (khớp 02).
- Chưa đối chiếu được bằng Grep: chủ sở hữu `1F`, layer gắn từng INSERT, tọa độ X lẫn dấu, Y chung → ghi "chưa tự đối chiếu".
- Số học trong Excel: xem mục cuối.

| STT | File | Vị trí | Vấn đề | Mức độ | Giao lại cho | Đề xuất sửa |
|---|---|---|---|---|---|---|
| 1 | 02 | Mục 1, 5.1, 6 | 02 ghi Excel "CHƯA tạo" nhưng file `KL-thoat-nuoc-demo.xlsx` đã tồn tại. Cần xác nhận lại. | Cao | ky-su-boc-khoi-luong; kiem-tra-khoi-luong | Cập nhật trạng thái, ghi rõ ai tạo file và lúc nào. |
| 2 | 00 vs 02 | 00 mục 3 "proxy là cống" | 00 khẳng định hình cống nằm trong proxy; 02 nói chưa phân loại proxy. Không khớp, 00 kết luận chưa đủ bằng chứng. | Trung bình | điều phối | Sửa 00 thành "có 1.212 proxy, chưa xác định proxy nào là cống. Cần xác nhận lại". |
| 3 | 02 | Mục 3.2 | Bảng cống 6 cột, thiếu "Diễn giải"/"Nguồn" trong khi mục 3.1 đủ 7 cột. | Trung bình | ky-su-boc-khoi-luong | Đưa về 7 cột; cột Nguồn ghi `Tài liệu không đề cập`. |
| 4 | 02 | Mục 2, 6 | Script nằm trong scratchpad, ngoài dự án, chưa chạy thử; xóa thư mục tạm là mất. | Trung bình | ky-su-boc-khoi-luong | Lưu script vào `python/` hoặc thư mục demo (tên `NN_`), hoặc ghi rõ chỉ tham khảo. |
| 5 | 02 | Mục 3.3 | "ĐM TT38/2026", "công bố giá HCM" chưa dẫn nguồn trong hồ sơ. | Thấp | ky-su-boc-khoi-luong | Ghi nguồn (anh Tuyên cung cấp, F1) + "Cần xác nhận lại hiệu lực". |
| 6 | 02 | Mục 3.1 STT 2 cột Nguồn | Ghi "chưa có kích thước kết cấu" là lý do, không phải nguồn. | Thấp | ky-su-boc-khoi-luong | Ghi `Tài liệu không đề cập (chưa mở block mặt cắt giếng)`. |
| 7 | 02 | Mục 3.2 | "chỉ có trong bảng layer" chưa đủ; còn là tên STYLE chữ. | Thấp | ky-su-boc-khoi-luong | Bổ sung "và là tên style chữ, không phải hình học". |
| 8 | 02 vs 00 | Tên "giếng thu" vs nhãn "Hố Ga" | Bản vẽ ghi HG01..HG30; "giếng thu" là suy diễn. 02 đã nêu, 00 chưa đưa vào "Cần xác nhận lại". | Thấp | điều phối | Thêm vào 00 mục 5 dòng "30 vị trí HG đều là giếng thu? Cần xác nhận lại". |
| 9 | 00 | Mục 3 cột Sản phẩm | Dòng kiem-tra-khoi-luong chưa ghi tên file đầu ra. | Thấp | điều phối | Ghi tên file đầu ra theo quy ước `NN_`. |

Nội dung đã soát và đạt:
- Số giếng thu 00 (30) và 02 (30) khớp nhau và khớp DXF.
- Phạm vi: cả hai file chỉ nói thoát nước (giếng thu + cống dọc).
- Phụ thuộc nhất quán giữa 00 và 02.
- Cả 00 và 02 đủ 6 mục mẫu chung.
- Không tự điền giá; không tự tính chiều dài cống từ khoảng cách hố ga (02 từ chối đúng). Mã hiệu, đơn giá, kết cấu giếng, kích thước cống đều `[Chờ bổ sung]`.
- Các điểm `Cần xác nhận lại` đã nêu rõ.
- Cần soát thêm: tọa độ X lẫn dấu (23 âm, 7 dương), Y chung 1206630.195 — chưa đối chiếu được, đề nghị người lập kiểm nếu dùng vị trí.

File đã đọc: `handoff/00_ke-hoach.md`, `handoff/02_khoi-luong.md`, `F:\demo\Acad_BD_TD_TN Nhi Binh 5.dxf` (Grep/Read đoạn dòng 14105–14154), Glob thư mục demo.
File chưa đọc được: `KL-thoat-nuoc-demo.xlsx` (nhị phân, cần kiem-tra-khoi-luong); script trong scratchpad; `gn-dutoan/SKILL.md`; các handoff 01, 03+.

---

## Soát số học Excel (đứng thay kiem-tra-khoi-luong — agent chính chạy Python)

- Sheet trong file: `KL thoat nuoc`, `Giếng thu`, `Bảng tọa độ trong bản vẽ`.
- Sheet `Giếng thu`: **30 dòng dữ liệu** (A2:A31).
- Dòng giếng thu (hàng 7) ô Khối lượng là **công thức** `=COUNTA('Giếng thu'!A2:A31)` → đếm đúng vùng 30 dòng = 30 cái. Không gõ tay số.
- Bảng chính đủ **7 cột** theo gn-dutoan; mọi ô Mã hiệu định mức và Khối lượng cống đều `[Chờ bổ sung]`, không có số bịa.
- Giá trị (data_only) đang trống vì file do chương trình tạo, chưa mở lưu bằng Excel — đây là chuyện bình thường, chỉ cần mở F1/Excel một lần để tính lại công thức. Không tính là lỗi.
- Kết luận số học: **Đạt** ở phạm vi đã có; phần cống chờ bổ sung số liệu, không kiểm được.

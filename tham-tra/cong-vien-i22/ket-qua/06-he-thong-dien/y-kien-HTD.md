# Ý kiến thẩm tra – Hạng mục 06: Hệ thống điện (mã `HTD`)

Dự án: Xây dựng Công viên I.22 – xã Tân Xuân (nay xã Hóc Môn, TP.HCM). Báo cáo số 2611/BCTTr/2026_GN. Thẩm tra độc lập, vốn đầu tư công. Hệ thống điện thuộc phần hạ tầng kỹ thuật, chủ trì: ông Lê Văn Hoàng.

> **DỰ THẢO** do Claude soạn ngày 28/10/2026 để anh Tuyên duyệt. Kết luận cuối cùng do anh quyết định. Chỗ ghi "cần anh xác nhận" là giả thiết hoặc nhận định chưa chắc chắn.

## Hồ sơ đã kiểm tra

- Bản vẽ `01. DIEN-BVTC-CV-I22.dwg`, 6 tờ: **Đ-01** mặt bằng cấp điện tổng thể (tủ DB.T, bãi tiếp địa, chi tiết mương cáp), **Đ-02** mặt bằng chiếu sáng tổng thể (10 mạch TT_L1 ÷ TT_L10, danh mục đèn, chi tiết móng trụ, chi tiết trụ), **Đ-03** sơ đồ nguyên lý tủ điện chính DB.T, **Đ-04** mặt bằng cấp điện, chiếu sáng nhà hội quán (tầng 1, 2, mái) và nhà rác-XLNT, **Đ-05** mặt bằng điện nhẹ tổng thể, sơ đồ mạng, camera, **Đ-06** điện nhẹ nhà hội quán, thống kê vật tư. Khung tên là xref bị thiếu; bảng thống kê vật tư Đ-06 là ảnh nhúng, không đọc được.
- Dự toán `6.HT dien.xlsx`: 97 công tác (tổng thể 31, khối nhà hội quán + phụ trợ 37, điện nhẹ 29), chi phí trực tiếp 2.155.421.012 đ, Gxd **2.669.119.064 đ** (khớp dòng HM 6 sheet XD-TB của `0.TMĐT.xlsx`).
- Phần chung: thuyết minh `01. TM TKBVTC-DIEN` (có phụ lục bảng tính phụ tải, chọn CB, cáp), `03. QUY TRINH VH&BT-MEP`, thuyết minh kiến trúc phần A (điện), B (internet – wifi), C (camera); `0.TMĐT.xlsx`; khái toán TKCS `260630 KHÁI TOÁN TKCS` (.xlsx).
- Không có trong hồ sơ: kết quả tính Dialux; tính toán sụt áp, nối đất, móng trụ; số liệu điện trở suất đất, địa chất; thỏa thuận đấu nối với Điện lực; báo giá vật tư, thiết bị.

## Tóm tắt

| | Mức A | Mức B | Mức C | Cộng |
|---|---|---|---|---|
| Thiết kế | 0 | 5 | 7 | 12 |
| Dự toán | 3 | 5 | 6 | 14 |

Giá trị dự toán HM 06 (chỉ tính các ý kiến đã lượng hóa): đề nghị **2.669.119.068 đ** (cộng lại từ bảng, lệch 4 đ so với hồ sơ do làm tròn), thẩm tra **2.285.637.209 đ**, **giảm 383.481.859 đ (−14,37%)**. Trong đó:
- Giảm do khối lượng (DT-HTD-03 ÷ 07): chi phí trực tiếp −94.110.227 đ, tương đương Gxd khoảng **−116,5 triệu đ** (−4,37%).
- Giảm do chuyển giá mua thiết bị điện nhẹ 215.566.800 đ (chưa VAT) sang chi phí thiết bị (DT-HTD-02): Gxd giảm thêm khoảng 266,9 triệu đ, nhưng chi phí thiết bị tăng 232.812.144 đ (sau VAT). Tính chung Gxd + Gtb giảm **150.669.715 đ**.
- Giá trị còn có thể thay đổi lớn theo DT-HTD-01 (khoảng 1.371,7 triệu đ vật liệu, thiết bị chưa có báo giá), DT-HTD-08, 09, 10, 11.

## VI. Ý kiến về thiết kế

### VI.1. Sự phù hợp với bước thiết kế trước

**TK-HTD-01 – Mức B (Kiến nghị sửa) – Toàn hạng mục 06 so với khái toán TKCS (260630 KHÁI TOÁN TKCS, sheet XD-TB, mục 'Hệ thống điện tổng thể'):**
- Nội dung: TKCS tính hệ thống điện tổng thể khoảng 1.529,8 triệu đ (102 đèn trụ cao 3 m, 20 đèn pha sân thể thao 200W, 70 đèn hắt cây 36W, 69 đèn nấm 5W, cáp CXV 3Cx2,5 3.625 m, ống PVC D32 3.679 m...). Điện trong nhà hội quán nằm trong suất vốn nhà chính; TKCS còn có 'thiết bị xây lắp' 247,6 triệu đ theo suất vốn, TMĐT không còn khoản này. Bước BVTC: 78 (+8) trụ trang trí 3,5 m, 8 đèn pha sân, 10 đèn cắm cỏ, 18 đèn nấm, thêm 3 trụ đèn 7,5 m bãi xe, thêm hệ thống camera, wifi và toàn bộ điện trong nhà hội quán, nhà rác-XLNT. Gxd HM 06 là 2.669.119.064 đ, tăng khoảng 1.139 triệu đ (+74%) so với phần điện tổng thể của TKCS.
- Căn cứ: Luật Xây dựng số 135/2025/QH15 (hiệu lực 01/7/2026) – quy định về sự phù hợp của thiết kế bước sau với thiết kế bước trước (điều, khoản cần tra cứu); khái toán TKCS 63.947.000.000 đ
- Đề xuất: Đơn vị thiết kế lập bảng so sánh quy mô, chủng loại đèn, thiết bị giữa TKCS và BVTC, giải trình nguyên nhân tăng (bổ sung camera, wifi, điện trong nhà; giảm số đèn pha sân từ 20 xuống 8). Ghi chú: chưa có số, ngày quyết định phê duyệt dự án để đối chiếu (xem phiếu thông tin dự án).

### VI.2. Quy chuẩn, tiêu chuẩn, vật liệu, thống nhất hồ sơ

**TK-HTD-02 – Mức C (Lưu ý, làm rõ) – Thuyết minh TKBVTC điện (01. TM TKBVTC-DIEN), mục A.I.2, A.IV.1, B.I, A.III.4:**
- Nội dung: Danh mục tiêu chuẩn có văn bản cũ hoặc chưa rõ hiệu lực: '11 TCN-18-84' (quy phạm trang bị điện cũ, đã có bộ 11 TCN 18÷21-2006), 'TCN68-136:1995' (tiêu chuẩn ngành bưu điện cũ), 'TCVN 5175-90'. Chưa viện dẫn QCVN 07-7:2023/BXD (công trình chiếu sáng, ban hành kèm TT 15/2023/TT-BXD, hiệu lực 01/7/2024) là quy chuẩn bắt buộc cho chiếu sáng công cộng ngoài trời. TCVN 13608:2023 thẩm tra chưa tra được. QCVN 09:2017/BXD vẫn áp dụng đến hết 31/01/2027 (QCVN 04-3:2026/BXD có hiệu lực từ 01/02/2027).
- Căn cứ: QCVN 07-7:2023/BXD (TT 15/2023/TT-BXD, hiệu lực 01/7/2024); QCVN 12:2014/BXD (cần kiểm tra hiệu lực); QCVN 09:2017/BXD và QCVN 04-3:2026/BXD (TT 61/2026/TT-BXD, hiệu lực 01/02/2027 – cần kiểm tra); TCVN 13608:2023 (cần kiểm tra hiệu lực)
- Đề xuất: Cập nhật danh mục quy chuẩn, tiêu chuẩn còn hiệu lực; bổ sung QCVN 07-7:2023/BXD; bỏ các tiêu chuẩn đã thay thế.

**TK-HTD-03 – Mức C (Lưu ý, làm rõ) – Đ-03 (ghi chú, sơ đồ DB.T), Đ-02 (danh mục chiếu sáng, mục 5), Đ-04 (ký hiệu ổ cắm); thuyết minh mục A.II.4; dự toán công tác 1, 6:**
- Nội dung: Hồ sơ chưa thống nhất: (1) Thuyết minh ghi hệ thống '1 pha, 3 dây', ghi chú Đ-03 ghi '1 pha 2 dây'. (2) Cáp nguồn: bảng tính thuyết minh 'CXV-3x1Cx35', Đ-03 'CXV/DSTA 3Cx35', diễn giải dự toán '2Cx35'. (3) Đèn bãi xe: Đ-02 ghi 'bóng LED 100W, trụ cao 7,5 m'; bảng phụ tải L8 = 3 × 100W = 0,3 kW; thuyết minh đặc tính kỹ thuật ghi đèn đường 150W; dự toán công tác 1 ghi 'đèn pha 150W, trụ 6 m + cần 1,5 m'. (4) Ghi chú timer Đ-03 có hai dòng 'TIMER-2' khác giờ (19h–22h và 18h–21h), không có TIMER-3. (5) Ký hiệu ổ cắm Đ-04 ghi '16A-22V'. (6) Bảng phụ tải có 3 mạch dự phòng (20A, 20A, 25A) nhưng sơ đồ Đ-03 không thể hiện.
- Căn cứ: Yêu cầu thống nhất hồ sơ thiết kế giữa thuyết minh, bản vẽ và dự toán
- Đề xuất: Thống nhất số dây, quy cách cáp nguồn, công suất và chiều cao trụ đèn bãi xe, ghi chú timer, ký hiệu ổ cắm, mạch dự phòng; cập nhật dự toán tương ứng.

**TK-HTD-04 – Mức C (Lưu ý, làm rõ) – Toàn bộ 6 tờ Đ-01 ÷ Đ-06; chi tiết móng trụ đèn (Đ-02); bảng thống kê vật tư (Đ-06):**
- Nội dung: (1) Tỷ lệ ghi trên tờ khác tỷ lệ khung nhìn: Đ-01, Đ-02, Đ-05 ghi 1/200 nhưng khung nhìn 1/250; Đ-04, Đ-06 ghi 1/100 nhưng khung nhìn 1/111 (MB nhà rác-XLNT 1/120) – cần anh xác nhận khi in vì khung tên là xref bị thiếu trong file. (2) Chi tiết móng trụ: kích thước bị gõ đè, hai kích thước đo được 300 nhưng ghi '240' và 'tối thiểu 800 mm'. (3) Bảng thống kê vật tư Đ-06 là ảnh nhúng (OLE), không đọc, kiểm tra được số liệu. (4) Khung tên không đọc được (xref thiếu) nên không kiểm tra được số hiệu, ngày, người ký.
- Căn cứ: Yêu cầu về thể hiện hồ sơ thiết kế (tỷ lệ, kích thước, khung tên)
- Đề xuất: Sửa tỷ lệ ghi hoặc tỷ lệ khung nhìn; ghi kích thước đúng hình vẽ; gửi kèm bảng thống kê vật tư dạng Excel hoặc PDF; gắn khung tên vào file nộp thẩm tra.

**TK-HTD-09 – Mức B (Kiến nghị sửa) – Đ-02, chiếu sáng sân thể thao (mạch TT_L9, TT_L10: 8 trụ 6 m, đèn pha LED 200W); thuyết minh mục A.II.1:**
- Nội dung: Thuyết minh yêu cầu sân đa năng 400 lux, tính bằng Dialux nhưng không kèm kết quả. Thẩm tra tính sơ bộ: 8 đèn × 24.000 lm = 192.000 lm; sân theo vị trí trụ ≈ 26,0 × 17,3 m = 448,5 m²; hệ số sử dụng 0,5, hệ số duy trì 0,8 (giả thiết – cần anh xác nhận) → độ rọi trung bình ≈ 171 lux, chỉ khoảng 43% yêu cầu 400 lux. TKCS bố trí 20 đèn pha. Ngược lại, đèn trụ trang trí 30W đặt dày (mạch L1: 21 đèn trên khoảng 120 m tuyến, khoảng cách ≈ 5,7 m) cho độ rọi lối đi ước ≈ 50 lux, cao hơn nhiều so với 10 lux yêu cầu.
- Căn cứ: QCVN 07-7:2023/BXD (yêu cầu chiếu sáng công cộng – điều, khoản cần tra cứu); thuyết minh mục A.II.1
- Đề xuất: Bổ sung kết quả tính Dialux cho sân thể thao và các khu vực; điều chỉnh yêu cầu độ rọi theo cấp sử dụng sân (tập luyện, giải trí) hoặc tăng số đèn; xem xét giãn khoảng cách đèn trụ trang trí để tiết kiệm chi phí.

**TK-HTD-10 – Mức C (Lưu ý, làm rõ) – Toàn hạng mục 06; nhà hội quán (HM 01):**
- Nội dung: Hồ sơ chỉ có chống sét lan truyền trên đường nguồn (SPD tại tủ DB.T) và cho cổng LAN camera; chưa có thiết kế hoặc đánh giá sự cần thiết chống sét đánh thẳng cho nhà hội quán 2 tầng đặt giữa công viên, trụ đèn pha sân và cột camera. Hồ sơ HM 01 cũng không có phần chống sét.
- Căn cứ: TCVN 9385:2012 Chống sét cho công trình xây dựng – hướng dẫn thiết kế, kiểm tra và bảo trì (cần kiểm tra hiệu lực)
- Đề xuất: Đơn vị thiết kế đánh giá rủi ro sét và bổ sung thiết kế chống sét đánh thẳng (nếu cần) cho nhà hội quán; xác định thuộc HM 01 hay HM 06.

**TK-HTD-11 – Mức C (Lưu ý, làm rõ) – Đ-04 (mặt bằng cấp điện, chiếu sáng nhà hội quán); thuyết minh Phần 2 mục B.I.2:**
- Nội dung: HM 06 đã gồm điện chiếu sáng, ổ cắm, quạt trong nhà hội quán và chiếu sáng nhà rác-XLNT (trả lời điểm kiểm tra chéo TK-HQ-02). Tuy nhiên thuyết minh phần thi công nêu 'chiếu sáng an toàn và chiếu sáng hướng dẫn thoát hiểm' nhưng bản vẽ, dự toán không có đèn chiếu sáng sự cố, đèn chỉ dẫn thoát nạn; chưa có bố trí PCCC (báo cháy, bình chữa cháy) cho nhà hội quán.
- Căn cứ: QCVN 06:2022/BXD và Sửa đổi 1:2023 – yêu cầu chiếu sáng sự cố, chỉ dẫn thoát nạn (điều, khoản cần tra cứu; cần kiểm tra hiệu lực)
- Đề xuất: Đơn vị thiết kế xác định yêu cầu PCCC của nhà hội quán theo quy mô; bổ sung đèn sự cố, đèn exit (nếu thuộc diện phải có) vào HM 06 hoặc HM 01.

**TK-HTD-12 – Mức C (Lưu ý, làm rõ) – Đ-01 'Chi tiết mương cáp cấp nguồn điển hình'; Đ-02 tuyến cáp chiếu sáng; thuyết minh mục A.III.3:**
- Nội dung: Thuyết minh yêu cầu 'nơi băng qua đường hoặc rãnh thoát nước mưa, cáp phải luồn ống sắt', nhưng bản vẽ và dự toán chỉ có ống HDPE xoắn, không có chi tiết băng đường, không có ống thép. Chưa có mặt bằng tuyến mương cáp ghi kích thước, vị trí băng qua sân đường, giao cắt với cống thoát nước (HM 07). Dự toán HM 06 không có công tác hoàn trả mặt sân, đường, nên chưa thấy tính trùng với HM 03, nhưng cần quy định trình tự: mương cáp, ống chờ băng đường phải làm trước khi thi công kết cấu sân đường của HM 03.
- Căn cứ: Thuyết minh mục A.III.3; TCVN 7997:2009 Cáp điện lực đi ngầm trong đất – phương pháp lắp đặt (cần kiểm tra hiệu lực)
- Đề xuất: Bổ sung mặt bằng tuyến mương cáp có kích thước, chi tiết băng đường (ống bảo vệ), vị trí giao cắt với HM 07; ghi chú trình tự thi công phối hợp với HM 03.

### VI.3. An toàn công trình, kết quả tính kiểm tra

**TK-HTD-05 – Mức B (Kiến nghị sửa) – Đ-03 sơ đồ nguyên lý tủ DB.T: mạch DB.T/L1 ÷ L5 (MCB 1P 10–16A), DB.BSH (MCB 2P-16A), DB.XLNT (MCB 2P-32A):**
- Nội dung: Các mạch chiếu sáng trong nhà L1 ÷ L5, mạch cấp nguồn tủ bơm nước sinh hoạt và tủ XLNT chỉ có MCB, không có thiết bị chống dòng rò (RCD/RCBO). Thuyết minh mục A.III.1.e yêu cầu 'độ nhạy 30 mA cho mạch cuối'. Hồ sơ chưa nêu sơ đồ nối đất (TT hay TN-C-S). Nếu là sơ đồ TT (nối đất tại chỗ R ≤ 4 Ω, nguồn từ lưới hạ áp điện lực), MCB 32A đường cong C chỉ cắt sự cố chạm vỏ khi dòng ≥ khoảng 320 A, tức điện trở nối đất ≤ 50/320 ≈ 0,16 Ω – không đạt được, nên các mạch này không được bảo vệ chống điện giật khi chạm vỏ (bơm, tủ XLNT đặt ngoài trời, nơi ẩm ướt).
- Căn cứ: TCVN 7447-4-41:2010 (IEC 60364-4-41:2005) mục 411.5 – bảo vệ trong sơ đồ TT (cần kiểm tra hiệu lực); QCVN 12:2014/BXD (cần kiểm tra hiệu lực); thuyết minh mục A.III.1.e
- Đề xuất: Ghi rõ sơ đồ nối đất của hệ thống; bổ sung RCD/RCBO cho các mạch L1 ÷ L5, DB.BSH, DB.XLNT (hoặc RCD tổng có chọn lọc); cập nhật dự toán. Mức B – anh cân nhắc nâng mức A vì liên quan an toàn người.

**TK-HTD-06 – Mức C (Lưu ý, làm rõ) – Thuyết minh, phụ lục 'Bảng tính công suất điện – chọn CB và dây dẫn'; Đ-03:**
- Nội dung: Thẩm tra tính kiểm tra lại (chi tiết ở mục kết quả tính kiểm tra): công suất đặt 26,536 kW, tính toán 16,718 kW, 19,668 kVA, dòng 89,4 A; CB tổng 100A; cáp 35 mm² – khớp hồ sơ, các mạch nhánh đạt điều kiện phát nóng. Tồn tại: (1) Thuyết minh yêu cầu 'đảm bảo độ sụt áp cho phép' nhưng không có bảng tính sụt áp; thẩm tra tính sơ bộ mạch xa nhất L7 (khoảng 223 m cáp 2,5 mm²) sụt áp 2,2 ÷ 4,3% cộng cáp nguồn khoảng 1,4% ở phụ tải tính toán, có thể vượt 3% khuyến nghị cho chiếu sáng. (2) Mạch đi ngầm (D1) dùng hệ số K1 theo nhiệt độ không khí 35°C, K2 = 1 trong khi nhiều mạch đi chung mương gần tủ DB.T (chưa xét hệ số nhóm). (3) Cấp nguồn 1 pha 89,4 A từ lưới điện lực: chưa có văn bản thỏa thuận đấu nối. (4) Phụ tải XLNT dành 4,5 kW (MCB 32A, cáp 6 mm²) trong khi tổng công suất thiết bị XLNT trong TMĐT (sheet HTXLNT) khoảng 1,43 kW; bơm cấp nước 1,5 kW chưa đối chiếu với bơm tăng áp biến tần của HM 07.
- Căn cứ: TCVN 9207:2012 (cần kiểm tra hiệu lực); TCVN 7447-5-52:2010 phụ lục G (sụt áp, tham khảo – cần kiểm tra hiệu lực); thuyết minh mục A.II.2
- Đề xuất: Bổ sung bảng tính sụt áp từng mạch; xét hệ số nhóm và nhiệt độ đất cho cáp ngầm; bổ sung thỏa thuận đấu nối với Điện lực (xem xét cấp nguồn 3 pha); đối chiếu công suất tủ XLNT, tủ bơm với HM 02, HM 07.

**TK-HTD-07 – Mức B (Kiến nghị sửa) – Đ-01 bãi tiếp địa tủ DB.T (3 cọc Þ16 L = 2,4 m, cáp đồng trần 25 mm², 'R < 4 Ohm'); chi tiết móng trụ (1 cọc/trụ):**
- Nội dung: Hồ sơ yêu cầu điện trở nối đất ≤ 4 Ω nhưng không có tính toán, không có số liệu điện trở suất đất. Thẩm tra tính sơ bộ với điện trở suất giả thiết 100 Ω.m: 1 cọc ≈ 35,8 Ω; 3 cọc cách 3 m ≈ 15,3 Ω; cáp nối 6 m ≈ 23,5 Ω; cả hệ ≈ 10 Ω > 4 Ω. Muốn đạt 4 Ω với 3 cọc thì điện trở suất đất phải ≤ khoảng 39 Ω.m (cần anh xác nhận giả thiết).
- Căn cứ: TCVN 9358:2012 Lắp đặt hệ thống nối đất thiết bị cho các công trình công nghiệp (cần kiểm tra hiệu lực); TCVN 7447-5-54:2005 (cần kiểm tra hiệu lực); thuyết minh mục A.IV
- Đề xuất: Bổ sung tính toán nối đất theo điện trở suất đất đo tại hiện trường; ghi chú trên bản vẽ: đo nghiệm thu, nếu R > 4 Ω thì bổ sung cọc hoặc dùng hóa chất giảm điện trở; cập nhật dự toán.

**TK-HTD-08 – Mức B (Kiến nghị sửa) – Đ-02 'Chi tiết móng trụ đèn (điển hình)'; dự toán công tác 24 ÷ 30:**
- Nội dung: Một chi tiết móng dùng chung cho 89 trụ có chiều cao khác nhau (3,5 m trang trí; 6 m + cần 1,5 m đèn pha sân; 7,5 m bãi xe): móng BT M200 0,6×0,6×1,2 m, 4 bulong M24×1250. Hồ sơ không có tính toán móng trụ chịu gió. Thẩm tra tính sơ bộ trụ 7,5 m (áp lực gió tính toán giả thiết 1,0 kN/m² – cần anh xác nhận theo TCVN 2737:2023 cho xã Hóc Môn): mô men chân trụ ≈ 5,5 kN.m, trong khi mô men giữ do trọng lượng khối móng + trụ chỉ ≈ 3,7 kN.m; khả năng chống lật phụ thuộc phản lực ngang của đất, cần số liệu địa chất (chưa có trong hồ sơ, nền đất yếu miền Nam). Ngược lại, với trụ trang trí 3,5 m Ø76 thì móng 0,43 m³ và bulong M24×1250 là lớn.
- Căn cứ: TCVN 2737:2023 Tải trọng và tác động (thay TCVN 2737:1995); TCVN 9362:2012 (cần kiểm tra hiệu lực); QCVN 07-7:2023/BXD
- Đề xuất: Bổ sung tính toán móng trụ (gió, lật, trượt, sức chịu tải ngang của đất) cho từng loại trụ; thiết kế móng riêng cho trụ 7,5 m, trụ đèn pha sân và trụ trang trí 3,5 m; cập nhật khối lượng.

#### Kết quả tính kiểm tra (bổ sung cho TK-HTD-05 ÷ 09)

**1. Phụ tải và chọn CB, cáp tổng** (số liệu hồ sơ, thẩm tra tính lại):
- Công suất đặt: ổ cắm 6,6 + chiếu sáng trong nhà 3,711 + chiếu sáng ngoài nhà 4,6 + bơm 1,5 + XLNT 4,5 + máy lạnh 1,125 + dự phòng 4,5 = **26,536 kW** (khớp).
- Ptt = 26,536 × 0,9 × 0,7 = **16,718 kW**; Stt = 16,718 / 0,85 = **19,668 kVA**; I = 19.668 / 220 = **89,4 A** (khớp). MCCB 2P-100A ≥ 89,4 A: đạt. Cáp 35 mm² đi ngầm (D1): Icp 122 A × 0,96 = 117 A ≥ 100 A: đạt.
- Mạch nhánh: Ilv = P / (220 × 0,85), ví dụ ổ cắm 1,8 kW: 9,63 A ≤ CB 16A ≤ Idd 18,3 A (2,5 mm² A1): đạt; XLNT 4,5 kW: 24,1 A ≤ 32A ≤ 44,2 A (6 mm² D1): đạt. Các mạch còn lại tương tự, đạt điều kiện phát nóng.
- Ghi chú: Icp hồ sơ dùng (2,5 mm² 29 A; 4 mm² 37 A; 6 mm² 46 A ở D1) là giá trị cho cách điện PVC – thiên về an toàn với cáp CXV (XLPE). Chưa xét hệ số nhóm, nhiệt độ đất. Với 6 ÷ 10 mạch chiếu sáng chung mương, giả thiết hệ số nhóm 0,5 và nhiệt độ đất 0,89 thì mạch 2,5 mm² còn ≈ 29 × 0,89 × 0,5 = 12,9 A > CB 10A: vẫn đạt.

**2. Sụt áp mạch chiếu sáng ngoài nhà** (thẩm tra đo tuyến cáp trên Đ-02, chiều dài từ DB.T đến đầu tuyến lấy theo đường thẳng × 1,2; r(2,5 mm², 70°C) = 8,87 Ω/km, r(4 mm²) = 5,52 Ω/km; ΔU = 2·I·r·L; hai cận: tải tập trung cuối tuyến và tải phân bố đều ≈ 1/2):

| Mạch | Cáp | I (A) | L (m) | ΔU tập trung cuối (%) | ΔU phân bố đều (%) |
|---|---|---|---|---|---|
| TT_L1 (21 × 30W) | 2,5 | 3,37 | 103 | 2,79 | ≈ 1,4 |
| TT_L5 (14 × 30W) | 2,5 | 2,25 | 114 | 2,07 | ≈ 1,0 |
| TT_L6 (16 × 30W) | 2,5 | 2,57 | 129 | 2,68 | ≈ 1,3 |
| TT_L7 (15 × 30W, xa nhất) | 2,5 | 2,41 | 223 | 4,33 | ≈ 2,2 |
| TT_L9, TT_L10 (4 × 200W) | 4 | 4,28 | 43 ÷ 67 | 0,92 ÷ 1,44 | ≈ 0,5 ÷ 0,7 |
| Cáp nguồn 35 mm², 25 m, 89,4 A | 35 | 89,4 | 25 | 1,36 | – |
| DB.XLNT, 6 mm², 20 m | 6 | 24,1 | 20 | 1,62 | – |

Kết quả: mạch xa nhất L7 cộng cáp nguồn khoảng 3,6 ÷ 5,7% (ở phụ tải tính toán toàn tủ). Hồ sơ cần bảng tính sụt áp chính thức với chiều dài thực tế (TK-HTD-06).

**3. Nối đất bãi tiếp địa DB.T** (3 cọc Þ16 L = 2,4 m cách 3 m, cáp nối 25 mm² dài 6 m chôn sâu 0,8 m; điện trở suất đất giả thiết ρ = 100 Ω.m – cần anh xác nhận):
- 1 cọc: R = ρ/(2πL) × [ln(4L/d) − 1] = 100/(2π × 2,4) × [ln(600) − 1] ≈ **35,8 Ω**.
- 3 cọc, hệ số sử dụng ≈ 0,78: 35,8 / (3 × 0,78) ≈ **15,3 Ω**. Cáp nối nằm ngang: R = ρ/(2πL) × ln(L²/(h·d)) ≈ 2,65 × 8,86 ≈ **23,5 Ω**.
- Cả hệ ≈ (15,3 × 23,5)/(15,3 + 23,5)/0,9 ≈ **10 Ω > 4 Ω**. Đạt 4 Ω khi ρ ≤ khoảng 39 Ω.m.

**4. Móng trụ đèn 7,5 m** (áp lực gió tính toán giả thiết 1,0 kN/m², hệ số khí động 1,2 – cần anh xác nhận theo TCVN 2737:2023):
- Thân trụ bát giác Ø164 ÷ 55, cao 7,5 m: diện tích chắn gió ≈ 7,5 × 0,11 = 0,83 m² → F ≈ 0,99 kN đặt ở 3,75 m → M ≈ 3,7 kN.m. Đèn + cần ≈ 0,2 m² → F ≈ 0,24 kN ở 7,5 m → M ≈ 1,8 kN.m. Tổng **M ≈ 5,5 kN.m** tại chân trụ.
- Khối móng 0,6 × 0,6 × 1,2 m: G ≈ 10,8 kN + trụ ≈ 1,5 kN → mô men giữ quanh mép móng ≈ 12,3 × 0,3 ≈ **3,7 kN.m < 5,5 kN.m**. Móng chỉ ổn định nhờ phản lực ngang của đất, cần tính theo số liệu địa chất (TK-HTD-08).

**5. Độ rọi sân thể thao** (phương pháp quang thông; hệ số sử dụng 0,5, hệ số duy trì 0,8 – giả thiết, cần anh xác nhận):
- 8 trụ ở hai hàng dài 26,0 m, cách nhau 17,3 m (đo trên Đ-02) → diện tích ≈ 448,5 m². Quang thông 8 × 24.000 = 192.000 lm.
- E_tb ≈ 192.000 × 0,5 × 0,8 / 448,5 ≈ **171 lux < 400 lux** yêu cầu trong thuyết minh (TK-HTD-09).

### VI.4. Dây chuyền công nghệ

Không có. Tủ điều khiển XLNT (72 triệu đ) thuộc chi phí thiết bị HTXLNT trong TMĐT; HM 06 chỉ cấp nguồn đến tủ DB.XLNT và DB.BSH (xem TK-HTD-06).

### VI.5. Yêu cầu hoàn thiện hồ sơ (phần HM 06)

- Thiết kế: 0 ý kiến mức A, 5 mức B, 7 mức C.
- Dự toán: 3 ý kiến mức A, 5 mức B, 6 mức C.
- Ý kiến mức A bắt buộc sửa trước khi trình thẩm định: DT-HTD-01, DT-HTD-02, DT-HTD-03. Anh cân nhắc nâng TK-HTD-05 (thiếu chống dòng rò cho bơm, XLNT, chiếu sáng trong nhà) lên mức A vì liên quan an toàn người.

## VII. Ý kiến về dự toán

### VII.1.1 – VII.1.3. Căn cứ pháp lý, sự phù hợp với TMĐT, phương pháp lập

- Giá trị HM 06 trong dự toán tổng hợp `0.TMĐT.xlsx` (sheet XD-TB dòng 6, nhóm "Công trình hạ tầng") là 2.669.119.064 đ, khớp THKP của hạng mục.
- So với khái toán TKCS: xem TK-HTD-01.

**DT-HTD-13 – Mức C (Lưu ý, làm rõ) – Sheet 'THKP hạng mục':**
- Nội dung: Hồ sơ dùng tỷ lệ công trình HTKT cho cả hạng mục: chi phí chung 5,5% × T; chi phí không xác định khối lượng 2% × T; TNCT 5,5%; nhà tạm 1,1% × Gxdtt × (1+8%); VAT 8%. Tỷ lệ khớp Bảng 3.3, 3.5, 3.6 Phụ lục III TT 36/2026 cho HTKT. Nhưng HM 06 gồm cả điện trong nhà hội quán (công trình dân dụng: 7,3%; 2,5%; 5,5%). Ước tính phần trong nhà (công tác 32 ÷ 68, khoảng 224,9 triệu đ chi phí trực tiếp hồ sơ, gồm cả tủ DB.T) nếu áp tỷ lệ dân dụng thì tăng khoảng 5,5 triệu đ trước thuế. Tỷ lệ nhà tạm 1,1% cần thống nhất theo Gxd trước thuế trong TMĐT (khoảng 19,2 tỷ, Bảng 3.7: 1,0%) – xem điểm kiểm tra chéo TH.
- Căn cứ: TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD) Phụ lục III, Bảng 3.3, 3.5, 3.6, 3.7; VAT 8% theo NQ 204/2025/QH15, NĐ 174/2025/NĐ-CP (đến 31/12/2026 – kiểm tra thuế suất tại thời điểm lập)
- Đề xuất: Thống nhất cách xếp loại công trình phần điện trong nhà (tách sang HM 01 hoặc áp tỷ lệ dân dụng cho phần này) và tỷ lệ nhà tạm ở bước tổng hợp (ý kiến TH).

### VII.1.4. Khối lượng, định mức, đơn giá, các khoản chi phí

**DT-HTD-01 – Mức A (Bắt buộc sửa) – Sheet 'Giá tháng' – các dòng ghi nguồn 'Tham khảo giá thị trường'; công tác 1 ÷ 5, 15 ÷ 17, 32 ÷ 34, 43 ÷ 91:**
- Nội dung: Phần lớn vật liệu, thiết bị ghi nguồn 'Tham khảo giá thị trường', không kèm báo giá, chứng thư thẩm định giá: tổng giá trị vật liệu loại này khoảng 1.371,7 triệu đ, bằng 77,7% chi phí vật liệu và 63,6% chi phí trực tiếp HM 06. Lớn nhất: đèn trụ trang trí 7.524.790 đ/bộ × 86 bộ (647,1 triệu đ); trụ đèn pha, trụ bãi xe 18.850.000 đ/bộ × 11 bộ (207,4 triệu đ); camera, switch, router, đầu ghi, UPS. Một số giá bất thường: đèn LED cắm cỏ 18W 6.528.340 đ/bộ (TKCS: đèn hắt cây 36W 995.159 đ/bộ gồm cả lắp đặt); dây nhảy CAT6 1 m 191.400 đ/sợi. Nhóm cáp, ống, CB ghi nguồn 'Bảng giá công bố Cadivi, Sino Vanlock' (giá hãng), chưa rõ có trong TB 32431/TB-SXD hay không.
- Căn cứ: TT 37/2026/TT-BXD (hiệu lực 01/7/2026), phần xác định giá vật liệu, thiết bị (điều, khoản cần tra cứu); TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD) Phụ lục IV tiết 2.2.1.1 (giá vật liệu từ công bố giá, báo giá, công trình tương tự; không có thì thẩm định giá); dự án vốn đầu tư công
- Đề xuất: Bổ sung báo giá (tối thiểu 3 báo giá) hoặc chứng thư thẩm định giá cho đèn, trụ đèn, thiết bị điện nhẹ; ghi rõ gồm hay chưa gồm VAT, vận chuyển, lắp đặt; ghi nguồn theo số thứ tự trong TB 32431 cho vật liệu có trong công bố giá. Thẩm tra tạm giữ giá trị, sẽ điều chỉnh sau khi có báo giá.

**DT-HTD-02 – Mức A (Bắt buộc sửa) – Công tác 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 84 (switch, router, đầu ghi hình, ổ cứng, màn hình, AP wifi, camera, UPS):**
- Nội dung: Giá mua các thiết bị điện nhẹ (camera, đầu ghi, switch, router, wifi, màn hình, UPS) được đưa vào chi phí vật liệu của chi phí xây dựng, nên bị tính thêm chi phí chung, chi phí không xác định khối lượng, thu nhập chịu thuế tính trước và nhà tạm. Đây là thiết bị, thuộc chi phí thiết bị (TKCS có khoản 'thiết bị xây lắp' riêng). Giá trị giá mua 215.566.800 đ (chưa VAT). Nếu chuyển sang Gxd thẩm tra giảm thêm khoảng 267 triệu đ, chi phí thiết bị tăng 232.812.144 đ (sau VAT), tổng mức đầu tư giảm khoảng 34,1 triệu đ (chưa tính các chi phí tư vấn tính theo Gtb).
- Căn cứ: NĐ 206/2026/NĐ-CP về quản lý chi phí đầu tư xây dựng (hiệu lực 01/7/2026), quy định nội dung chi phí xây dựng, chi phí thiết bị (điều, khoản cần tra cứu); TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD); dự án vốn đầu tư công
- Đề xuất: Tách giá mua thiết bị điện nhẹ sang chi phí thiết bị (bảng chi phí thiết bị riêng có báo giá), giữ chi phí lắp đặt trong chi phí xây dựng. Danh mục thiết bị chuyển là giả thiết thẩm tra (tủ rack, patch panel, PDU, chống sét LAN vẫn để trong Gxd) – cần anh xác nhận.

**DT-HTD-03 – Mức A (Bắt buộc sửa) – Công tác 47 – BA.23301 Đèn trụ trang trí Ø76 cao 3,5 m LED 30W (mục 'khối nhà hội quán + phụ trợ'), 8 bộ:**
- Nội dung: Bản vẽ Đ-02 có 78 trụ trang trí 30W (mạch L1 21, L4 12, L5 14, L6 16, L7 15; khớp bảng phụ tải 0,63 + 0,36 + 0,42 + 0,48 + 0,45 kW), đã tính đủ ở công tác 3 (78 bộ). Móng trụ (công tác 24 ÷ 30) chỉ tính 89 móng = 3 + 8 + 78. Mặt bằng Đ-04 và bảng phụ tải không có thêm 8 trụ. Công tác 47 tính thừa 8 bộ, chi phí trực tiếp 63.062.379 đ.
- Căn cứ: TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD) – khối lượng đo bóc theo thiết kế; bản vẽ Đ-02, Đ-04; dự án vốn đầu tư công
- Đề xuất: Loại công tác 47 (giảm 63.062.379 đ chi phí trực tiếp), hoặc bổ sung bản vẽ thể hiện 8 trụ này kèm móng, cáp. Cần anh xác nhận.

**DT-HTD-04 – Mức B (Kiến nghị sửa) – Công tác 27 – BA.14404 Ống HDPE xoắn D40/30 chờ trong móng trụ:**
- Nội dung: Diễn giải 89 trụ × 1,6 m = 142,4 m nhưng ghi đơn vị '100m' với khối lượng 1,424, trong khi đơn giá 87.353 đ là đơn giá cho 1 m (giống công tác 11 cùng mã) nên thành tiền chỉ 124.391 đ. Thẩm tra: 142,4 m × 87.353 đ = 12.439.055 đ, tăng 12.314.664 đ chi phí trực tiếp.
- Căn cứ: TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD) (đo bóc khối lượng, đơn vị tính theo định mức); TT 38/2026/TT-BXD – định mức xây dựng (hiệu lực 01/7/2026)
- Đề xuất: Sửa đơn vị tính thành 'm', khối lượng 142,4.

**DT-HTD-05 – Mức B (Kiến nghị sửa) – Công tác 16 – BA.19102 Cọc đồng tiếp đất L2400 D16 (120 cọc); công tác 17 – Mối hàn hóa nhiệt (120 mối):**
- Nội dung: Không có diễn giải. Theo bản vẽ: mỗi móng trụ 1 cọc (chi tiết móng trụ) × 89 móng + bãi tiếp địa tủ DB.T 3 cọc (Đ-01) = 92 cọc, 92 mối hàn. Thẩm tra giảm 28 cọc, 28 mối hàn: −20.450.354 đ chi phí trực tiếp. Ngoài ra phần điện nhẹ (công tác 94 ÷ 97) lại tính thêm 1 bãi tiếp địa (3 cọc, 15 m cáp 25 mm², hộp kiểm tra) – chưa rõ là bãi riêng cho tủ rack hay trùng bãi DB.T (tủ rack đặt cạnh DB.T trên Đ-01); tên vật tư 'cọc đồng' nhưng bản vẽ ghi 'thép mạ đồng' (giá 325.000 đ phù hợp cọc thép mạ đồng).
- Căn cứ: Bản vẽ Đ-01, Đ-02 (chi tiết móng trụ); TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD)
- Đề xuất: Diễn giải số cọc, mối hàn theo bản vẽ; làm rõ bãi tiếp địa riêng cho tủ rack; ghi đúng chủng loại cọc. Cần anh xác nhận số cọc 92.

**DT-HTD-06 – Mức B (Kiến nghị sửa) – Công tác 87 – BA.17202 Ổ cắm RJ45 – Data, 390 cái:**
- Nội dung: Hệ thống điện nhẹ có 12 camera dome, 10 camera thân, 4 AP wifi (26 điểm) và 35 dây nhảy; 390 nhân RJ45 không phù hợp quy mô, không có diễn giải. Thẩm tra tính 26 điểm × 2 đầu (đầu thiết bị và patch panel loại 'unloaded') = 52 cái, giảm 20.060.805 đ chi phí trực tiếp (cần anh xác nhận).
- Căn cứ: TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD) (đo bóc khối lượng theo thiết kế)
- Đề xuất: Diễn giải số lượng ổ, nhân RJ45 theo sơ đồ nguyên lý mạng (Đ-05).

**DT-HTD-07 – Mức B (Kiến nghị sửa) – Công tác 26 – AF.81311 Ván khuôn (diễn giải gồm ván khuôn bê tông lót 21,36 m²):**
- Nội dung: Diễn giải ván khuôn gồm cả bê tông lót đá 4×6 M100 dày 100 dưới móng trụ (89 × 0,6 × 4 × 0,1 = 21,36 m²). Bê tông lót đổ trực tiếp xuống đáy hố đào, thông thường không tính ván khuôn. Thẩm tra 249,2 m² (hồ sơ 270,6 m²), giảm 2.851.353 đ chi phí trực tiếp – cần anh xác nhận.
- Căn cứ: TT 38/2026/TT-BXD – định mức xây dựng (hiệu lực 01/7/2026), thuyết minh áp dụng định mức ván khuôn (cần tra cứu); bản vẽ chi tiết móng trụ
- Đề xuất: Bỏ ván khuôn bê tông lót, hoặc giải trình biện pháp thi công cần ván khuôn lót.

**DT-HTD-08 – Mức B (Kiến nghị sửa) – Công tác 31 – BA.14302 'CCLĐ lớp gạch thẻ bảo vệ đường ống', 662 md; sheet 'Giá tháng' dòng 'Lớp gạch thẻ bảo vệ đường ống' 24.000 đ/m:**
- Nội dung: Vận dụng mã BA.14302 (lắp đặt ống nhựa) cho công tác lát một lớp gạch thẻ bảo vệ cáp, không có thuyết minh vận dụng; vật liệu tính gộp 24.000 đ/m, nguồn 'Tham khảo QĐ 2966/QĐ-UBND' (chưa rõ văn bản), không thể hiện số viên gạch/m, gạch loại gì. Giá trị 25.141.081 đ.
- Căn cứ: TT 38/2026/TT-BXD – định mức xây dựng (hiệu lực 01/7/2026) – điều kiện áp dụng, vận dụng định mức (mã hiệu cần tra cứu); TT 37/2026/TT-BXD (hiệu lực 01/7/2026)
- Đề xuất: Áp định mức xây, lát gạch phù hợp (mã hiệu cần tra cứu) hoặc lập định mức mới có thuyết minh; vật liệu gạch tính theo số viên/m theo chi tiết mương cáp, giá theo TB 32431. Thẩm tra tạm giữ giá trị.

**DT-HTD-09 – Mức C (Lưu ý, làm rõ) – Công tác 6 ÷ 14, 66 ÷ 68, 89 ÷ 93 (cáp, ống luồn, cáp đồng trần), sheet 'DGKL':**
- Nội dung: Các công tác cáp, ống chỉ ghi tổng khối lượng, không diễn giải theo mạch, đoạn (CXV 3Cx2,5 1.452 m; ống HDPE 32/25 1.415 m + 620 m; CV 1Cx1,5 1.610 m...). Thẩm tra đo trên Đ-02: tuyến cáp chiếu sáng vẽ khoảng 648 m (13 đoạn), chưa kể đoạn từ tủ DB.T ra đầu tuyến, đoạn lên trụ và trong thân trụ – chưa đủ cơ sở kết luận. Mương cáp 662 m: diễn giải 620 m trùng đúng chiều dài ống điện nhẹ, chưa rõ cách tính.
- Căn cứ: TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD) – đo bóc khối lượng phải có diễn giải theo bản vẽ
- Đề xuất: Bổ sung bảng diễn giải khối lượng cáp, ống, mương theo từng mạch (đoạn trong mương, đoạn lên trụ, trong thân trụ, dự phòng đấu nối). Thẩm tra tạm giữ khối lượng.

**DT-HTD-10 – Mức C (Lưu ý, làm rõ) – Công tác 36 ÷ 41 (MCB, RCBO), 48 ÷ 65 (đèn, quạt, công tắc, ổ cắm trong nhà), 80 ÷ 82 (AP, camera):**
- Nội dung: (1) Số CB khác sơ đồ Đ-03: RCBO 16A sơ đồ 7 (S1 ÷ S4, TT_L1, L9, L10) – dự toán 6; RCBO 10A sơ đồ 7 – dự toán 8; MCB 1P-16A sơ đồ 2 – dự toán 3; MCB 2P-16A, 2P-32A sơ đồ 1 cái mỗi loại – dự toán 2 cái mỗi loại. (2) Số camera, AP đếm sơ bộ trên Đ-05, Đ-06 (camera thân khoảng 12 ÷ 13, camera dome khoảng 6, AP khoảng 3) khác dự toán (10, 12, 4). (3) Đèn, quạt, công tắc trong nhà: ký hiệu trên Đ-04 phần lớn là khối lồng, bảng thống kê Đ-06 là ảnh nhúng, thẩm tra chưa đối chiếu được.
- Căn cứ: Yêu cầu thống nhất bản vẽ và dự toán; TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD)
- Đề xuất: Lập bảng thống kê vật tư (Excel) đếm theo bản vẽ; thống nhất số lượng CB, camera, AP giữa sơ đồ, mặt bằng và dự toán.

**DT-HTD-11 – Mức C (Lưu ý, làm rõ) – Công tác 1, 2 (đơn giá đã gồm 'móng trụ đèn 04 bulong M24×1250'), 29, 30 (SX, LD thép hình 0,507 tấn), 3 (trụ trang trí):**
- Nội dung: Thép hình 0,507 tấn là bản mã 240×240×6 (2 bản/trụ) và bản nhỏ cho 89 trụ, trong khi đơn giá trụ ở công tác 1, 2 (11 trụ) đã gồm bộ móng bulong – có thể tính trùng phần khung móng cho 11 trụ này. Ngược lại 78 trụ trang trí (công tác 3) không có công tác bulong M24×1250 riêng, chưa rõ đơn giá trụ đã gồm bulong chưa. Bulong dài 1.250 trong khi móng cao 1.200.
- Căn cứ: Chi tiết móng trụ Đ-02; TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD)
- Đề xuất: Làm rõ thành phần đơn giá trụ đèn (gồm bulong, bản mã hay không); bỏ phần trùng; thống nhất chiều dài bulong với chiều cao móng.

**DT-HTD-12 – Mức C (Lưu ý, làm rõ) – Sheet 'Giá tháng' – lỗi nhập liệu, nguồn giá:**
- Nội dung: (1) 'Dây nhảy CAT6 1m' đơn vị 'm', giá 191.400 đ nhưng giá sau VAT 22.143 đ. (2) 'Cáp tín hiệu HDMI' đơn vị 'sợi' trong dự toán nhưng giá lấy theo đơn giá cáp mạng 20.130 đ/m. (3) Cát: giá sau VAT 376.971 đ nhỏ hơn giá gốc 388.950 đ; đá 1×2, đá 4×6, cát vàng có tỷ lệ 'giá sau VAT' không thống nhất. (4) Thép hình, thép tấm ghi 'Bảng giá công bố tháng 7/2026 thép VN Kyoie' (giá hãng, không phải TB 32431); gỗ, đinh, nước ghi 'Tham khảo QĐ 2966/QĐ-UBND' chưa rõ văn bản, còn hiệu lực hay không. (5) Mã chuẩn của nhiều thiết bị gán 'Aptomat3Pha50' (không đúng loại vật tư).
- Căn cứ: TT 37/2026/TT-BXD (hiệu lực 01/7/2026) – xác định giá vật liệu (cần tra cứu điều khoản); TB 32431/TB-SXD-KTVLXD ngày 09/9/2026 của Sở Xây dựng TP.HCM
- Đề xuất: Sửa các lỗi nhập liệu; ghi nguồn giá theo số thứ tự trong TB 32431; giải trình hoặc thay QĐ 2966/QĐ-UBND bằng công bố giá hiện hành.

**DT-HTD-14 – Mức C (Lưu ý, làm rõ) – Công tác 18 ÷ 23 (đào, đắp, đắp cát, vận chuyển đất):**
- Nội dung: (1) Vận chuyển đất thừa 109,5 m³ tính 3 đoạn (≤ 1 km, 4 km tiếp theo, ngoài 5 km) nhưng hồ sơ không nêu vị trí, cự ly bãi đổ thải. (2) Không có công tác hút nước hố móng, mương cáp trong khi khu vực mực nước ngầm cao. (3) Không có ống thép băng đường như thuyết minh yêu cầu (TK-HTD-12). (4) Đào đất mương tính từ mặt hoàn thiện, chưa rõ đào trước hay sau san nền HM 03 (nếu sau san nền thì đất đào là cát san nền).
- Căn cứ: TT 36/2026/TT-BXD (hiệu lực 01/7/2026; đính chính QĐ 1538/QĐ-BXD, VBHN 89/2026/VBHN-TT-BXD); điều kiện thi công thực tế (miền Nam, mùa mưa, nước ngầm cao)
- Đề xuất: Bổ sung cự ly, vị trí đổ thải có xác nhận; biện pháp tiêu nước; thống nhất trình tự với HM 03 để xác định loại đất đào và khối lượng.

**Bảng các công tác có chênh lệch (đơn giá = VL + NC + M, chưa VAT, đ):**

| STT | Mã hiệu | Nội dung công tác | Đơn vị | KL đề nghị | KL thẩm tra | Đơn giá đề nghị | Đơn giá thẩm tra | Thành tiền đề nghị | Thành tiền thẩm tra | Tăng (+) / Giảm (−) | Ý kiến số |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 16 | BA.19102 | CCLĐ Cọc đồng tiếp đất L2400, D16 | cọc | 120,000 | 92,000 | 424.512 | 424.512 | 50.941.442 | 39.055.106 | -11.886.336 | DT-HTD-05 |
| 17 | BA.18302 | CCLĐ Mối hàn hóa nhiệt | mối | 120,000 | 92,000 | 305.858 | 305.858 | 36.702.936 | 28.138.918 | -8.564.018 | DT-HTD-05 |
| 26 | AF.81311 | GCLD ván khuôn | 100m2 | 2,706 | 2,492 | 13.324.080 | 13.324.080 | 36.054.960 | 33.203.607 | -2.851.353 | DT-HTD-07 |
| 27 | BA.14404 | CCLD Ống HPDE xoắn D40/30 | 100m → m | 1,424 | 142,400 | 87.353 | 87.353 | 124.391 | 12.439.055 | 12.314.664 | DT-HTD-04 |
| 47 | BA.23301 | CCLĐ Đèn trụ trang trí - Thân đèn Ø76, cao 3m5, Led 30W | bộ | 8,000 | 0,000 | 7.882.797 | 7.882.797 | 63.062.379 | 0 | -63.062.379 | DT-HTD-03 |
| 70 | BA.18302 | CCLĐ Core Switch 24 cổng SFP | bộ | 1,000 | 1,000 | 15.865.958 | 106.958 | 15.865.958 | 106.958 | -15.759.000 | DT-HTD-02 |
| 71 | BA.18302 | CCLĐ Switch L2 Pro 24 cổng PoE + 2 SFP + 2 Combo Ports | bộ | 1,000 | 1,000 | 12.999.758 | 106.958 | 12.999.758 | 106.958 | -12.892.800 | DT-HTD-02 |
| 72 | BA.18302 | CCLĐ Switch 24 cổng RJ45 | bộ | 1,000 | 1,000 | 1.830.758 | 106.958 | 1.830.758 | 106.958 | -1.723.800 | DT-HTD-02 |
| 74 | BA.18302 | CCLĐ Router | Cái | 1,000 | 1,000 | 16.824.758 | 106.958 | 16.824.758 | 106.958 | -16.717.800 | DT-HTD-02 |
| 77 | BA.18302 | CCLĐ Đầu ghi hình 32 kênh | Bộ | 1,000 | 1,000 | 22.036.958 | 106.958 | 22.036.958 | 106.958 | -21.930.000 | DT-HTD-02 |
| 78 | BA.18302 | CCLĐ Ổ cứng lưu trữ hình ảnh camera an ninh | Bộ | 1,000 | 1,000 | 14.682.758 | 106.958 | 14.682.758 | 106.958 | -14.575.800 | DT-HTD-02 |
| 79 | BA.18302 | CCLĐ Màn hình chuyên dụng cho CCTV 50 inch | Cái | 1,000 | 1,000 | 13.621.958 | 106.958 | 13.621.958 | 106.958 | -13.515.000 | DT-HTD-02 |
| 80 | BA.18302 | CCLĐ Wi-Fi 6 Access Point | bộ | 4,000 | 4,000 | 6.124.958 | 106.958 | 24.499.831 | 427.831 | -24.072.000 | DT-HTD-02 |
| 81 | BA.18302 | CCLĐ Camera IP Dome 2M | cái | 12,000 | 12,000 | 4.584.758 | 106.958 | 55.017.094 | 1.283.494 | -53.733.600 | DT-HTD-02 |
| 82 | BA.18302 | CCLĐ Camera IP Thân 2M | cái | 10,000 | 10,000 | 2.544.758 | 106.958 | 25.447.578 | 1.069.578 | -24.378.000 | DT-HTD-02 |
| 84 | BA.18302 | CCLĐ Bộ lưu điện - UPS 3KVA - Thời gian lưu 10 phút | Bộ | 1,000 | 1,000 | 16.375.958 | 106.958 | 16.375.958 | 106.958 | -16.269.000 | DT-HTD-02 |
| 87 | BA.17202 | CCLĐ Ổ cắm RJ45 - Data | cái | 390,000 | 52,000 | 59.351 | 59.351 | 23.147.083 | 3.086.278 | -20.060.805 | DT-HTD-06 |
| | | **Cộng chi phí trực tiếp T** | | | | | | **2.155.421.015** | **1.845.743.988** | **-309.677.027** | |

### VII.2. Tổng hợp giá trị theo khoản mục chi phí (HM 06, tạm tính)

| Khoản mục | Đề nghị | Thẩm tra | Tăng (+) / Giảm (−) |
|---|---|---|---|
| CHI PHÍ TRỰC TIẾP (T) | 2.155.421.015 | 1.845.743.988 | -309.677.027 |
| Chi phí chung C = T × 5,5% | 118.548.156 | 101.515.919 | -17.032.236 |
| Chi phí công việc không xác định được KL TT = T × 2% | 43.108.420 | 36.914.880 | -6.193.541 |
| Thu nhập chịu thuế tính trước TL = (T+C+TT) × 5,5% | 127.439.268 | 109.129.613 | -18.309.654 |
| Chi phí xây dựng trước thuế Gxdtt | 2.444.516.859 | 2.093.304.400 | -351.212.458 |
| Thuế GTGT = Gxdtt × 8% | 195.561.349 | 167.464.352 | -28.096.997 |
| Chi phí xây dựng sau thuế | 2.640.078.207 | 2.260.768.752 | -379.309.455 |
| Nhà tạm để ở và điều hành thi công = Gxdtt × 1,1% × (1+8%) | 29.040.860 | 24.868.456 | -4.172.404 |
| TỔNG CỘNG Gxd (làm tròn đồng) | 2.669.119.068 | 2.285.637.209 | -383.481.859 |

Ghi chú: giữ nguyên tỷ lệ và cách tính của hồ sơ (xem DT-HTD-13). Giá trị chuyển sang chi phí thiết bị (DT-HTD-02): 215.566.800 đ chưa VAT, 232.812.144 đ sau VAT. Nếu anh không chấp nhận DT-HTD-02, Gxd thẩm tra giảm khoảng 116,5 triệu đ thay vì 383,5 triệu đ. File `So sanh du toan HTD.xlsx` có công thức để anh tự kiểm tra lại.

## Điểm cần kiểm tra chéo (đã ghi vào phiếu thông tin dự án)

- **HM 01 – HM 06:** HM 06 đã gồm điện chiếu sáng, ổ cắm, quạt, điện nhẹ (wifi, camera) trong nhà hội quán (Đ-04, Đ-06; dự toán mục "khối nhà hội quán + phụ trợ") → trả lời TK-HQ-02 phần điện. Chưa có chiếu sáng sự cố, exit, PCCC, chống sét đánh thẳng cho nhà hội quán (TK-HTD-10, 11) – xác định thuộc HM 01 hay HM 06.
- **HM 02 – HM 06:** HM 06 cấp nguồn tủ DB.XLNT (4,5 kW, MCB 2P-32A, CXV 3Cx6 trong HDPE Ø40/30) và tủ DB.BSH bơm sinh hoạt (1,5 kW, 2P-16A, CXV 3Cx4); chiếu sáng nhà rác-XLNT có trong Đ-04. Tổng công suất thiết bị XLNT (TMĐT sheet HTXLNT) chỉ khoảng 1,43 kW; tủ điều khiển XLNT nằm trong chi phí thiết bị. Cần thống nhất công suất, vị trí tủ với HM 02 (TK-HTD-06).
- **HM 03 – HM 06:** Dự toán HM 06 chỉ có đào, đắp cát, gạch thẻ, đắp đất mương cáp, không có hoàn trả kết cấu sân đường → không trùng HM 03. Nhưng thiếu ống bảo vệ băng đường (thuyết minh yêu cầu ống thép), chưa quy định trình tự thi công mương cáp trước kết cấu sân đường (TK-HTD-12, DT-HTD-14).
- **HM 05 – HM 06:** 10 đèn LED cắm cỏ "1 đèn/cây bóng mát" – đối chiếu số cây bóng mát của HM 05; đèn trụ, móng trụ đặt trong khu cây xanh, sân lát.
- **HM 07 – HM 06:** Bơm tăng áp biến tần, tủ điều khiển bơm thuộc HM 07; HM 06 dành 1,5 kW – đối chiếu công suất bơm. Tuyến mương cáp giao cắt cống thoát nước HM 07.
- **TH (chi phí):** Thiết bị điện nhẹ 215,6 triệu đ đang nằm trong Gxd (DT-HTD-02); TKCS có khoản "thiết bị xây lắp" 247,6 triệu đ không còn trong TMĐT. Phần điện trong nhà dùng tỷ lệ chi phí HTKT (DT-HTD-13).

## Ghi chú trên bản vẽ CAD

Bản sao có đám mây và số ý kiến trên layer `TT_YKIEN` (màu 1): `01. DIEN-BVTC-CV-I22_TT-HTD.dwg` (cùng thư mục, định dạng AutoCAD 2018). 12 đám mây trong không gian mô hình: TK-HTD-03 (ghi chú Đ-03; trụ đèn bãi xe Đ-02), TK-HTD-04, 08 (chi tiết móng trụ), TK-HTD-05 (mạch L1 ÷ L5, bơm, XLNT trên Đ-03), TK-HTD-06 (thông số tủ DB.T), TK-HTD-07 (bãi tiếp địa Đ-01), TK-HTD-09 (sân thể thao), TK-HTD-10, 11 (Đ-04 nhà hội quán), TK-HTD-12 (chi tiết mương cáp Đ-01). TK-HTD-01, 02 và các ý kiến dự toán không có vị trí riêng trên bản vẽ.

## Nguồn tra cứu hiệu lực văn bản (28/10/2026)

- NĐ 206/2026/NĐ-CP, TT 36, 37, 38/2026/TT-BXD, Luật Xây dựng 135/2025/QH15, VAT 8%: dùng kết quả tra cứu của HM 02, HM 03 (ngày 27/10/2026) – xem `y-kien-NB.md`, `y-kien-SN.md`.
- QCVN 07:2023/BXD (gồm QCVN 07-7:2023/BXD công trình chiếu sáng), ban hành kèm TT 15/2023/TT-BXD, hiệu lực 01/7/2024, thay QCVN 07:2016/BXD; có Sửa đổi 1:2025 (TT 42/2025/TT-BXD): https://luatvietnam.vn/xay-dung/thong-tu-15-2023-tt-bxd-quy-chuan-quoc-gia-ve-he-thong-cong-trinh-ha-tang-ky-thuat-290124-d1.html ; https://thuvienphapluat.vn/TCVN/Xay-dung/QCVN-07-2023-BXD-SD1-2025-He-thong-cong-trinh-ha-tang-ky-thuat-922140.aspx
- QCVN 04-3:2026/BXD thay QCVN 09:2017/BXD, ban hành kèm TT 61/2026/TT-BXD, hiệu lực 01/02/2027 (cần kiểm tra lại văn bản gốc): https://moc.gov.vn/vn/tin-tuc/1196/96031/ban-hanh-quy-chuan-ky-thuat-quoc-gia-ve-cong-trinh-dan-dung--phan-3-cong-trinh-xay-dung-su-dung-nang-luong-hieu-qua.aspx ; https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/61-bxd.signed.pdf
- QCVN 12:2014/BXD (TT 20/2014/TT-BXD): không tìm thấy văn bản thay thế; Bộ Xây dựng có nhiệm vụ soát xét (QĐ 422/QĐ-BXD 2020) – **cần kiểm tra hiệu lực**: https://luatvietnam.vn/xay-dung/quy-chuan-viet-nam-qcvn-12-2014-bxd-bo-xay-dung-157297-d3.html ; https://dns1.moc.gov.vn/Images/editor/files/Congvan2020/Thang%204/BXD_422-Q%C4%90-BXD_27032020_signed.pdf
- TCVN 2737:2023 Tải trọng và tác động, thay TCVN 2737:1995: https://thuvienphapluat.vn/TCVN/Xay-dung/TCVN-2737-2023-Tai-trong-va-tac-dong-920293.aspx
- TCVN 9385:2012 chống sét: không tìm thấy văn bản thay thế – **cần kiểm tra hiệu lực**: https://thuvienphapluat.vn/TCVN/Xay-dung/TCVN-9385-2012-chong-set-cho-cong-trinh-xay-dung-Huong-dan-thiet-ke-907546.aspx
- 11 TCN 18-84: bộ quy phạm trang bị điện đã có bản 11 TCN 18÷21-2006; chưa tra được văn bản bãi bỏ chính thức: https://thuvienphapluat.vn/TCVN/Dien-dien-tu/11TCN-20-2006-Quy-pham-trang-bi-dien-Phan-III-Trang-bi-phan-phoi-Tram-bien-ap-908741.aspx
- TCVN 13608:2023, TCVN 7447 (các phần), TCVN 9207:2012, TCVN 9358:2012, TCVN 7997:2009, TCVN 9362:2012, QCVN 06:2022/BXD: chưa tra được toàn văn hoặc tình trạng, đã ghi "cần kiểm tra hiệu lực" tại từng ý kiến.

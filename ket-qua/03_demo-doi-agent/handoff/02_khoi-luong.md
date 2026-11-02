# 02 Bóc khối lượng: Hệ thống thoát nước (giếng thu và cống dọc), khu Nhị Bình

## 1. Việc được giao
- Bóc khối lượng sơ bộ hạng mục "Hệ thống thoát nước: giếng thu và cống dọc" từ DXF, theo skill gn-dutoan. Không bóc hạng mục khác.
- Xuất Excel `KL-thoat-nuoc-demo.xlsx` (7 cột theo gn-dutoan) và bàn giao md này.
- TRẠNG THÁI: phần đếm giếng thu đã làm xong và kiểm chứng. File Excel CHƯA tạo được (xem mục 5, điểm 1).

## 2. Đầu vào đã đọc
- `F:\demo\Acad_BD_TD_TN Nhi Binh 5.dxf` (chỉ đọc, không sửa, không ghi đè).
- Cách đọc: máy của agent này không có shell nên không chạy được ezdxf. Đã đọc thẳng nội dung text của DXF bằng công cụ Grep và Read (mã nhóm DXF), nên con số đếm là kết quả đọc trực tiếp, không phải ước lượng.
- `.claude/skills/gn-dutoan/SKILL.md`, `mau-ha-tang-ky-thuat.md` (cột Excel, quy tắc).
- `ket-qua/03_demo-doi-agent/handoff/00_ke-hoach.md`.
- Script chuẩn bị sẵn, chưa chạy: `C:\Users\Desktop\AppData\Local\Temp\claude\D--SOFTWARE-15--AI-15-4-Claude-15-4-1-Lop-hoc-Cesslobal-02--AI-Xay-Dung-AI-Cad-K1\b9120200-7e83-40f6-9fdd-34e7a44e731f\scratchpad\boc_thoat_nuoc_demo.py` (nằm ngoài dự án).

## 3. Kết quả

### 3.1 Giếng thu
| STT | Mã hiệu định mức | Tên công việc | ĐVT | Diễn giải | Khối lượng | Nguồn |
|---|---|---|---|---|---|---|
| 1 | [Chờ bổ sung] | Giếng thu nước mặt | cái | Đếm INSERT block `KHGMBGiengThu` trong `*Model_Space` | 30,00 | DXF, ModelSpace, layer `TP121_TDTNuoc_matbang_quay` |
| 2 | [Chờ bổ sung] | Đào, đắp, BT, xây, nắp, lưới chắn rác giếng thu | cái | Cần bản vẽ chi tiết giếng thu | [Chờ bổ sung] | chưa có kích thước kết cấu |

Kiểm chứng số 30 (ba cách độc lập, đều ra 30):
- Đếm trực tiếp: 30 INSERT `KHGMBGiengThu`, cả 30 có chủ sở hữu (mã 330) là `1F`, tra ra đúng là `*Model_Space`. Tổng 33 lần xuất hiện tên block = 30 INSERT + 1 BLOCK_RECORD + 2 dòng BLOCK; không có INSERT lồng trong block khác. Cả 30 đều có ATTRIB đi kèm (cờ 66=1).
- Đối chiếu bảng trong bản vẽ: "Bảng tọa độ giếng thu Timcong_Trai-TuyenNhiBinh5_Thoatnuoc_5" (block `*T93`) có đúng 30 dòng HG01 đến HG30 (hàng cuối cách đều bước 4, đã đối chiếu thêm danh sách HG01..HG30 xuất hiện liên tục). Bảng "Bảng Thống Kê Hố Ga" (`*T81`, `*T94`) cũng liệt kê HG01 đến HG30.
- Các block liên quan cùng số lượng: `10.KHGiengThu1_and12` 30, `10.KHGiengThu1phu_and` 30, `DeMatCatGiengThu` 30. Riêng `MatCatGiengThu` đếm được 29 (lệch 1, xem mục 5).
- Số đếm của điều phối (khoảng 30) KHỚP với số của tôi (30).

### 3.2 Cống dọc
| STT | Mã hiệu định mức | Tên công việc | ĐVT | Khối lượng | Ghi chú |
|---|---|---|---|---|---|
| 3 | [Chờ bổ sung] | Cống dọc (chiều dài tim, đường kính, loại ống) | m | [Chờ bổ sung] | Không bóc được từ DXF |
| 4 | [Chờ bổ sung] | Đào đắp phui cống, đệm móng, mối nối, hố ga thăm | - | [Chờ bổ sung] | Phụ thuộc loại, độ sâu cống |

Kiểm chứng "layer cống trống":
- `TP15_BD_MB_Cong`, `TP16_BD_Timcong`: chỉ có trong bảng layer, không một đối tượng nào mang layer này trong toàn file.
- `51.TP_duong tim cong`, `52...bao ngoai cong`, `53...bao trong cong`: mỗi layer chỉ có 1 LWPOLYLINE + 2 MTEXT, đều nằm trong một block (chủ sở hữu `DD5E52`, không phải ModelSpace), nội dung là bảng chú thích ("Tp_tim cong", "Tp_duong bao ngoai cong"...). Không phải hình cống thật. Vì vậy ModelSpace không có chiều dài cống.
- Toàn file có 1.212 dòng chứa chuỗi `ACAD_PROXY_ENTITY` (gồm cả dòng khai báo CLASS). Chưa phân loại theo layer, nên chưa khẳng định proxy nào là cống.
- Không bịa chiều dài, đường kính, kết cấu cống.

Nguồn thay thế để bóc cống:
- Bảng thống kê cống (chưa thấy trong DXF).
- Trắc dọc thoát nước.
- Xuất từ phần mềm chuyên dụng đã tạo proxy (xuất lại ra DWG/DXF explode hoặc xuất bảng).

### 3.3 Nhận xét về đơn giá
- Mã hiệu định mức, hao hụt, đơn giá, thành tiền: [Chờ bổ sung]. Đơn giá theo công bố giá TP.HCM đúng kỳ, định mức đang dùng TT 38/2026 (nhắc kiểm tra văn bản còn hiệu lực).

## 4. Giả định đã dùng
- Mỗi INSERT `KHGMBGiengThu` = 1 giếng thu (giả định của điều phối, khớp với bảng HG01 đến HG30).
- Đếm trong ModelSpace, không tính block lồng hay PaperSpace.
- Chưa dùng đơn vị bản vẽ cho phép tính nào (chỉ đếm cái), nên chưa phụ thuộc INSUNITS.

## 5. Chỗ chưa chắc (Cần xác nhận lại)
1. File `KL-thoat-nuoc-demo.xlsx` CHƯA được tạo: môi trường agent này không có shell (không chạy được Python/ezdxf/openpyxl, Write không ghi được file nhị phân .xlsx). Cần chạy lệnh ở mục 6. Phải chạy script mới coi là có bảng Excel.
2. Vị trí 30 block: tất cả có cùng Y = 1206630.195, nằm thẳng hàng, layer `TP121_TDTNuoc_matbang_quay` (có chữ "TD" và "matbang_quay", có vẻ là dải mặt bằng nằm trong tờ trắc dọc thoát nước). Cần xác nhận đây có phải ký hiệu mặt bằng mà anh muốn đếm, hay còn ký hiệu giếng thu khác trên mặt bằng tuyến. Hai cách cùng ra 30 nên khả năng cao là đúng.
3. Tọa độ X của 30 block có dấu lẫn lộn: 23 giá trị âm (khoảng -599668 đến -600339), 7 giá trị dương (khoảng 600122 đến 600486), trong khi khoảng cách giữa các block rất đều (khoảng 25 đến 30). Giống lỗi dấu khi xuất file. Không ảnh hưởng số đếm nhưng cần soi lại nếu dùng vị trí.
4. `MatCatGiengThu` đếm 29, các block cùng họ đều 30. Có thể thiếu một mặt cắt hoặc một INSERT thuộc dạng khác. Chưa kiểm tra INSERT này nằm ModelSpace hay block lồng.
5. Loại giếng thu (hàm ếch, thu đơn, thu kép), kết cấu, kích thước: Tài liệu không đề cập trong phần đã đọc (chưa mở nội dung block `MatCatGiengThu`, `DeMatCatGiengThu`). Ghi [Chờ bổ sung].
6. Bảng liệt kê dùng chữ "Hố Ga" (HG01 đến HG30): cần xác nhận 30 vị trí này đều là giếng thu, không lẫn hố ga thăm.
7. Cống dọc: không có chiều dài, đường kính, loại ống, độ dốc. Tôi không tự tính chiều dài từ khoảng cách các hố ga trong bảng tọa độ vì chưa biết thứ tự nối tuyến và đường kính. Chỉ ghi là hướng tham khảo: bảng tọa độ và cao độ đỉnh, đáy HG01 đến HG30 đã có sẵn trong bản vẽ.

## 6. Việc người sau cần làm
- Chạy script ở mục 2 để tạo Excel (chỉ đọc DXF, từ chối ghi đè nếu file đích đã có):
  `python -I "<đường dẫn script>" "F:\demo\Acad_BD_TD_TN Nhi Binh 5.dxf" "D:\SOFTWARE\15. AI\15.4 Claude\15.4.1 Lop hoc Cesslobal\02. AI_Xay Dung\AI_Cad_K1\ket-qua\03_demo-doi-agent\KL-thoat-nuoc-demo.xlsx"`
  Script chưa được chạy thử, có thể có lỗi nhỏ. Sau khi chạy: so con số đếm in ra màn hình (kỳ vọng 30, layer cống trong ModelSpace = 0) với bảng này. Nếu khác, tin kết quả script và báo lại.
- Agent kiểm tra số học: kiểm tra ô F7 của Excel là công thức COUNTA đúng vùng, và sheet "Giếng thu" có 30 dòng.
- Người dùng cung cấp bảng thống kê cống hoặc trắc dọc thoát nước (hoặc xuất từ phần mềm chuyên dụng) để bóc cống.
- Người dùng cung cấp bản vẽ chi tiết giếng thu (kết cấu, kích thước) để bóc đào, đắp, bê tông, xây.
- Gán mã hiệu định mức TT 38/2026 và đơn giá TP.HCM theo công bố giá đúng kỳ trên F1 (anh duyệt một bảng).

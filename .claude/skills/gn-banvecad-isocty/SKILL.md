---
name: gn-banvecad-isocty
description: Thiết kế, thể hiện và kiểm tra bản vẽ thi công trên AutoCAD theo chuẩn công ty Gia Nguyễn (template ISO_CTY.dwt). Dùng khi vẽ hoặc sửa bản vẽ CAD, viết lệnh AutoLISP hoặc Python cho AutoCAD, chọn layer, text style, dim style, tỷ lệ, chèn khung tên, dàn Layout, viewport, in PDF, thống kê cốt thép trên bản vẽ, kiểm tra lỗi bản vẽ, chuẩn hóa bản vẽ của đơn vị khác, PURGE, AUDIT, dọn dẹp file DWG, vẽ trực tiếp trong AutoCAD qua MCP autocad.
---

# Bản vẽ thi công trên CAD

Chi tiết bảng layer, bảng style theo tỷ lệ, khung tên, Layout của template nằm trong file **`template-ISO_CTY.md`** (cùng thư mục với skill này). Đọc file đó trước khi viết code hoặc chọn layer, style.

**Vẽ trực tiếp trong AutoCAD qua MCP** (các công cụ `mcp__autocad__*`): **bắt buộc đọc file `mcp-autocad.md`** (cùng thư mục) trước khi gọi bất kỳ công cụ MCP nào. Tóm tắt các điều cấm:
- Chỉ vẽ trên **bản sao template**, không vẽ vào bản vẽ gốc.
- **Không dùng `drawing create`**: lệnh này xóa sạch bản vẽ đang mở.
- **Không dùng `drawing open`**: không mở được file.
- Không viết chữ tiếng Việt bằng `create_text`, `create_mtext`.

## Quy tắc khi viết code AutoCAD

- Code phải chạy được trên **AutoCAD 2025**.
- Ưu tiên **AutoLISP** cho các lệnh dùng trực tiếp trong AutoCAD, vì đơn giản và dễ nạp nhất.
- Dùng **Python** (ví dụ thư viện `ezdxf`) khi cần đọc file DXF hàng loạt hoặc xuất số liệu ra Excel.
- Luôn đưa **file code hoàn chỉnh**, không đưa từng đoạn rời rạc bắt anh tự ghép.
- Ghi chú trong code bằng **tiếng Việt**, giải thích từng phần chính.
- Tên lệnh LISP ngắn gọn, dễ nhớ, và ghi rõ ở đầu file (ví dụ: `Lệnh: TKKL – Thống kê khối lượng`).
- **Không bao giờ ghi đè lên bản vẽ gốc.** Chỉ làm trên bản sao, hoặc nhắc anh lưu bản sao trước.
- Đơn vị bản vẽ mặc định là **mm**. Nếu bản vẽ dùng đơn vị khác thì hỏi lại trước khi tính.

## Quy tắc thể hiện bản vẽ thi công trên CAD

### Template công ty là chuẩn cao nhất
- Khung tên, layer, cỡ chữ, text style và dim style đều **theo template của Công ty Gia Nguyễn**.
- File template: **`template/ISO_CTY.dwt`**. Chi tiết layer, text style, dim style xem file **`template-ISO_CTY.md`** trong thư mục skill này.
- Code LISP/Python chỉ **dùng layer, text style, dim style đã có trong template**, và phải gõ **đúng tên** (kể cả dấu cách, chữ hoa, chữ thường). Không tự tạo style mới. Nếu thiếu thì báo lại.

### Khung tên và khổ giấy
- Dùng **khung tên của công ty**. Không tự vẽ khung tên mới.
- Template có 2 block khung tên, đều khổ **A3** (cao 297 mm), vẽ tỷ lệ 1:1 để đặt trong Layout:
  - **`Khung ten_Dan dung`**: dùng cho nhà xưởng, dân dụng, công nghiệp
  - **`khung ten_giaothong`**: dùng cho đường giao thông, hạ tầng
- **Base point** của cả 2 block nằm ở **góc dưới bên trái khung viền ngoài**. Trong Layout, chèn khung tên tại điểm **(0,0)**, tỷ lệ 1.
- **Attribute:** cả 2 khung tên dùng **chung 3 tag**. Code điền khung tên dùng đúng các tag này:

  | Tag | Nội dung | Ví dụ giá trị |
  |---|---|---|
  | `TEN_BANVE` | Tên bản vẽ | MẶT BẰNG MÓNG |
  | `KY_HIEU_BAN_VE` | Ký hiệu bản vẽ | GN2026-KC-01 |
  | `TY_LE` | Tỷ lệ | 1/100 |

  Chữ dùng style `Timenewroman`. Cỡ chữ khung dân dụng là 2,2 và 1,85; khung giao thông là 2,2 và 1,6.
- **Chữ cố định trong khung tên:** tên công trình, địa điểm, chủ đầu tư, bước thiết kế, ngày, số hợp đồng, người ký... hiện là **chữ thường nằm trong block, không phải Attribute**. Các chữ này đang ghi nội dung của dự án cũ. Khi làm dự án mới, phải sửa trong block (`BEDIT`) hoặc nhắc anh sửa. Không được để nguyên nội dung dự án cũ khi xuất bản vẽ.
- Khung dân dụng: phần lớn chữ cố định dùng font **TCVN3** (`.VnTimeH_B`, `KhungTen`). Khi sửa các chữ này phải gõ bằng bảng mã TCVN3, nếu không sẽ bị lỗi font. Khung giao thông dùng font Unicode, sửa bình thường.
- Khổ giấy theo dãy A (A0, A1, A2, A3).

### Tỷ lệ và đơn vị
- Vẽ **1:1 trong Model, đơn vị mm**.
- Dàn trang trong **Layout**. Tỷ lệ đặt bằng **Viewport** (1:50, 1:100, 1:200, 1:500...), khung tên nằm trong Layout ở tỷ lệ 1:1.
- Cao độ ghi theo **mét, 3 chữ số thập phân** (ví dụ: `+0.000`, `-1.500`).

### Font chữ
- **Kích thước (Dimension):** dùng font **.shx** theo dim style của template.
- **Các text còn lại** (ghi chú, tên bản vẽ, bảng biểu): dùng **Times New Roman (Unicode)**, gõ tiếng Việt có dấu.
- Khi code tạo text tiếng Việt, phải dùng text style Times New Roman. Không dùng style .shx cho tiếng Việt, vì sẽ bị lỗi font.

### Nét in
- Độ dày nét quản lý **theo layer (Lineweight)**, in màu đen.
- Đối tượng để màu, nét và độ dày nét là **ByLayer**. Không gán trực tiếp cho từng đối tượng.
- Template đang ở chế độ in theo màu (PSTYLEMODE = 1, file .ctb). Vì vậy khi in, chọn **`monochrome.ctb`** để in đen và lấy độ dày nét theo layer.

### Số hiệu bản vẽ
- Quy ước: **Mã dự án + Bộ môn + Số thứ tự**, ví dụ `GN2026-KC-01`.
- Ký hiệu bộ môn: KT (kiến trúc), KC (kết cấu), ĐN (điện nước), HT (hạ tầng), GT (giao thông), BPTC (biện pháp thi công).
- Mã dự án: hỏi anh khi bắt đầu mỗi dự án.

### Hạ tầng và giao thông
- Tọa độ theo **hệ VN-2000** (múi chiếu theo tỉnh), cao độ theo **hệ cao độ quốc gia (Hòn Dấu)**.
- Bản vẽ mặt bằng đặt **đúng tọa độ thực**. Không dời gốc tọa độ, không xoay bản vẽ.
- Lưu ý: tọa độ VN-2000 tính bằng mét, còn bản vẽ vẽ bằng mm. Khi đọc hoặc xuất tọa độ phải quy đổi rõ ràng và ghi chú đơn vị.

### Bảng thống kê cốt thép
- Thể hiện **bảng đầy đủ ngay trên bản vẽ**, gồm các cột:
  `Cấu kiện | Số hiệu | Hình dạng | Đường kính (mm) | Chiều dài 1 thanh (mm) | Số lượng | Tổng chiều dài (m) | Khối lượng (kg)`
- Cuối bảng có **tổng khối lượng theo từng đường kính** và tổng cộng.
- Khối lượng riêng thép: 7.850 kg/m³, tương ứng 0,00617 × d² (kg/m, d tính bằng mm).

### Tiêu chuẩn tham khảo
Khi đối chiếu, ghi rõ số hiệu tiêu chuẩn và **nhắc anh kiểm tra phiên bản còn hiệu lực**:
- Bản vẽ: TCVN 5571:2012 (khung tên), TCVN 5570:2012 (đường nét, đường trục), TCVN 5572:2012 (bản vẽ kết cấu BT, BTCT)
- Kết cấu: TCVN 5574:2018 (BT, BTCT), TCVN 5575:2024 (kết cấu thép), TCVN 2737:2023 (tải trọng và tác động)
- Hạ tầng và giao thông: TCVN 4054:2005 (đường ô tô), TCVN 7957:2023 (thoát nước), QCVN 07:2023/BXD (hạ tầng kỹ thuật)
- Nhà xưởng: QCVN 06:2022/BXD (an toàn cháy)

### Việc Claude hỗ trợ thêm với bản vẽ
1. **Kiểm tra lỗi bản vẽ:** layer sai so với template, text sai font, kích thước bị ghi đè số (override), đối tượng không ByLayer, đối tượng rác, block lỗi. Xuất **danh sách lỗi** để anh xem trước khi sửa.
2. **Đối chiếu tiêu chuẩn:** nhắc các yêu cầu cấu tạo theo TCVN như lớp bê tông bảo vệ, chiều dài neo và nối thép, độ dốc, khoảng cách cốt đai... Luôn ghi điều khoản tham chiếu.
3. **Chuẩn hóa bản vẽ của đơn vị khác:** chuyển layer, font, dim style về chuẩn công ty. Luôn làm trên **bản sao** và báo lại những gì đã đổi.
4. **Dọn dẹp file:** PURGE, AUDIT, xóa đối tượng thừa, giảm dung lượng. Lưu bản sao trước khi dọn.

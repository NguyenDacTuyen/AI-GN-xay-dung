# Vẽ trực tiếp trong AutoCAD qua MCP (tài liệu tra cứu của skill gn-banvecad-isocty)

Cách dùng máy chủ MCP `autocad` để vẽ và sửa bản vẽ theo chuẩn template ISO_CTY.dwt. Mọi điều dưới đây đã được **chạy thử thật** ngày 19/10/2026 trên AutoCAD 2025 với bản sao template (`ket-qua/_thu-mcp/thu-mcp.dwg`).

## Thông tin cài đặt
- Mã nguồn MCP: `C:\Users\Desktop\mcp\vn-autocad-claude` (repo andyluu98/vn-autocad-claude, bản 3.2). Khai báo trong `.mcp.json` của dự án, tên máy chủ `autocad`.
- Thư mục trao đổi lệnh giữa Claude và AutoCAD: `C:\temp`.
- AutoCAD phải **đang mở** và đã nạp `mcp_dispatch.lsp`. Anh đã cho nạp tự động qua Startup Suite, nên bản vẽ nào mở ra cũng tự có.
- Có 8 nhóm công cụ: `system`, `drawing`, `entity`, `layer`, `block`, `annotation`, `view`, `pid`. Không dùng nhóm `pid` (dành cho sơ đồ công nghệ P&ID).

## Khi nào dùng MCP, khi nào viết file LISP
| Dùng MCP (em vẽ trực tiếp) | Viết file `.lsp` cho anh chạy |
|---|---|
| Vẽ, sửa, kiểm tra một bản vẽ cụ thể ngay bây giờ | Lệnh anh muốn dùng lại nhiều lần, ở nhiều bản vẽ |
| Đọc thông tin bản vẽ: layer, đối tượng, khung tên | Khi AutoCAD không bật MCP, hoặc anh làm ở máy khác |

## Quy tắc bắt buộc
1. **Luôn làm trên bản sao template, không vẽ vào bản vẽ gốc.** Bản vẽ mới thì chép `template/ISO_CTY.dwt` thành file `.dwg` mới. Sửa bản vẽ có sẵn thì chép ra bản sao trước. Bản sao để trong `ket-qua/<tên dự án>/`.
2. **Đường dẫn và tên file không dấu tiếng Việt.** Công cụ đọc sai đường dẫn có dấu (ví dụ `Tài liệu`).
3. **Không đụng vào bản vẽ anh đang mở** khi anh chưa đồng ý. Trước khi làm, kiểm tra `DWGNAME` để chắc đang ở đúng bản sao.
4. **Cấm dùng `drawing` → `create`.** Lệnh này **xóa sạch toàn bộ đối tượng** của bản vẽ đang mở rồi purge, không phải tạo bản vẽ mới.
5. **Không dùng `drawing` → `open`.** Lệnh báo thành công nhưng **không mở được file** (AutoCAD đang ở chế độ nhiều bản vẽ). Mở file bằng `execute_lisp` theo mẫu ở Bước 2 bên dưới.
6. **Hạn chế `view` → `get_screenshot`** (và `include_screenshot`). Ảnh trả về rất nặng, tốn nhiều bộ nhớ làm việc. Kiểm tra kết quả bằng `entity` → `list`, `count`, `get` thay vì chụp màn hình. Chỉ chụp khi anh yêu cầu.
7. **Không viết chữ tiếng Việt bằng `annotation` → `create_text` hoặc `entity` → `create_mtext`.** Hai lệnh này tự tạo text style mới `MCP_VN` (font Arial), sai chuẩn template. Dùng `entmake` qua `execute_lisp` (Bước 4).
8. **Tham số `layer` phải đúng tuyệt đối tên layer của template.** Gõ sai tên, công cụ sẽ **tự tạo layer mới màu trắng** mà không báo. Chép tên từ `template-ISO_CTY.md`.
9. Trong lúc em đang gửi lệnh, nhắc anh **không gõ lệnh khác trong AutoCAD**.

## Quy trình vẽ một bản vẽ mới

**Bước 1: Kiểm tra kết nối.** Gọi `system` → `status`. Kết quả phải là `backend: file_ipc`. Nếu là `ezdxf` thì AutoCAD chưa mở hoặc chưa nạp `mcp_dispatch.lsp`, báo anh.

**Bước 2: Chép template rồi mở bản sao.**
- Chép file bằng lệnh shell, ví dụ `Copy-Item "template\ISO_CTY.dwt" "ket-qua\<du-an>\<ten-ban-ve>.dwg"`.
- Mở bằng `system` → `execute_lisp` (đường dẫn dùng dấu `/`):
  ```lisp
  (vl-load-com)
  (setq d (vla-open (vla-get-documents (vlax-get-acad-object)) "D:/.../ket-qua/<du-an>/<ten-ban-ve>.dwg" :vlax-false))
  (vla-activate d)
  (vla-get-name d)
  ```
- Kiểm tra lại bằng `drawing` → `get_variables` với `DWGNAME`, `CLAYER`, `TEXTSTYLE`, `DIMSTYLE`.

**Bước 3: Vẽ hình.** Dùng `entity` → `create_line`, `create_polyline`, `create_rectangle`, `create_circle`, `create_arc`, luôn kèm tham số `layer` đúng tên. Ví dụ thép chủ: `layer: "10.TP_Thep chu"`. Đối tượng tạo ra để màu ByLayer (đã kiểm tra). Vẽ nhiều đối tượng một lúc thì dùng `system` → `batch` cho nhanh.

**Bước 4: Viết chữ (có dấu tiếng Việt).** Dùng `execute_lisp` với `entmake`, chỉ định layer, text style theo tỷ lệ và chiều cao trong Model:
  ```lisp
  (entmake (list '(0 . "TEXT") '(8 . "6.TP_Tex tNote") '(7 . "02.TP_1-100 Note")
                 '(10 1000.0 2000.0 0.0) '(40 . 250.0) '(1 . "Ghi chú thép chủ")))
  ```
  Chữ tiếng Việt viết thẳng trong chuỗi đều hiển thị đúng Unicode (đã kiểm tra). Chọn style và chiều cao theo bảng tỷ lệ trong `template-ISO_CTY.md`. Ví dụ 1:100: ghi chú `02.TP_1-100 Note` cao 250, tiêu đề `01.TP_1-100 Title` cao 350, layer tiêu đề `8.TP_Text Title`.

**Bước 5: Ghi kích thước.** Đặt dim style và layer trước, rồi mới ghi:
  ```lisp
  (command "_.-DIMSTYLE" "_R" "01.TP_1-100")
  (setvar "CLAYER" "1.Tp_dim")
  ```
  Sau đó gọi `annotation` → `create_dimension_linear` (hoặc `aligned`, `angular`, `radius`). Đã kiểm tra: kích thước nhận đúng dim style `01.TP_1-100` và layer `1.Tp_dim`.

**Bước 6: Điền khung tên trong Layout.**
- Tìm khung tên bằng `execute_lisp`:
  ```lisp
  (setq ss (ssget "_X" '((0 . "INSERT") (2 . "Khung ten_Dan dung") (410 . "A3_DanDung"))))
  (if ss (cdr (assoc 5 (entget (ssname ss 0)))) "khong tim thay")
  ```
  Bản giao thông thì đổi thành `khung ten_giaothong` và `A3_GiaoThong`.
- Điền bằng `block` → `update_attribute` với các tag `TEN_BANVE`, `KY_HIEU_BAN_VE`, `TY_LE`. Chữ có dấu hiển thị đúng (đã kiểm tra).
- Đặt tỷ lệ viewport theo tỷ lệ bản vẽ và khóa viewport (xem `template-ISO_CTY.md`, mục Layout).

**Bước 7: Kiểm tra và lưu.**
- Kiểm tra bằng `entity` → `list` / `count` theo layer, hoặc `execute_lisp` đọc thuộc tính đối tượng.
- Lưu bằng `drawing` → `save` (không truyền `path`, lưu đè lên chính bản sao). Muốn xuất PDF thì dùng `drawing` → `plot_pdf`.
- Báo anh đường dẫn file và danh sách những gì đã vẽ.

## Lỗi thường gặp và cách xử lý
| Hiện tượng | Nguyên nhân | Cách xử lý |
|---|---|---|
| `execute_lisp` báo **Timeout** | Đoạn LISP bị lỗi, hoặc kết quả trả về có dấu ngoặc kép hay chữ có dấu | Viết LISP đơn giản, kết quả trả về chỉ gồm chữ không dấu ghép bằng `strcat`. Muốn kiểm tra chữ có dấu thì trả về mã ký tự (`ascii`), không trả chuỗi |
| `block` → `get_attributes` báo Timeout | Giá trị Attribute có chữ tiếng Việt | Đọc bằng `execute_lisp`, trả về độ dài và mã ký tự |
| Xuất hiện layer lạ màu trắng | Gõ sai tên layer ở tham số `layer` | Xóa đối tượng vẽ sai, purge layer lạ, vẽ lại với tên đúng |
| Xuất hiện text style `MCP_VN` | Đã dùng `create_text` / `create_mtext` với chữ có dấu | Chuyển các chữ đó sang style đúng của template, rồi purge `MCP_VN` |
| `status` trả về `ezdxf` | AutoCAD chưa mở, chưa mở bản vẽ, hoặc chưa nạp `mcp_dispatch.lsp` | Nhờ anh mở AutoCAD và mở một bản vẽ, kiểm tra Startup Suite |

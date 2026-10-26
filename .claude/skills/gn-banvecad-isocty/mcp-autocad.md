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
1. **Luôn làm trên bản sao template, không vẽ vào bản vẽ gốc.** Bản vẽ mới thì chép `template/ban-ve/ISO_CTY.dwt` thành file `.dwg` mới. Sửa bản vẽ có sẵn thì chép ra bản sao trước. Bản sao để trong `ket-qua/<tên dự án>/`.
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
- Chép file bằng lệnh shell, ví dụ `Copy-Item "templatean-ve\ISO_CTY.dwt" "ket-qua\<du-an>\<ten-ban-ve>.dwg"`.
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
| `drawing` → `plot_pdf` báo thành công nhưng **không có file PDF** | Hạn chế của công cụ MCP | In bằng lệnh `-PLOT` theo cài đặt in sẵn của Layout (xem mục "Bài học khi vẽ bể tự hoại") |
| Công cụ MCP **treo đến 30 phút** khi in PDF | File PDF cùng tên đã tồn tại hoặc đang mở trong trình xem PDF, AutoCAD dừng chờ hỏi ghi đè | Nhờ anh bấm **Esc** trong AutoCAD. Lần sau: xóa PDF cũ trước khi in; nếu không xóa được (đang mở) thì in ra tên mới |

## Multileader bằng code (đã chạy thử 20/10/2026, trang thử `ket-qua/_mau-iso/thu-mau.dwg`)
Bản vẽ phải có sẵn kiểu Multileader và block mẫu (xem SKILL.md, quy tắc 7; nếu chưa có thì `(load ".../lisp/gn-mau-iso.lsp") (c:GNMAU)`).
```lisp
;; ms = Model space; ax ay = điểm mũi tên; lx ly = điểm gãy
(setq ml (vlax-invoke ms 'AddMLeader (mapcar 'float (list ax ay 0 lx ly 0)) 0))
(vla-put-Layer ml "42.Tp_M learder")
(vla-put-StyleName ml "TP_1-50 GhiChu")
(vla-put-TextString ml "BT L\U+00D3T B7,5 D\U+00C0Y 100")      ; xuống dòng: \\P
;; Số hiệu thép: thêm
(vla-put-ContentType ml 1)
(vla-put-ContentBlockName ml "GN_SoHieuThep")                ; hoặc GN_SoHieuThep_T (vòng tròn bên trái)
(vla-SetDoglegDirection ml 0 (vlax-3d-point -1.0 0.0 0.0))   ; chỉ với block; hướng sang trái
(vla-SetBlockAttributeValue ml <ObjectID của ATTDEF SO_HIEU trong block> "1")
(vla-SetBlockAttributeValue ml <ObjectID của ATTDEF THEP> "2%%c14")
;; Cuối cùng: dời cả ghi chú để điểm gãy về đúng (lx ly), rồi đặt lại đường dẫn
(setq v (vlax-invoke ml 'GetLeaderLineVertices 0))
(vla-Move ml (vlax-3d-point (nth 3 v) (nth 4 v) 0.0) (vlax-3d-point lx ly 0.0))
(vlax-invoke ml 'SetLeaderLineVertices 0 (mapcar 'float (list ax ay 0 lx ly 0)))
```
Lỗi đã gặp:
- Tọa độ truyền cho `AddMLeader`, `InsertBlock` phải là **số thực**. Số nguyên (ví dụ `(* 50 -5)`) báo `Exception occurred` hoặc `Invalid input`.
- `SetDoglegDirection` **báo lỗi với ghi chú chữ**. Ghi chú chữ tự chọn hướng theo vị trí điểm gãy, không cần gọi.
- Đổi hướng đường ngang làm **cả ghi chú dịch đi** một đoạn. Phải dời lại như 3 dòng cuối ở trên.
- `entmake` không có mã 410 thì vẽ vào **không gian đang mở** (Layout nếu CTAB là Layout). Đặt `(setvar "CTAB" "Model")` trước khi vẽ vào Model.
- Kiểu Multileader: kiểu chữ nằm trên đường ngang là `TextLeftAttachmentType` = `TextRightAttachmentType` = **7** (gạch chân dòng cuối). Giá trị 5 và 6 không gạch chân. Không gán được `ArrowSymbol ""` (báo `Key not found`), nhưng kiểu mới tạo mặc định đã là mũi tên đặc.
- ObjectID của ATTDEF: duyệt block bằng `vlax-for`, lọc `AcDbAttributeDefinition` theo `TagString`, rồi `vla-get-ObjectID`.

## Bài học khi vẽ bể tự hoại GN2026-HT-01 (20/10/2026)
1. **Bản vẽ nhiều đối tượng thì không gọi MCP từng đối tượng.** Viết chương trình Python chứa toàn bộ thông số, sinh ra file `.lsp` (các hàm `L`, `PL`, `CI`, `TX`, `HT`, `DM`...). Sau đó nạp bằng `execute_lisp` với `(load "D:/.../lisp/<ten>.lsp")` và gọi **từng phần** (mỗi lần gọi phải xong trong khoảng 10 giây). Cùng chương trình Python ghi ra file số liệu khối lượng cho dự toán. Mẫu tham khảo: `python/be_tu_hoai_10m3.py`.
2. **Chữ tiếng Việt trong file `.lsp`:** đổi ký tự có dấu sang mã `\\U+XXXX` trong chuỗi LISP. Đã chạy đúng.
3. **Hatch:** đặt `HPNAME`, `HPSCALE`, `HPANG` rồi `(command "_.-HATCH" "_S" <tập đối tượng> "" "")`. Tỷ lệ dùng cho bản vẽ 1/50 đơn vị mm: AR-CONC 0,4–0,6; AR-SAND 0,6; GRAVEL 0,6.
4. **Model của template có sẵn 6 đối tượng mẫu:** 2 khung tên thu nhỏ và các chữ "A3", "(dùng cho bản vẽ...)". Chúng nằm quanh tọa độ (3700–4550, 6500–7000) và sẽ chồng lên hình vẽ. **Xóa chúng trong bản sao** trước khi vẽ.
5. **Đặt tỷ lệ viewport:** sửa trực tiếp dữ liệu viewport (`entmod` mã 12, 45) **không có tác dụng**. Cách đúng: mở khóa viewport, `(setvar "CTAB" "<layout>")`, `(command "_.MSPACE")`, `(setvar "CVPORT" <số viewport>)`, `(command "_.ZOOM" "_C" (list x y) "1/50xp")`, `(command "_.PSPACE")`, rồi khóa lại. Vùng Model thấy được ở tỷ lệ 1/50 trong Layout A3: rộng 16.600, cao 14.350 mm.
6. **In PDF:** `(setvar "FILEDIA" 0) (setvar "BACKGROUNDPLOT" 0) (command "_.-PLOT" "_N" "<layout>" "" "" "<đường dẫn pdf>" "_N" "_Y")`, sau đó trả lại `FILEDIA`. Phải chắc file PDF **chưa tồn tại** trước khi in: kiểm tra bằng `(findfile <đường dẫn>)`, nếu có rồi thì in ra tên mới (`_v2`, `_v3`...). Nếu file đã có, nhất là đang mở trong trình xem PDF, AutoCAD sẽ đứng chờ câu hỏi ghi đè và treo MCP (đã treo 30 phút, anh phải bấm Esc).
7. **Kiểm tra bằng mắt:** chuyển PDF thành ảnh bằng PyMuPDF (`pymupdf`, đã cài) rồi xem. Cách này nhẹ hơn nhiều so với `get_screenshot`.
8. **Không đặt tên biến `t` trong `execute_lisp`.** `t` là hằng số đúng (T) của AutoLISP; ghi đè sẽ làm hỏng các đoạn LISP khác.
   **Tương tự với `pi`:** AutoLISP không phân biệt chữ hoa, chữ thường, nên biến tên `pI`, `PI` chính là `pi`. Đặt biến cục bộ tên `pI` làm `pi` thành nil, gây lỗi `bad argument type numberp: nil` khi vẽ mũi tên. Đặt tên khác (ví dụ `pIn`).
9. **Tên bản vẽ trong khung tên dân dụng** chỉ chứa được khoảng 30 ký tự (cột rộng khoảng 62 mm). Dài hơn sẽ tràn ra ngoài khổ giấy. Kiểm tra bằng khung bao (`vla-GetBoundingBox`) của Attribute.

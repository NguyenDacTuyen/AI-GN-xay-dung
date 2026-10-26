# Chi tiết template ISO_CTY.dwt (tài liệu tra cứu của skill gn-banvecad-isocty)

Đọc từ `template/ban-ve/ISO_CTY.dwt` (trước 26/10/2026 nằm ở `template/ISO_CTY.dwt`), cập nhật lần cuối ngày 16/10/2026 sau khi anh sửa template. Cài đặt chung: đơn vị **mm** (INSUNITS = 4), hệ mét, LTSCALE = 1, in theo màu (.ctb). Loại nét có sẵn: Continuous, CENTER, HIDDEN.

### Cách chọn style theo tỷ lệ (quan trọng nhất)
Template **không dùng Annotative**. Mỗi tỷ lệ có một bộ style riêng, chữ đã được phóng to sẵn để in ra đúng cỡ. Vì vậy:
- Chữ và kích thước đặt **trong Model**, chọn bộ style **trùng với tỷ lệ Viewport** của bản vẽ đó.
- Cỡ chữ in ra giấy: **kích thước 2,2 mm**, **ghi chú 2,5 mm**, **tiêu đề 3,5 mm**.
- Font: kích thước dùng **`viet buddy.shx`** (hệ số rộng 0,75); ghi chú và tiêu đề dùng **Times New Roman** (`times.ttf`). Khi gửi bản vẽ cho người khác phải gửi kèm file font `viet buddy.shx`.

| Tỷ lệ | Dim style | Text style kích thước (cao) | Text style ghi chú (cao) | Text style tiêu đề (cao) |
|---|---|---|---|---|
| 1:1 | `00.TP_1-1` | `28.TP_1-1 dim` (2,2) | `29.TP_1-1 Note` (2,5) | `30.TP_1-1 Title` (3,5) |
| 1:5 | `10.TP_1-5` | `31.TP_1-5 dim` (11) | `32.TP_1- 5 Note` (12,5) | `33.TP_1-5 Title` (17,5) |
| 1:10 | `05.TP_1-10` | `15.TP_1-10 dim` (22) | `14.TP_1-10 Note` (25) | `13.TP_1-10 Title` (35) |
| 1:15 | `11.TP_1-15` | `34.TP_1-15 dim` (33) | `35.TP_1-15 Note` (37,5) | `36.TP_1-15 Tile` (52,5) |
| 1:20 | `04.TP_1-20` | `12.TP_1-20 dim` (44) | `11.TP_1-20 Note` (50) | `10.TP_1-20 Title` (70) |
| 1:25 | `06.TP_1-25` | `16.TP_1-25 dim` (55) | `17.TP_1-25 Note` (62,5) | `18.TP_1-25 Title` (87,5) |
| 1:50 | `03.TP_1-50` | `09.TP_1-50 dim` (110) | `08.TP_1-50 Note` (125) | `07.TP_1-50 Title` (175) |
| 1:75 | `12.TP_1-75` | `37.TP_1-75 Dim` (165) | `38.TP_1-75 Note` (187,5) | `39.TP_1-75 Tile` (262,5) |
| 1:100 | `01.TP_1-100` | `03.TP_1-100 dim` (220) | `02.TP_1-100 Note` (250) | `01.TP_1-100 Title` (350) |
| 1:125 | `13.TP_1-125` | `40.TP_1-125 dim` (275) | `41.TP_1-125 Note` (312,5) | `42.TP_1-125 Title` (437,5) |
| 1:150 | `07.TP_1-150` | `21.TP_1-150 dim` (330) | `20.TP_1-150 Note` (375) | `19.TP_1-150 Title` (525) |
| 1:200 | `02.TP_1-200` | `06.TP_1-200 dim` (440) | `05.TP_1-200 Note` (500) | `04.TP_1-200 Title` (700) |
| 1:250 | `08.TP_1-250` | `22.TP_1-250 dim` (550) | `23.TP_1-250 Note` (625) | `24.TP_1-250 Titlle` (875) |
| 1:500 | `09.TP_1-500` | `27.TP_1-500 dim` (1100) | `26.TP_1-500 Note` (1250) | `25.TP_1-500 Titlle` (1750) |
| 1:1000 | `14.TP_1-1000` | `43.TP_1-1000 dim` (2200) | `44.TP_1-1000 Note` (2500) | `45.TP_1-1000 Tile` (3500) |
| 1:2000 | `15.TP_1-2000` | `46.TP_1-2000 dim` (4400) | `47.TP_1-2000 Note` (5000) | `48.TP_1-2000 Title` (7000) |

Tên style giữ nguyên như trong template, kể cả chỗ gõ sai (`Tile`, `Titlle`, `1- 5`). Code phải dùng đúng tên này.

Tất cả dim style bộ TP đều dùng đầu mũi tên **ArchTick** (gạch chéo), chữ nằm trên đường kích thước, màu chữ 60.

**Style cũ, không dùng cho bản vẽ mới:**
- Text style: `Standard`, `Annotative`, `VNI-HELVE-CON`, `KhungTen`, `.VnTimeH_B`, `.VnTimeH_B_1`, `.VnTimeH_B_2`, `KT-CN`, `Times New Roman`, `TP_Timenewroman`, `Timenewroman`, `ARIAL`, `Arial_3`, `Arial_B_3`, `Arial_4`, `_STYLE`, `THUOCLA`, `Mech-Q`. Lưu ý: `KhungTen` và `.VnTimeH_B*` dùng font TCVN3 (.VnTimeH), `KT-CN` dùng font VNI, nên gõ tiếng Việt Unicode vào sẽ bị lỗi. Các style tên "ARIAL..." thực chất lại dùng font Times.
- Dim style: `ISO-25`, `Standard`, `Annotative`, `ku 100`, `KT_CN 1-1000-R` (style này ghi đơn vị mét, có chữ "m" phía sau).

### Danh sách layer
Độ dày nét tính bằng mm. Tất cả layer dưới đây đều in, trừ khi ghi "**không in**".

**Ghi chú, kích thước, trình bày chung**

| Layer | Màu | Loại nét | Độ dày |
|---|---|---|---|
| `1.Tp_dim` | 140 | Continuous | 0,13 |
| `7.TP_text dim` | 60 | Continuous | 0,13 |
| `6.TP_Tex tNote` | 3 | Continuous | 0,25 |
| `8.TP_Text Title` | 4 | Continuous | 0,25 |
| `42.Tp_M learder` | 150 | Continuous | 0,13 |
| `9.Tp_Truc` | 145 | CENTER | 0,09 |
| `2.Tp_Cat` | 221 | Continuous | 0,09 |
| `3.TP_Hatch` | 8 | Continuous | 0,09 |
| `34.Tp_Hatch TKe` | 8 | Continuous | 0,13 |
| `4.Tp_Net dut` | 8 | HIDDEN | 0,13 |
| `5.TP_net thay` | 140 | Continuous | 0,30 |
| `35.Tp_Duong bao` | 1 | Continuous | 0,35 |
| `13.TP_bangTK` | 137 | Continuous | 0,13 |
| `18.TP_Bang dau TK` | 3 | Continuous | 0,20 |
| `20.TP_Khung ten` | 6 | Continuous | 0,40 |

**Kiến trúc, nhà xưởng**

| Layer | Màu | Loại nét | Độ dày |
|---|---|---|---|
| `30.TP_Wall` | 6 | Continuous | 0,15 |
| `57.TP_Net tuong` | 140 | Continuous | 0,20 |
| `31.TP_Column` | 4 | Continuous | 0,15 |
| `38.Tp_Floor` | 222 | Continuous | 0,20 |
| `36.Tp_Tran` | 53 | Continuous | 0,20 |
| `39.Tp_Cua so` | 6 | Continuous | 0,15 |
| `40.Tp_cua di` | 4 | Continuous | 0,15 |
| `41.Tp_cau thang` | 5 | Continuous | 0,20 |
| `59.TP_Mai ngoi` | 1 | Continuous | 0,18 |
| `62.Tp_Ton` | 183 | Continuous | 0,18 |
| `12.TP_Funiture` | 144 | Continuous | 0,20 |
| `26.TP_Thiet bi` | 255 | Continuous | 0,15 |
| `19.TP_San Vuon` | 3 | Continuous | 0,13 |
| `32.Tp_Cay co` | 3 | Continuous | 0,13 |

**Kết cấu (BTCT, thép)**

| Layer | Màu | Loại nét | Độ dày |
|---|---|---|---|
| `56.Tp_net betong` | 3 | Continuous | 0,30 |
| `37.Tp_Beam` | 150 | Continuous | 0,20 |
| `10.TP_Thep chu` | 1 | Continuous | 0,20 |
| `11.TP_Thep dai` | 6 | Continuous | 0,18 |
| `14.TP_Coc` | 6 | HIDDEN | 0,25 |
| `58.TP_thep hinh` | 4 | Continuous | 0,20 |
| `60.TP_Keo thep` | 1 | Continuous | 0,30 |
| `61.Tp_Xago thep` | 6 | Continuous | 0,20 |
| `63.Tp_Tru sat` | 2 | Continuous | 0,30 |
| `43.Tp_day KCAD` | 6 | Continuous | 0,18 |

**Hạ tầng, giao thông (mặt bằng)**

| Layer | Màu | Loại nét | Độ dày |
|---|---|---|---|
| `15.TP_tim duong` | 1 | CENTER | 0,30 |
| `21.TP_Mep duong` | 3 | Continuous | 0,20 |
| `22.TP_Mep le` | 5 | Continuous | 0,30 |
| `65.TP_Bovia` | 4 | Continuous | 0,15 |
| `66.TP_Lo gioi XD` | 1 | Continuous | 0,35 |
| `44. TP_Ao duong` | 135 | Continuous | 0,13 |
| `28.TP_Bien bao GT` | 4 | Continuous | 0,15 |
| `29.TP_vach son duong` | 255 | Continuous | 0,15 |
| `33.Tp_Duong do TK` | 1 | Continuous | 0,30 |
| `16.TP_hientrang` | 8 | Continuous | 0,13 |
| `64.TP.Duong cu` | 2 | HIDDEN | 0,13 |
| `17.TP_Text CDTK` | 2 | Continuous | 0,20 |
| `27.TP_Text CDHT` | 3 | Continuous | 0,15 |
| `49.TP_Taluy dao` | 3 | Continuous | 0,13 |
| `50.TP_Taluy dap` | 4 | Continuous | 0,13 |
| `23.TP_Duong TNM` | 93 | Continuous | 0,20 |
| `25.TP_Duong TNT` | 6 | Continuous | 0,20 |
| `24.TP_Ho GA` | 4 | Continuous | 0,20 |
| `51.TP_duong tim cong` | 8 | HIDDEN | 0,13 |
| `52.TP_duong bao ngoai cong` | 150 | Continuous | 0,25 |
| `53.TP_duong bao trong cong` | 3 | Continuous | 0,15 |

**Trắc dọc, trắc ngang**

| Layer | Màu | Loại nét | Độ dày |
|---|---|---|---|
| `46.TP_bang TD_TN` | 3 | Continuous | 0,15 |
| `48.TP_Text dau bang TN_TD` | 4 | Continuous | 0,20 |
| `47.TP_Text CDTKTN_TD` | 2 | Continuous | 0,25 |
| `45.TP_Duong giong TN_TD` | 135 | Continuous | 0,09 |
| `54.Tp_duong giong TD_TN tu nhien` | 8 | HIDDEN | 0,13 |
| `55.Tp_duong den tu nhien TD_TN` | 3 | HIDDEN | 0,13 |

**Layer hệ thống và layer cũ:** `0`, `Defpoints` (không in), `2S_DIM CHUAN`, `KHUNGIN`, `A-khungten`. Không vẽ đối tượng mới lên các layer này. Riêng `KHUNGIN` và `A-khungten` đang được dùng bên trong block khung tên, nên **không xóa**.

### Các điểm đã được anh sửa trong template (16/10/2026)
- Tiêu đề 1:50 sửa từ 350 thành **175**, 1:15 từ 52,2 thành **52,5**, 1:250 từ 870 thành **875**. Giờ tất cả tiêu đề in ra đều đúng 3,5 mm.
- Layer `65.TP_Bovia` và `66.TP_Lo gioi XD` đã chuyển sang **có in**.
- Đã thêm 2 block khung tên `Khung ten_Dan dung` và `khung ten_giaothong`.
- Đã xóa layer `0-KHUNG TEN - TEXT`.

- Đã đưa Attribute vào 2 block khung tên, thống nhất tên tag và dời base point về góc dưới trái khung.
- Đã đổi tên Layout và cài đặt in (xem mục Layout bên dưới).

**Ngày 17/10/2026:**
- Đã thu gọn chữ ở khung dân dụng. Cả 2 khung tên giờ nằm gọn trong khổ A3 (420 × 297 mm).
- Đã tạo viewport trên layer `Defpoints`, nằm gọn trong vùng vẽ.
- Đã chuyển khung tên (trong Layout và Model) sang layer `20.TP_Khung ten`.

### Layout có sẵn trong template

| Layout | Khung tên | Máy in | Khổ giấy | Nét in |
|---|---|---|---|---|
| `A3_DanDung` | `Khung ten_Dan dung` tại (0,0) | DWG To PDF.pc3 | ISO full bleed A3 (420 × 297 mm) | monochrome.ctb |
| `A3_GiaoThong` | `khung ten_giaothong` tại (0,0) | DWG To PDF.pc3 | ISO full bleed A3 (420 × 297 mm) | monochrome.ctb |

**Viewport (layer `Defpoints`, không in viền):**
- `A3_DanDung`: rộng 332 × cao 287 mm, chiếm phần bên trái tờ giấy (x từ 20 đến 352 mm). Cột khung tên nằm ở bên phải.
- `A3_GiaoThong`: rộng 396 × cao 253 mm, chiếm phần phía trên tờ giấy (y từ 39 đến 292 mm). Khung tên nằm ở dải dưới.

Tỷ lệ viewport trong template chưa đặt theo tỷ lệ chuẩn. Khi tạo bản vẽ mới:
1. Copy Layout tương ứng.
2. Đặt tỷ lệ viewport đúng bằng tỷ lệ bản vẽ (1:50, 1:100...), trùng với bộ text style và dim style đang dùng.
3. Khóa viewport (Display Locked = Yes) để không lỡ tay zoom làm sai tỷ lệ.
4. Điền 3 Attribute của khung tên.

**Lưu ý khi đọc file bằng code:** mỗi Layout luôn có thêm một viewport hệ thống, là chính trang giấy của Layout (viewport số 1, nằm trên layer `0`). Kích thước của nó thay đổi theo mức zoom màn hình. Đây **không phải** viewport bản vẽ, không xóa được và không cần kiểm tra.

### Điểm còn lại (chỉ để biết, Claude không tự sửa)
- Chữ cố định trong khung tên vẫn ghi nội dung dự án cũ (xem mục Khung tên). Nếu muốn Claude tự điền cho từng dự án, nên chuyển thêm các ô tên công trình, địa điểm, chủ đầu tư, bước thiết kế, ngày, số hợp đồng thành Attribute.
- Vẫn còn các block mẫu layer cũ (`ISO_LAYER TEXT_THANH PHAT`, `layer mau`...). Các block này chỉ dùng để tham khảo, không chèn vào bản vẽ.

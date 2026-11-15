# Bóc khối lượng từ trắc dọc thoát nước, xuất theo mẫu (tài liệu tra cứu skill gn-dutoan)

Áp dụng cho hạ tầng thoát nước. Anh chốt 02-03/11/2026, đã chạy khớp mẫu với dự án Nhị Bình.
Có **2 bộ công cụ** (cùng nguyên tắc, cùng file mẫu `template/du-toan/thoat-nuoc-giao-thong/mau-boc-khoi-luong-tong-hop.xlsx`):
- **Hầm ga (giếng thu):** `python/boc-ham-ga-thoat-nuoc.py` + `chay-boc-ham-ga.bat` → xuất tab "Dao dap ho ga".
- **Cống + mối nối/gối cống:** `python/boc-cong-moinoi-thoat-nuoc.py` + `chay-boc-cong-moinoi.bat` → xuất tab "Dao dap cong" và "Moi noi-goi cong". Các cột kỹ thuật **tra VLOOKUP vào sheet "DINH HINH CONG"** trong file mẫu. Xem mục "Bộ cống + mối nối" cuối file.

Bên dưới mô tả bộ hầm ga trước, rồi tới bộ cống + mối nối.

## Nguyên tắc (2 bước tách bạch)
1. **Tính (động) từ bản vẽ:** đọc file DXF trắc dọc thoát nước theo **tên layer**, ra danh sách hầm ga (bao nhiêu giếng, Ø nào, cao độ nào cũng được). Khối lượng dùng **công thức** Excel, số thô chỉ là cao độ/đường kính đọc từ bản vẽ.
2. **Định dạng theo mẫu:** lấy **chính file Excel mẫu làm nền** rồi chỉ **thêm/bớt số hàng** cho khớp số giếng. Giữ nguyên 100% định dạng mẫu (in ngang, lề, chiều cao hàng, độ rộng cột, số lẻ, định dạng cột, lặp dòng tiêu đề khi in, ô gộp).
   - **Tuyệt đối không** dựng bảng từ đầu rồi tự định dạng lại (dễ sai, thiếu định dạng). **Không** mở mẫu rồi điền tay vào số hàng cố định (công trình khác số giếng sẽ sai).

## Chương trình & cách chạy
- Chương trình: `python/boc-ham-ga-thoat-nuoc.py` (phần **CẤU HÌNH** đầu file: đường dẫn DXF, MAU, OUT và **tên layer**).
- Chạy nhanh: `chay-boc-ham-ga.bat` (thư mục gốc dự án).
- Hướng dẫn cho anh Tuyên: `python/HUONG-DAN-boc-ham-ga.md`.
- Cần thư viện `ezdxf`, `openpyxl`.
- Nếu không thấy layer, chương trình **in ra danh sách layer** của bản vẽ để sửa lại phần CẤU HÌNH.

## Layer đọc trên trắc dọc (bộ layer chuẩn Nhị Bình)
| Số liệu | Layer |
|---|---|
| Cao độ mặt đất tự nhiên | `TP33_TD_Caodotunhien` |
| Cao độ đáy (lòng trong) cống | `TP115_TD_Caodo_daycong_TR` |
| Cao độ đỉnh/nắp giếng | `TP45_TD_Caodo_dinhGiengthu` (1 giá trị/giếng) |
| Cao độ đáy hố ga/giếng | `TP46_TD_Caodo_daygienhthu` |
| Đường kính cống (text `%%cNNN`) | `TP118_TD_Khoangcachgiengthu` |
| Chiều dài cống (nếu bóc cống) | `TP113_TD_Dodoccong` (cột độ dốc–chiều dài) |

Ghép theo **vị trí X** (nearest). Công trình đặt tên layer khác thì sửa trong CẤU HÌNH.

## Bảng hầm ga — cột và công thức (sheet "Dao dap ho ga")
Thứ tự cột (anh chốt): STT · Tên hầm ga · Loại hầm ga (số Ø, định dạng `\Ø0`) · Cao độ đỉnh HG · Cao độ tự nhiên · **Cao độ đáy hầm ga** (đọc trực tiếp TP46) · Cao độ đáy cống · B_lòng trong HG · B_bê tông lót HG · B_phui đào HG · Chiều sâu đào HG · V đào · Thép thân Ø≤10 · Thép thang Ø>10 · VK thành HG · BT thành HG · DT cừ tràm.

Công thức chính (tham chiếu sheet "Thong so"):
- Đáy hầm ga = đọc TP46 (không tính qua hố lắng).
- B_bê tông lót = lòng + 2·vách + 2·(mở rộng lót mỗi bên).
- B_phui đào = B_bê tông lót + 2·a.
- **Chiều sâu đào = cao độ tự nhiên − cao độ đáy hầm ga + dày bản đáy + dày BT lót + dày cát đệm** (dấu CỘNG).
- V đào = B_phui² × chiều sâu.
- Thép thân (Ø≤10) = (thép 1 hầm/1,0 m) × chiều cao thân (= đỉnh − đáy hầm ga).
- Thép thang (Ø16, >10) = (chiều cao thân / bước nấc) × dài nấc × đơn trọng Ø16.
- VK thành = (chu vi lòng + chu vi khuôn) × chiều cao thân; BT thành = (khuôn² − lòng²) × chiều cao thân. khuôn = lòng + 2·vách.
- Dòng TỔNG: SUM các cột khối lượng.

## Thông số (sheet "Thong so", ô vàng = cần xác nhận theo bản vẽ chi tiết)
Đường kính ngoài cống D400/D600; cát đệm cống 5 cm; BT lót M150 cống; mái dốc hào cống (Nhị Bình: 1/2); lòng trong hầm ga D400 0,8 / D600 1,0; vách thân 0,2; cát đệm hầm ga 0,2; BT lót hầm ga 0,1; bản đáy hầm ga; lót mở rộng mỗi bên 0,2; thép thân 90,444 kg/hầm/1,0 m; bước nấc thang; đơn trọng Ø16 1,578 kg/m; cừ tràm 25 cây/m². **Lấy đúng từ chi tiết hầm ga/cống, không tự bịa.**

## Sau khi ra bảng
- Mở file một lần trong Excel để công thức tính ra giá trị.
- Kiểm số giếng, cao độ khớp bản vẽ; sửa ô vàng cho đúng công trình.
- Mã hiệu định mức, đơn giá: để `[Chờ bổ sung]`, áp trên **F1** (xem `quy-trinh-f1.md`).

---

## Bộ cống + mối nối (`python/boc-cong-moinoi-thoat-nuoc.py`)

Xuất 2 tab "Dao dap cong" và "Moi noi-goi cong". Mỗi đoạn cống ghép **2 giếng đầu/sau** (giếng kẹp theo vị trí X). Chiều dài đoạn lấy từ cột độ dốc–chiều dài trắc dọc (`TP113_TD_Dodoccong`). Số kỹ thuật **tra VLOOKUP vào sheet "DINH HINH CONG"** (theo đường kính, m) — bảng này nằm trong file mẫu.

Layer đọc: như bộ hầm ga + `TP113_TD_Dodoccong` (chiều dài cống). Đường kính từ `TP118` (text `%%cNNN`).

### Tab "Dao dap cong" (20 cột, công thức chính)
- B_đáy phui = tra định hình (cột 13). Thành cống = (Dngoài − Ø)/2, Dngoài tra định hình (cột 17).
- Cao độ đáy móng = đáy cống TB − thành cống − cát lót (cột 2) − BT lót (cột 3).
- H đào = cao độ tự nhiên TB − đáy móng.
- B_phui = B_đáy + 0,5·H đào (ta-luy ngang:đứng = 1:2 → m = 0,5).
- V đào = H đào × B_phui × chiều dài.
- V cống chiếm chỗ = (tiết diện cống + BT lót + cát lót, tra định hình) × chiều dài.
- V lòng cát lưng cống = V đào − V chiếm chỗ.
- Cột đường kính định dạng `\Ø0` (hiện Ø600/Ø400).

### Tab "Moi noi-goi cong" (17 cột)
- Chia ống 4/3/2/1 m theo chiều dài đoạn; số mối nối = tổng ống − 1; số gối = 2 × tổng ống.
- Vữa mối nối = số mối × (vữa 1 mối, định hình cột 7); VK chèn mối nối = số mối × (chu vi VK chèn, cột 9); BT chèn gối = số gối × (BT 1 gối, cột 11).
- V đệm cát / BT lót đáy = tiết diện (cột 5 / cột 6) × chiều dài; VK lót đáy = 2 × cao VK lót (cột 8) × chiều dài.
- Chiều dài cừ tràm = số gối × số cừ/gối (cột 16) × 4 m. **Lưu ý:** định hình thường thiếu "số cừ tại gối" cho một số Ø (ví dụ D400) → cột cừ = 0, cần điền vào định hình.

Dòng TỔNG dùng SUM; chữ "TỔNG" ghi vào ô neo A của vùng gộp A..C. Sau khi điền, chạy `norm()` đồng bộ font Times New Roman 11 + canh giữa + viền cho mọi ô dữ liệu (các ô trước trống trong mẫu hay bị Calibri).

## Giới hạn / mở rộng
- Đã tự động hóa: **hầm ga**, **đào đắp cống**, **mối nối/gối cống**. Ván khuôn/bê tông hầm ga nằm trong bộ hầm ga (v8).
- Mọi số kỹ thuật cống lấy từ sheet "DINH HINH CONG" — một nguồn duy nhất; đổi định hình là bảng tự cập nhật.
- Bản vẽ khác chuẩn layer, hoặc file mẫu đổi số cột/bố cục → dò lại layer và đối chiếu header tab trước khi chạy (số cột script phải khớp header mẫu, nếu không sẽ lệch cột).
- **Không ghi đè file mẫu**; luôn xuất ra file kết quả riêng đặt tên theo công trình.

---

## Quy trình chung và bộ bóc TỔNG HỢP 1 file (chuyển từ SKILL.md)

Khi bóc **đào đắp + bê tông hầm ga (giếng thu)** hạ tầng thoát nước: làm theo file tra cứu **`boc-tu-trac-doc.md`** (cùng thư mục skill). Nguyên tắc 2 bước:
1. **Tính động** từ DXF trắc dọc theo tên layer (bao nhiêu giếng cũng được), khối lượng dùng công thức.
2. **Lấy chính file Excel mẫu làm nền**, chỉ thêm/bớt số hàng cho khớp số giếng → giữ nguyên 100% định dạng mẫu (in ngang, lề, hàng, cột, số lẻ, ô gộp).
Không dựng bảng từ đầu rồi tự định dạng; không mở mẫu điền tay vào số hàng cố định.

Hai bộ công cụ (cùng file mẫu `template/du-toan/thoat-nuoc-giao-thong/mau-boc-khoi-luong-tong-hop.xlsx`, cùng sheet "DINH HINH CONG" để tra):
- **Hầm ga (giếng thu):** `python/boc-ham-ga-thoat-nuoc.py` (`chay-boc-ham-ga.bat`) → tab "Dao dap ho ga".
- **Cống + mối nối/gối cống:** `python/boc-cong-moinoi-thoat-nuoc.py` (`chay-boc-cong-moinoi.bat`) → tab "Dao dap cong" + "Moi noi-goi cong", mỗi đoạn ghép 2 giếng đầu/sau, tra VLOOKUP vào "DINH HINH CONG".

Tên layer, cột, công thức, thông số, bảng định hình: xem **`boc-tu-trac-doc.md`**. Bản vẽ khác chuẩn layer thì sửa CẤU HÌNH đầu chương trình (tự in danh sách layer nếu sai tên). Số cột trong chương trình phải khớp header tab của file mẫu, nếu không sẽ lệch cột.

### Bóc TỔNG HỢP 1 file: thoát nước + giao thông (chốt 04/11/2026)

Khi cần ra **1 file Excel đủ cả thoát nước và giao thông** theo một mẫu tổng hợp: dùng
**`python/boc-tong-hop-thoat-nuoc-giao-thong.py`** (`chay-boc-tong-hop.bat`). Chương trình gọi lại 2 bộ trên, rồi ghép thành 1 file:
- Mẫu tổng hợp: `template/du-toan/thoat-nuoc-giao-thong/mau-boc-khoi-luong-tong-hop.xlsx` (7 sheet: Thong so, DINH HINH CONG, Dao dap cong, Dao dap ho ga, Moi noi-goi cong, Dao dap nen duong, Tong hop).
- **Thoát nước** (cống, hầm ga, mối nối/gối): bóc tự động từ DXF như trên.
- **Giao thông** (`Dao dap nen duong`): KHÔNG đọc tự động từ bản vẽ được (dải bảng san nền trong DXF không tin cậy). Anh **xuất CSV từ anddesign**; chương trình đổ vào, **số cột công tác động** theo CSV. Công trình không có giao thông thì để `CSV_GIAOTHONG = ""`.
- **Tong hop**: công thức **tự tìm dòng TỔNG** (INDEX/MATCH), giao thông dò theo **tên công tác** → dùng lại cho mọi công trình dù khác số lượng/số cột.
- Viền ngoài cùng mọi bảng kẻ **nét đậm** (medium), viền trong mảnh.

**Bản đồ cột (phải khớp tiêu đề mẫu, nếu sửa mẫu phải sửa chương trình):**
- `Dao dap cong`: R=V đào, S=V cống chiếm chỗ, T=V lòng cát lưng cống (đắp trả).
- `Moi noi-goi cong`: H=số mối nối, I=số gối, J=vữa, K=VK chèn mối nối, L=BT chèn gối, M=tổng dài, **N=cát đệm đáy cống, O=VK bê tông lót đáy cống, P=BT lót đáy cống**, Q=cừ tràm gối cống.
- `Dao dap ho ga`: L=V đào, M=thép thân, N=thép thang, O=VK thành, P=BT thành, **Q=VK lót hầm ga, R=BT lót hầm ga M150, S=cừ tràm**. (Cột VK lót=4·I·B14, BT lót=I²·B14 với I=B_bê tông lót HG, B14=dày BT lót HG.)
- `Tong hop` giao thông: mỗi công tác = `INDEX` cột KL tại dòng TỔNG, dò theo tên ở hàng 5 của `Dao dap nen duong`.

CẤU HÌNH (sửa đầu chương trình): `MAU` (mặc định trỏ mẫu trong template), `DXF`, `CSV_GIAOTHONG`, `OUT`. 4 ô thông số thi công hầm ga trong `Thong so` (B9 hố lắng, B14 dày BT lót HG, B18 bản đáy HG, B19 mở rộng BT lót, B20 bước nấc thang) lấy từ **bản vẽ chi tiết hầm ga**, không có trong DINH HINH CONG.

## Đã chốt (15/11/2026)
- **File mẫu chuẩn** cho hầm ga, cống, mối nối, giao thông: `template/du-toan/thoat-nuoc-giao-thong/mau-boc-khoi-luong-tong-hop.xlsx` (7 sheet). Cả 3 chương trình bóc đều trỏ mẫu này; không còn dùng `mau hamga.xlsx` ở `F:\demo\`. `DXF` và `OUT` vẫn là đường dẫn công trình cũ (Nhị Bình), phải sửa trong CẤU HÌNH khi làm công trình mới.
- **Phần mềm xuất CSV giao thông:** anddesign (file CSV mẫu tên `...addesign.csv`).

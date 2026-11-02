# Hướng dẫn bóc khối lượng đào đắp hầm ga cho công trình mới

Công cụ: `python/boc-ham-ga-thoat-nuoc.py` (chạy nhanh bằng `chay-boc-ham-ga.bat` ở thư mục gốc dự án).
Nó đọc bản vẽ trắc dọc thoát nước → ra bảng đào đắp hầm ga, **giữ đúng định dạng file mẫu** (in ngang, lề, hàng, cột, số lẻ...), tự co giãn số hàng theo số giếng.

## Cần có trước
1. **Python** đã cài, kèm 2 thư viện (cài 1 lần, mở Command Prompt gõ):
   `pip install ezdxf openpyxl`
2. **File bản vẽ DXF** trắc dọc thoát nước của công trình (nếu bản vẽ là DWG: mở AutoCAD, gõ `DXFOUT` để lưu ra .dxf).
3. **File Excel mẫu** `mau hamga.xlsx` (đã có; dùng lại cho mọi công trình).

## Điều kiện quan trọng về LAYER
Công cụ đọc số liệu **theo tên layer** trên trắc dọc. Nó chạy đúng khi bản vẽ mới dùng **cùng bộ layer** như bản Nhị Bình:
- Cao độ tự nhiên: `TP33_TD_Caodotunhien`
- Cao độ đáy cống: `TP115_TD_Caodo_daycong_TR`
- Cao độ nắp giếng: `TP45_TD_Caodo_dinhGiengthu`
- Cao độ đáy giếng: `TP46_TD_Caodo_daygienhthu`
- Đường kính (text %%cNNN): `TP118_TD_Khoangcachgiengthu`

Nếu công trình mới đặt **tên layer khác**, mở `python/boc-ham-ga-thoat-nuoc.py`, sửa đúng tên ở phần **CẤU HÌNH** (đầu file). Nếu chạy mà báo "Khong tim thay layer", nó sẽ in ra danh sách layer có trong bản vẽ để anh đối chiếu sửa cho đúng.

## Các bước làm (từng bước)
1. Chép **DXF công trình mới** vào máy, nhớ đường dẫn.
2. Mở file `python/boc-ham-ga-thoat-nuoc.py` bằng Notepad, sửa 3 dòng trong **CẤU HÌNH**:
   - `DXF = r"..."` → đường dẫn bản vẽ mới
   - `MAU = r"..."` → đường dẫn file mẫu
   - `OUT = r"..."` → nơi lưu + tên file kết quả (nên đổi tên theo tên công trình)
   Lưu lại.
3. Nhấp đúp `chay-boc-ham-ga.bat` (hoặc mở Command Prompt tại thư mục dự án gõ:
   `python -I "python\boc-ham-ga-thoat-nuoc.py"`).
4. Màn hình báo `XONG. So gieng = ...` là đã ra file Excel ở đường dẫn OUT.
5. Mở file Excel kết quả, kiểm:
   - Số hầm ga, cao độ đã đúng bản vẽ chưa.
   - Sheet **"Thong so"**: sửa các **ô vàng** cho đúng công trình (Dngoài, lòng hầm ga, vách, bản đáy, mái dốc, thép, cừ tràm...). Bảng tự tính lại.
6. Mở file trong Excel một lần để công thức tính ra giá trị (file do chương trình tạo chưa tính sẵn).
7. Áp **mã hiệu định mức, đơn giá** trên phần mềm F1 (ĐM TT38/2026, đơn giá HCM) — bước này anh làm như thường lệ.

## Khi khó / không chắc
- Bản vẽ khác chuẩn layer, hoặc thiếu hàng cao độ đáy giếng trên trắc dọc → đưa file DXF + file mẫu cho Claude, nói "bóc hầm ga theo mẫu", Claude sẽ dò lại layer và chạy giúp.
- Công cụ này mới làm cho **hầm ga thoát nước**. Các bảng khác (đào đắp cống, mối nối/gối, ván khuôn/bê tông) đã có trong các bản v5–v8 ở `ket-qua/03_demo-doi-agent/`; cần tự động hóa thêm thì báo Claude.

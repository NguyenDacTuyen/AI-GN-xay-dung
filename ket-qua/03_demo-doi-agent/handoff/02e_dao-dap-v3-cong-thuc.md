# 02e — Đào đắp cống + hố ga v3 (toàn công thức, sửa theo 7 góp ý)

File: `ket-qua/03_demo-doi-agent/KL-dao-dap-thoat-nuoc_demo_v3.xlsx`. **Toàn bộ khối lượng là công thức Excel**, trỏ về sheet "Thong so" và cột số thô đọc từ bản vẽ (tô xanh). Mở bằng Excel/F1 để thấy giá trị.

## Xử lý theo 7 góp ý của anh
1. **Đường kính ngoài cống** — suy từ thể tích bê tông/ống trong chi tiết 13a (ống L=4 m): D400 V=0,291 m³ → **Dngoài 0,503 m** (thành 51 mm); D600 V=0,548 m³ → **Dngoài 0,731 m** (thành 66 mm). Đã đưa vào sheet Thong so.
2. **Chiều dài cống** = khoảng cách tim 2 hố ga − khuôn ngoài hố ga (công thức cột J). Dòng "chiều dài cống" trên trắc dọc là đối tượng proxy, không đọc được, nên dùng cách trừ hố ga theo đúng ý anh.
3. **BT lót M150 dưới cống** — chi tiết móng cống 14 CÓ lớp này; **chiều dày chưa đọc được từ hình cắt** (nằm trong DIM hình, không có trong ghi chú chữ). Đang để ô nhập 0,10 m — **anh xác nhận/sửa ô B5**.
4. **Cao độ đáy cống = đáy lòng trong** (invert). Công thức đã sửa đúng: đáy ngoài = đáy lòng trong − bề dày thành cống; đáy móng = đáy ngoài − cát đệm − BT lót. (Trước đây thiếu phần bề dày thành.)
5. **Toàn công thức**, không số thô — chỉ 3 cột tô xanh là số đọc từ bản vẽ (khoảng cách tim-tim, cao độ mặt đất, cao độ đáy lòng trong).
6. **Mái dốc đào** — chi tiết móng cống có hình cắt hào, nhưng **trị số mái dốc nằm trong hình học, chưa tự đọc được** (ghi "1/20, 1/10" là tỷ lệ bản vẽ, không phải mái dốc). Đang để ô nhập m = 0 (đào đứng/phui đào). **Anh cho hệ số mái dốc để điền ô B6**, hoặc chỉ tôi ghi chú cụ thể để đọc.
7. **Hầm ga** — từ chi tiết 10: lòng trong D400≈0,80 / D600≈1,00 m, **vách 0,20 m**, lót cát đáy 20 cm, nắp M300, vách BTCT M200. Lòng/vách lấy theo DIM mặt bằng — anh xác nhận ô B10–B12.

## Kết quả v3 (theo thông số hiện tại)
| Hạng mục | ĐVT | KL |
|---|---|---|
| Giếng thu | cái | 30 |
| Cống D400 / D600 (đã trừ khuôn hố ga) | m | 453,3 / 327,0 |
| Đào móng hào cống | m³ | 986,6 |
| Cát đệm 5 cm | m³ | 46,8 |
| BT lót M150 | m³ | 93,5 |
| Đắp trả hào cống | m³ | 619,0 |
| Đào hố ga | m³ | 191,8 |
| Thép hầm ga (ước) | kg | ~4.310 |
| Cừ tràm gia cố | cây | ~26.041 |

## Còn cần anh (2 ô chưa đọc được từ hình + phạm vi)
- **B5 — BT lót dày** (chi tiết móng cống): anh cho số.
- **B6 — mái dốc hào m** (chi tiết móng cống): anh cho số.
- Phạm vi gia cố cừ tràm: toàn tuyến hay chỉ đoạn nền yếu.
- Mã hiệu định mức / đơn giá: `[Chờ bổ sung]` (áp trên F1).

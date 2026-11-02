# 02d — Đào đắp cống + hố ga v2 (thay giả định bằng số từ bản vẽ chi tiết)

Nguồn chi tiết (anh để ở `F:\demo`):
- `13a.CHI TIET CONG D400-D600-D800.dxf`
- `14.CHI TIET MONG-GOI CONG...dxf`
- `10.CHI TIET HAM GA D400-D800.dxf`

File kết quả: `ket-qua/03_demo-doi-agent/KL-dao-dap-thoat-nuoc_demo_v2.xlsx` (bản v1 giữ nguyên). Khối lượng đã tính sẵn (giá trị).

## Số LẤY ĐƯỢC từ bản vẽ chi tiết (đã thay vào)
- Cát đệm dưới cống = **5 cm** (chi tiết 14: "CÁT ĐỆM = 5cm").
- BT lót đá 1×2 **M150** dưới cống/gối (chi tiết 14).
- Cấp bê tông: **cống M300**, **gối cống M200**, **vách hầm ga BTCT M200**, **nắp hầm ga M300**, lót M150 (chi tiết 13a/14/10).
- **Gia cố cừ tràm 25 cây/m², L=4 m** (chi tiết 14 và 10) — nền đất yếu.
- Hầm ga: **lót cát đáy 20 cm** (chi tiết 10).
- Thép 1 hầm ga ≈ **90,444 kg cho chiều cao 1,0 m** (bảng tổng hợp thép, chi tiết 10).
- Tải trọng H30-XB80; chiều cao đất đắp trên cống tối thiểu 0,50 m (chi tiết 13a).

## Kết quả v2
| Hạng mục | ĐVT | KL |
|---|---|---|
| Giếng thu | cái | 30 |
| Cống D400 / D600 | m | 473,74 / 343,83 |
| Đào móng hào cống | m³ | 963,8 |
| Cát đệm (5cm) | m³ | 48,3 |
| BT lót M150 dưới cống | m³ | 96,5 |
| Đắp trả hào cống | m³ | 593,3 |
| Đào hố ga | m³ | 191,8 |
| Thép hầm ga (ước) | kg | ~4.310 |
| Cừ tràm gia cố | cây | ~26.795 |
| Nắp hầm ga M300 | cái | 30 |

## CÒN GIẢ ĐỊNH / cần anh xác nhận (ô vàng trong sheet "Thong so")
- **Dngoài cống** D400=0,48 / D600=0,72 m (bề dày thành giả định) — cần khớp đúng chi tiết 13a.
- **Lòng hầm ga** D400≈0,80 / D600≈1,00 m, **vách 0,20 m** — đọc sơ bộ từ DIM mặt bằng, cần xác nhận ô kích thước cụ thể.
- **BT lót dưới cống dày 0,10 m** — chi tiết 14 có lớp này nhưng chưa chốt chiều dày.
- **Bề rộng làm việc hào a = 0,30 m/bên**, đào thành đứng (m=0) — theo biện pháp, cần xác nhận.
- **Phạm vi gia cố cừ tràm**: đang tính toàn tuyến; xác nhận chỉ gia cố đoạn nền yếu hay toàn bộ.
- Thép hầm ga tính xấp xỉ theo chiều cao (90,44 kg cho 1,0 m); hầm cao khác 1,0 m thì nội suy — cần bảng thép theo từng chiều cao để chính xác.
- Mã hiệu định mức, đơn giá, thành tiền: `[Chờ bổ sung]` (anh áp trên F1).
- Gối cống BTCT M200 (đúc sẵn, 2 gối/ống, ống L=4m): chưa đưa vào bảng — cần nếu bóc chi tiết cấu kiện.

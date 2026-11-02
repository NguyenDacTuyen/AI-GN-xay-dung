# 02b — Bổ sung cống dọc (sau khi anh chỉ nguồn: bảng trắc dọc thoát nước)

Trước đó cống để `[Chờ bổ sung]` vì hình cống nằm trong proxy. Anh chỉ ra bản vẽ ĐÃ có bảng trắc dọc thoát nước → bóc lại được từ chữ trên trắc dọc.

## Nguồn
- Layer `TP118_TD_Khoangcachgiengthu`: mỗi đoạn có 1 text đường kính (`%%c600`, `%%c400` = Ø600, Ø400) + 1 text khoảng cách giếng thu (m). 29 đoạn giữa 30 giếng.
- Layer `TP113_TD_Dodoccong`: độ dốc dọc 0,17%–0,25%.
- Layer `TP114/TP115`: cao độ đỉnh/đáy cống (54 giá trị mỗi loại) — chưa bóc chi tiết theo đoạn.

## Kết quả (ghép đường kính với khoảng cách theo vị trí, 0 cặp ghép sai > 5 m)
| Đường kính | Số đoạn | Tổng chiều dài (m) |
|---|---|---|
| Ø400 | 17 | 473,74 |
| Ø600 | 12 | 343,83 |
| **Tổng** | **29** | **817,57** |

File: `ket-qua/03_demo-doi-agent/KL-thoat-nuoc-demo_v2.xlsx` (sheet "KL thoat nuoc" + "Chi tiet doan cong"). Bản v1 giữ nguyên.

## Chỗ cần xác nhận lại
- Chiều dài lấy theo **khoảng cách giếng thu** trên trắc dọc; cần xác nhận là tim–tim giếng hay chiều dài thông thủy cống (có thể lệch chút ở phạm vi giếng).
- TP113 có 27 giá trị độ dốc / 27 chiều dài, lệch so với 29 đoạn của TP118 — cần xác nhận 2 đoạn còn lại (có thể là cống ngang hoặc đoạn đặc biệt).
- Cống một tuyến hay hai bên đường: cần xác nhận để không thiếu/thừa.
- Mã hiệu định mức, đơn giá, đào đắp phui cống, gối/đệm/mối nối: vẫn `[Chờ bổ sung]`.

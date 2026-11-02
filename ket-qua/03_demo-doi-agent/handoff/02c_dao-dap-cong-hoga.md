# 02c — Bảng tính đào đắp cống và hố ga (DEMO)

File: `ket-qua/03_demo-doi-agent/KL-dao-dap-thoat-nuoc_demo.xlsx` — 4 sheet: Thong so, Dao dap cong, Dao dap ho ga, Tong hop. Khối lượng dùng **công thức**, trỏ về sheet "Thong so" nên anh chỉnh thông số là tự tính lại.

## Số liệu lấy thẳng từ bản vẽ (trắc dọc thoát nước)
- Chiều dài từng đoạn + đường kính: layer `TP118` → 29 đoạn (D400: 17 đoạn / 473,74 m; D600: 12 đoạn / 343,83 m).
- Cao độ đáy cống từng điểm: `TP115`. Cao độ mặt đất tự nhiên: `TP33`. Cao độ nắp giếng thu: `TP45` (30 giếng, 1,62–2,04 m). Mực so sánh MSS −4,00 → cao độ là **tuyệt đối**.
- Chiều sâu đào (mặt đất − đáy móng): min 0,50 / TB 0,82 / max 1,41 m. Một tuyến liên tục 30 giếng / 29 đoạn.

## Kết quả sơ bộ (theo thông số mặc định)
| Hạng mục | ĐVT | KL |
|---|---|---|
| Giếng thu | cái | 30 |
| Cống D400 / D600 | m | 473,74 / 343,83 |
| Đào móng cống | m³ | 915,5 |
| Đệm dưới cống | m³ | 96,5 |
| Cống chiếm chỗ | m³ | 225,7 |
| Đắp trả hào cống | m³ | 593,3 |
| Đào hố ga (30 giếng) | m³ | 68,6 |

## Công thức dùng
- Cao độ đáy móng = cao độ đáy cống − chiều dày đệm.
- Chiều sâu đào H = cao độ mặt đất − cao độ đáy móng.
- Bề rộng hào B = Dngoài + 2·a. V đào = (B + m·H)·H·L (hào hình thang; m=0 là đào đứng).
- V đệm = B·t_đệm·L. V cống chiếm chỗ = π/4·Dngoài²·L. V đắp trả = V đào − V đệm − V cống.
- Hố ga: V đào = Brộng·Bdài·(cao độ nắp − (đáy cống − hố lắng)).

## GIẢ ĐỊNH — cần anh xác nhận lại (sheet "Thong so", ô vàng)
- a = 0,30 m (bề rộng thi công mỗi bên hào).
- t_đệm = 0,10 m; m = 0 (đào thành đứng, có văng chống).
- Dngoài: D400→0,48 m; D600→0,72 m (giả định cống BTCT — cần tra định hình thực tế).
- Hố lắng dưới đáy cống tại giếng = 0,30 m.
- Hố ga: hố đào 1,20 × 1,20 m (CHƯA có bản vẽ chi tiết giếng → `[Chờ bổ sung]`).

## Cần xác nhận / còn thiếu
- Cống **một tuyến** (theo trắc dọc) — anh xác nhận bình đồ không có tuyến thứ 2 chưa lên trắc dọc này.
- Chiều dài theo **khoảng cách giếng thu**; xác nhận tim–tim hay thông thủy.
- Độ dốc có 27 giá trị / 29 đoạn (TP113) — 2 đoạn cần xác nhận.
- Chiều sâu đào tính từ **cao độ tự nhiên**; nếu thi công sau khi đào/đắp nền thì đổi mốc.
- Mã hiệu định mức, đơn giá, thành tiền: `[Chờ bổ sung]` (anh áp trên F1).
- Kết cấu giếng thu (bê tông, xây, nắp gang, lưới chắn rác): `[Chờ bổ sung]` — cần bản vẽ chi tiết.

# 02i — v7: bảng đào hầm ga theo cột anh yêu cầu

File: `ket-qua/03_demo-doi-agent/KL-thoat-nuoc-tonghop_demo_v7.xlsx`.

## Cột sheet "Dao dap ho ga" (đúng thứ tự anh yêu cầu)
STT · Tên hầm ga · Loại hầm ga · Cao độ đỉnh hầm ga · **Cao độ tự nhiên** (chèn giữa đỉnh và đáy cống) · Cao độ đáy cống · Chiều rộng lòng trong HG · **Chiều rộng lớp BT lót** (thay cho "chiều rộng khuôn") · Bphui đào HG · Cao độ đáy hầm ga · Chiều sâu đào HG · V đào HG · Thép hầm ga · DT cừ tràm · (O mm – cột phụ để công thức IF).

## Số liệu đọc từ chi tiết hầm ga (file 10)
- Lòng trong: D400 0,80 m / D600 1,00 m; vách thân 0,20 m.
- **Chiều rộng lớp BT lót = lòng + 2·vách + 2·0,20** (lót mở rộng 0,20 mỗi bên, khớp DIM 1800 cho D600): D400 **1,60 m** / D600 **1,80 m**.
- Bphui đào = chiều rộng lót + 2·a (a=0,30): D400 **2,20 m** / D600 **2,40 m**.
- Cát đệm 0,20 m; BT lót M150 0,10 m; bản đáy hầm ga 0,30 m (ô vàng – cần xác nhận).
- Cao độ đáy hầm ga = cao độ đáy cống − hố lắng (0,30 m).

## Công thức chiều sâu đào (làm đúng như anh ghi)
`Chiều sâu đào = Cao độ tự nhiên − Cao độ đáy hầm ga − dày bản đáy − dày BT lót − dày cát đệm`
- Kết quả: min 0,09 / TB 0,52 / max 0,96 m.
- V đào hầm ga = Bphui² × chiều sâu đào. Tổng ≈ 82,7 m³.

## CẦN ANH XÁC NHẬN
- **Dấu của các lớp trong công thức chiều sâu:** đang **trừ** (theo anh ghi) → đáy đào nông hơn đáy hầm ga. Nếu ý anh là đào **sâu hơn** đáy hầm ga (cộng dày bản đáy + BT lót + cát đệm) thì chiều sâu sẽ lớn hơn, em đổi dấu ngay.
- Chiều dày bản đáy hầm ga (ô B18, đang 0,30 m).
- Hố lắng dưới đáy cống (ô B9, đang 0,30 m) — nếu đáy hầm ga = đáy cống thì để 0.

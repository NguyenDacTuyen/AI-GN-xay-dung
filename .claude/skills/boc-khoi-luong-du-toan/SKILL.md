---
name: boc-khoi-luong-du-toan
description: Bóc tách khối lượng từ bản vẽ (DWG, DXF, PDF) và lập dự toán, tổng mức đầu tư, bảng khối lượng mời thầu, bảng so sánh giá thầu vật tư theo định mức, đơn giá Việt Nam, xuất file Excel. Dùng khi anh Tuyên yêu cầu bóc khối lượng, tính khối lượng, thống kê vật tư, lập dự toán, áp mã hiệu định mức, tra đơn giá, giá vật liệu, so sánh báo giá vật tư.
---

# Bóc khối lượng và dự toán

Phạm vi:
- **Bóc khối lượng:** đọc bản vẽ DWG/DXF để bóc tách khối lượng và vật tư.
- **Dự toán, tổng mức đầu tư:** lập dự toán, tổng mức, bảng so sánh giá thầu vật tư.

Luôn tuân thủ mục **"Định mức, đơn giá và văn bản pháp lý"** trong CLAUDE.md: ghi rõ nguồn, kiểm tra hiệu lực văn bản, không tự bịa mã hiệu định mức hay đơn giá.

Nếu cần đọc bản vẽ CAD bằng code thì dùng thêm skill `gn-banvecad-isocty` để biết layer và đơn vị của template công ty. Nếu việc là **thẩm tra** dự toán của người khác thì dùng skill `tham-tra`.

## Quy tắc bóc khối lượng và dự toán

- Kết quả xuất ra **file Excel** (.xlsx), gồm các cột:
  `STT | Mã hiệu định mức | Tên công việc / vật tư | Đơn vị | Diễn giải cách tính | Khối lượng | Ghi chú`
- Phần **diễn giải cách tính** phải ghi rõ để anh kiểm tra lại được, ví dụ: `2 x (10,5 x 0,3 x 0,5)`.
- Trong Excel, dùng **công thức** thay vì nhập sẵn con số, để anh dễ kiểm tra và sửa.
- Đơn vị dùng theo thông lệ dự toán: m, m², m³, tấn, kg, cái, bộ...
- Sắp xếp theo hạng mục công trình, giống bảng khối lượng mời thầu thông thường.
- Nếu bản vẽ thiếu số liệu hoặc không rõ thì **liệt kê ra để hỏi**, không tự đoán.

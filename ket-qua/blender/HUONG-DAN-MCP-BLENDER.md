# Hướng dẫn dùng MCP Blender (vn-mcp-blender)

Ngày cài: 30/10/2026. Nguồn: https://github.com/andyluu98/vn-mcp-blender (bản 0.1.0)

## Đã cài những gì

| Thành phần | Vị trí |
|---|---|
| Chương trình MCP (Python riêng, không đụng Python chung của máy) | `C:\Users\Desktop\mcp\vn-mcp-blender\` |
| Add-on trong Blender 5.2 | `%APPDATA%\Blender Foundation\Blender\5.2\scripts\addons\mcp_xaydung_addon.py` |
| Khai báo cho Claude | `.mcp.json` của dự án, mục `blender` (mục `autocad` giữ nguyên) |

Claude nói chuyện với Blender qua cổng **9877** trên chính máy anh, không gửi dữ liệu ra ngoài.

## Mỗi lần làm việc (3 bước)

1. Mở Blender.
2. Đưa chuột vào khung nhìn 3D, bấm phím **N** → chọn tab dọc **MCP Xây Dựng** → bấm **Bật kết nối**.
   Thấy dòng "Đang chạy ở cổng 9877" là được.
3. Mở Claude, gõ thử: *"kiểm tra kết nối Blender"*.

Lưu ý: bật add-on trong Preferences **chưa đủ**, phải bấm thêm nút **Bật kết nối** ở bước 2. Đây là bước hay quên nhất.
Chỉ mở **một** cửa sổ Blender, vì chỉ một cửa sổ giữ được cổng 9877.

## Khi Claude báo "Không nối được tới Blender"

1. Blender có đang mở không?
2. `Edit > Preferences > Add-ons`, gõ "MCP": dòng **MCP Xây Dựng** đã tích chưa?
3. Đã bấm **Bật kết nối** chưa?
4. Vẫn không được: tắt Blender, mở lại, làm lại bước 2.

## Mô hình mẫu nhà cấp 4 (file `nha-cap4-test-5x12m.blend`)

Kích thước giả định để test:

- Nhà 1 tầng, 5,0 x 12,0 m tính theo tim tường
- Tường bao 200, tường ngăn 100, cao tường 3,6 m tính từ mặt nền
- Nền cos +0,45 so với sân; 2 bậc tam cấp, mỗi bậc 150
- Mái tôn 2 mái, nóc chạy dọc nhà, dốc 30%, vươn 600 hai bên, 500 hai đầu hồi; có tường thu hồi hai đầu
- Mặt bằng: phòng khách 4,5 m (trước), phòng ngủ 3,8 x 3,5 m, hành lang ~1,1 m bên phải, bếp và WC phía sau
- Cửa đi chính 1,4 x 2,4 m; cửa sau 0,9 x 2,2; cửa phòng ngủ 0,9 x 2,2; cửa WC 0,75 x 2,1
- Cửa sổ 1,2 (1,4) x 1,5 m bệ 0,9; cửa sổ bếp 1,2 x 1,2 bệ 1,1; cửa sổ WC 0,6 x 0,6 bệ 1,6

Ảnh phối cảnh: `nha-cap4-test-5x12m_phoi-canh.png`.

Khối lượng tool tự bóc chỉ để thử: nó tính cả khối nền tôn cao 0,45 và lớp sân vào "bê tông", nên **không dùng cho dự toán**.

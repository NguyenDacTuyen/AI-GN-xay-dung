# CLAUDE.md – Dự án AI_Cad_K1

Thông tin về anh Tuyên, cách trả lời, nguyên tắc chung, định mức, văn bản pháp lý và biện pháp thi công nằm trong **CLAUDE.md global** (`C:\Users\Desktop\.claude\CLAUDE.md`), áp dụng cho mọi dự án. File này chỉ ghi phần riêng của dự án `AI_Cad_K1`.

## Mục đích thư mục này

Dùng AI để hỗ trợ công việc xây dựng hằng ngày:

1. **Tự động hóa AutoCAD:** viết AutoLISP và Python để vẽ, sửa, thống kê bản vẽ
2. **Bóc khối lượng:** đọc bản vẽ DWG/DXF để bóc tách khối lượng và vật tư
3. **Dự toán, tổng mức đầu tư:** lập dự toán, tổng mức, bảng so sánh giá thầu vật tư
4. **Biện pháp thi công:** soạn thuyết minh và hỗ trợ bản vẽ biện pháp thi công
5. **Thẩm tra:** thẩm tra hồ sơ thiết kế bản vẽ thi công và dự toán

## Skill theo từng lĩnh vực

Quy tắc chi tiết của từng lĩnh vực nằm trong các skill ở thư mục `.claude/skills/`. Claude tự mở skill khi việc khớp lĩnh vực; anh cũng có thể gọi thẳng bằng `/tên-skill`.

| Skill | Dùng cho |
|---|---|
| `/gn-banvecad-isocty` | Vẽ, sửa, kiểm tra bản vẽ thi công trên AutoCAD theo template ISO_CTY.dwt; viết LISP/Python cho AutoCAD; vẽ trực tiếp qua MCP `autocad`; khung tên, Layout, layer, style, in PDF |
| `/gn-dutoan` | Bóc khối lượng, lập dự toán, tổng mức đầu tư, bảng khối lượng mời thầu, so sánh giá vật tư, xuất Excel |
| `/tham-tra` | Thẩm tra thiết kế và dự toán: ý kiến TK/DT mức A/B/C, báo cáo kết quả thẩm tra theo mẫu công ty |

Khi thêm lĩnh vực mới: tạo skill mới trong `.claude/skills/`, rồi thêm một dòng vào bảng này. Không viết thêm quy tắc chi tiết vào CLAUDE.md.

## Tổ chức thư mục (đề xuất)

```
AI_Cad_K1/
├── CLAUDE.md          ← file này (chỉ phần riêng của dự án)
├── .claude/skills/    ← quy tắc chi tiết theo lĩnh vực
│   ├── gn-banvecad-isocty/      SKILL.md + template-ISO_CTY.md (bảng layer, style, khung tên, Layout) + mcp-autocad.md (vẽ qua MCP)
│   ├── gn-dutoan/               SKILL.md + mau-hang-muc-chung.md + 3 file mẫu theo lĩnh vực + mau-tong-hop.md
│   └── tham-tra/                SKILL.md + mau-bao-cao.md (bố cục mẫu báo cáo, căn cứ pháp lý)
├── template/          ← mẫu công ty, chỉ đọc, không sửa: ISO_CTY.dwt, 1.2 Bao cao tham tra (sua).docx
│   └── du-toan/       ← mẫu dự toán Excel: dan-dung-cong-nghiep/, ha-tang-ky-thuat/, giao-thong/, tong-hop/
├── lisp/              ← các file AutoLISP (.lsp)
├── python/            ← các file Python (.py)
├── ban-ve/            ← bản vẽ đầu vào (DWG/DXF), chỉ đọc, không sửa
├── ket-qua/           ← file Excel, Word xuất ra
├── tham-tra/          ← mỗi dự án thẩm tra 1 thư mục con: dau-vao/ (hồ sơ nhận, chỉ đọc) và ket-qua/
├── tai-lieu/          ← định mức, đơn giá, tiêu chuẩn tham khảo
└── _luu-tru/          ← bản sao lưu cũ (CLAUDE.md trước khi tách skill, trước khi tách global)
```

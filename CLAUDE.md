# CLAUDE.md – Dự án AI_Cad_K1

## Về người dùng

- **Tên:** Nguyễn Đắc Tuyên, Kỹ sư xây dựng, 15 năm kinh nghiệm
- **Công ty:** Công ty Cổ phần Đầu tư Xây dựng Gia Nguyễn
- **Loại công trình:** nhà xưởng, hạ tầng kỹ thuật (san nền, thoát nước, cấp nước...), đường giao thông
- **Phụ trách:** thiết kế bản vẽ thi công, lập dự toán và tổng mức đầu tư, thầu vật tư, bóc tách khối lượng, thiết kế biện pháp thi công
- **Khu vực công trình:** chủ yếu **miền Nam**
- **Lập trình:** **mới bắt đầu.** Anh rất vững chuyên môn xây dựng nhưng chưa quen lập trình.

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
| `/gn-banvecad-isocty` | Vẽ, sửa, kiểm tra bản vẽ thi công trên AutoCAD theo template ISO_CTY.dwt; viết LISP/Python cho AutoCAD; khung tên, Layout, layer, style, in PDF |
| `/boc-khoi-luong-du-toan` | Bóc khối lượng, lập dự toán, tổng mức đầu tư, bảng khối lượng mời thầu, so sánh giá vật tư, xuất Excel |
| `/tham-tra` | Thẩm tra thiết kế và dự toán: ý kiến TK/DT mức A/B/C, báo cáo kết quả thẩm tra theo mẫu công ty |

Khi thêm lĩnh vực mới: tạo skill mới trong `.claude/skills/`, rồi thêm một dòng vào bảng này. Không viết thêm quy tắc chi tiết vào CLAUDE.md.

## Phần mềm đang dùng

- **AutoCAD 2025** / Civil 3D
- **Excel**
- Phần mềm dự toán (G8, Eta, Delta, Acitt...)
- Revit / Tekla / SAP2000

## Cách trả lời

- Luôn trả lời bằng **tiếng Việt**, dùng đúng thuật ngữ ngành xây dựng Việt Nam.
- Không cần giải thích kiến thức xây dựng cơ bản, vì anh là kỹ sư có kinh nghiệm.
- **Phần lập trình thì phải giải thích đơn giản, từng bước một**, vì anh mới bắt đầu học:
  - Nói rõ code dùng để làm gì trước khi đưa code.
  - Hướng dẫn cụ thể cách chạy (ví dụ: gõ `APPLOAD` để nạp file `.lsp`, rồi gõ tên lệnh).
  - Tránh dùng từ chuyên môn lập trình. Nếu buộc phải dùng thì giải thích ngắn gọn.

## Nguyên tắc chung cho mọi việc

- **Không bao giờ sửa hoặc ghi đè file gốc** (bản vẽ, hồ sơ nhận về, file mẫu trong `template/`). Chỉ làm trên bản sao.
- Chỗ nào thiếu số liệu hoặc không rõ thì **hỏi lại**, không tự đoán.

## Định mức, đơn giá và văn bản pháp lý

- **Luôn ghi rõ nguồn:** số hiệu văn bản (Nghị định, Thông tư, Quyết định), mã hiệu định mức, tiêu chuẩn (TCVN, TCXDVN).
- Khu vực chủ yếu là **miền Nam**, nên ưu tiên đơn giá, giá vật liệu và công bố giá của các tỉnh, thành phía Nam.
- Văn bản pháp lý về xây dựng **thay đổi thường xuyên**, và địa giới các tỉnh, thành đã được sắp xếp lại từ năm 2025. Vì vậy:
  - Luôn **nhắc anh kiểm tra văn bản còn hiệu lực** trước khi dùng.
  - Nếu không chắc một văn bản còn hiệu lực hay không thì nói rõ là không chắc, không khẳng định.
- Không tự bịa mã hiệu định mức hay đơn giá. Nếu không có số liệu chính xác thì để trống và ghi chú "cần tra cứu".

## Biện pháp thi công

- Thuyết minh viết theo văn phong hồ sơ kỹ thuật, có các mục: căn cứ, trình tự thi công, biện pháp an toàn, kiểm tra chất lượng.
- Bám sát điều kiện thực tế của nhà xưởng, hạ tầng và đường giao thông ở miền Nam: nền đất yếu, mùa mưa, mực nước ngầm cao...
- Nếu cần tạo file Word thì dùng định dạng .docx.

## Tổ chức thư mục (đề xuất)

```
AI_Cad_K1/
├── CLAUDE.md          ← file này (chỉ thông tin chung)
├── .claude/skills/    ← quy tắc chi tiết theo lĩnh vực
│   ├── gn-banvecad-isocty/      SKILL.md + template-ISO_CTY.md (bảng layer, style, khung tên, Layout)
│   ├── boc-khoi-luong-du-toan/  SKILL.md
│   └── tham-tra/                SKILL.md + mau-bao-cao.md (bố cục mẫu báo cáo, căn cứ pháp lý)
├── template/          ← mẫu công ty, chỉ đọc, không sửa: ISO_CTY.dwt, 1.2 Bao cao tham tra (sua).docx
├── lisp/              ← các file AutoLISP (.lsp)
├── python/            ← các file Python (.py)
├── ban-ve/            ← bản vẽ đầu vào (DWG/DXF), chỉ đọc, không sửa
├── ket-qua/           ← file Excel, Word xuất ra
├── tham-tra/          ← mỗi dự án thẩm tra 1 thư mục con: dau-vao/ (hồ sơ nhận, chỉ đọc) và ket-qua/
├── tai-lieu/          ← định mức, đơn giá, tiêu chuẩn tham khảo
└── _luu-tru/          ← bản sao lưu cũ (CLAUDE.md trước khi tách skill)
```

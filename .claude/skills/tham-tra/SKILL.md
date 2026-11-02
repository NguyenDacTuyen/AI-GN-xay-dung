---
name: tham-tra
description: Thẩm tra hồ sơ thiết kế bản vẽ thi công và thẩm tra dự toán xây dựng theo quy định Việt Nam, gồm thẩm tra độc lập cho chủ đầu tư và kiểm tra nội bộ hồ sơ của Gia Nguyễn. Dùng khi anh Tuyên yêu cầu thẩm tra, soát xét, kiểm tra hồ sơ thiết kế, kiểm tra dự toán, đối chiếu quy chuẩn tiêu chuẩn, viết ý kiến thẩm tra (TK-xx, DT-xx, mức A/B/C), lập báo cáo kết quả thẩm tra, bảng so sánh dự toán, ghi chú đám mây REVCLOUD trên bản vẽ, thẩm tra dự án nhiều hạng mục và tổng hợp các hạng mục thành báo cáo chung.
---

# Thẩm tra hồ sơ thiết kế và dự toán

Khi soạn **báo cáo kết quả thẩm tra (Word)**: đọc file **`mau-bao-cao.md`** (cùng thư mục với skill này) trước. File đó có định dạng, phần mở đầu, bố cục 6 phần (I–VI), danh mục căn cứ pháp lý và các lỗi đã biết của file mẫu.

Skill liên quan: `gn-banvecad-isocty` (ghi chú trên file CAD, kiểm tra thể hiện bản vẽ), `gn-dutoan` (bóc lại khối lượng).

Dự án có **nhiều hạng mục** (mỗi hạng mục có bản vẽ, dự toán riêng): làm theo mục **"Dự án nhiều hạng mục"** ở cuối file này.

### Vai trò và trách nhiệm
- Anh làm cả hai việc: **thẩm tra độc lập** (kiểm tra hồ sơ do đơn vị khác lập, theo hợp đồng với chủ đầu tư) và **kiểm tra nội bộ** (kiểm tra hồ sơ của Gia Nguyễn trước khi nộp). Đầu mỗi việc, hỏi rõ đang làm việc nào.
  - **Thẩm tra độc lập:** văn phong khách quan, trung lập. Ý kiến nào cũng phải có căn cứ.
  - **Kiểm tra nội bộ:** có thể nói thẳng, ngắn gọn, tập trung vào lỗi cần sửa trước khi nộp.
- Claude chỉ **soạn dự thảo** ý kiến và báo cáo. **Kết luận cuối cùng do anh quyết định và ký.** Claude không tự kết luận "đủ điều kiện" hay "không đủ điều kiện" thay anh.
- Chỗ nào Claude không chắc (số liệu thiếu, bản vẽ không rõ, cách hiểu tiêu chuẩn chưa thống nhất) thì ghi rõ là **"cần anh xác nhận"**. Không được đoán rồi viết như đã chắc chắn.

### Căn cứ pháp lý, quy chuẩn, tiêu chuẩn
- Kiểm tra sự tuân thủ **luật, nghị định, thông tư, quy chuẩn (QCVN) và tiêu chuẩn (TCVN) hiện hành** về xây dựng, quản lý chi phí, đầu tư công, PCCC, môi trường.
- Hệ thống văn bản thay đổi thường xuyên: luật xây dựng và các nghị định hướng dẫn liên tục được sửa đổi, các tỉnh đã sáp nhập từ năm 2025. Vì vậy, **trước khi ghi căn cứ vào ý kiến hoặc báo cáo**:
  1. Tra cứu tình trạng hiệu lực của văn bản (dùng WebSearch nếu có).
  2. Ghi đủ số hiệu, tên văn bản, và **điều, khoản** cụ thể làm căn cứ.
  3. Nếu không tra được thì ghi **"cần kiểm tra hiệu lực"** ngay bên cạnh văn bản đó.
- Xác định văn bản áp dụng theo **thời điểm lập và phê duyệt hồ sơ**. Nếu dự án chuyển tiếp giữa văn bản cũ và mới thì nêu rõ để anh quyết.

### Nguồn vốn quyết định mức độ bắt buộc
Đầu mỗi dự án, hỏi **nguồn vốn**:
- **Vốn đầu tư công** và **vốn nhà nước ngoài đầu tư công:** phải tuân thủ chặt quy định quản lý chi phí của nhà nước (phương pháp lập, định mức, giá, các khoản chi phí). Sai quy định thì xếp mức **A**.
- **Vốn tư nhân** (nhà xưởng, KCN...): chủ đầu tư được tự quyết nhiều hơn. Định mức và đơn giá nhà nước dùng để **tham khảo, so sánh**. Chênh lệch so với quy định thường là mức **B** hoặc **C**, trừ khi vi phạm quy chuẩn hoặc an toàn.

### Thẩm tra bản vẽ thi công: nội dung kiểm tra
1. **Phù hợp với bước thiết kế trước:** so với thiết kế cơ sở, BCKTKT hoặc thiết kế kỹ thuật đã duyệt, về quy mô, công năng, giải pháp kết cấu, vật liệu chính, cao độ, tọa độ. Thay đổi nào cũng phải nêu ra.
2. **Tuân thủ quy chuẩn, tiêu chuẩn:** cấu tạo, kích thước tối thiểu, lớp bê tông bảo vệ, neo và nối cốt thép, độ dốc, PCCC (nhà xưởng), an toàn giao thông, thoát nước...
3. **Kiểm tra tính toán:**
   - Tải trọng và tổ hợp, nội lực, tiết diện, cốt thép, móng và nền (đặc biệt là nền đất yếu ở miền Nam), kết cấu áo đường, thủy lực thoát nước.
   - Claude **tính kiểm tra lại các cấu kiện chính** bằng công thức theo TCVN, trình bày đủ công thức, số liệu đầu vào, kết quả và **so sánh với hồ sơ**. Không thay thế phần mềm tính kết cấu. Giả thiết nào tự đặt ra thì phải ghi rõ.
4. **Thống nhất hồ sơ:** khớp giữa các bộ môn (kiến trúc, kết cấu, điện nước, hạ tầng), giữa mặt bằng, mặt cắt và chi tiết, giữa bản vẽ và thuyết minh, và giữa bảng thống kê thép với hình vẽ.
5. **Thể hiện bản vẽ:** khung tên, số hiệu, tỷ lệ, ghi chú vật liệu, cấp bê tông, mác thép, chỉ dẫn kỹ thuật.

### Thẩm tra dự toán: nội dung kiểm tra
1. **Khối lượng:** bóc lại từ bản vẽ, so với bảng khối lượng của dự toán. **Nêu mọi chênh lệch**, kể cả sai số nhỏ, kèm diễn giải cách tính của cả hai bên. Phát hiện chỗ tính trùng, tính thiếu, sai đơn vị.
2. **Định mức:** đúng mã hiệu, đúng điều kiện thi công (cự ly, độ sâu, chiều cao, loại đất, biện pháp), đúng hệ số điều chỉnh. Định mức vận dụng hoặc định mức mới phải có cơ sở.
3. **Giá vật liệu, nhân công, máy:**
   - Ưu tiên **công bố giá của Sở Xây dựng tỉnh, thành nơi xây dựng**, tại thời điểm lập dự toán. Từ năm 2025, dùng công bố giá của tỉnh, thành sau sáp nhập.
   - Vật liệu không có trong công bố giá thì dùng **báo giá thị trường** (thường từ 3 báo giá). Ghi rõ nguồn, ngày báo giá, và đã gồm hay chưa gồm VAT và vận chuyển.
   - Kiểm tra cự ly và chi phí vận chuyển đến chân công trình.
4. **Các khoản chi phí:** chi phí trực tiếp, chi phí gián tiếp (chi phí chung, lán trại, hạng mục không xác định được khối lượng...), thu nhập chịu thuế tính trước, VAT (kiểm tra thuế suất áp dụng tại thời điểm lập), dự phòng (khối lượng và trượt giá), chi phí tư vấn và chi phí khác nếu có.
5. **Lỗi trong file Excel:** số gõ tay thay cho công thức, công thức tham chiếu sai ô, dòng bị ẩn, tổng không khớp giữa các sheet (tổng hợp, chi tiết, vật tư).

### File đầu vào
- Dự toán: thường là **Excel xuất từ phần mềm dự toán** (G8, Eta, Delta, Acitt...). Đọc đủ các sheet: tổng hợp kinh phí, dự toán chi tiết, phân tích đơn giá, tổng hợp vật tư, giá vật liệu.
- Nếu anh chỉ có file gốc của phần mềm dự toán thì nhờ anh **xuất ra Excel** trước.
- Hồ sơ đầu vào chỉ đọc, **không sửa file gốc**.

### Phân loại ý kiến: 3 mức

| Mức | Tên | Khi nào dùng |
|---|---|---|
| **A** | **Bắt buộc sửa** | Vi phạm quy chuẩn, luật, nghị định; sai tính toán ảnh hưởng an toàn chịu lực; sai khối lượng hoặc giá làm thay đổi đáng kể giá trị; trái thiết kế bước trước đã duyệt |
| **B** | **Kiến nghị sửa** | Chưa tối ưu, chưa phù hợp tiêu chuẩn khuyến khích áp dụng, chênh lệch khối lượng hoặc giá cần điều chỉnh |
| **C** | **Lưu ý, làm rõ** | Thiếu thông tin, thể hiện chưa rõ, cần đơn vị thiết kế giải trình hoặc bổ sung |

Mỗi ý kiến phải có đủ 5 nội dung: **vị trí** (số hiệu bản vẽ hoặc mã công tác), **nội dung**, **căn cứ** (văn bản, điều khoản), **mức độ** (A/B/C), **đề xuất xử lý**.

### Kết quả xuất ra
1. **Báo cáo kết quả thẩm tra (Word .docx):** theo **mẫu của Gia Nguyễn** (xem file `mau-bao-cao.md`).
2. **Bảng tổng hợp ý kiến (Excel, chỉ dùng nội bộ để theo dõi phản hồi, không đính kèm báo cáo):**
   `STT | Bản vẽ / Hạng mục | Nội dung ý kiến | Căn cứ | Mức độ (A/B/C) | Đề xuất xử lý | Phản hồi của đơn vị thiết kế | Ý kiến sau phản hồi`
3. **Bảng so sánh dự toán (Excel):**
   `STT | Mã hiệu | Nội dung công tác | Đơn vị | KL đề nghị | KL thẩm tra | Đơn giá đề nghị | Đơn giá thẩm tra | Thành tiền đề nghị | Thành tiền thẩm tra | Tăng (+) / Giảm (−) | Lý do`
   Có dòng tổng theo từng hạng mục và tổng cộng. Dùng công thức Excel để anh tự kiểm tra lại được.
4. **Ghi chú trên bản vẽ (CAD):**
   - Chỉ làm trên **bản sao** của file. Khoanh **đám mây (REVCLOUD)** vào chỗ có ý kiến, ghi số thứ tự ý kiến trùng với bảng tổng hợp.
   - Riêng file ghi chú thẩm tra được tạo thêm layer **`TT_YKIEN`** (màu 1, đỏ) để chứa đám mây và ghi chú. Đây là ngoại lệ duy nhất cho quy tắc "không tạo layer mới".


### Quy tắc khi soạn báo cáo từ mẫu
- Nội dung trong mẫu là của dự án cũ. Phải thay **toàn bộ**: tên dự án (cả trong header), chủ đầu tư, số báo cáo, ngày, số liệu, nhà thầu, văn bản của dự án.
- ⚠️ Các phần V đến VIII trong mẫu viết sẵn toàn câu kết luận tốt ("phù hợp", "Không yêu cầu", "đủ điều kiện"). **Không được giữ nguyên các câu này.** Chỉ ghi "phù hợp" cho tiểu mục nào **đã thực sự kiểm tra và không có ý kiến**. Kết luận ở mục VIII do anh quyết định.

**Cách ghi ý kiến thẩm tra trong báo cáo** (anh chốt ngày 17/10/2026: **không dùng phụ lục**)
- Ý kiến chi tiết ghi **trực tiếp trong mục VI (thiết kế) và VII (dự toán)**, đặt ngay dưới tiểu mục liên quan.
- **Đánh số ý kiến:**
  - Thiết kế: `TK-01`, `TK-02`...
  - Dự toán: `DT-01`, `DT-02`...
  - Số ý kiến tăng liên tục trong cả báo cáo, và phải **trùng** với số ghi trên đám mây trong file CAD và số trong bảng Excel theo dõi.
  - **Dự án nhiều hạng mục** (anh chốt ngày 18/10/2026, cách A): thêm mã hạng mục vào giữa, `TK-<mã>-NN` và `DT-<mã>-NN`, ví dụ `TK-HQ-01`, `DT-SN-03`. Mỗi hạng mục đánh số riêng từ 01. Mã hạng mục lấy theo phiếu thông tin dự án. Mã `TH` dùng cho ý kiến về phần chung và ý kiến liên hạng mục.
- **Mỗi ý kiến viết thành một khối** theo mẫu sau. Dòng đầu in đậm, các dòng sau dùng gạch đầu dòng cấp 1:
  > **TK-01 – Mức A (Bắt buộc sửa) – Bản vẽ GN2026-KC-03, dầm trục 2–3:**
  > - Nội dung: ...
  > - Căn cứ: <văn bản / tiêu chuẩn>, điều ..., khoản ...
  > - Đề xuất: ...
- **Vị trí đặt ý kiến trong mục VI (thiết kế):**
  - VI.1: ý kiến về sự phù hợp với bước thiết kế trước.
  - VI.2: ý kiến về quy chuẩn, tiêu chuẩn, vật liệu.
  - VI.3: ý kiến về an toàn chịu lực và an toàn công trình lân cận, gồm cả kết quả tính kiểm tra.
  - VI.4: ý kiến về dây chuyền công nghệ (nếu có).
  - VI.5 "Yêu cầu hoàn thiện hồ sơ": **tổng hợp** số ý kiến theo từng mức (A, B, C), và liệt kê các ý kiến mức A bắt buộc sửa trước khi trình thẩm định.
- **Vị trí đặt ý kiến trong mục VII (dự toán):**
  - VII.1.1 đến VII.1.3: ý kiến về căn cứ pháp lý, sự phù hợp với tổng mức đầu tư, phương pháp lập.
  - VII.1.4: ý kiến về khối lượng, định mức, đơn giá, các khoản chi phí. Kèm thêm **bảng các công tác có chênh lệch**:
    `STT | Mã hiệu | Nội dung công tác | Đơn vị | KL đề nghị | KL thẩm tra | Đơn giá đề nghị | Đơn giá thẩm tra | Thành tiền đề nghị | Thành tiền thẩm tra | Tăng (+) / Giảm (−) | Ý kiến số`
    Nêu **mọi chênh lệch**. Bảng chỉ gồm các công tác có chênh lệch, các công tác khớp thì không đưa vào.
  - VII.2: bảng tổng hợp giá trị theo khoản mục chi phí (như trong mẫu). Số tăng giảm phải khớp với tổng của các bảng ở VII.1.4.
- Tiểu mục nào không có ý kiến thì ghi một câu kết luận ngắn, ví dụ "Phù hợp, không có ý kiến."
- **Bảng tổng hợp ý kiến (Excel)** vẫn lập, nhưng chỉ để **theo dõi nội bộ** phản hồi của đơn vị thiết kế qua các lần sửa. Bảng này **không đính kèm** báo cáo. Nội dung ý kiến trong Excel và trong báo cáo phải giống nhau. Vì số liệu thay đổi theo từng dự án, **mỗi dự án lập một file Excel riêng**, lưu tại `tham-tra/<tên dự án>/ket-qua/` (anh xác nhận ngày 17/10/2026).
- Danh sách căn cứ và bảng tiêu chuẩn phải chọn lại theo **loại công trình**. Mẫu đang dùng cho đường giao thông; với nhà xưởng thì bổ sung nhóm kết cấu thép, nền móng, PCCC (QCVN 06), điện, cấp thoát nước công trình. Kiểm tra hiệu lực từng văn bản.
- Thuế VAT trong mẫu ghi 8% (theo chính sách giảm thuế có thời hạn). Kiểm tra thuế suất áp dụng tại thời điểm lập dự toán.
- Người ký và số chứng chỉ: **hỏi anh** chủ trì từng bộ môn của dự án là ai. Không tự lấy theo mẫu.

### Dự án nhiều hạng mục
Anh chốt ngày 18/10/2026: **chép hồ sơ một lần, thẩm tra từng hạng mục, rồi tổng hợp ra một báo cáo chung cho toàn dự án.** Không thẩm tra tất cả hạng mục trong một lượt, vì dễ sót lỗi.

**Cấu trúc thư mục**
```
tham-tra/<tên dự án>/
├── dau-vao/
│   ├── 00-chung/                ← thuyết minh chung, dự toán tổng hợp, quyết định, TMĐT, hợp đồng
│   └── NN-<hạng mục>/
│       ├── ban-ve/
│       └── du-toan/
└── ket-qua/
    ├── thong-tin-du-an.md       ← phiếu thông tin dự án, dùng chung cho mọi hạng mục
    ├── NN-<hạng mục>/           ← kết quả từng hạng mục
    └── tong-hop/                ← kết quả tổng hợp và báo cáo Word chung
```

**Quy trình 6 bước**
1. **Chép hồ sơ:** anh chép một lần, theo đúng thư mục hạng mục.
2. **Đọc phần chung:** đọc `dau-vao/00-chung/`, điền **phiếu thông tin dự án** `ket-qua/thong-tin-du-an.md` (chủ đầu tư, nguồn vốn, cấp công trình, căn cứ, công bố giá, danh mục hạng mục và mã). Thông tin còn thiếu thì hỏi anh.
3. **Thẩm tra từng hạng mục:** mỗi lượt một hạng mục, **luôn đọc phiếu thông tin dự án trước**. Kết quả lưu vào `ket-qua/NN-<hạng mục>/`:
   - Bảng ý kiến (Excel) của hạng mục
   - Bảng so sánh dự toán (Excel) của hạng mục
   - Bản sao bản vẽ có đám mây ghi chú
   - Chỗ nào liên quan tới hạng mục khác (đấu nối, cao độ, khối lượng có thể trùng) thì ghi thêm vào mục "Điểm cần kiểm tra chéo" của phiếu thông tin dự án.
   - Làm xong thì cập nhật cột "Trạng thái" của hạng mục trong phiếu.
   - Có thể làm mỗi hạng mục ở **một phiên riêng, chạy song song**. Mỗi phiên **chỉ sửa thư mục kết quả của hạng mục mình** và đúng dòng của hạng mục mình trong phiếu.
4. **Anh duyệt từng hạng mục:** sửa, bỏ hoặc thêm ý kiến trước khi tổng hợp.
5. **Tổng hợp toàn dự án:** lưu vào `ket-qua/tong-hop/`:
   - Kiểm tra chéo giữa các hạng mục theo danh sách trong phiếu: đấu nối, cao độ (san nền, đường, hố ga, cống), khối lượng bị trùng hoặc bị sót giữa các hạng mục.
   - Cộng chi phí xây dựng sau thẩm tra của từng hạng mục, so với dự toán tổng hợp của hồ sơ.
   - Tính lại chi phí cấp dự án (QLDA, tư vấn, chi phí khác, dự phòng) theo chi phí xây dựng **sau** thẩm tra.
   - Đối chiếu thuyết minh chung với nội dung từng hạng mục.
   - Ý kiến phát sinh ở bước này đánh số `TK-TH-NN`, `DT-TH-NN`.
   - Lập **bảng ý kiến tổng hợp** và **bảng so sánh dự toán tổng hợp** (gộp từ các hạng mục, có dòng tổng theo từng hạng mục).
6. **Báo cáo Word chung** cho toàn dự án, theo `mau-bao-cao.md`:
   - Mục VI và VII: trong mỗi tiểu mục, ý kiến **xếp nhóm theo hạng mục** (tiêu đề nhỏ "Hạng mục 1: Nhà hội quán"...), ý kiến `TH` đặt cuối.
   - Mục VII.1.4: bảng các công tác có chênh lệch, **chia theo hạng mục**.
   - Mục VII.2: ngoài bảng theo khoản mục chi phí như mẫu, thêm **bảng chi phí xây dựng theo từng hạng mục** (đề nghị, thẩm tra, tăng giảm).
   - Mục VI.5: tổng hợp số ý kiến A/B/C **theo từng hạng mục**.

**Bảng Excel theo dõi ý kiến:** mỗi hạng mục một file trong thư mục của hạng mục, cộng thêm một file tổng hợp trong `tong-hop/`. Nội dung ý kiến phải giống nhau giữa file hạng mục, file tổng hợp và báo cáo.

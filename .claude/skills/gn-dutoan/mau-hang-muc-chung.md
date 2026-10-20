# Cấu trúc chung của mẫu dự toán hạng mục (tài liệu tra cứu của skill gn-dutoan)

Áp dụng cho cả 3 mẫu: dân dụng công nghiệp, hạ tầng kỹ thuật, giao thông. Đọc ngày 20/10/2026, **chỉ đọc các sheet đang hiện** (sheet ẩn không đọc, theo yêu cầu của anh).

Cả 3 mẫu là file Excel xuất từ phần mềm dự toán, nên có chung bố cục 4 sheet chính. Phần khác nhau giữa các lĩnh vực (tỷ lệ chi phí, sheet đi kèm, lỗi riêng) ghi trong file của từng lĩnh vực.

## Định dạng chung
- Khổ **A4 nằm ngang**. Lề trái khoảng 1,5–1,8 cm, lề phải 0,2–0,5 cm, lề trên khoảng 1 cm, lề dưới 1,2–1,6 cm.
- Chân trang giữa: **"Trang &P/&N"** (Trang x/y).
- Font **Times New Roman** toàn bộ:
  - Tên bảng 20 đậm, căn giữa.
  - Dòng "Công trình", "Hạng mục", "Địa điểm": 14 (hoặc 13) đậm, căn giữa, viết hoa.
  - Tiêu đề cột 11 đậm, căn giữa, gộp 2 dòng.
  - Nội dung 11.
- Định dạng số:
  - Tiền: `#,##0` (không số lẻ).
  - Khối lượng: `#,##0.0000` hoặc `0.000`.
  - Định mức: `0.000`.
- Nhiều cột trung gian của phần mềm được **ẩn khi in**. Khi lập file mới, **giữ nguyên các cột ẩn này**, chỉ quan tâm các cột hiện ghi dưới đây.

## Sheet 1: Bảng chi tiết khối lượng (tên sheet `cong trinh` hoặc `Công trình`)
- Dòng 1: **BẢNG CHI TIẾT KHỐI LƯỢNG CÔNG TÁC XÂY DỰNG**.
- Dòng 2 (nghiêng): "(Ban hành kèm theo Thông tư số ...)". Kiểm tra hiệu lực thông tư trước khi dùng.
- Dòng 3–5: CÔNG TRÌNH, HẠNG MỤC (nếu có), ĐỊA ĐIỂM.
- Tiêu đề cột 2 dòng. Các cột **hiện khi in**:

  | Cột | Nội dung | Rộng |
  |---|---|---|
  | A | STT | 5 |
  | C | Mã hiệu công tác (mã định mức) | 9–10 |
  | D | Danh mục công tác, và các dòng diễn giải khối lượng bên dưới | 52–57 |
  | E | Đơn vị | 8–9 |
  | L | Khối lượng | 8–9 |
  | O, P | Đơn giá nhân công, máy thi công | 10–11 |
  | S, T | Thành tiền nhân công, máy thi công | 12–14 |

- Cột ẩn quan trọng: M, N (đơn giá vật liệu, vật liệu phụ), Q, R (thành tiền vật liệu), X (bộ đơn giá áp dụng, ví dụ `DNA_2022_QD_39_SC_Vung1`), Y (định mức áp dụng, ví dụ `12/2021/TT-BXD`).
- **Nhóm công tác:** dòng tiêu đề nhóm in đậm ở cột D, đánh số `I)`, `I.1.`, `A.`, `1.`...
- **Mỗi công tác:**
  - Một dòng chính: STT, mã hiệu, tên công tác, đơn vị.
  - Ngay dưới là **các dòng diễn giải**: cột D ghi chữ dạng `58,8*0,25*2 = 29,4` (dấu phẩy thập phân), cột K ghi số kết quả. Có thể ghi tên bộ phận trước, ví dụ `Kho 11: 0,3*2*52,8*2 = 63,36`.
- **Công thức:**
  - `L = ROUND(SUM(K<dòng diễn giải đầu>:K<dòng cuối>),4)`.
  - `Q..T = ROUND(L*M..P,0)` (thành tiền = khối lượng × đơn giá, làm tròn đồng).
- **Dòng tổng cuối:** cột C ghi `THM`, cột D ghi **TỔNG HẠNG MỤC**, `Q..T = SUM(...)`.
- **Phần ký:** "Người thực hiện" (bên trái) và "Người chủ trì" (bên phải), kèm "Chứng chỉ hành nghề hoạt động xây dựng số ...", "Lĩnh vực hành nghề: Định giá xây dựng hạng ...". **Hỏi anh** tên và số chứng chỉ, không tự lấy theo mẫu.

## Sheet 2: Bảng phân tích vật tư (tên sheet `Phan tich vat tu` hoặc `Hao phí vật tư`)
- Dòng 1: **BẢNG PHÂN TÍCH VẬT TƯ**. Dòng 2–4 lấy từ sheet 1 bằng công thức (`='cong trinh'!A3`...).
- Cột hiện: A STT, B Mã hiệu, D Tên công tác hoặc vật tư (rộng 65–75), E Đơn vị, F Khối lượng thi công, G Định mức, I Vật tư.
- Mỗi công tác:
  - Một dòng lấy từ sheet 1 (STT, mã, tên, đơn vị, khối lượng `F = 'cong trinh'!L#`).
  - Bên dưới là 3 nhóm **"Vật liệu"**, **"Nhân công"**, **"Máy thi công"** (chữ nghiêng đậm).
  - Mỗi hao phí một dòng: mã, tên bắt đầu bằng `" - "`, đơn vị, định mức G, hệ số H, `I = ROUND(F*G*H,6)`.

## Sheet 3: Bảng tổng hợp vật liệu (tên sheet `vat tu` hoặc `Vật liệu`)
- Dòng 1: **BẢNG TỔNG HỢP VẬT LIỆU**. Mẫu hạ tầng và giao thông có thêm dòng 2 (nghiêng): "(Theo thông báo giá vật liệu xây dựng tháng ... năm ... của Sở Xây dựng ...)". Góc phải: "Đơn vị: đồng".
- Cột hiện: A STT, B Mã hiệu, E Tên vật tư, F Đơn vị, **H Nguồn mua** (ghi nguồn giá, ví dụ "Giá vật liệu tháng 6/2025 - Đồng Nai: ... (Xem trang ...)"), I Khối lượng, **Y Giá hiện trường**, **AD Thành tiền**.
- Cột ẩn: giá gốc, giá thông báo, cước ô tô, cước bộ, cước sông, % hao hụt vận chuyển, % hao hụt bảo quản, chênh lệch giá.
- **Công thức:**
  - Giá hiện trường `Y = M+P+R+T+X`, trong đó giá thông báo M cộng cước vận chuyển P, R, T, cộng hao hụt `X = ROUND((M+P+R+T)*(W+V),0)`.
  - Thành tiền `AD = ROUND(I*Y,0)`.
  - Mỗi vật tư có các dòng con lấy khối lượng từ sheet 2 (`='Phan tich vat tu'!I#`), dòng vật tư cộng lại bằng `SUM`.
  - Vật liệu khác tính theo %: `ROUND((AD#+AD#+...)*I#/100,2)`.
- **3 dòng tổng cuối:** "Cộng vật liệu chính", "Cộng vật liệu phụ", "Tổng vật liệu" (dùng `SUMIF`).
- **Ghi đủ nguồn giá** ở cột H cho từng vật tư (công bố giá tháng nào, tỉnh nào, trang nào, hoặc báo giá của đơn vị nào, ngày nào).

## Sheet 4: Bảng tổng hợp kinh phí hạng mục (tên sheet `Tong hop du toan`)
- Dòng 1: **BẢNG TỔNG HỢP KINH PHÍ HẠNG MỤC**. Dòng 2–4 lấy từ sheet 1.
- 5 cột: **STT | Khoản mục chi phí | Ký hiệu | Cách tính | Thành tiền**. Cột "Cách tính" ghi bằng công thức nối chữ, ví dụ `=C14&" x 6,2%"`.
- Bố cục khoản mục (tỷ lệ % của từng lĩnh vực xem file lĩnh vực):

  | STT | Khoản mục | Ký hiệu | Thành tiền lấy từ |
  |---|---|---|---|
  | I | CHI PHÍ TRỰC TIẾP | | |
  | 1 | Chi phí vật liệu | VL | Tổng vật liệu (sheet 3, cột AD) |
  | 2 | Chi phí nhân công | NC | Tổng hạng mục (sheet 1, cột S) |
  | 3 | Chi phí máy thi công | M | Tổng hạng mục (sheet 1, cột T) |
  | | Chi phí trực tiếp | T | VL + NC + M |
  | II | CHI PHÍ GIÁN TIẾP | | |
  | 1 | Chi phí chung | C | T × % |
  | 2 | Chi phí nhà tạm tại hiện trường để ở và điều hành thi công | LT | T × % |
  | 3 | Chi phí một số công tác không xác định được khối lượng từ thiết kế | TT | T × % |
  | | Chi phí gián tiếp | GT | C + LT + TT |
  | III | THU NHẬP CHỊU THUẾ TÍNH TRƯỚC | TL | (T + GT) × % |
  | | Chi phí xây dựng trước thuế | G | T + GT + TL |
  | IV | THUẾ GIÁ TRỊ GIA TĂNG | GTGT | G × % |
  | V | **CHI PHÍ XÂY DỰNG** | **Gxd** | G + GTGT |

- Mẫu hạ tầng và giao thông có thêm dòng **TỔNG DỰ TOÁN (Tdt) = Gxd**.
- Dưới bảng là dòng **"Bằng chữ: ..."**. Phải viết lại đúng theo số Gxd mới, không để chữ của dự án cũ.
- **Phần ký:** "... , ngày ... tháng ... năm ...", rồi "ĐƠN VỊ LẬP", "CÔNG TY CỔ PHẦN TƯ VẤN ĐẦU TƯ XÂY DỰNG GIA NGUYỄN", "GIÁM ĐỐC", rồi "NGƯỜI LẬP" kèm số chứng chỉ kỹ sư định giá. **Hỏi anh** tên người ký và số chứng chỉ.
- Theo cách A: file hạng mục **dừng ở Gxd**. Không tính QLDA, tư vấn, chi phí khác, dự phòng (các khoản này nằm trong file tổng hợp, xem `mau-tong-hop.md`).

## Quy tắc khi lập file mới từ mẫu
1. **Chép file mẫu** sang thư mục kết quả của dự án, đặt tên theo quy ước trong `SKILL.md`, rồi thay nội dung. **Không sửa file mẫu.**
2. Thay toàn bộ thông tin dự án cũ: tên công trình, hạng mục, địa điểm, nguồn giá, dòng bằng chữ, ngày tháng, người ký.
3. **Tỷ lệ chi phí chung, LT, TT, TL, VAT trong mẫu chỉ là của dự án cũ.** Phải xác định lại theo loại, quy mô công trình và văn bản hiện hành. Ghi căn cứ, nhắc anh kiểm tra.
4. Bộ đơn giá (cột X) và định mức (cột Y) phải đúng **tỉnh, thành nơi xây dựng** và văn bản còn hiệu lực.
5. Giữ đúng chuỗi liên kết công thức: sheet 1 → sheet 2 → sheet 3 → sheet 4. **Không gõ số tay** vào các ô đang là công thức.
6. Sau khi lập, kiểm tra:
   - Tổng vật liệu (sheet 3) khớp dòng VL (sheet 4).
   - Tổng nhân công, máy (sheet 1) khớp dòng NC, M (sheet 4).
   - Không còn ô lỗi `#REF!`, `#NAME?`, `#VALUE!`.

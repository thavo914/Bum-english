# 📖 Quy Trình (Workflow) Chuyển Đổi Tài Liệu & Đề Thi Từ PDF Sang Markdown

Tài liệu này hướng dẫn chi tiết quy trình số hóa và chuẩn hóa toàn bộ tài liệu ôn thi (PDF) sang định dạng Markdown chuẩn barem cho hai môn **Toán** và **Tiếng Anh** phục vụ lộ trình học tập của **Bum (14 tuổi)**.

---

## 🛠️ 1. Bản Đồ Công Cụ Sẵn Có Trong Thư Mục `/scripts`

| Kịch Bản Chuyển Đổi | Script Chuyên Dụng | Tính Năng Cốt Lõi |
| :--- | :--- | :--- |
| **Đề thi & Chuyên đề Toán** (chứa công thức, MathType) | [`scripts/format_math_exams.py`](format_math_exams.py) | • Dịch ký tự font MathType PUA (`\uf0b3` $\to \ge$, `\uf044` $\to \Delta$,...);<br>• Tự động ghép phân số, căn thức vào cú pháp LaTeX `$...$`;<br>• Đóng gói lời giải vào thẻ `<details><summary>`. |
| **Đề thi Tiếng Anh & Trắc nghiệm tổng hợp** | [`scripts/convert_exam_pdf_to_md.py`](convert_exam_pdf_to_md.py) | • Bóc tách câu hỏi, 4 phương án trắc nghiệm A-B-C-D;<br>• Tự động trích xuất hình ảnh (biển báo, poster) vào thư mục `images/`;<br>• Nhận diện bảng biểu tra cứu từ vựng & đáp án. |
| **Cập nhật ngân hàng câu hỏi Toán (Registry)** | [`scripts/build_math_registry.py`](build_math_registry.py) | • Quét toàn bộ file Markdown đề thi/chuyên đề trong kho;<br>• Phân loại dạng bài, điểm số và gắn nhãn độ khó **Level 1 đến 5**;<br>• Xuất dữ liệu ra `math-question-registry.json`. |
| **Tra cứu câu hỏi & Xuất đề luyện tập cho Bum** | [`scripts/query_math_registry.py`](query_math_registry.py) | • CLI lọc câu hỏi theo độ khó, dạng bài, từ khóa thực tế;<br>• Xuất file đề thi tự luyện tức thì theo cấp độ mong muốn. |

---

## ⚡ 2. Quy Trình 4 Bước Thực Hiện

### Bước 1: Chuẩn Bị & Đặt File PDF Vào Đúng Cấu Trúc
Tùy vào thể loại tài liệu, hãy đặt file PDF vào đúng thư mục quy định:
- **Đề thi chính thức môn Toán (Hà Nội, TP.HCM,...)**:  
  👉 Lưu vào: [`math/exams/pdf/`](../math/exams/pdf/)
- **Đề thi chính thức môn Tiếng Anh**:  
  👉 Lưu vào: [`english/exams/`](../english/exams/)
- **Tài liệu theo dạng bài / Chuyên đề Toán**:  
  👉 Lưu vào thư mục chuyên đề tương ứng: [`math/topics/<chuyen-de-slug>/pdf/`](../math/topics/)  
  *(Ví dụ: `math/topics/05-giai-toan-bang-cach-lap-pt-hpt/pdf/`)*

---

### Bước 2: Chạy Script Chuyển Đổi Tự Động

Mở terminal tại thư mục gốc của repository:

#### 🔹 Trường hợp A: Chuyển đổi đề thi / tài liệu Toán
```bash
# Convert 1 file tài liệu Toán cụ thể:
py scripts/format_math_exams.py "math/topics/05-giai-toan-bang-cach-lap-pt-hpt/pdf/ten-file.pdf" --output "math/topics/05-giai-toan-bang-cach-lap-pt-hpt/md/ten-file.md"

# Convert toàn bộ PDF trong một thư mục:
py scripts/format_math_exams.py "math/exams/pdf" --output-dir "math/exams/md"
```

#### 🔹 Trường hợp B: Chuyển đổi đề thi Tiếng Anh
```bash
# Convert toàn bộ đề tiếng Anh trong thư mục english/exams:
py scripts/convert_exam_pdf_to_md.py "english/exams" --output-dir "english/exams/md"
```

> [!NOTE]
> Yêu cầu cài đặt thư viện một lần duy nhất nếu máy tính chưa có:
> ```bash
> pip install pymupdf
> ```

---

### Bước 3: Hậu Kiểm & Chuẩn Hóa Sư Phạm (Quality Assurance Cho Bum)

Dù script tự động xử lý phần lớn công việc, để tài liệu đạt chuẩn sư phạm cao nhất cho học sinh 14 tuổi ôn thi vào 10, người vận hành hoặc AI Assistant cần rà soát 4 tiêu chí:

1. **Công thức toán học (LaTeX)**:
   - Các biến số, số mũ, phân số hiển thị đẹp mắt: `$x \in \mathbb{N}^*$`, `$S = v \times t$`, `$\dfrac{a}{b}$`.
   - Hệ phương trình dùng môi trường `$\begin{cases} ... \end{cases}$`.
2. **Ẩn lời giải để chủ động tự luyện**:
   - Mọi lời giải chi tiết và đáp số đều phải nằm gọn trong:
     ```html
     <details>
     <summary><b>🔍 Xem Hướng Dẫn & Lời Giải Chi Tiết</b></summary>
     
     ... nội dung lời giải từng bước ...
     </details>
     ```
3. **Bẫy đề thi (Trap Buster)**:
   - Nếu là chuyên đề lý thuyết hoặc dạng bài hay nhầm lẫn (như quên đổi đơn vị phút sang giờ, quên điều kiện ẩn mẫu), hãy bổ sung hộp cảnh báo `> [!IMPORTANT]` hoặc `> [!WARNING]`.
4. **Bảng phân tích đại lượng**:
   - Đối với dạng bài toán thực tế lập PT/HPT, luôn khuyến khích kẻ bảng 3 cột ($S, v, t$ hoặc Năng suất, Thời gian, Khối lượng công việc) để Bum hình thành phản xạ nháp trước khi viết bài giải.

---

### Bước 4: Đánh Chỉ Mục (Indexing) & Cập Nhật Ngân Hàng Câu Hỏi

1. **Cập nhật README của thư mục**:
   - Mở file `README.md` trong thư mục tài liệu đó, bổ sung dòng liên kết tới file Markdown và PDF tương ứng vào bảng danh mục.
2. **Quét lại ngân hàng câu hỏi đề thi (nếu là file đề thi mới)**:
   ```bash
   py scripts/build_math_registry.py
   ```
   Hệ thống sẽ tự động quét, phân loại độ khó và cập nhật danh sách câu hỏi tại [`math/exams/QUESTION_REGISTRY.md`](../math/exams/QUESTION_REGISTRY.md).

---

## ❓ 3. Xử Lý Các Sự Cố Thường Gặp (Troubleshooting)

- **Lỗi `ModuleNotFoundError: No module named 'fitz'` hoặc `'pymupdf'`**:
  - Chạy `pip install pymupdf` trong terminal (hoặc kích hoạt môi trường conda / python tương ứng).
- **File PDF dạng ảnh scan (không có văn bản thô để bóc tách)**:
  - Sử dụng trực tiếp công cụ AI Multimodal (`view_file` trong Antigravity) để thực hiện OCR trực quan với độ chính xác cao nhất, sau đó định dạng lại sang Markdown.
- **Ký tự toán học bị biến dạng thành ô vuông hoặc ký tự lạ**:
  - Bổ sung mã ký tự PUA đó vào từ điển `SYMBOL_MAP` trong file [`scripts/format_math_exams.py`](format_math_exams.py).

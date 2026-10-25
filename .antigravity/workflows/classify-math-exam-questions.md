---
description: Classifies, tags, and registers Grade 10 Math entrance exam questions by 9 core categories and difficulty scale 1-5 into a searchable registry.
---

# Workflow: /classify-math-exam-questions

Use this workflow whenever new Grade 10 Math entrance exam papers (PDFs/Markdown from Hà Nội, TP.HCM, Đà Nẵng, Cần Thơ, v.v.) are added to the repository, or when querying and categorizing questions for **Bum** (14 years old, Grade 8/9, preparing for Grade 10 Entrance Exam).

---

## 🎯 Objectives & Pedagogical Vision

1. **Chuẩn Hóa Đề Thi Tuyển Sinh Môn Toán**: Bóc tách, định dạng công thức Toán học chuẩn LaTeX MathJax 3 (`$ ... $` cho inline, `$$ ... $$` cho block) từ các file PDF đề thi gốc sang Markdown.
2. **Hệ Thống Phân Loại Đa Chiều (Taxonomy)**: Gắn nhãn tự động mọi câu hỏi theo **9 Chuyên Đề Cốt Lõi**, **Tỉnh/Thành**, **Số Điểm**, và **Thang Đo Độ Khó 1 – 5**.
3. **Ngân Hàng Dữ Liệu Tái Sử Dụng Lâu Dài**: Duy trì cơ sở dữ liệu kép gồm `math/exams/math-question-registry.json` (dành cho script tự động truy vấn) và `math/exams/QUESTION_REGISTRY.md` (dành cho người dạy và học sinh tra cứu trực quan).
4. **Phục Vụ Lộ Trình Học Của Bum**: Giúp sinh đề kiểm tra nhanh, bài tập hàng ngày bám sát 100% cấu trúc đề thi chính thức mà không bị bỡ ngỡ khi bước vào phòng thi thật.

---

## 📂 Architecture & Files

```
math/exams/
├── README.md                      # Danh mục tổng quan các bộ đề thi vào 10
├── WORKFLOW_REVIEW.md             # Hướng dẫn chi tiết quy trình review và phân loại
├── math-question-registry.json     # Cơ sở dữ liệu câu hỏi dạng JSON (112+ câu)
├── QUESTION_REGISTRY.md           # Danh mục tra cứu Markdown kèm thống kê trực quan
├── pdf/                           # File đề thi PDF nguyên bản (21+ đề)
├── images/                        # Hình học phẳng, đồ thị, bảng biểu trích xuất
└── md/                            # File đề thi chuẩn Markdown đã được format công thức

scripts/
├── format_math_exams.py           # Tiền xử lý PDF -> Markdown & chuẩn hóa ký hiệu MathType
├── build_math_registry.py         # Quét toàn bộ đề md/ -> Trích xuất câu hỏi -> Cập nhật JSON & MD
└── query_math_registry.py         # Công cụ CLI tra cứu, lọc câu hỏi & xuất đề quiz tự động
```

---

## 🏷️ Standardized Taxonomy

### 1. 9 Chuyên Đề Trọng Tâm (Core Categories)

| Category Slug | Tên Chuyên Đề | Dạng Bài Điển Hình & Nội Dung Khảo Sát |
| :--- | :--- | :--- |
| **`can_thuc`** | Căn thức & Rút gọn đại số | Rút gọn biểu thức chứa căn bậc hai, tính giá trị biểu thức khi biết $x$, so sánh biểu thức với số, tìm $x$ nguyên để $P$ nguyên. |
| **`he_phuong_trinh`** | Hệ phương trình bậc nhất | Hệ PT 2 ẩn cơ bản, hệ PT đặt ẩn phụ (chứa căn, phân thức), hệ PT có chứa tham số $m$. |
| **`pt_bac_hai_viet`** | Phương trình bậc hai & Vi-ét | Giải PT bậc hai, điều kiện có 2 nghiệm phân biệt, hệ thức Vi-ét đối xứng ($x_1^2+x_2^2$), Vi-ét bất đối xứng, tìm tham số $m$. |
| **`ham_so_do_thi`** | Hàm số & Đồ thị | Vẽ Parabol $(P): y=ax^2$ và đường thẳng $(d): y=mx+n$, tìm tọa độ giao điểm, tương giao $(d)$ và $(P)$. |
| **`toan_thuc_te`** | Toán thực tế & Ứng dụng | Giải bài toán bằng cách lập PT/HPT (chuyển động, năng suất, kinh tế giảm giá, hóa học dung dịch). |
| **`xac_suat_thong_ke`** | Xác suất & Thống kê | Đọc bảng tần số ghép nhóm, biểu đồ đoạn thẳng, xác suất cổ điển của biến cố ngẫu nhiên. |
| **`hinh_khong_gian`** | Hình học không gian thực tế | Diện tích xung quanh, thể tích hình trụ, hình nón, hình cầu gắn liền với đời sống (thùng nước, nón lá, quả bóng). |
| **`hinh_hoc_phang`** | Hình học phẳng tổng hợp | Tứ giác nội tiếp, góc với đường tròn, tiếp tuyến, tam giác đồng dạng, hệ thức lượng, chứng minh thẳng hàng/vuông góc. |
| **`bat_dang_thuc_cuc_tri`** | Bất đẳng thức & Cực trị (Câu điểm 10) | BĐT Cauchy (AM-GM), BĐT Bunhiacopski, kỹ thuật chọn điểm rơi, tìm GTLN / GTNN, cực trị hình học. |

---

### 2. Thang Đo Độ Khó Tuyển Sinh (Difficulty Scale 1 – 5)

| Thang Điểm | Độ Khó | Thang Điểm Tuyển Sinh | Mô Tả & Tiêu Chí Đánh Giá |
| :---: | :--- | :---: | :--- |
| **Level 1** | **Nhận biết (Easy)** | **5.0 – 6.0 điểm** | Nhớ công thức, thay số trực tiếp: tính giá trị biểu thức căn khi $x = x_0$, đọc số liệu từ biểu đồ/bảng tần số, tìm tọa độ điểm trên đồ thị. |
| **Level 2** | **Thông hiểu (Standard)** | **6.0 – 7.5 điểm** | Nắm chắc thuật toán cơ bản: rút gọn biểu thức có 2-3 phân thức, chứng minh PT có nghiệm ($\Delta > 0$), tính xác suất biến cố đơn giản, câu a hình chứng minh tứ giác nội tiếp. |
| **Level 3** | **Vận dụng (Challenging)** | **7.5 – 8.5 điểm** | Phân tích bài toán nhiều bước: lập PT/HPT toán thực tế chuyển động/năng suất, Vi-ét đối xứng, bất phương trình rút gọn, câu b hình chứng minh góc bằng nhau hoặc tia phân giác. |
| **Level 4** | **Vận dụng cao (Advanced)** | **8.5 – 9.25 điểm** | Tư duy liên kết sâu: Vi-ét bất đối xứng có tham số $m$, câu c hình học chứng minh hệ thức tích ($DM \cdot CA = CF \cdot CO$), hình không gian biến thiên có ẩn phụ. |
| **Level 5** | **Xuất sắc (Điểm 10)** | **9.5 – 10.0 điểm** | Kỹ thuật tách ghép đại số đỉnh cao: BĐT Cauchy 3 số dương, chọn điểm rơi thông minh, cực trị hình học tìm vị trí điểm để diện tích đạt cực đại/cực tiểu. |

---

## 🔄 Step-by-Step Execution Workflow

### Bước 1: Tiếp Nhận & Format Đề Thi Mới
1. Đặt các file PDF đề thi mới vào thư mục [math/exams/pdf/](file:///c:/Users/Admin/source/repos/nephew-english/math/exams/pdf).
2. Chạy script định dạng và làm sạch ký hiệu MathType/Symbol:
   ```bash
   py scripts/format_math_exams.py
   ```
   *Script sẽ trích xuất văn bản, xử lý các ký tự Hy Lạp / toán học ($\Delta, \ge, \ne$), ghép câu văn bị ngắt dòng và lưu vào [math/exams/md/](file:///c:/Users/Admin/source/repos/nephew-english/math/exams/md).*

---

### Bước 2: Quét & Cập Nhật Question Registry
Chạy công cụ bóc tách câu hỏi tự động:
```bash
py scripts/build_math_registry.py
```
*Tác vụ tự động*:
- Đọc từng file `.md` trong `math/exams/md/`.
- Nhận diện các câu hỏi (Câu 1, Câu 2, Câu 3...).
- Gắn thẻ `category`, `sub_category`, `difficulty`, `province`, `points`.
- Cập nhật cơ sở dữ liệu [math/exams/math-question-registry.json](file:///c:/Users/Admin/source/repos/nephew-english/math/exams/math-question-registry.json) và bảng danh mục [math/exams/QUESTION_REGISTRY.md](file:///c:/Users/Admin/source/repos/nephew-english/math/exams/QUESTION_REGISTRY.md).

---

### Bước 3: Tra Cứu & Khai Thác Dữ Liệu
Sử dụng công cụ tương tác CLI để tra cứu khi thiết kế bài học hoặc làm đề luyện:

```bash
# Xem thống kê phân bố câu hỏi
py scripts/query_math_registry.py --stats

# Lọc câu hỏi theo chuyên đề và độ khó
py scripts/query_math_registry.py --category can_thuc --difficulty 2 --limit 5

# Lọc câu hỏi hình học theo độ khó vận dụng
py scripts/query_math_registry.py --category hinh_hoc_phang --difficulty 3

# Tìm kiếm từ khóa đề thi thực tế
py scripts/query_math_registry.py --keyword "năng suất"
py scripts/query_math_registry.py --keyword "parabol"

# Xuất nhanh một bài kiểm tra mẫu
py scripts/query_math_registry.py --difficulty 2 --limit 5 --random --export-quiz "math/assessments/quick-quiz-level-2.md"
```

---

## 📋 Quality Assurance Checklist

- [ ] Mọi công thức Toán đều dùng chuẩn MathJax (`$ ... $` hoặc `$$ ... $$`), không dùng ký tự Unicode bị vỡ.
- [ ] Mọi câu hỏi đều được gán đúng chuyên đề (Category) trong số 9 chuyên đề cốt lõi.
- [ ] Độ khó 1–5 phản ánh chính xác vị trí và mức phân hóa trong đề thi tuyển sinh vào lớp 10.
- [ ] Hình vẽ minh họa (nếu có) được lưu đúng tại `math/exams/images/` và hiển thị chính xác trong file Markdown.

# 🛠️ Bộ Kịch Bản & Công Cụ Tự Động Hóa (Automation Scripts)

Thư mục chứa các công cụ Python phục vụ việc tự động hóa, chuyển đổi dữ liệu đề thi, bóc tách công thức toán học và quản lý cơ sở dữ liệu bài tập trong repository học tập của **Bum (14 tuổi)**.

---

## 📌 Hướng Dẫn Quy Trình (Workflows)

- 📖 **Quy trình chuyển đổi PDF sang Markdown**: Xem chi tiết tại [`WORKFLOW_CONVERT.md`](WORKFLOW_CONVERT.md)
- 📋 **Quy trình review & phân loại độ khó câu hỏi Level 1–5**: Xem chi tiết tại [`../math/exams/WORKFLOW_REVIEW.md`](../math/exams/WORKFLOW_REVIEW.md)

---

## 📂 Danh Mục Công Cụ

1. **[`format_math_exams.py`](format_math_exams.py)**: Chuyển đổi PDF đề thi & chuyên đề môn Toán (chuẩn hóa MathType, LaTeX, đóng gói lời giải `<details>`).
2. **[`convert_exam_pdf_to_md.py`](convert_exam_pdf_to_md.py)**: Chuyển đổi PDF đề thi môn Tiếng Anh và trắc nghiệm tổng hợp (bóc tách ảnh minh họa).
3. **[`build_math_registry.py`](build_math_registry.py)**: Quét đề thi Markdown môn Toán, phân loại dạng bài & độ khó Level 1–5, cập nhật cơ sở dữ liệu `math-question-registry.json`.
4. **[`query_math_registry.py`](query_math_registry.py)**: CLI tra cứu câu hỏi theo dạng bài, độ khó và xuất đề thi luyện tập cá nhân hóa.
5. **[`build_question_registry.py`](build_question_registry.py)** & **[`query_registry.py`](query_registry.py)**: Bộ công cụ tương ứng dành cho ngân hàng câu hỏi Tiếng Anh.

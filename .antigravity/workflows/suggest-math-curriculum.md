---
description: Proposes a cohesive weekly math curriculum theme, roadmap ordered from easy to hard, and targeted exam trap recovery based on Grade 10 Math entrance exams and Bum's past mistakes.
---

# Workflow: /suggest-math-curriculum

Use this workflow to plan and preview the upcoming week's math curriculum for **Bum** (14 years old, Grade 8/9, preparing for Grade 10 Entrance Exam) before generating weekly math lesson files. Môn Toán không phân chia theo ngày mà tổ chức theo tuần hoàn chỉnh và **bài tập được sắp xếp theo thứ tự từ dễ lên khó**.

---

## 🎯 Purpose & Scope

1. **Xác Định Tuần Học Kế Tiếp**: Quét thư mục [math/lessons/](file:///c:/Users/Admin/source/repos/nephew-english/math/lessons) để nhận diện chỉ số tuần tiếp theo `<N>` (ví dụ: `week-02-he-phuong-trinh`).
2. **Tuân Thủ Thứ Tự Từ Dễ Lên Khó**: Lộ trình 12 tuần được bố trí chặt chẽ từ Giai đoạn 1 (Level 1-2: 7.0đ) $\rightarrow$ Giai đoạn 2 (Level 2-3: 8.5đ) $\rightarrow$ Giai đoạn 3 (Level 3-4: 9.25đ) $\rightarrow$ Giai đoạn 4 (Level 4-5: Điểm 10) theo [math/lessons/README.md](file:///c:/Users/Admin/source/repos/nephew-english/math/lessons/README.md).
3. **Đối Chiếu Sổ Tay Bẫy Sai (`MISTAKE_LOG.md`)**: Rà soát các bẫy đang có trạng thái 🔴 **Active** hoặc 🟡 **In-Review** (từ TRAP-01 đến TRAP-07) để lên kế hoạch "phục thù" trong các bài tập tuần mới.
4. **Khai Thác Đề Thi Mẫu Từ Registry**: Chạy script tra cứu câu hỏi thực tế:
   ```bash
   py scripts/query_math_registry.py --category <topic_slug> --difficulty 2 --limit 3
   py scripts/query_math_registry.py --category <topic_slug> --difficulty 3 --limit 3
   ```
5. **Đầu Ra (Output)**: Tạo file tổng quan tuần tại `math/lessons/week-<N>-<topic>/week-overview.md` để người dạy và học sinh dễ dàng nắm bắt mục tiêu và các chặng luyện tập từ dễ lên khó.

---

## 🛠️ Step-by-Step Execution Guide

### Bước 1: Quét Tiến Độ & Lọc Bẫy Cần Khắc Phục
1. Kiểm tra thư mục `math/lessons/` để xem tuần tiếp theo theo bảng lộ trình 12 tuần.
2. Mở file [math/assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/math/assessments/MISTAKE_LOG.md):
   - Chọn ra 1–2 bẫy trọng tâm cần ưu tiên tiêu diệt trong tuần mới.
   - Loại bỏ các bẫy đã đạt 🟢 **Mastered** để tránh sự nhàm chán lặp lại.

---

### Bước 2: Truy Vấn Ngân Hàng Đề Thi Để Lấy Câu Mẫu
Chạy công cụ CLI để xem các mẫu câu hỏi thi thật thuộc chuyên đề tuần này:
```bash
py scripts/query_math_registry.py --category <topic_slug> --difficulty 2 --limit 3
py scripts/query_math_registry.py --category <topic_slug> --difficulty 3 --limit 3
```

---

### Bước 3: Soạn Thảo File `math/lessons/week-<N>-<topic>/week-overview.md`

Sử dụng cấu trúc template chuẩn (không phân chia theo ngày, phân hóa theo cấp độ từ dễ lên khó):

```markdown
# ⚡ Kế Hoạch Tuần <N>: <Tên Chuyên Đề Bắt Tai Kèm Icon> 🚀
> **Đối tượng**: Bum (14 tuổi – Chuẩn bị thi vào lớp 10 THPT)  
> **Chuyên đề trọng tâm**: <Tên chuyên đề trong math/topics/>  
> **Mục tiêu tuần**: Luyện tập từ DỄ LÊN KHÓ (Level 1 $\rightarrow$ Level 4) + Triệt tiêu bẫy TRAP-XX!

---

## 🎯 Phân Tích Lỗ Hổng & Chiến Thuật Khắc Phục Tuần Này

| Bẫy Lỗi Bum Dễ Mắc (Từ Mistake Log) | Bản Chất Sai Lầm | Chặng Luyện Phản Xạ | Mục Tiêu Bài Học |
| :--- | :--- | :---: | :--- |
| **TRAP-01**: Quên đối chiếu ĐKXĐ | Ra nghiệm $x$ xong kết luận ngay mà không nhìn lại điều kiện ở đầu đề bài. | **Level 1 & Level 3** | Rèn phản xạ "Khoanh tròn ĐKXĐ" ngay từ dòng đầu tiên. |
| **TRAP-02**: Nhầm dấu trừ trước ngoặc | Khi quy đồng mẫu, quên đổi dấu các hạng tử ở tử số phân thức thứ hai. | **Level 2** | Quy tắc đặt ngoặc vuông an toàn trước khi phá ngoặc. |

---

## 📅 Các Chặng Luyện Tập Trong Tuần (Từ Dễ Lên Khó)

- **🟢 Chặng 1: Level 1 (Nhận biết - 5.0đ - 6.0đ)**: Nhớ công thức, ĐKXĐ, tính nhẩm phản xạ 10s/câu.
- **🟡 Chặng 2: Level 2 (Thông hiểu - 6.5đ - 7.5đ)**: Rút gọn căn số, biến đổi thuật toán 4 bước chuẩn.
- **🟠 Chặng 3: Level 3 (Vận dụng đề thi thật - 7.5đ - 8.5đ)**: Trích từ đề thi vào 10 Hà Nội & TP.HCM.
- **🔴 Chặng 4: Level 4 (Vận dụng cao - 8.5đ - 9.25đ)**: Câu hỏi phụ phân loại học sinh khá giỏi.
- **🕵️ Chặng 5: Thợ Săn Bẫy Thi (Trap Buster)**: Soi lỗi sai trong bài mẫu và sửa lại.

---

## 🏁 Kế Hoạch Cuối Tuần: Checkpoint Test
- Sau khi hoàn thành bài tập, chạy workflow `/generate-math-weekly-assessment` để làm bài kiểm tra tổng hợp 60 phút tại `math/assessments/test-week-<N>.md`.
```

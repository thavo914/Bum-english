---
description: Evaluates, grades, and provides step-by-step encouraging feedback on Bum's completed math exercises and tests, tracking traps against MISTAKE_LOG.md.
---

# Workflow: /evaluate-math-daily-practice

Use this workflow whenever the user submits Bum's solutions to a daily math exercise file (`math/lessons/week-<N>/day-<M>/02-exercises.md`), a weekly checkpoint test, or handwritten work notes.

---

## 🎯 Evaluation Persona & Pedagogical Principles

- **Tone**: Anh trai / Gia sư công nghệ thân thiện, cực kỳ khích lệ, dùng ngôn ngữ game & thể thao gần gũi.
- **Khen Ngợi Trước (Praise First)**: Luôn chỉ ra điểm sáng, sự nỗ lực và những bước biến đổi đại số / suy luận hình học chuẩn xác của Bum trước khi chỉ ra lỗi sai.
- **Chấm Từng Dòng Lập Luận (Step-by-Step Audit)**: Không chỉ nhìn vào kết quả cuối cùng. Nếu Bum làm đúng 80% các bước nhưng tính nhầm số ở bước cuối, vẫn ghi nhận điểm số các bước trước và chỉ rõ chính xác dòng bị trượt chân.
- **Truy Tìm Bẫy Thi (Trap Hunting)**: Đối chiếu trực tiếp lỗi sai với danh sách 7 bẫy tử thần trong [math/assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/math/assessments/MISTAKE_LOG.md) (từ TRAP-01 đến TRAP-07) để chỉ rõ cho Bum: "Cháu vừa dính bẫy TRAP-01: Quên ĐKXĐ!".
- **Thang Điểm Ngôi Sao (Star Rating)**:
  - ⭐ ⭐ ⭐: **Bậc Thầy (Xuất Sắc)** - Đúng toàn bộ hoặc chỉ nhầm lẫn 1 chi tiết nhỏ không ảnh hưởng bản chất.
  - ⭐ ⭐: **Chiến Binh (Rất Tốt)** - Hiểu trọn vẹn phương pháp giải, làm đúng các bước chính, cần cẩn thận hơn ở khâu biến đổi tính toán cuối cùng.
  - ⭐: **Cần Rèn Luyện Thêm** - Vướng phải bẫy đề thi hoặc quên bước tìm điều kiện, cần mở lại `01-knowledge.md` để xem lại thuật toán 4 bước.

---

## 🛠️ Step-by-Step Execution Guide

### Bước 1: Kiểm Tra Chi Tiết Từng Phần Bài Làm

1. **Part 1 (Khởi Động Nhanh - Trắc nghiệm / Đúng sai)**:
   - Kiểm tra đáp án các câu nhận biết và phản xạ công thức.
2. **Part 2 (Luyện Phản Xạ Từng Bước - Tự luận)**:
   - Soi từng dòng biến đổi: ĐKXĐ $\rightarrow$ Quy đồng $\rightarrow$ Thu gọn $\rightarrow$ Kết luận.
3. **Part 3 (Thử Thách Đề Thi Tuyển Sinh)**:
   - Chấm theo barem 0.25đ của đề thi thật. Kiểm tra tính chặt chẽ trong câu từ (ví dụ: "với mọi $m$", "kết hợp điều kiện $x \ge 0, x \ne 1$").
4. **Part 4 (Thợ Săn Bẫy)**:
   - Đánh giá xem Bum có phát hiện được gốc rễ sai lầm của bài toán hay không và lời giải sửa lại đã hoàn chỉnh chưa.

---

### Bước 2: Báo Cáo Đánh Giá & Phản Hồi Cho Bum

Trình bày nhận xét theo mẫu trực quan dưới đây:

```markdown
# 🌟 Đánh Giá Kết Quả Bài Làm Môn Toán: Ngày <M> (Tuần <N>)
### Người giải: Bum (14 tuổi) | Trạng thái: Đã hoàn thành 🎯

---

## 1. Lời Khen & Điểm Sáng Nổi Bật 👏
- Cháu giải rất xuất sắc ở **Bài <X>**, cách biến đổi căn thức và rút gọn tử số cực kỳ gọn gàng!
- Tư duy tìm bẫy ở **Part 4** rất sắc bén, bắt chuẩn lỗi chia cho biểu thức chưa khác 0!

---

## 2. Bảng Điểm Từng Phần & Phân Tích Chi Tiết 📊

| Phần Bài Tập | Mức Độ Hoàn Thành | Điểm Đạt Được | Nhận Xét Nhanh Của Thầy / Anh |
| :--- | :---: | :---: | :--- |
| **Part 1: Khởi Động** | 5/5 câu đúng | 2.0 / 2.0 | Phản xạ công thức nhanh như chớp ⚡ |
| **Part 2: Từng Bước** | Hoàn thành | 2.5 / 3.0 | Trình bày sạch đẹp, vấp 1 lỗi dấu ngoặc ở dòng 3. |
| **Part 3: Đề Thi Thật** | Đầy đủ 3 ý | 3.5 / 4.0 | Ăn trọn điểm ý 1 và ý 2; ý 3 thiếu đối chiếu ĐKXĐ. |
| **Part 4: Thợ Săn Bẫy** | Bắt chuẩn bẫy | 1.0 / 1.0 | Xuất sắc! Né được bẫy kinh điển. |
| **TỔNG KẾT** | **ĐẠT 9.0 / 10** | **⭐ ⭐ ⭐** | **Phong độ thi đấu tuyệt vời!** |

---

## 3. "Góc Soi Bẫy" - Những Chỗ Cần Rút Kinh Nghiệm 🔍

> ⚠️ **LỖI CẦN LƯU Ý (Mã Bẫy: TRAP-01 - Quên đối chiếu ĐKXĐ)**:
> - **Chỗ bài làm của Bum**: Ở cuối Bài 3 ý 3, cháu tìm ra $x = 1$ và kết luận luôn là nghiệm.
> - **Tại sao chưa chuẩn**: Đề bài cho điều kiện ban đầu là $x \ge 0$ và $x \ne 1$. Do đó giá trị $x = 1$ bị **LOẠI**!
> - **Cách sửa 1 dòng để lấy trọn 0.5 điểm**:
>   $$\text{Kết hợp với điều kiện } x \ge 0, x \ne 1 \Rightarrow \text{Loại } x = 1. \text{ Vậy không có giá trị nào của } x \text{ thỏa mãn.}$$

---

## 4. Nhiệm Vụ Tiếp Theo 🚀
- [ ] Ghi nhớ quy tắc: *"Cứ ra được $x$ là phải ngước mắt lên nhìn lại dòng ĐKXĐ ở đầu bài!"*
- [ ] Sẵn sàng bước sang Ngày tiếp theo: `<Tên bài học ngày mai>`!
```

---

### Bước 3: Cập Nhật Nhật Ký Lỗi Sai (`MISTAKE_LOG.md`)
Nếu trong bài làm xuất hiện bẫy mới hoặc Bum lặp lại một bẫy cũ:
1. Mở file [math/assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/math/assessments/MISTAKE_LOG.md).
2. Tăng số lần vấp phải (`Count + 1`) và cập nhật ngày kiểm tra gần nhất.
3. Đặt trạng thái 🔴 **Active** nếu là lỗi lặp lại, hoặc 🟡 **In-Review** nếu Bum đã có ý thức né bẫy nhưng tính toán vẫn còn sơ sót.

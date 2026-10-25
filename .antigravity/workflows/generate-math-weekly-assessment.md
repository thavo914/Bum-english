---
description: Generates a standardized Grade 10 Math weekly checkpoint test (assessments/test-week-<N>.md) with official exam questions, 10-point rubric, and trap lifecycle tracking.
---

# Workflow: /generate-math-weekly-assessment

Use this workflow at the end of each study week (sau khi hoàn thành Day 5) hoặc vào dịp cuối tuần để tạo một bài kiểm tra tổng hợp định kỳ môn Toán cho **Bum** tại `math/assessments/test-week-<N>.md`.

---

## 🎯 Purpose & Design Principles

1. **Chuẩn Đề Thi Tuyển Sinh Vào Lớp 10**: Mô phỏng 100% cấu trúc đề thi chính thức từ ngân hàng [math/exams/math-question-registry.json](file:///c:/Users/Admin/source/repos/nephew-english/math/exams/math-question-registry.json).
2. **Đánh Giá Đa Tầng Độ Khó (Phân Hóa 1 – 5)**:
   - **Level 1 & Level 2 (5.0 – 6.5 điểm)**: Lấy chắc điểm cơ bản, kiểm tra triệt để lỗi tính toán và quên điều kiện.
   - **Level 3 (2.0 – 2.5 điểm)**: Vận dụng tư duy lập hệ phương trình, bài toán thực tế, hệ thức Vi-ét, tứ giác nội tiếp.
   - **Level 4 & 5 (1.0 – 1.5 điểm)**: Phân hóa học sinh khá giỏi (câu c hình học, bất đẳng thức cực trị).
3. **Cập Nhật Vòng Đời Lỗi Sai (`MISTAKE_LOG.md`)**:
   - Tích hợp các câu hỏi bẫy nhằm kiểm tra lại các lỗi 🔴 **Active** hoặc 🟡 **In-Review** trong [math/assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/math/assessments/MISTAKE_LOG.md).
   - Nếu Bum giải đúng và không mắc bẫy -> Chuyển trạng thái sang 🟢 **Mastered**.
   - Nếu Bum tiếp tục vấp bẫy -> Ghi nhận chi tiết để ưu tiên khắc phục trong tuần tiếp theo.
4. **Biểu Điểm Giám Khảo Chi Tiết (Từng 0.25đ)**: Cung cấp barem chấm thi chuẩn của Sở GD&ĐT để Bum hiểu rõ tiêu chí ăn điểm của từng dòng lập luận.

---

## 📂 Target File Location

Mỗi bài kiểm tra tuần được lưu tại:
```
math/assessments/
└── test-week-<N>.md   # Ví dụ: test-week-01.md, test-week-02.md
```

---

## 📋 2 Cấu Trúc Đề Thi Tùy Chọn

### Lựa Chọn A: Bài Kiểm Tra Tuần 45 Phút (Weekly Sprint Test - Thang Điểm 10)
Phù hợp kiểm tra nhanh tiến độ học 5 ngày trong tuần:
- **Câu 1 (2.0 điểm - Level 1 & 2)**: Căn thức và rút gọn đại số (tính giá trị, rút gọn biểu thức, so sánh).
- **Câu 2 (2.5 điểm - Level 2 & 3)**: Giải bài toán bằng cách lập PT/HPT hoặc phương trình bậc hai & hệ thức Vi-ét.
- **Câu 3 (1.5 điểm - Level 2 & 3)**: Toán thực tế (hình không gian hoặc ứng dụng kinh tế / phần trăm).
- **Câu 4 (3.0 điểm - Level 2 & 4)**: Hình học phẳng (câu a chứng minh tứ giác nội tiếp 1.5đ, câu b chứng minh góc/tỷ số 1.0đ, câu c nâng cao 0.5đ).
- **Câu 5 (1.0 điểm - Level 5)**: Bất đẳng thức hoặc tìm giá trị lớn nhất / nhỏ nhất (Thử thách điểm 10).

---

### Lựa Chọn B: Đề Thi Thử Toàn Diện 90 – 120 Phút (Full Mock Exam)
Mô phỏng trọn vẹn 1 đề thi tuyển sinh chính thức (Hà Nội hoặc TP.HCM) gồm 5 bài lớn (10 đến 12 ý hỏi), sử dụng câu hỏi trích xuất trực tiếp bằng lệnh:
```bash
py scripts/query_math_registry.py --random --limit 5 --export-quiz "math/assessments/mock-exam-week-<N>.md"
```

---

## 🛠️ Step-by-Step Execution Guide

### Bước 1: Tra Cứu Lỗi Sai & Ngân Hàng Đề
1. Mở file [math/assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/math/assessments/MISTAKE_LOG.md) để kiểm tra các bẫy TRAP-01 đến TRAP-07 đang còn kích hoạt.
2. Dùng công cụ CLI để lọc các câu hỏi phù hợp với chủ đề tuần vừa học:
   ```bash
   py scripts/query_math_registry.py --category <chu_de> --difficulty 2 --limit 3
   py scripts/query_math_registry.py --category <chu_de> --difficulty 3 --limit 2
   ```

---

### Bước 2: Biên Soạn File `math/assessments/test-week-<N>.md`

Sử dụng cấu trúc template chuẩn dưới đây:

```markdown
# 🎯 Đề Kiểm Tra Đánh Giá Tuần <N> (Math Week <N> Checkpoint)
### Khảo Sát Năng Lực Toán Tuyển Sinh Lớp 10 – Dành Riêng Cho Bum (14 Tuổi)

> ⏱️ **Thời gian làm bài**: 60 – 90 phút (Không dùng tài liệu)  
> 🎯 **Mục tiêu điểm số**: 8.0 – 9.0 điểm | Khắc phục triệt để bẫy TRAP-XX  
> 🏷️ **Chuyên đề trọng tâm**: <Tên các chuyên đề học trong tuần>

---

## ĐỀ BÀI (THANG ĐIỂM 10)

### Bài 1 (2.0 điểm): Căn thức & Rút gọn đại số (Level 1 – 2)
Cho hai biểu thức:
$$
A = \frac{\sqrt{x}+1}{\sqrt{x}-2} \quad \text{và} \quad B = \frac{\sqrt{x}}{\sqrt{x}+2} + \frac{2\sqrt{x}}{x-4} \quad (\text{với } x \ge 0, x \ne 4)
$$
1. Tính giá trị của biểu thức $A$ khi $x = 9$. *(0.5 điểm)*
2. Rút gọn biểu thức $B$. *(1.0 điểm)*
3. Tìm các giá trị của $x$ để biểu thức $P = \frac{B}{A} < \frac{1}{2}$. *(0.5 điểm)*

---

### Bài 2 (2.0 điểm): Hệ phương trình & Toán thực tế (Level 2 – 3)
1. Giải hệ phương trình sau:
   $$
   \begin{cases} \frac{2}{x-1} + \sqrt{y+2} = 4 \\ \frac{1}{x-1} - 2\sqrt{y+2} = -3 \end{cases}
   $$ *(1.0 điểm)*
2. Một đội xe dự định điều một số xe cùng loại để chở 40 tấn hàng... *(1.0 điểm)*

---

### Bài 3 (2.0 điểm): Phương trình bậc hai & Định lý Vi-ét (Level 3 – 4)
Cho phương trình: $x^2 - 2(m-1)x + m^2 - 3 = 0$ ($m$ là tham số).
1. Tìm $m$ để phương trình có hai nghiệm phân biệt $x_1, x_2$. *(1.0 điểm)*
2. Tìm $m$ để hai nghiệm thỏa mãn hệ thức: $x_1^2 + x_2^2 + x_1 x_2 = 10$. *(1.0 điểm)*

---

### Bài 4 (3.0 điểm): Hình học phẳng (Level 2 – 4)
Cho đường tròn $(O; R)$ và điểm $A$ nằm ngoài đường tròn...
1. Chứng minh tứ giác $ABOC$ nội tiếp đường tròn. *(1.25 điểm)*
2. Chứng minh $AO \perp BC$ tại $H$ và $AH \cdot AO = AB^2$. *(1.0 điểm)*
3. Kẻ đường kính $CD$... Chứng minh $OI \perp AD$. *(0.75 điểm)*

---

### Bài 5 (1.0 điểm): Bất đẳng thức & Cực trị (Level 5 - Câu Điểm 10)
Cho các số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Tìm giá trị nhỏ nhất của biểu thức:
$$
P = \frac{a^2}{b+1} + \frac{b^2}{c+1} + \frac{c^2}{a+1}
$$

---

## 🔑 BAREM CHẤM ĐIỂM & ĐÁP ÁN CHI TIẾT (ANSWER KEY)

<details>
<summary>👉 Nhấn vào đây để xem đáp án chi tiết và biểu điểm từng 0.25đ của giám khảo</summary>

### Bài 1 (2.0 điểm)
- **Ý 1 (0.5đ)**: Thay $x = 9$ (TMĐK) $\Rightarrow A = \frac{\sqrt{9}+1}{\sqrt{9}-2} = \frac{4}{1} = 4$. *(0.5đ)*
- **Ý 2 (1.0đ)**:
  - Mẫu thức chung là $(\sqrt{x}-2)(\sqrt{x}+2)$. *(0.25đ)*
  - Quy đồng: $B = \frac{\sqrt{x}(\sqrt{x}-2) + 2\sqrt{x}}{(\sqrt{x}-2)(\sqrt{x}+2)}$. *(0.25đ)*
  - Khai triển và thu gọn tử thức: $x - 2\sqrt{x} + 2\sqrt{x} = x$. *(0.25đ)*
  - Kết luận: $B = \frac{x}{x-4}$. *(0.25đ)*
- **Ý 3 (0.5đ)**:
  - Lập biểu thức $P = \frac{B}{A} = \frac{\sqrt{x}}{\sqrt{x}+1}$. *(0.25đ)*
  - Giải BPT $P < \frac{1}{2} \Leftrightarrow \frac{\sqrt{x}-1}{2(\sqrt{x}+1)} < 0 \Leftrightarrow \sqrt{x} < 1 \Leftrightarrow 0 \le x < 1$. *(0.25đ)*

*(Tiếp tục đáp án chi tiết các Bài 2, 3, 4, 5 với barem điểm tương tự)*

</details>

---

## 📊 BẢNG ĐÁNH GIÁ TIẾN ĐỘ & NHẬT KÝ BẪY SAI

| Tổng Điểm Đạt Được | Đánh Giá Năng Lực | Hướng Hành Động Tiếp Theo |
| :---: | :--- | :--- |
| **9.0 – 10.0** | ⭐ ⭐ ⭐ **Thần Đồng Toán Học** | Làm chủ trọn vẹn kiến thức tuần, sẵn sàng chinh phục các câu điểm 10 tiếp theo. |
| **7.5 – 8.75** | ⭐ ⭐ **Chiến Binh Vững Vàng** | Tư duy tốt, cần rà soát lại kỹ năng giải câu c hình hoặc căn chỉnh lại thời gian. |
| **Dưới 7.5** | ⭐ **Cần Tăng Tốc Phản Xạ** | Bị mất điểm ở các câu cơ bản; ghi nhận mã lỗi vào `MISTAKE_LOG.md` để rèn lại ngay. |
```

---

## 📋 Quality Assurance Checklist

- [ ] Tổng điểm bài thi tròn 10.0 điểm, phân bổ điểm từng ý rõ ràng ($0.25đ, 0.5đ, 1.0đ$).
- [ ] Công thức Toán biên soạn chuẩn LaTeX MathJax ($ ... $, $$ ... $$).
- [ ] Phần đáp án cung cấp đầy đủ điều kiện xác định và đối chiếu điều kiện ở từng bước.
- [ ] Kết quả bài thi được đối chiếu với `math/assessments/MISTAKE_LOG.md` để cập nhật trạng thái lỗi.

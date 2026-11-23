# 🧮 Tuần 3 – Phần 4: Ôn Tập Căn Thức & Biến Đổi (`01-can-thuc-va-bien-doi`)
### Luyện Thi Vào Lớp 10 (1★ – 2★) – Dành Cho Bum (14 Tuổi)

---

## 1. Kiến Thức Cốt Lõi Cần Nhớ (1★–2★) 💡

- **3 mẫu ĐKXĐ bắt buộc thuộc lòng**:
  - $\sqrt{A}$ xác định $\iff A \ge 0$.
  - $\dfrac{1}{\sqrt{A}}$ xác định $\iff A > 0$.
  - $\dfrac{1}{\sqrt{A} - B}$ xác định $\iff A \ge 0$ và $A \ne B^2$.
- **Hằng đẳng thức phá căn**:
  $$
  \sqrt{A^2} = |A| = \begin{cases} A & (A \ge 0) \\ -A & (A < 0) \end{cases}
  $$
- **Quy trình rút gọn nhanh**: Phân tích mẫu thức thành nhân tử ($x - 1 = (\sqrt{x} - 1)(\sqrt{x} + 1)$), quy đồng giữ dấu ngoặc cẩn thận rồi rút gọn nhân tử chung giữa tử và mẫu.

---

## 2. Bài Tập Ôn Tập (1★–2★) ⚔️

### 🟢 Level 1 (1★) – Phản Xạ Nhanh
1. Điều kiện xác định của biểu thức $\dfrac{1}{\sqrt{x - 5}}$ là:
   - A. $x \ge 5$
   - B. $x > 5$
   - C. $x \ne 5$
   - D. $x \le 5$
2. Giá trị của biểu thức $\sqrt{(2 - \sqrt{5})^2}$ bằng:
   - A. $2 - \sqrt{5}$
   - B. $\sqrt{5} - 2$
   - C. $5 - 2$
   - D. $3$

### 🟡 Level 2 (2★) – Tính Giá Trị & Rút Gọn Cơ Bản
**Bài 2.1**: Cho hai biểu thức:
$$
A = \dfrac{\sqrt{x} + 2}{\sqrt{x} - 1} \quad \text{và} \quad B = \dfrac{\sqrt{x}}{\sqrt{x} - 1} - \dfrac{2}{\sqrt{x} + 1} - \dfrac{2}{x - 1} \quad (\text{với } x \ge 0, x \ne 1)
$$
1. Tính giá trị của biểu thức $A$ khi $x = 9$. *(1★)*
2. Rút gọn biểu thức $B$. *(2★)*

**Bài 2.2 (Trích Đề Tham Khảo Tuyển Sinh Lớp 10 Hà Nội 2025 – Đề số 10)**:
> 📌 **Nguồn**: [`de-tham-khao-thi-vao-10-mon-toan-ha-noi-nam-2025-de-so-10`](../../exams/md/de-tham-khao-thi-vao-10-mon-toan-ha-noi-nam-2025-de-so-10-1746432567.md) – Câu 2 (ý 1 & 2).

Cho hai biểu thức:
$$
A = \dfrac{\sqrt{x} - 1}{\sqrt{x} - 3} \quad \text{và} \quad B = \dfrac{2\sqrt{x}}{\sqrt{x} - 2} - \dfrac{\sqrt{x} + 2}{\sqrt{x} - 3} + \dfrac{6\sqrt{x} - 8}{x - 5\sqrt{x} + 6} \quad (\text{với } x \ge 0, x \ne 4, x \ne 9)
$$
1. Tính giá trị của $A$ khi $x = 16$. *(1★)*
2. Chứng minh $B = \dfrac{\sqrt{x} + 2}{\sqrt{x} - 3}$. *(2★)*

---

## 🔑 Đáp Án Chi Tiết

<details>
<summary>👉 Nhấn vào đây để xem lời giải chi tiết</summary>

- **Level 1**:
  1. **B** ($x - 5 > 0 \iff x > 5$).
  2. **B** ($|2 - \sqrt{5}| = \sqrt{5} - 2$ vì $\sqrt{5} > \sqrt{4} = 2$).

- **Bài 2.1**:
  1. Thay $x = 9$ (TMĐK) vào $A$:
     $$
     A = \dfrac{\sqrt{9} + 2}{\sqrt{9} - 1} = \dfrac{3 + 2}{3 - 1} = \mathbf{\dfrac{5}{2}}
     $$
  2. Với $x \ge 0, x \ne 1$:
     $$
     B = \dfrac{\sqrt{x}(\sqrt{x} + 1) - 2(\sqrt{x} - 1) - 2}{(\sqrt{x} - 1)(\sqrt{x} + 1)}
     $$
     $$
     = \dfrac{x + \sqrt{x} - 2\sqrt{x} + 2 - 2}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \dfrac{x - \sqrt{x}}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \dfrac{\sqrt{x}(\sqrt{x} - 1)}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \mathbf{\dfrac{\sqrt{x}}{\sqrt{x} + 1}}
     $$

- **Bài 2.2 (Đề Hà Nội 2025 – Đề số 10)**:
  1. Thay $x = 16$ (thỏa mãn ĐKXĐ) vào $A$:
     $$
     A = \dfrac{\sqrt{16} - 1}{\sqrt{16} - 3} = \dfrac{4 - 1}{4 - 3} = \mathbf{3}
     $$
  2. Với $x \ge 0, x \ne 4, x \ne 9$, phân tích $x - 5\sqrt{x} + 6 = (\sqrt{x} - 2)(\sqrt{x} - 3)$:
     $$
     B = \dfrac{2\sqrt{x}(\sqrt{x} - 3) - (\sqrt{x} + 2)(\sqrt{x} - 2) + (6\sqrt{x} - 8)}{(\sqrt{x} - 2)(\sqrt{x} - 3)}
     $$
     $$
     = \dfrac{2x - 6\sqrt{x} - (x - 4) + 6\sqrt{x} - 8}{(\sqrt{x} - 2)(\sqrt{x} - 3)} = \dfrac{x - 4}{(\sqrt{x} - 2)(\sqrt{x} - 3)} = \dfrac{(\sqrt{x} - 2)(\sqrt{x} + 2)}{(\sqrt{x} - 2)(\sqrt{x} - 3)} = \mathbf{\dfrac{\sqrt{x} + 2}{\sqrt{x} - 3}} \text{ (đpcm)}
     $$
</details>

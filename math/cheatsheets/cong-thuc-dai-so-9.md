# ⚡ Sổ Tay Công Thức Đại Số 9 (One-Page Cheatsheet)

Dành cho **Bum (14 tuổi)** – Tra cứu siêu tốc, học thuộc trước khi bước vào phòng thi Tuyển sinh vào lớp 10!

---

## 1. 7 Hằng Đẳng Thức Đáng Nhớ Cốt Lõi
1. $(A + B)^2 = A^2 + 2AB + B^2$
2. $(A - B)^2 = A^2 - 2AB + B^2$
3. $A^2 - B^2 = (A - B)(A + B)$
4. $(A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$
5. $(A - B)^3 = A^3 - 3A^2B + 3AB^2 - B^3$
6. $A^3 + B^3 = (A + B)(A^2 - AB + B^2)$
7. $A^3 - B^3 = (A - B)(A^2 + AB + B^2)$

---

## 2. Căn Bậc Hai & Các Phép Biến Đổi Căn Thức
- **Điều kiện xác định (ĐKXĐ)**: $\sqrt{A}$ có nghĩa $\iff A \ge 0$.
- **Hằng đẳng thức căn thức**: $\sqrt{A^2} = |A| = \begin{cases} A & \text{nếu } A \ge 0 \\ -A & \text{nếu } A < 0 \end{cases}$
- **Nhân & chia căn thức**:
  - $\sqrt{A \cdot B} = \sqrt{A} \cdot \sqrt{B}$ (với $A \ge 0, B \ge 0$)
  - $\sqrt{\dfrac{A}{B}} = \dfrac{\sqrt{A}}{\sqrt{B}}$ (với $A \ge 0, B > 0$)
- **Đưa thừa số ra ngoài / vào trong dấu căn**:
  - $\sqrt{A^2 B} = |A|\sqrt{B} = \begin{cases} A\sqrt{B} & (A \ge 0, B \ge 0) \\ -A\sqrt{B} & (A < 0, B \ge 0) \end{cases}$
- **Trục căn thức ở mẫu**:
  - $\dfrac{A}{\sqrt{B}} = \dfrac{A\sqrt{B}}{B}$ ($B > 0$)
  - $\dfrac{C}{\sqrt{A} \pm B} = \dfrac{C(\sqrt{A} \mp B)}{A - B^2}$ ($A \ge 0, A \ne B^2$)
  - $\dfrac{C}{\sqrt{A} \pm \sqrt{B}} = \dfrac{C(\sqrt{A} \mp \sqrt{B})}{A - B}$ ($A \ge 0, B \ge 0, A \ne B$)

---

## 3. Hàm Số Bậc Nhất $y = ax + b$ ($a \ne 0$)
- **Tính đồng biến / nghịch biến**:
  - $a > 0 \implies$ hàm số **đồng biến** trên $\mathbb{R}$ (đồ thị dốc lên từ trái qua phải).
  - $a < 0 \implies$ hàm số **nghịch biến** trên $\mathbb{R}$ (đồ thị dốc xuống).
- **Vị trí tương đối của $(d_1): y = a_1x + b_1$ và $(d_2): y = a_2x + b_2$**:
  - Cắt nhau $\iff a_1 \ne a_2$
  - Song song $\iff a_1 = a_2$ và $b_1 \ne b_2$
  - Trùng nhau $\iff a_1 = a_2$ và $b_1 = b_2$
  - Vuông góc $\iff a_1 \cdot a_2 = -1$

---

## 4. Hệ Hai Phương Trình Bậc Nhất Hai Ẩn
$$ \begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases} $$
- **2 Phương pháp giải chính**:
  1. *Phương pháp thế*: Rút 1 ẩn từ một phương trình rồi thế vào phương trình còn lại.
  2. *Phương pháp cộng đại số*: Nhân hai vế để cân bằng hệ số của một ẩn rồi cộng/trừ để triệt tiêu ẩn đó.

---

## 5. Phương Trình Bậc Hai $ax^2 + bx + c = 0$ ($a \ne 0$)
- **Biệt thức $\Delta$ và $\Delta'$**:
  - $\Delta = b^2 - 4ac$
  - $\Delta' = (b')^2 - ac$ (với $b = 2b'$)
- **Số nghiệm**:
  - $\Delta < 0 \implies$ Phương trình **vô nghiệm**.
  - $\Delta = 0 \implies$ Có nghiệm kép: $x_1 = x_2 = -\dfrac{b}{2a} = -\dfrac{b'}{a}$.
  - $\Delta > 0 \implies$ Có 2 nghiệm phân biệt: $x_{1,2} = \dfrac{-b \pm \sqrt{\Delta}}{2a} = \dfrac{-b' \pm \sqrt{\Delta'}}{a}$.
- **Trường hợp nhẩm nghiệm nhanh**:
  - Nếu $a + b + c = 0 \implies x_1 = 1;\; x_2 = \dfrac{c}{a}$.
  - Nếu $a - b + c = 0 \implies x_1 = -1;\; x_2 = -\dfrac{c}{a}$.

---

## 6. Định Lý Vi-ét & Các Dạng Biểu Thức Đối Xứng
Nếu phương trình có 2 nghiệm $x_1, x_2$ ($\Delta \ge 0$):
$$ S = x_1 + x_2 = -\dfrac{b}{a}, \quad P = x_1 \cdot x_2 = \dfrac{c}{a} $$
- **Các hệ thức thường gặp**:
  - $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1x_2 = S^2 - 2P$
  - $(x_1 - x_2)^2 = (x_1 + x_2)^2 - 4x_1x_2 = S^2 - 4P \implies |x_1 - x_2| = \sqrt{S^2 - 4P}$
  - $\dfrac{1}{x_1} + \dfrac{1}{x_2} = \dfrac{x_1 + x_2}{x_1 x_2} = \dfrac{S}{P}$
  - $x_1^3 + x_2^3 = (x_1 + x_2)(x_1^2 - x_1x_2 + x_2^2) = S(S^2 - 3P)$
- **Dấu của 2 nghiệm**:
  - 2 nghiệm trái dấu $\iff P < 0$ (hay $a \cdot c < 0$)
  - 2 nghiệm cùng dấu $\iff \Delta \ge 0$ và $P > 0$
  - 2 nghiệm cùng dương $\iff \Delta \ge 0,\; P > 0,\; S > 0$
  - 2 nghiệm cùng âm $\iff \Delta \ge 0,\; P > 0,\; S < 0$

---

## 7. Bất Đẳng Thức Cô-si (AM-GM) Cho 2 Số Không Âm
Với $a \ge 0,\; b \ge 0$:
$$ a + b \ge 2\sqrt{ab} $$
- Dấu "$=$" xảy ra khi và chỉ khi $a = b$.
- Hệ quả hay dùng: $a + \dfrac{1}{a} \ge 2$ (với $a > 0$).

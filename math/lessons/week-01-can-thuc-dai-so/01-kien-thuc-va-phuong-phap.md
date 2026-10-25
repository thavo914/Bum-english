# ⚡ Tuần 1: Căn Thức Bậc Hai & Rút Gọn Biểu Thức Đại Số
### Chuyên Đề Nền Tảng Tuyển Sinh Vào Lớp 10 – Dành Cho Bum (14 Tuổi)

> 🎯 **Mục tiêu chuyên đề tuần này**: Làm chủ toàn bộ kiến thức về Căn thức, nắm vững thuật toán 4 bước rút gọn biểu thức đại số, triệt tiêu mọi bẫy sai ngu để **ăn trọn 2.0 điểm Câu 1 trong đề thi vào 10**!

---

## 1. Bản Chất Kiến Thức Cốt Lõi (Core Theory) 💡

### 1.1. Căn Bậc Hai Số Học
- Với số dương $a$, số $\sqrt{a}$ được gọi là **căn bậc hai số học** của $a$.
- Số dương $a$ có đúng hai căn bậc hai đối nhau: $\sqrt{a}$ (dương) và $-\sqrt{a}$ (âm).
- *Lưu ý sống còn*: Ký hiệu $\sqrt{a}$ luôn luôn $\ge 0$.  
  *Ví dụ*: Căn bậc hai của $25$ là $5$ và $-5$, nhưng $\sqrt{25} = 5$ (không bao giờ bằng $-5$).

### 1.2. Điều Kiện Xác Định (ĐKXĐ) Của Căn Thức 🛡️
Biểu thức $\sqrt{A}$ chỉ xác định (có nghĩa) khi biểu thức dưới dấu căn **không âm**:
$$
\sqrt{A} \text{ có nghĩa} \iff \mathbf{A \ge 0}
$$

| Biểu thức | Điều kiện xác định | Ví dụ cụ thể |
| :--- | :---: | :--- |
| $\sqrt{A}$ | $A \ge 0$ | $\sqrt{2x - 6}$ có nghĩa $\iff 2x - 6 \ge 0 \iff x \ge 3$ |
| $\dfrac{1}{\sqrt{A}}$ | $A > 0$ *(mẫu phải khác 0)* | $\dfrac{1}{\sqrt{x - 1}}$ có nghĩa $\iff x - 1 > 0 \iff x > 1$ |
| $\sqrt{\dfrac{1}{A}}$ | $A > 0$ | $\sqrt{\dfrac{3}{x + 2}}$ có nghĩa $\iff x + 2 > 0 \iff x > -2$ |

---

## 2. Hằng Đẳng Thức "Phá Giáp" $\sqrt{A^2} = |A|$ ⚔️

> [!IMPORTANT]
> Căn bậc hai và lũy thừa bậc hai triệt tiêu nhau nhưng **BẮT BUỘC** phải đưa về dấu Giá trị tuyệt đối:
> $$
> \sqrt{A^2} = \mathbf{|A|} = \begin{cases} A & \text{khi } A \ge 0 \\ -A & \text{khi } A < 0 \end{cases}
> $$

### Thuật toán phá căn 2 bước không trượt phát nào:
1. **Bước 1**: Đưa về trị tuyệt đối $|A|$.
2. **Bước 2**: Xét dấu biểu thức bên trong:
   - Nếu $A \ge 0 \implies$ Giữ nguyên: $|A| = A$.
   - Nếu $A < 0 \implies$ Đổi dấu toàn bộ: $|A| = -A$.

*Ví dụ mẫu*:
- $\sqrt{(\sqrt{5} - 2)^2} = |\sqrt{5} - 2| = \sqrt{5} - 2$ *(vì $\sqrt{5} > 2 \implies \sqrt{5} - 2 > 0$)*.
- $\sqrt{(2 - \sqrt{5})^2} = |2 - \sqrt{5}| = -(2 - \sqrt{5}) = \sqrt{5} - 2$ *(vì $2 < \sqrt{5} \implies 2 - \sqrt{5} < 0$)*.

---

## 3. Các Phép Biến Đổi Căn Thức Cốt Lõi 🛠️

### 3.1. Khai phương một tích và một thương
- Với $A \ge 0, B \ge 0$: $\sqrt{A \cdot B} = \sqrt{A} \cdot \sqrt{B}$
- Với $A \ge 0, B > 0$: $\sqrt{\dfrac{A}{B}} = \dfrac{\sqrt{A}}{\sqrt{B}}$

### 3.2. Đưa thừa số ra ngoài / vào trong dấu căn
- Đưa ra ngoài: $\sqrt{A^2 B} = |A| \sqrt{B} = \begin{cases} A\sqrt{B} & (A \ge 0, B \ge 0) \\ -A\sqrt{B} & (A < 0, B \ge 0) \end{cases}$
- Đưa vào trong: Với $A \ge 0 \implies A\sqrt{B} = \sqrt{A^2 B}$; Với $A < 0 \implies A\sqrt{B} = -\sqrt{A^2 B}$.

### 3.3. Trục căn thức ở mẫu (Kỹ thuật Nhân Liên Hợp)
| Dạng phân thức | Lượng liên hợp nhân cả tử & mẫu | Kết quả sau khi trục căn |
| :---: | :---: | :---: |
| $\dfrac{m}{\sqrt{A}}$ | Nhân với $\sqrt{A}$ | $\dfrac{m\sqrt{A}}{A}$ |
| $\dfrac{m}{\sqrt{A} - B}$ | Nhân liên hợp với $(\sqrt{A} + B)$ | $\dfrac{m(\sqrt{A} + B)}{A - B^2}$ |
| $\dfrac{m}{\sqrt{A} + \sqrt{B}}$ | Nhân liên hợp với $(\sqrt{A} - \sqrt{B})$ | $\dfrac{m(\sqrt{A} - \sqrt{B})}{A - B}$ |

---

## 4. Thuật Toán 4 Bước Rút Gọn Biểu Thức Đại Số Vào 10 📋

Khi làm bài toán rút gọn dạng $P = \left( \frac{\sqrt{x}}{\sqrt{x}-1} - \frac{1}{x-\sqrt{x}} \right) : \frac{\sqrt{x}+1}{x-1}$, tuân thủ đúng 4 bước:

- **Bước 1 (Soi ĐKXĐ)**: Tìm hoặc ghi lại ĐKXĐ đề bài đã cho (thường là $x \ge 0, x \ne 1, x \ne 4$). *(0.25đ)*
- **Bước 2 (Quy đồng mẫu thức)**:
  - Phân tích các mẫu thức thành nhân tử: $x - 1 = (\sqrt{x}-1)(\sqrt{x}+1)$, $x - \sqrt{x} = \sqrt{x}(\sqrt{x}-1)$.
  - Xác định mẫu thức chung (MTC).
  - Nhân tử phụ cho từng phân thức.
- **Bước 3 (Thu gọn tử thức)**:
  - Phá ngoặc cẩn thận (đặc biệt chú ý dấu trừ trước phân thức).
  - Gom các hạng tử đồng dạng ($x$, $\sqrt{x}$, số tự do).
  - Phân tích tử thức thành nhân tử để triệt tiêu với mẫu thức.
- **Bước 4 (Kết luận)**:
  - Viết kết luận rõ ràng: *"Vậy với $x \ge 0, x \ne 1$ thì $P = ...$"*. *(0.25đ)*

---

## 5. Bẫy Tử Thần Đề Thi Cần Né (Watch Out Traps!) ⚠️

> 🚨 **TRAP-01: Quên Đối Chiếu ĐKXĐ Ở Câu Hỏi Phụ**:  
> Sau khi tìm được giá trị của $x$ (ví dụ giải $P = 2 \implies x = 4$), học sinh thường mừng rỡ kết luận ngay mà quên rằng điều kiện ban đầu là $x \ne 4$!  
> 💡 *Quy tắc sống còn*: Luôn viết chữ **(TMĐK)** hoặc **(Loại)** bên cạnh mỗi giá trị $x$ tìm được.

> 🚨 **TRAP-02: Nhầm Dấu Trừ Trước Ngoặc Khi Quy Đồng**:  
> Khi trừ một phân thức: $-\dfrac{\sqrt{x} - 2}{x - 1}$, khi đưa lên tử chung phải đặt dấu ngoặc: $-(\sqrt{x} - 2) = -\sqrt{x} + 2$. Nếu quên ngoặc thành $-\sqrt{x} - 2$ là sai toàn bộ bài toán!

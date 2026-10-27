# Chuyên Đề 04: Phương Trình Bậc Hai Một Ẩn & Định Lý Vi-ét

> **Trọng số trong đề thi Tuyển sinh vào lớp 10**: $1.5$ điểm (Câu phân loại điểm 8 - 9 trong hầu hết các tỉnh thành).

---

## 📂 Cấu Trúc Thư Mục Chuyên Đề

```
math/topics/04-phuong-trinh-bac-hai-va-viet/
├── README.md               # 📖 Công thức nghiệm, hệ thức Vi-ét & các dạng biểu thức đối xứng/bất đối xứng
├── pdf/                    # 📄 Tài liệu PDF chuyên đề gốc
└── md/                     # 📝 Chuyên đề & bài tập Markdown đã số hóa
```

---

## 🎯 Các Dạng Toán Trọng Tâm

1. **Công thức nghiệm & nhẩm nghiệm**:
   - Biệt thức $\Delta = b^2 - 4ac$ và biệt thức thu gọn $\Delta' = b'^2 - ac$ (với $b = 2b'$).
   - Nhẩm nghiệm nhanh: $a + b + c = 0 \implies x_1 = 1, x_2 = \dfrac{c}{a}$; $a - b + c = 0 \implies x_1 = -1, x_2 = -\dfrac{c}{a}$.
2. **Định lý Vi-ét thuận**:
   - Nếu PT $ax^2 + bx + c = 0$ ($a \ne 0$) có 2 nghiệm $x_1, x_2$ ($\Delta \ge 0$):
     $$\begin{cases} S = x_1 + x_2 = -\dfrac{b}{a} \\ P = x_1 x_2 = \dfrac{c}{a} \end{cases}$$
3. **Các dạng bài tập Vi-ét kinh điển**:
   - Biểu thức đối xứng:
     - $x_1^2 + x_2^2 = S^2 - 2P$
     - $(x_1 - x_2)^2 = S^2 - 4P \implies |x_1 - x_2| = \sqrt{S^2 - 4P}$
     - $x_1^3 + x_2^3 = S(S^2 - 3P)$
     - $\dfrac{1}{x_1} + \dfrac{1}{x_2} = \dfrac{S}{P}$
   - Biểu thức bất đối xứng: Kết hợp hệ thức đề bài với $x_1 + x_2 = S$ để giải hệ tìm $x_1, x_2$ theo tham số $m$, sau đó thế vào tích $x_1 x_2 = P$.
   - Dấu các nghiệm: 2 nghiệm cùng dấu ($P > 0$), 2 nghiệm trái dấu ($ac < 0$), 2 nghiệm dương ($P > 0, S > 0$), 2 nghiệm âm ($P > 0, S < 0$).

---

## ⚠️ Bẫy Đề Thi Cần Tránh Cho Bum

- **Quên tìm điều kiện để PT có nghiệm ($\Delta \ge 0$)**: Rất nhiều bạn áp dụng Vi-ét ngay mà không kiểm tra $\Delta \ge 0$, dẫn đến nhận giá trị $m$ làm PT vô nghiệm.
- **Quên điều kiện $a \ne 0$** khi hệ số $a$ chứa tham số $m$.
- **Đề bài yêu cầu "hai nghiệm phân biệt"** thì phải là $\Delta > 0$ (không có dấu bằng).

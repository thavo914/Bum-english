# 🚀 Chuyên Đề: Bài Toán Chuyển Động (Lập Phương Trình & Hệ Phương Trình)

> **Mục tiêu**: Nắm chắc phương pháp lập bảng đại lượng ($S, v, t$), xử lý thời gian nghỉ và lập phương trình chính xác cho kỳ thi vào lớp 10.

---

## 📌 1. Bảng Công Thức Cốt Lõi

| Đại Lượng | Ký Hiệu | Đơn Vị Thường Dùng | Công Thức Tính |
| :--- | :---: | :---: | :--- |
| **Quãng đường** | $S$ | $\text{km}$ hoặc $\text{m}$ | $S = v \times t$ |
| **Vận tốc** | $v$ | $\text{km/h}$ hoặc $\text{m/s}$ | $v = \dfrac{S}{t}$ |
| **Thời gian** | $t$ | $\text{giờ (h)}$ hoặc $\text{giây (s)}$ | $t = \dfrac{S}{v}$ |

> [!IMPORTANT]
> **Quy tắc đổi đơn vị thời gian**:
> - $15 \text{ phút} = \dfrac{15}{60} \text{ h} = \dfrac{1}{4} \text{ h}$
> - $20 \text{ phút} = \dfrac{20}{60} \text{ h} = \dfrac{1}{3} \text{ h}$
> - $30 \text{ phút} = \dfrac{30}{60} \text{ h} = \dfrac{1}{2} \text{ h}$
> - $45 \text{ phút} = \dfrac{45}{60} \text{ h} = \dfrac{3}{4} \text{ h}$
> - $1 \text{ giờ } 12 \text{ phút} = 1 + \dfrac{12}{60} = \dfrac{6}{5} \text{ h}$

---

## 📝 2. Bài Toán Mẫu (Trích Đề Thi Tuyển Sinh Vào 10)

### 📌 Đề Bài:
Một người đi xe máy từ địa điểm $A$ đến địa điểm $B$ cách nhau $90\text{ km}$ với vận tốc dự định. Sau khi đi được $1\text{ giờ}$, người đó dừng lại nghỉ $15\text{ phút}$. Để đến $B$ đúng thời gian dự định, người đó phải tăng vận tốc thêm $10\text{ km/h}$ trên quãng đường còn lại. Tính vận tốc dự định của người đi xe máy.

---

### 💡 Bảng Phân Tích Đại Lượng (Kỹ Thuật Nháp Ra Bảng)

| Giai đoạn | Quãng đường $S$ (km) | Vận tốc $v$ (km/h) | Thời gian $t$ (giờ) |
| :--- | :---: | :---: | :---: |
| **Dự định cả quãng đường** | $90$ | $x$ | $\dfrac{90}{x}$ |
| **Thực tế chặng 1** ($1\text{ h}$) | $1 \cdot x = x$ | $x$ | $1$ |
| **Nghỉ** | $0$ | $0$ | $\dfrac{1}{4}$ |
| **Thực tế chặng 2** (còn lại) | $90 - x$ | $x + 10$ | $\dfrac{90 - x}{x + 10}$ |

---

### ✍️ Lời Giải Chi Tiết Chuẩn Barem Chấm Điểm

**Bước 1: Chọn ẩn và đặt điều kiện**
- Gọi vận tốc dự định của người đi xe máy là $x$ ($\text{km/h}$).
- Điều kiện: $x > 0$.

**Bước 2: Biểu diễn các đại lượng**
- Thời gian dự định đi hết quãng đường $AB$ là: $\dfrac{90}{x}$ (giờ).
- Trong $1$ giờ đầu, người đó đi được quãng đường là: $1 \cdot x = x$ ($\text{km}$).
- Quãng đường còn lại người đó phải đi là: $90 - x$ ($\text{km}$).
- Vận tốc trên quãng đường còn lại là: $x + 10$ ($\text{km/h}$).
- Thời gian người đó đi hết quãng đường còn lại là: $\dfrac{90 - x}{x + 10}$ (giờ).
- Đổi thời gian nghỉ: $15\text{ phút} = \dfrac{1}{4}\text{ giờ}$.
- Tổng thời gian thực tế từ lúc xuất phát đến khi tới $B$ là:
  $$1 + \dfrac{1}{4} + \dfrac{90 - x}{x + 10} = \dfrac{5}{4} + \dfrac{90 - x}{x + 10} \quad (\text{giờ})$$

**Bước 3: Lập phương trình và giải**
Vì người đó đến $B$ đúng thời gian dự định nên ta có phương trình:
$$\dfrac{5}{4} + \dfrac{90 - x}{x + 10} = \dfrac{90}{x}$$

Chuyển vế và quy đồng mẫu thức chung $4x(x + 10)$:
$$\dfrac{5x(x + 10) + 4x(90 - x)}{4x(x + 10)} = \dfrac{360(x + 10)}{4x(x + 10)}$$

Khử mẫu (do $x > 0$ nên mẫu thức khác 0):
$$5x^2 + 50x + 360x - 4x^2 = 360x + 3600$$
$$x^2 + 50x - 3600 = 0$$

Tính biệt thức $\Delta'$:
$$\Delta' = 25^2 - 1 \cdot (-3600) = 625 + 3600 = 4225 > 0$$
$$\sqrt{\Delta'} = \sqrt{4225} = 65$$

Phương trình có hai nghiệm phân biệt:
$$x_1 = -25 + 65 = 40 \quad (\text{Thỏa mãn } x > 0)$$
$$x_2 = -25 - 65 = -90 \quad (\text{Loại vì } x > 0)$$

**Bước 4: Kết luận**
Vậy vận tốc dự định của người đi xe máy là **$40\text{ km/h}$**.

---

## 🎯 3 Bài Tập Tự Luyện (Kèm Lời Giải Ẩn)

### Bài 1: Chuyển Động Cùng Chiều
Một ô tô dự định đi từ tỉnh A đến tỉnh B cách nhau $120\text{ km}$ trong một thời gian quy định. Sau khi đi được $1\text{ giờ}$ với vận tốc dự định, ô tô dừng lại $10\text{ phút}$ để tiếp nhiên liệu. Do đó, để đến B đúng giờ dự định, ô tô phải tăng vận tốc thêm $6\text{ km/h}$ trên quãng đường còn lại. Tính vận tốc dự định ban đầu của ô tô.

<details>
<summary><b>🔍 Xem Hướng Dẫn & Đáp Số Bài 1</b></summary>

- Đổi: $10\text{ phút} = \dfrac{1}{6}\text{ h}$.
- Phương trình: $1 + \dfrac{1}{6} + \dfrac{120 - x}{x + 6} = \dfrac{120}{x}$.
- Biến đổi về PT bậc hai: $x^2 + 6x - 4320 = 0$.
- Nghiệm: $x = 48$ (TM) hoặc $x = -90$ (Loại).
- **Đáp số**: Vận tốc dự định là **$48\text{ km/h}$**.
</details>

### Bài 2: Chuyển Động Ca Nô Ngược Dòng & Xuôi Dòng
Một ca nô xuôi dòng từ bến A đến bến B cách nhau $30\text{ km}$, rồi quay ngược dòng từ B về A hết tất cả $5\text{ giờ } 30\text{ phút}$. Tính vận tốc thực của ca nô biết vận tốc dòng nước là $3\text{ km/h}$.

<details>
<summary><b>🔍 Xem Hướng Dẫn & Đáp Số Bài 2</b></summary>

- Đổi: $5\text{ giờ } 30\text{ phút} = \dfrac{11}{2}\text{ h}$.
- Gọi vận tốc thực của ca nô là $x$ ($\text{km/h}, x > 3$).
- $v_{\text{xuôi}} = x + 3$, $v_{\text{ngược}} = x - 3$.
- Phương trình: $\dfrac{30}{x + 3} + \dfrac{30}{x - 3} = \dfrac{11}{2}$.
- Biến đổi: $11x^2 - 120x - 99 = 0$.
- Giải ra $x = 12$ (TM) hoặc $x = -\dfrac{33}{44}$ (Loại).
- **Đáp số**: Vận tốc thực của ca nô là **$12\text{ km/h}$**.
</details>

### Bài 3: Xe Đạp & Xe Máy Khởi Hành Cùng Lúc
Hai người khởi hành cùng một lúc từ thành phố A đến thành phố B cách nhau $60\text{ km}$. Người thứ nhất đi xe máy, người thứ hai đi xe đạp. Vận tốc xe máy lớn hơn vận tốc xe đạp là $20\text{ km/h}$ nên xe máy đến B trước xe đạp $2\text{ giờ}$. Tính vận tốc của mỗi xe.

<details>
<summary><b>🔍 Xem Hướng Dẫn & Đáp Số Bài 3</b></summary>

- Gọi vận tốc xe đạp là $x$ ($\text{km/h}, x > 0$) $\implies$ vận tốc xe máy là $x + 20$ ($\text{km/h}$).
- Phương trình: $\dfrac{60}{x} - \dfrac{60}{x + 20} = 2$.
- Biến đổi: $x^2 + 20x - 600 = 0$.
- Giải ra $x = 20$ (TM) hoặc $x = -30$ (Loại).
- **Đáp số**: Vận tốc xe đạp là **$20\text{ km/h}$**, vận tốc xe máy là **$40\text{ km/h}$**.
</details>

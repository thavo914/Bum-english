# ⚡ Tuần 2: Giải Bài Toán Bằng Cách Lập PT & HPT (Phần 1)
### Ôn Tập Dạng 1, 2 & Làm Chủ Dạng Mới 3, 4 – Dành Cho Bum (14 Tuổi)

> 🎯 **Mục tiêu chuyên đề tuần này**:
> - Thành thạo kỹ thuật lập bảng 3 cột biến đổi câu chữ đề bài thành phương trình.
> - Ôn chắc **Dạng 1 (Năng suất)** và **Dạng 2 (Làm chung - làm riêng)**.
> - Nắm vững phương pháp giải **Dạng 3 (Quan hệ các số & Cấu tạo số)** và **Dạng 4 (Nội dung hình học)**.
> - Nhận diện ngay bẫy trừ lối đi $2$ đầu và bẫy điều kiện chữ số để **ăn trọn $2.0$ điểm Câu II.1** trong đề thi vào 10!

---

## 1. Bản Chất Kiến Thức Cốt Lõi (Core Theory) 💡

### 1.1. Ôn Lại Dạng 1: Bài Toán Năng Suất Lao Động 🏭
- **Mối quan hệ 3 đại lượng**:
  $$
  \text{Khối lượng công việc} = \text{Năng suất } (1 \text{ ngày/giờ}) \times \text{Thời gian}
  $$
- **Hai trạng thái luôn xuất hiện trong đề**:
  - **Kế hoạch (Dự định)**: Năng suất định mức $x$, làm trong $t_{\text{dự kiến}}$ ngày để xong $S$ sản phẩm.
  - **Thực tế**: Năng suất tăng (hoặc giảm): $x + a$ hoặc $x - a$; hoàn thành sớm hơn hoặc muộn hơn: $t_{\text{thực tế}} = t_{\text{dự kiến}} - b$.
- **Phương trình chốt chặn**: So sánh thời gian thực tế với thời gian dự kiến:
  $$
  t_{\text{dự kiến}} - t_{\text{thực tế}} = t_{\text{sớm hơn}}
  $$

---

### 1.2. Ôn Lại Dạng 2: Công Việc Làm Chung, Làm Riêng 🤝
- **Quy ước vàng**: Coi toàn bộ khối lượng công việc hoàn thành là **$1$ đơn vị** (dù đề nói dệt thảm, sửa đường, hay bơm đầy bể nước).
- **Quy tắc tính năng suất một mình**:
  - Nếu người thứ nhất làm một mình xong toàn bộ việc trong $x$ giờ $\implies$ Mỗi giờ làm được **$\dfrac{1}{x}$ công việc**.
  - Nếu người thứ hai làm một mình xong trong $y$ giờ $\implies$ Mỗi giờ làm được **$\dfrac{1}{y}$ công việc**.
- **Cùng làm chung**: Năng suất được cộng dồn trực tiếp:
  $$
  \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{t_{\text{chung}}}
  $$
- *Lưu ý*: Không bao giờ lấy thời gian cộng thời gian ($x + y \ne t_{\text{chung}}$).

---

### 1.3. Học Mới Dạng 3: Bài Toán Về Quan Hệ Các Số & Cấu Tạo Số 🔢

#### A. Cấu tạo số tự nhiên trong hệ thập phân:
- Số có 2 chữ số:
  $$
  \overline{ab} = 10a + b \quad (a, b \in \mathbb{N}; \ 1 \le a \le 9, \ 0 \le b \le 9)
  $$
  *(Trong đó $a$ là chữ số hàng chục, $b$ là chữ số hàng đơn vị).*
- Khi đổi chỗ hai chữ số cho nhau ta được số mới:
  $$
  \overline{ba} = 10b + a
  $$
- Viết thêm một chữ số $c$ vào bên phải $\overline{ab}$ được số có 3 chữ số:
  $$
  \overline{abc} = 100a + 10b + c
  $$

#### B. Mối quan hệ giữa hai số:
- Hai số hơn kém nhau $k$ đơn vị: $x - y = k$.
- Tổng các bình phương: $x^2 + y^2 = M$.
- Hiệu các bình phương: $x^2 - y^2 = N$.
- Tổng các lập phương: $x^3 + y^3 = K$ (dùng hằng đẳng thức $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$ để rút gọn).

---

### 1.4. Học Mới Dạng 4: Bài Toán Có Nội Dung Hình Học 📐

#### A. Hình chữ nhật:
- Nửa chu vi: $p = a + b = \dfrac{P}{2}$ ($a$ là chiều dài, $b$ là chiều rộng, $0 < b < a < p$).
- Diện tích ban đầu: $S = a \cdot b$.
- Khi thay đổi kích thước: Tăng chiều dài thêm $m$, giảm chiều rộng đi $n \implies S_{\text{mới}} = (a + m)(b - n)$.

> [!IMPORTANT]
> 🚨 **Kỹ thuật "Lối đi bao quanh vườn" (Bẫy đề thi cực nặng)**:
> Một khu vườn có chiều dài ban đầu là $a$, chiều rộng là $b$. Nếu làm một lối đi xung quanh vườn rộng $d\text{ m}$ (thuộc đất trong vườn) thì:
> - Chiều dài phần đất còn lại: $a' = \mathbf{a - 2d}$ *(vì lối đi chiếm $d$ ở bên trái VÀ $d$ ở bên phải)*.
> - Chiều rộng phần đất còn lại: $b' = \mathbf{b - 2d}$ *(vì lối đi chiếm $d$ ở bên trên VÀ $d$ ở bên dưới)*.
> - Diện tích còn lại: $S_{\text{còn lại}} = (a - 2d)(b - 2d)$.

#### B. Tam giác vuông:
- Hai cạnh góc vuông $a, b$ và cạnh huyền $c$ ($a, b, c > 0$).
- Diện tích tam giác vuông: $S = \dfrac{1}{2} a \cdot b$.
- Định lý Pytago:
  $$
  a^2 + b^2 = c^2
  $$

---

## 2. Kỹ Thuật Lập Bảng Phân Tích Đề Bài 📋

Bảng phân tích là "vũ khí bí mật" giúp Bum không bao giờ bị rối chữ. Chỉ cần kẻ khung 3 cột, mọi phương trình sẽ tự động lộ diện!

### Ví dụ mẫu 1: Bảng Năng Suất (Dạng 1)
| Trạng thái | Năng suất ($1$ ngày) | Thời gian ($t$) | Khối lượng ($S$) |
| :--- | :---: | :---: | :---: |
| **Kế hoạch** | $x$ (tấm/ngày) | $\dfrac{3000}{x}$ (ngày) | $3000$ (tấm) |
| **Thực tế giai đoạn 1** | $x$ | $8$ (ngày) | $8x$ (tấm) |
| **Thực tế giai đoạn 2** | $x + 10$ | $\dfrac{3000 - 8x}{x + 10}$ | $3000 - 8x$ |

$\implies$ Phương trình chốt: $\dfrac{3000}{x} - \left(8 + \dfrac{3000 - 8x}{x + 10}\right) = 2$.

### Ví dụ mẫu 2: Bảng Hình Học (Dạng 4)
| Trạng thái | Chiều dài | Chiều rộng | Diện tích |
| :--- | :---: | :---: | :---: |
| **Ban đầu** | $x\text{ (m)}$ | $140 - x\text{ (m)}$ | $x(140 - x)$ |
| **Sau khi làm lối đi** | $x - 4\text{ (m)}$ | $(140 - x) - 4 = 136 - x\text{ (m)}$ | $(x - 4)(136 - x)$ |

$\implies$ Phương trình chốt: $(x - 4)(136 - x) = 4256$.

---

## 3. Thuật Toán Chuẩn 4 Bước Trình Bày Ăn Trọn 2.0 Điểm 🛡️

- **Bước 1 (Chọn ẩn & Đặt điều kiện chính xác)**:
  - Gọi đại lượng đề bài hỏi làm ẩn số $x$ (hoặc 2 ẩn $x, y$).
  - Ghi kèm **đơn vị** và **điều kiện thích hợp**:
    - Số người, sản phẩm, ngày công: $x \in \mathbb{N}^*$.
    - Chữ số hàng chục: $a \in \mathbb{N}, 1 \le a \le 9$; chữ số hàng đơn vị: $b \in \mathbb{N}, 0 \le b \le 9$.
    - Vận tốc, chiều dài, thời gian: $x > 0$. Chiều rộng $<$ Chiều dài $<$ Nửa chu vi.
- **Bước 2 (Biểu diễn các đại lượng chưa biết theo ẩn)**:
  - Viết thành từng câu văn ngắn gọn, rõ ràng kèm đơn vị.
- **Bước 3 (Lập phương trình hoặc hệ phương trình)**:
  - Viết câu dẫn: *"Vì theo đề bài... nên ta có phương trình (hệ phương trình):"*
- **Bước 4 (Giải PT/HPT, Soi ĐKXĐ & Kết luận)**:
  - Giải phương trình bậc nhất hoặc phương trình bậc hai $ax^2 + bx + c = 0$ (tính $\Delta$ hoặc phân tích nhân tử).
  - Đối chiếu từng nghiệm với điều kiện: ghi rõ **(TMĐK)** hoặc **(Loại)**.
  - Viết câu kết luận trả lời đúng câu hỏi đề bài yêu cầu kèm đơn vị.

---

## 4. Bẫy Tử Thần Đề Thi Cần Né (Watch Out Traps!) ⚠️

> 🚨 **TRAP-01: Bẫy Lối Đi Bao Quanh Mảnh Đất (Sai Hàng Loạt!)**  
> Lối đi rộng $2\text{ m}$ xung quanh vườn thì chiều dài bị thụt vào $2\text{ m}$ bên trái và $2\text{ m}$ bên phải $\implies$ Giảm $2 \times 2 = 4\text{ m}$.  
> Học sinh hay làm ẩu: Lấy $x - 2$ thay vì $x - 4$ là mất trắng điểm cả bài!  
> 💡 *Khắc phục*: Cứ nhớ từ khóa *"xung quanh / bao quanh"* $\implies$ Phải trừ **$2 \times \text{bề rộng lối đi}$**.

> 🚨 **TRAP-02: Bẫy ĐKXĐ Chữ Số Của Bài Toán Quan Hệ Số**  
> Chữ số hàng chục $a$ đứng đầu nên **không được bằng 0** ($1 \le a \le 9, a \in \mathbb{N}$). Chữ số hàng đơn vị $b$ có thể bằng 0 ($0 \le b \le 9, b \in \mathbb{N}$).  
> Nếu giải ra nghiệm phân số hoặc số âm mà không ghi "(Loại)" là bị trừ điểm lập tức!

> 🚨 **TRAP-03: Lấy Thời Gian Làm Riêng Cộng Trực Tiếp**  
> Đề bài: "Hai bạn cùng làm trong 4 giờ thì xong". Một số bạn viết ngay phương trình $x + y = 4$!  
> 💡 *Quy tắc sống còn*: Thời gian không cộng dồn được, chỉ có **năng suất (phần việc làm trong $1$ giờ)** mới cộng dồn: $\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{4}$.


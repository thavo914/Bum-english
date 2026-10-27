# Chuyên Đề 05: Giải Bài Toán Bằng Cách Lập Phương Trình & Hệ Phương Trình

> **Trọng số trong đề thi Tuyển sinh vào lớp 10**: $1.5 - 2.0$ điểm (Thường là **Câu II.1** trong đề thi tự luận Hà Nội hoặc chuỗi bài toán thực tế đề TP.HCM).
> **Đối tượng**: Thiết kế riêng cho **Bum (14 tuổi)** – Tư duy thực chiến, bẻ khóa bẫy đề thi, bám sát barem điểm chuẩn của Sở GD&ĐT.

---

## 📂 Cấu Trúc Thư Mục Chuyên Đề

```
math/topics/05-giai-toan-bang-cach-lap-pt-hpt/
├── README.md               # 📖 Hướng dẫn phương pháp, phân loại dạng bài & bẫy đề thi
├── pdf/                    # 📄 File tài liệu chuyên đề gốc định dạng PDF
└── md/                     # 📝 File bài tập, chuyên đề đã được số hóa sang Markdown
```

---

## ⚡ Quy Trình 3 Bước Chuẩn Barem (Không Bị Trừ Điểm)

### Bước 1: Lập Phương Trình hoặc Hệ Phương Trình
1. **Chọn ẩn số và đặt điều kiện thích hợp cho ẩn**:
   - Nếu gọi 1 ẩn $\implies$ giải bằng phương trình.
   - Nếu gọi 2 ẩn ($x, y$) $\implies$ giải bằng hệ phương trình (rất nên dùng nếu mối quan hệ giữa 2 đại lượng độc lập rõ ràng).
   - *Lưu ý đơn vị và điều kiện*: Người, sản phẩm, ngày công $\implies x \in \mathbb{N}^*$; Vận tốc, thời gian, chiều dài $\implies x > 0$.
2. **Biểu diễn các đại lượng chưa biết** theo ẩn số và các đại lượng đã biết.
3. **Lập phương trình / hệ phương trình** biểu diễn mối quan hệ giữa các đại lượng (dựa vào câu chữ đề bài: *"nhiều hơn"*, *"ít hơn"*, *"vượt mức"*, *"đến sớm/muộn"*).

### Bước 2: Giải Phương Trình hoặc Hệ Phương Trình
- Chọn phương pháp tối ưu:
  - Nếu là hệ PT bậc nhất: Phương pháp thế hoặc phương pháp cộng đại số.
  - Nếu là PT bậc hai: Nhẩm nghiệm ($a+b+c=0$ hoặc $a-b+c=0$) hoặc tính biệt thức $\Delta$ / $\Delta'$.

### Bước 3: Đối Chiếu Điều Kiện & Kết Luận
- So sánh từng nghiệm tìm được với điều kiện đặt ra ở Bước 1.
- Ghi rõ **(Thỏa mãn - TM)** hoặc **(Loại - L)**.
- Trả lời đúng câu hỏi đề bài yêu cầu kèm đơn vị.

---

## 🎯 5 Dạng Toán Cốt Lõi Thường Gặp Nhất

### Dạng 1: Bài Toán Chuyển Động (Chiếm 60% Đề Thi)
- **Công thức cốt lõi**: $S = v \times t \implies v = \dfrac{S}{t}, \quad t = \dfrac{S}{v}$.
- **Kỹ thuật lập bảng 3 cột**: Vận tốc ($v$), Thời gian ($t$), Quãng đường ($S$).
- **Các kịch bản thường gặp**:
  1. *Chuyển động trên đường bộ*: Đi nhanh hơn, đi chậm hơn, khởi hành sau, dừng lại nghỉ trên đường.
  2. *Chuyển động dưới nước (Ca nô / Tàu thủy)*:
     - $v_{\text{xuôi dòng}} = v_{\text{thực}} + v_{\text{dòng nước}}$
     - $v_{\text{ngược dòng}} = v_{\text{thực}} - v_{\text{dòng nước}}$

---

### Dạng 2: Bài Toán Năng Suất & Công Việc Chung - Riêng
- **Công thức cốt lõi**: $\text{Khối lượng công việc} = \text{Năng suất} \times \text{Thời gian}$.
- **Quy ước công việc chung - riêng**:
  - Coi toàn bộ công việc hoàn thành là **$1$**.
  - Nếu làm một mình xong trong $x$ ngày $\implies$ Mỗi ngày làm được $\dfrac{1}{x}$ công việc.
  - Hai người/đội cùng làm thì năng suất cộng dồn: $\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{t_{\text{chung}}}$.
- **Kịch bản kế hoạch & thực tế**: Theo kế hoạch mỗi ngày làm $x$ sản phẩm; thực tế mỗi ngày vượt mức $m$ sản phẩm ($x + m$).

---

### Dạng 3: Bài Toán Có Nội Dung Hình Học
- **Công thức cốt lõi**:
  - Hình chữ nhật: Chu vi $P = 2(a + b)$, Diện tích $S = a \times b$.
  - Tam giác vuông: Diện tích $S = \dfrac{1}{2} a \times b$, Định lý Pytago $a^2 + b^2 = c^2$.
- **Kịch bản**: Tăng chiều dài, giảm chiều rộng thì diện tích thay đổi.

---

### Dạng 4: Bài Toán Quan Hệ Số & Chữ Số
- **Công thức cốt lõi**:
  - Số có 2 chữ số: $\overline{ab} = 10a + b$ ($a \in \mathbb{N}^*, 1 \le a \le 9; b \in \mathbb{N}, 0 \le b \le 9$).
  - Số có 3 chữ số: $\overline{abc} = 100a + 10b + c$.
- **Kịch bản**: Viết thêm chữ số vào bên trái/phải, đổi chỗ hai chữ số cho nhau.

---

### Dạng 5: Bài Toán Thực Tế Kinh Tế, Tài Chính & Phần Trăm
- **Công thức cốt lõi**:
  - Giá sau khi giảm $p\%$: $\text{Giá mới} = \text{Giá gốc} \times (1 - p\%)$.
  - Giá sau khi tăng $p\%$: $\text{Giá mới} = \text{Giá gốc} \times (1 + p\%)$.
  - Nồng độ phần trăm: $C\% = \dfrac{m_{\text{chất tan}}}{m_{\text{dung dịch}}} \times 100\%$.
- **Kịch bản**: Hai mặt hàng có tổng giá trị niêm yết, nhân dịp khuyến mãi mặt hàng 1 giảm $x\%$, mặt hàng 2 giảm $y\%$, khách hàng thanh toán tổng cộng $T$ đồng.

---

## ⚠️ 4 Bẫy Đề Thi "Chí Mạng" Cần Tránh (Trap Buster)

| Mã Bẫy | Lỗi Bum Rất Dễ Mắc | Cách Khắc Phục Chuẩn Xác |
| :---: | :--- | :--- |
| **TRAP-01** | **Quên đổi đơn vị thời gian**: Đề cho thời gian nghỉ $15$ phút, để nguyên số $15$ thay vì đổi ra $\dfrac{1}{4}$ giờ. | Đọc đề bài, lấy bút gạch chân tất cả các mốc thời gian có đơn vị "phút" và đổi ngay ra giờ ($\text{giờ} = \dfrac{\text{phút}}{60}$). |
| **TRAP-02** | **Quên đặt điều kiện hoặc đặt thiếu điều kiện cho ẩn**: Quên điều kiện $x \in \mathbb{N}^*$ cho số sản phẩm, số người. | Người, cây cối, xe cộ, sản phẩm $\implies x \in \mathbb{N}^*$. Chiều dài, vận tốc, thời gian $\implies x > 0$. |
| **TRAP-03** | **Quên đối chiếu điều kiện ở kết luận**: Giải ra phương trình bậc hai có $x_1 = 40$ và $x_2 = -10$, vội vàng kết luận cả hai nghiệm. | Luôn viết rõ bên cạnh nghiệm: $40$ (TM), $-10$ (Loại vì $x > 0$). |
| **TRAP-04** | **Nhầm lẫn giữa vận tốc dòng nước và vận tốc canô**: Nhầm công thức $v_{\text{ngược}} = v_{\text{nước}} - v_{\text{thực}}$ dẫn tới vận tốc bị âm. | Luôn nhớ: Thuyền chạy ngược dòng thì vận tốc thực của thuyền phải lớn hơn vận tốc nước: $v_{\text{ngược}} = v_{\text{thực}} - v_{\text{nước}}$. |

---

## 📚 Danh Mục Tài Liệu Kèm Theo

| STT | File Tài Liệu (Markdown) | File Gốc (PDF) | Mô Tả Dạng Bài |
| :---: | :--- | :--- | :--- |
| **01** | [01-toan-chuyen-dong-co-ban-den-nang-cao.md](md/01-toan-chuyen-dong-co-ban-den-nang-cao.md) | *Tài liệu biên soạn nội bộ* | Bảng $S, v, t$, kỹ thuật xử lý thời gian nghỉ, đổi đơn vị phút sang giờ, bài tập có giải chi tiết |
| **02** | [chuyen-de-giai-bai-toan-bang-cach-lap-phuong-trinh.md](md/chuyen-de-giai-bai-toan-bang-cach-lap-phuong-trinh.md) | [chuyen-de-giai-bai-toan-bang-cach-lap-phuong-trinh.pdf](pdf/chuyen-de-giai-bai-toan-bang-cach-lap-phuong-trinh.pdf) | Toàn văn 52 trang: Lý thuyết 7 dạng cơ bản, 13 bài nâng cao, 33 câu trắc nghiệm & bộ 3 phiếu tự luyện (kèm lời giải chi tiết) |



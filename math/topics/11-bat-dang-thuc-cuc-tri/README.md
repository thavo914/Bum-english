# Chuyên Đề 11: Bất Đẳng Thức & Giá Trị Lớn Nhất, Nhỏ Nhất (Câu Điểm 10)

> **Trọng số trong đề thi Tuyển sinh vào lớp 10**: $0.5$ điểm (Câu cuối cùng phân loại học sinh xuất sắc và chọn thủ khoa).

---

## 📂 Cấu Trúc Thư Mục Chuyên Đề

```
math/topics/11-bat-dang-thuc-cuc-tri/
├── README.md               # 📖 Kỹ thuật Cô-si, Cauchy-Schwarz, chọn điểm rơi & đổi biến
├── pdf/                    # 📄 Tài liệu PDF chuyên đề gốc
└── md/                     # 📝 Chuyên đề & bài tập Markdown đã số hóa
```

---

## 🎯 Các Kỹ Thuật Đánh Giá Điểm Rơi Bắt Buộc

1. **Bất đẳng thức AM-GM (Cô-si)**:
   - Cho $a, b \ge 0$: $a + b \ge 2\sqrt{ab}$. Dấu "=" xảy ra $\iff a = b$.
   - Cho $a, b, c \ge 0$: $a + b + c \ge 3\sqrt[3]{abc}$. Dấu "=" xảy ra $\iff a = b = c$.
   - Các hệ quả thường dùng:
     - $(a + b)^2 \ge 4ab$
     - $\dfrac{1}{a} + \dfrac{1}{b} \ge \dfrac{4}{a + b}$ (BĐT cộng mẫu số)
2. **Kỹ thuật chọn điểm rơi (Point of Equality)**:
   - Dự đoán giá trị của các biến khi biểu thức đạt Min/Max (thường là tâm đối xứng: $a = b = c = 1$ hoặc $a = b = \dfrac{1}{2}$).
   - Tách ghép hệ số để bảo toàn dấu bằng khi áp dụng Cô-si.
   - Thêm bớt hạng tử để khử mẫu số.
3. **Bất đẳng thức Cauchy-Schwarz (BĐT Bunhiacopxki)**:
   - Dạng Engel (BĐT Schwarz cộng mẫu):
     $$\dfrac{x_1^2}{a_1} + \dfrac{x_2^2}{a_2} + \dots + \dfrac{x_n^2}{a_n} \ge \dfrac{(x_1 + x_2 + \dots + x_n)^2}{a_1 + a_2 + \dots + a_n}$$
4. **Phương pháp miền giá trị / Đưa về hằng đẳng thức bậc hai**:
   - $P = A(x - x_0)^2 + m \ge m \implies \min P = m$.

---

## ⚠️ Lời Khuyên Chiến Lược Làm Bài Thi Cho Bum

- **Chiến lược làm bài**: Làm câu này SAU CÙNG khi đã kiểm tra kỹ 9.5 điểm đầu tiên ít nhất 2 lần.
- **Không bao giờ áp dụng BĐT Cô-si mà không kiểm tra dấu "="**: Nếu dấu bằng không xảy ra thì toàn bộ bài làm đều bị 0 điểm.

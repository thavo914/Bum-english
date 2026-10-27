# Chuyên Đề 02: Hàm Số Bậc Nhất, Parabol & Tương Giao Đồ Thị

> **Trọng số trong đề thi Tuyển sinh vào lớp 10**: $1.0 - 1.5$ điểm (Đặc biệt là **Bài 1** đề TP.HCM và câu phụ trong đề Hà Nội).

---

## 📂 Cấu Trúc Thư Mục Chuyên Đề

```
math/topics/02-ham-so-va-do-thi/
├── README.md               # 📖 Hướng dẫn lý thuyết, thuật toán giải & bẫy vẽ hình
├── pdf/                    # 📄 Tài liệu PDF chuyên đề gốc
└── md/                     # 📝 Chuyên đề & bài tập Markdown đã số hóa
```

---

## 🎯 Các Dạng Toán Trọng Tâm

1. **Hàm số bậc nhất $y = ax + b$ ($a \ne 0$)**:
   - Tính đồng biến ($a > 0$), nghịch biến ($a < 0$).
   - Điều kiện để điểm $M(x_0; y_0)$ thuộc đồ thị.
   - Vị trí tương đối của hai đường thẳng: cắt nhau ($a \ne a'$), song song ($a = a', b \ne b'$), trùng nhau ($a = a', b = b'$), vuông góc ($a \cdot a' = -1$).
2. **Hàm số bậc hai Parabol $y = ax^2$ ($a \ne 0$)**:
   - Bảng giá trị 5 điểm đối xứng qua trục tung $Oy$.
   - Vẽ đồ thị Parabol chuẩn xác, không bị gãy nét ở đỉnh $O(0;0)$.
3. **Tương giao giữa Parabol $(P): y = ax^2$ và Đường thẳng $(d): y = mx + n$**:
   - Phương trình hoành độ giao điểm: $ax^2 - mx - n = 0$.
   - Số giao điểm tương ứng với số nghiệm của phương trình ($\Delta > 0 \implies 2$ giao điểm, $\Delta = 0 \implies$ tiếp xúc, $\Delta < 0 \implies$ không cắt).
   - Tìm tọa độ giao điểm và tính diện tích tam giác tạo bởi các giao điểm.

---

## ⚠️ Bẫy Đề Thi Cần Tránh Cho Bum

- **Quên điều kiện $a \ne 0$** khi đề bài yêu cầu tìm $m$ để hàm số là hàm bậc nhất hoặc hàm bậc hai.
- **Vẽ Parabol dùng thước thẳng nối điểm**: Parabol là đường cong trơn mượt, bắt buộc vẽ bằng thước cong Parabol (thước mây).
- **Nhầm lẫn giữa hoành độ ($x$) và tung độ ($y$)** khi tìm tọa độ giao điểm.

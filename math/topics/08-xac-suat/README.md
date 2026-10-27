# Chuyên Đề 08: Các Dạng Bài Toán Về Xác Suất (Chương Trình Mới GDPT 2018)

> **Trọng số trong đề thi Tuyển sinh vào lớp 10**: $0.5 - 1.0$ điểm (Phần kiến thức mới cập nhật trong cấu trúc đề thi vào 10 từ năm 2025).

---

## 📂 Cấu Trúc Thư Mục Chuyên Đề

```
math/topics/08-xac-suat/
├── README.md               # 📖 Không gian mẫu, xác suất cổ điển & xác suất thực nghiệm
├── pdf/                    # 📄 Tài liệu PDF chuyên đề gốc
└── md/                     # 📝 Chuyên đề & bài tập Markdown đã số hóa
```

---

## 🎯 Các Dạng Toán Trọng Tâm

1. **Phép thử ngẫu nhiên & Không gian mẫu**:
   - Liệt kê đầy đủ các kết quả có thể xảy ra của phép thử (Tung đồng xu 1-2-3 lần, gieo xúc xắc, rút thẻ bài, chọn học sinh).
   - Xác định số phần tử không gian mẫu $n(\Omega)$.
   - Sử dụng sơ đồ hình cây (Tree diagram) hoặc bảng 2 chiều để không bị đếm sót kết quả.
2. **Xác định biến cố và biến cố thuận lợi**:
   - Biến cố chắc chắn ($P = 1$), biến cố không thể ($P = 0$).
   - Biến cố đối $\bar{A}$: $P(\bar{A}) = 1 - P(A)$.
   - Số kết quả thuận lợi cho biến cố $A$: $n(A)$.
3. **Công thức xác suất cổ điển**:
   $$P(A) = \dfrac{n(A)}{n(\Omega)}$$
   - Ứng dụng: Xác suất lấy được bi cùng màu, quả cầu ghi số nguyên tố, tổng số chấm gieo được chia hết cho 3.
4. **Xác suất thực nghiệm**:
   - Tần số xuất hiện của biến cố trong $N$ lần thử nghiệm lặp lại.
   - Ước lượng xác suất bằng tần số tương đối khi số lần thử $N$ đủ lớn.

---

## ⚠️ Bẫy Đề Thi Cần Tránh Cho Bum

- **Đếm trùng hoặc đếm sót phần tử**: Khi gieo 2 con xúc xắc, không gian mẫu có $6 \times 6 = 36$ phần tử. Cặp $(1; 2)$ và $(2; 1)$ là HAI kết quả khác nhau!
- **Quên biến cố đối**: Với các bài toán có từ khóa *"ít nhất một"*, luôn tính xác suất của biến cố đối *"không có cái nào"* rồi lấy $1 - P(\bar{A})$ sẽ nhanh hơn rất nhiều!

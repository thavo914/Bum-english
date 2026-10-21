---
description: Generates a standardized 30-question CEFR A1-A2 weekly checkpoint test (assessments/test-week-<N>.md) modeled after Grade 10 entrance exams.
---

# Workflow: /generate-weekly-assessment

Use this workflow at the end of each study week (after Day 5) or during weekend review to generate a comprehensive 30-question assessment in `assessments/test-week-<N>.md`.

---

## 🎯 Purpose & Design Principles

1. **Chuẩn Đề Tuyển Sinh Lớp 10**: 30 câu hỏi trắc nghiệm 4 lựa chọn (A, B, C, D) mô phỏng chính xác cấu trúc đề thi chính thức từ ngân hàng đề [graduation exam/question-registry.json](file:///c:/Users/Admin/source/repos/nephew-english/graduation%20exam/question-registry.json).
2. **Đánh Giá Toàn Diện Sau 1 Tuần**: Tổng hợp ngữ pháp và 25 từ vựng đã học trong 5 ngày vừa qua, kết hợp kiểm tra 1–2 bẫy ngữ pháp của tuần trước để đánh giá mức độ làm chủ.
3. **Cập Nhật Vòng Đời Lỗi Sai (`MISTAKE_LOG.md`)**:
   - Những câu Bum làm đúng -> Chuyển trạng thái sang 🟢 **Mastered** (không hỏi lại nữa).
   - Những câu Bum làm sai -> Ghi nhận vào [assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/assessments/MISTAKE_LOG.md) với trạng thái 🔴 **Active** để đưa vào tuần kế tiếp.
4. **Không Baby Talk - Teen Focused**: Bối cảnh đề thi sinh động, xoay quanh game, công nghệ, bóng đá, đời sống bạn bè, đồ ăn vặt và phim ảnh.

---

## 📂 Target File Location
Mỗi bài test tuần được lưu tại:
```
assessments/
└── test-week-<N>.md   # Ví dụ: test-week-01.md, test-week-02.md, test-week-03.md
```

---

## 📋 Cấu Trúc Chuẩn 30 Câu Hỏi (Standard 30-Question Blueprint)

Mỗi bài test tuần có thời gian làm bài **35 – 45 phút**, gồm đúng 3 phần:

### 1. PHẦN 1: GRAMMAR & SENTENCE STRUCTURES (10 Câu: Q1 – Q10)
- **Q1 – Q6**: Kiểm tra trực tiếp các cấu trúc ngữ pháp học trong tuần (thì động từ, câu điều kiện, so sánh, đại từ, liên từ).
- **Q7 – Q8**: Kiểm tra các bẫy ngữ pháp đề thi hay ra (*Watch Out traps*).
- **Q9 – Q10**: **Spiral Review**: 2 câu kiểm tra lại các lỗi 🔴 Active hoặc 🟡 In-Review từ tuần trước để xác nhận Bum đã nhớ dạng hay chưa.

### 2. PHẦN 2: VOCABULARY & COLLOCATIONS (10 Câu: Q11 – Q20)
- **Q11 – Q16**: Kiểm tra từ vựng mục tiêu học trong tuần (nghĩa theo ngữ cảnh, cụm từ cố định *collocations*).
- **Q17 – Q18**: Cụm động từ (*Phrasal Verbs*) hoặc Từ đồng nghĩa/trái nghĩa cơ bản.
- **Q19 – Q20**: Biến đổi từ loại (*Word form*) hoặc cấu tạo từ tính từ/danh từ.

### 3. PHẦN 3: GIAO TIẾP, BIỂN BÁO & ĐỌC HIỂU (10 Câu: Q21 – Q30)
- **Q21 – Q24**: Giao tiếp tình huống hàng ngày tuổi teen (đáp lại lời rủ rê, khen ngợi, mượn đồ, xin lỗi, cảm ơn).
- **Q25 – Q26**: Đọc hiểu biển báo giao thông hoặc thông báo ngắn (*Signs & Notices*).
- **Q27 – Q30**: Đọc hiểu 1 đoạn tin nhắn nhóm Discord/Zalo hoặc 1 đoạn văn ngắn (4 câu hỏi: ý chính, chi tiết sự thật, từ thay thế, suy luận).

---

## 📝 Template Chuẩn Của File `assessments/test-week-<N>.md`

```markdown
# 🎯 CEFR A1–A2 Progress Test: Week <N> Checkpoint (Bài Test Đánh Giá Tuần <N>)
### Dành riêng cho Bum (14 tuổi – THCS Lớp 8/9)
> **Mục tiêu**: Đánh giá toàn diện kiến thức Tuần <N> (<Tên Theme>) và kiểm tra mức độ khắc phục các bẫy ngữ pháp.

---

## 📌 Hướng dẫn làm bài (Test Instructions)
- **Thời gian làm bài gợi ý**: 35 – 45 phút.
- **Số lượng**: Đúng 30 câu trắc nghiệm (Chọn **A, B, C**, hoặc **D**).
- **Lưu ý**: Hãy tự tin làm bài theo phản xạ tự nhiên của mình. Sau khi làm xong, hãy mở phần Đáp án chi tiết ở cuối trang để đối chiếu và xem giải mã từng câu nhé!

---

## 📝 PHẦN 1: GRAMMAR & SENTENCE BUILDER (Cấu Trúc & Ngữ Pháp Cốt Lõi)
*Chọn đáp án chính xác nhất để hoàn thành câu.*

#### Question 1
<Sentence stem>
- A. ...
- B. ...
- C. ...
- D. ...

... (Question 2 đến Question 10)

---

## 📝 PHẦN 2: VOCABULARY & COLLOCATIONS (Từ Vựng & Cụm Từ)
*Chọn từ hoặc cụm từ thích hợp nhất.*

#### Question 11
<Sentence stem>
- A. ...
- B. ...
- C. ...
- D. ...

... (Question 12 đến Question 20)

---

## 📝 PHẦN 3: GIAO TIẾP, BIỂN BÁO & ĐỌC HIỂU (Situational, Signs & Reading)

#### Question 21
<Dialogue stem: e.g. Phong: "..." - Nam: "...">
- A. ...
- B. ...
- C. ...
- D. ...

... (Question 22 đến 26)

*Đọc đoạn tin nhắn / thông báo sau và trả lời các câu hỏi từ 27 đến 30:*
<Short reading passage / Discord chat text>

#### Question 27
<Question on passage>
- A. ...
- B. ...
- C. ...
- D. ...

... (Question 28 đến Question 30)

---

<details>
<summary>Click to reveal Answer Key & Detailed Explanations 🔍</summary>

### 🔑 BẢNG ĐÁP ÁN NHANH (Answer Table)
| 1. | 2. | 3. | 4. | 5. | 6. | 7. | 8. | 9. | 10. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | | | | | | | | |

| 11. | 12. | 13. | 14. | 15. | 16. | 17. | 18. | 19. | 20. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | | | | | | | | |

| 21. | 22. | 23. | 24. | 25. | 26. | 27. | 28. | 29. | 30. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | | | | | | | | |

### 📖 HƯỚNG DẪN GIẢI CHI TIẾT
- **Câu 1: <Đáp án đúng>**
  *Giải thích*: <Giải thích ngắn gọn 1-2 câu, nêu rõ công thức ngữ pháp>
...
- **Câu 30: <Đáp án đúng>**
  *Giải thích*: ...

</details>

---

## 📊 BẢNG ĐÁNH GIÁ KẾT QUẢ & ĐIỀU CHỈNH TIẾN ĐỘ
| Số câu đúng | Xếp loại năng lực | Đánh giá & Hướng xử lý |
| :---: | :---: | :--- |
| **25 – 30 / 30** | ⭐ ⭐ ⭐ **Mastered (Xuất sắc)** | Nắm chắc toàn bộ kiến thức tuần. Chuyển các bẫy lỗi sang 🟢 **Mastered** trong `MISTAKE_LOG.md`. Sẵn sàng 100% cho tuần mới! |
| **18 – 24 / 30** | ⭐ ⭐ **Good (Khá tốt)** | Nắm được kiến thức cơ bản. Xem lại 1-2 câu sai ở phần Giải thích chi tiết, ghi nhận vào `MISTAKE_LOG.md` để củng cố tiếp. |
| **< 18 / 30** | ⭐ **Review Needed (Cần ôn lại)** | Cần xem lại các file `01-knowledge.md` trong tuần và làm lại các câu bị sai trước khi qua tuần mới. |
```

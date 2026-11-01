---
description: Generates a standardized 30-question weekly checkpoint test (assessments/test-week-<N>.md) modeled after Grade 10 entrance exams (Hybrid format: MCQs + Productive writing from Week 4 onwards).
---

# Workflow: /generate-weekly-assessment

Use this workflow at the end of each study week (after Day 5) or during weekend review to generate a comprehensive 30-question assessment in `assessments/test-week-<N>.md`.

---

## 🎯 Purpose & Design Principles (Cơ Chế Phân Tầng 2 Giai Đoạn)

1. **Chuẩn Đề Tuyển Sinh Lớp 10 Theo Giai Đoạn**:
   - 🟢 **Giai đoạn 1 (Tuần 1 – Tuần 3)**: 30 câu trắc nghiệm 4 lựa chọn (A, B, C, D) cấp độ A1–A2 nhằm củng cố nhận thức cơ bản.
   - 🚀 **Giai đoạn 2 (Tuần 4 – Tuần 10)**: **Chuẩn Hybrid Đột Phá** gồm **20 câu trắc nghiệm khách quan** (mô phỏng kỹ năng tư duy & đọc hiểu của Đề Hà Nội) + **10 câu tự luận sản sinh** (Word Formation, Tra cứu mục từ điển, Viết lại câu chuẩn xác của Đề TP.HCM).
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
└── test-week-<N>.md   # Ví dụ: test-week-01.md, test-week-02.md, test-week-04.md
```

---

## 📋 Cấu Trúc Chuẩn 30 Câu Hỏi (Hybrid Blueprint Dành Cho Tuần 4 Trở Đi)

Thời gian làm bài: **45 phút**, gồm đúng 2 phần lớn:

### 🅰️ PHẦN 1: TRẮC NGHIỆM KHÁCH QUAN (20 Câu: Q1 – Q20)
- **Q1 – Q4: Ngữ âm & Trọng âm (Phonetics)**:
  - 2 câu phát âm (ưu tiên bẫy đuôi *-ed* ngoại lệ và các âm dễ nhầm /s/, /k/, /tʃ/).
  - 2 câu trọng âm từ 2 và 3 âm tiết.
- **Q5 – Q10: Ngữ pháp, Từ vựng & Hội thoại đời sống (Conversational Grammar & Vocab)**:
  - Đặt câu hỏi trong bối cảnh đối thoại 2 người (Son-Mom, Bum-Leo, Clerk-Customer).
  - Kiểm tra thì động từ, liên từ (*although, because, or, if*), mạo từ, đại từ quan hệ và phrasal verbs.
- **Q11 – Q12: Đọc hiểu Biển báo & Tin nhắn thực tế (Signs & Notices)**:
  - Đọc biển thông báo thiết bị điện tử / siêu thị / quy định công cộng.
- **Q13 – Q16: Đọc điền đoạn văn (Cloze Test)**:
  - Đoạn văn ngắn 120-150 từ về chủ đề Teen Tech, AI, thói quen sinh hoạt (kiểm tra từ loại, liên từ, từ vựng theo ngữ cảnh).
- **Q17 – Q18: Tư duy cấu trúc văn bản (Text Coherence - Form Hà Nội 2025)**:
  - 1 câu chọn câu chủ đề (Topic Sentence) mở đầu đoạn văn.
  - 1 câu sắp xếp 3 mệnh đề (a–b–c) thành đoạn văn logic.
- **Q19 – Q20: Spiral Review (Phục thù bẫy cũ)**:
  - 2 câu trắc nghiệm bẫy kiểm tra lại các lỗi 🔴 **Active** trong `MISTAKE_LOG.md`.

---

### 🅱️ PHẦN 2: TỰ LUẬN SẢN SINH (10 Câu: Q21 – Q30)
- **Q21 – Q24: Cấu tạo từ tự luận (Word Formation - Form TP.HCM Q29–Q34)**:
  - Cho từ gốc trong ngoặc `(CAPITALS)`, thí sinh tự xác định và viết từ loại (Noun/Adj/Adv) đúng chính tả. Tuyệt đối không cho gợi ý trắc nghiệm.
- **Q25 – Q26: Khai thác mục từ điển (Dictionary Entry Comprehension - Form TP.HCM Q35–Q36)**:
  - Cho 1 khung trích xuất mục từ điển (ví dụ: từ `habit`, `routine`, `energy`), yêu cầu điền cụm từ phù hợp ngữ cảnh (không quá 3 từ).
- **Q27 – Q30: Viết lại câu tự luận hoàn chỉnh (Sentence Transformation - Form TP.HCM Q37–Q40)**:
  - Viết lại câu giữ nguyên nghĩa với cấu trúc tuyển sinh: *wish*, *don't mind + V-ing*, *run out of*, *Although / In spite of*, *look forward to + V-ing*.

---

## 📝 Template Chuẩn Của File `assessments/test-week-<N>.md` (Tuần 4+)

```markdown
# 🎯 CEFR A2 → A2+ Progress Test: Week <N> Checkpoint (Bài Test Chuẩn Hybrid)
### Dành riêng cho Bum (14 tuổi – THCS Lớp 8/9 chuẩn bị thi vào lớp 10)
> **Mục tiêu**: Đánh giá toàn diện kiến thức Tuần <N> (<Tên Theme>), rèn luyện phản xạ trắc nghiệm logic (chuẩn Hà Nội) và năng lực tự luận sản sinh (chuẩn TP.HCM).

---

## 📌 Hướng dẫn làm bài (Test Instructions)
- **Thời gian làm bài gợi ý**: 45 phút.
- **Cấu trúc đề**: 20 câu Trắc nghiệm khách quan + 10 câu Tự luận viết tay.
- **Lưu ý**: Viết câu trả lời tự luận thật cẩn thận, đúng chính tả từng từ. Sau khi hoàn thành toàn bộ, nhấp vào phần Đáp án chi tiết để tự chấm điểm!

---

## 📝 PHẦN 1: TRẮC NGHIỆM KHÁCH QUAN (20 Questions - 6.0 Điểm)
*Mark the letter A, B, C or D on your answer sheet to indicate the correct answer.*

#### Question 1 (Pronunciation)
...
#### Question 5 (Conversational Grammar)
...
#### Question 11 (Sign & Notice)
...
#### Question 13 (Cloze Reading)
...
#### Question 17 (Text Coherence / Sentence Ordering)
...
#### Question 19 (Spiral Review)
...

---

## 📝 PHẦN 2: TỰ LUẬN SẢN SINH (10 Questions - 4.0 Điểm)

### I. Word Formation (Use the correct form of the word in capitals)
21. Teenagers should develop __________ habits to stay energetic. (HEALTH)
22. We are looking forward to __________ our robotics project next week. (PRESENT)
23. The cleaning robot works __________ and saves a lot of time. (AUTOMATIC)
24. He made a sudden __________ to change his daily routine. (DECIDE)

### II. Dictionary Entry Comprehension
> ### 📖 Dictionary Entry: <Word>
> <Extract from dictionary with definitions and bold examples>

25. Bum is trying to ______________________ of staying up late. (Do not use more than THREE words)
26. Healthy ______________________ play an important role in focus and health. (Do not use more than THREE words)

### III. Sentence Transformation (Rewrite each sentence so that it means the same)
27. Bum doesn't have a smartwatch, and he really wants to have one.  
   → Bum wishes _______________________________________________________________.
28. Lucie doesn't mind helping her friends with math exercises after class.  
   → It doesn't matter to Lucie to ______________________________________________.
29. Our wireless mouse has run out of battery.  
   → There is no battery left __________________________________________________.
30. Although the technology project was challenging, our team completed it on time.  
   → In spite of ______________________________________________________________.

---

<details>
<summary>Click to reveal Answer Key & Detailed Explanations 🔍</summary>

### 🔑 BẢNG ĐÁP ÁN TRẮC NGHIỆM (Part 1)
| 1. | 2. | 3. | 4. | 5. | 6. | 7. | 8. | 9. | 10. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | | | | | | | | |

| 11. | 12. | 13. | 14. | 15. | 16. | 17. | 18. | 19. | 20. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | | | | | | | | |

### ✍️ ĐÁP ÁN TỰ LUẬN (Part 2)
- **21. healthy** *(Giải thích từ loại & cấu trúc)*
- **22. presenting**
- **23. automatically**
- **24. decision**
- **25. break the habit**
- **26. eating habits**
- **27. he had a smartwatch**
- **28. help her friends with math exercises after class**
- **29. in our wireless mouse**
- **30. the challenge of the technology project, our team...**

</details>

---

## 📊 BẢNG ĐÁNH GIÁ KẾT QUẢ & ĐIỀU CHỈNH TIẾN ĐỘ
| Điểm số quy đổi | Xếp loại năng lực | Đánh giá & Hướng xử lý |
| :---: | :---: | :--- |
| **8.5 – 10.0 đ (26–30 câu)** | ⭐ ⭐ ⭐ **Mastered (Xuất sắc)** | Hoàn toàn làm chủ cả trắc nghiệm và tự luận. Sẵn sàng bứt phá các chủ đề tiếp theo! Chuyển các lỗi kiểm tra sang 🟢 **Mastered** trong `MISTAKE_LOG.md`. |
| **6.5 – 8.0 đ (20–25 câu)** | ⭐ ⭐ **Good (Khá tốt)** | Nắm chắc trắc nghiệm, cần rèn thêm độ chính xác khi viết từ loại và viết lại câu tự luận. Cập nhật các lỗi sai vào `MISTAKE_LOG.md`. |
| **< 6.5 đ (< 20 câu)** | ⭐ **Review Needed (Cần ôn lại)** | Cần xem lại các bảng Word Family trong `01-knowledge.md` và luyện viết lại câu trước khi sang tuần mới. |
```

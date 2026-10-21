---
description: Generates a complete 2-file daily lesson (01-knowledge.md and 02-exercises.md) for Bum (14 years old) with exercises aligned to Grade 10 entrance exams and targeted mistake recycling.
---

# Workflow: /generate-daily-lesson

Use this workflow to generate the 2 daily lesson files for any designated day (`day-01` to `day-05`) in a week folder (`lessons/week-<N>/`).

---

## 🎯 Target Persona & Level Constraints
- **Audience**: **Bum**, a 14-year-old student (Grade 8 / 9, Secondary School / THCS).
- **Target Level**: Strictly **CEFR A1–A2** (Elementary / Pre-intermediate).
- **Tone**: Cool, relatable, encouraging (gaming, tech, football, friends, school life, snacks, anime).
- **Strictly Avoid**: Toddler baby talk, academic jargon, and adult corporate buzzwords.
- **Time Commitment**: 30–35 minutes total (10 mins reading knowledge, 15 mins exercises, 5–10 mins speaking with AI Buddy Leo).

### 🎓 3 Core Principles for Exercise Quality:
1. **Bám Sát Đề Thi Mẫu (Exam Pattern Alignment)**:
   - Part 2 và Part 3 phải mô phỏng chính xác cấu trúc đề thi tuyển sinh vào lớp 10 chính thức từ ngân hàng câu hỏi `graduation exam/question-registry.json` (Trắc nghiệm 4 lựa chọn A/B/C/D, Viết lại câu có mũi tên gợi ý `→`, Biến đổi từ loại `(CAPITALS)`).
   - Tham khảo và tra cứu câu hỏi mẫu bằng lệnh: `py scripts/query_registry.py --category <dạng> --level A2`.
2. **Nhắc Lại Lỗi Sai Có Chọn Lọc (Targeted Error Rematch & Anti-Repetition)**:
   - Trước khi tạo bài tập, luôn kiểm tra sổ theo dõi lỗi sai [assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/assessments/MISTAKE_LOG.md).
   - **Chỉ chọn các lỗi đang có trạng thái 🔴 Active hoặc 🟡 In-Review**.
   - **TUYỆT ĐỐI KHÔNG lặp lại các lỗi đã 🟢 Mastered**: Khi Bum đã nhớ dạng bài và làm chủ kiến thức ở bài test tuần, dừng việc tạo câu hỏi phục thù cho dạng đó để tránh nhàm chán.
   - Mỗi file bài tập hàng ngày chỉ cần 1 câu "Thử Thách Phục Thù (Rematch Challenge)" thuộc nhóm 🔴 Active để củng cố phản xạ.
3. **Tránh Trùng Lặp (Context Variety)**:
   - Đảm bảo câu hỏi có ngữ cảnh mới mẻ, thay đổi tình huống giữa các ngày (ví dụ: Day 1 về game co-op, Day 2 về so sánh đồ công nghệ, Day 3 về đồ ăn vặt căng-tin, Day 4 về đá bóng, Day 5 về rủ rê xem phim).
   - Tuyệt đối không sao chép nguyên văn câu mẫu từ phần Knowledge sang phần Bài tập.

---

## 📂 Exact 2-File Directory Target
For the target week `<N>` and day `<M>`, generate exactly two files:
```
lessons/week-<N>/day-<M>/
├── 01-knowledge.md      # Definitions, 5 target words, 1 grammar bite, mini dialogue
└── 02-exercises.md      # Puzzles, exam-pattern builder, sentence rewriting, error rematch, AI voice mission, answers
```

> 💡 **Weekly Checkpoint Assessment**: Sau khi hoàn thành Day 5, sử dụng workflow `/generate-weekly-assessment` để tạo bài kiểm tra tổng hợp 30 câu hỏi tại `assessments/test-week-<N>.md` nhằm đo lường sự tiến bộ và cập nhật trạng thái lỗi sai trong [assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/assessments/MISTAKE_LOG.md).

---

## 📝 File 1: `01-knowledge.md` Structure

Every `01-knowledge.md` must follow this standardized template:

```markdown
# Day <M>: <Engaging Teen Title with Icon> 🎮

Brief 1-sentence friendly intro explaining what the student will learn today.

---

## 1. Word Power (5 Words for Today)

> 💡 **Đa Dạng Loại Từ (Word Class Diversity)**: 5 từ mục tiêu mỗi ngày nên phân bổ đa dạng gồm **Danh từ (n)**, **Động từ (v)**, **Tính từ (adj)** và **Cụm động từ (phrasal verb)** để chuẩn bị phản xạ cho câu hỏi Word Form và Cụm từ trong đề thi tuyển sinh lớp 10.

| Word | Loại từ (Type) | Pronunciation (IPA) | Vietnamese Meaning | Example Sentence |
| :--- | :---: | :--- | :--- | :--- |
| **<word 1>** | *(n) - danh từ* | /.../ | <nghĩa tiếng Việt gần gũi> | *<Teen example sentence in gaming, school, or friends>* |
| **<word 2>** | *(v) - động từ* | /.../ | ... | ... |
| **<word 3>** | *(adj) - tính từ* | /.../ | ... | ... |
| **<word 4>** | *(phr v) - cụm động từ* | /.../ | ... | ... |
| **<word 5>** | *(n/v) - danh/động từ* | /.../ | ... | ... |

> 💡 **Mở rộng cụm động từ & từ loại liên quan**:  
> • **<phrasal verb>** *(phr v)*: <ý nghĩa>  
> • **<derived word>** *(adj/n)*: <ý nghĩa>

---

## 2. Grammar Bite: <Core Grammar Pattern> ⚡

Explain the grammar rule in simple, crystal-clear terms with zero academic bloat.

### The Rule Formula:
- **<Subject>** + **<Grammar Element>** + **<Object/Complement>**
  - *<Clear Example 1>*
  - *<Clear Example 2>*

### ⚠️ Watch Out! (Bẫy đề thi hay gặp):
> 💡 **Watch out**: <Chỉ rõ bẫy ngữ pháp thường gặp trong đề thi lớp 10 hoặc lỗi Bum hay mắc, ví dụ: "Chủ ngữ ghép 'My brother and I' là 2 người -> dùng ARE chứ không chia AM theo chữ I đứng sát cạnh! ❌">

---

## 3. Mini-Dialogue: <Lively Teen Scenario> 🎧
A 4-line realistic dialogue between two friends or with AI Buddy Leo using today's words and grammar.
- **<Character A>**: "..."
- **<Character B>**: "..."
- **<Character A>**: "..."
- **<Character B>**: "..."
```

---

## 📝 File 2: `02-exercises.md` Structure

Every `02-exercises.md` must follow this standardized template:

```markdown
# Day <M>: Interactive Exercises & AI Mission 🚀

Complete these challenges to earn your 3 Stars today!

---

## Part 1: Word Match & Context Fill-in (Warm-up)
Word bank of 5 target words. 5 sentences with blanks set in authentic teen situations.

---

## Part 2: Grammar Builder (Form Chuẩn Đề Thi Tuyển Sinh) 🎯
*5 câu hỏi trắc nghiệm A, B, C, D mô phỏng chính xác form đề thi vào lớp 10, tập trung vào cấu trúc ngữ pháp hôm nay.*

#### Question 1
<Sentence with blank ______>
- A. <Option A>
- B. <Option B>
- C. <Option C>
- D. <Option D>

... (Question 2 đến 5)

---

## Part 3: Sentence Transformation & Mini-Translation (Viết Lại Câu & Dịch) ✏️
*3-4 câu luyện phản xạ diễn đạt và biến đổi câu theo form đề thi chính thức.*

1. <Vietnamese teen situation to translate into English>
   → __________________________________________________
2. <Sentence transformation with prompt: e.g. "Ted worked hard, so he got high marks.">
   → Because __________________________________________
3. <Sentence transformation or sentence builder from word prompts>
   → __________________________________________________

---

## Part 4: Thử Thách Phục Thù (Rematch Challenge - Real Exam Question) 🥊
*1 câu hỏi được trích xuất hoặc mô phỏng từ đề thi thật các tỉnh (tham khảo `graduation exam/question-registry.json`), chỉ nhắm vào 1 lỗi có trạng thái 🔴 **Active** trong [assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/assessments/MISTAKE_LOG.md). (Các lỗi đã 🟢 Mastered sẽ không lặp lại).*

#### Câu Phục Thù 1 *(Lấy cảm hứng từ Đề thi <Tỉnh> <Năm>)*
<Question stem targeting Bum's known mistake>
- A. ...
- B. ...
- C. ...
- D. ...
💡 *Gợi ý phục thù*: <Gợi ý ngắn 1 dòng nhắc Bum nhớ lại bẫy mà cháu từng vấp phải>

---

## Part 5: AI Voice Mission with Leo 🎙️
An interactive prompt for the student to speak with ChatGPT Voice Mode or Gemini Live Buddy Leo:
> **Your Mission Prompt**:  
> *"Hey Leo! I am 14 years old. Today I learned about [Topic]. Ask me 3 quick questions about [Topic] in simple English!"*

**Speaking Checklist**:
- [ ] Checklist item 1 (use 2 target words)
- [ ] Checklist item 2 (use today's grammar pattern)

---

<details>
<summary>Click to reveal Answer Key 🔍</summary>

### Part 1 Answers:
1. ...
2. ...

### Part 2 Answers:
1. **<A/B/C/D>** - *<Giải thích ngắn gọn 1 câu>*
2. ...

### Part 3 Suggested Translations:
1. ...
2. ...

### Part 4 Rematch Answer:
1. **<Đáp án đúng>** - *<Giải thích tại sao tránh được bẫy cũ>*

</details>

---

## 🏆 Daily Scorecard
- [ ] Part 1 & 2 Complete (1 Star ⭐)
- [ ] Part 3 & 4 (Phục Thù) Complete (1 Star ⭐)
- [ ] AI Leo Voice Mission Complete (1 Star ⭐)  
**Total Stars Earned Today**: ⭐ ⭐ ⭐ / 3
```

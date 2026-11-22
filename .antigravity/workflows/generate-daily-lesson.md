---
description: Generates a complete 2-file daily lesson (01-knowledge.md and 02-exercises.md) for Bum (14 years old) with exercises aligned to Grade 10 entrance exams, targeted mistake recycling, Linearthinking S-V-O dissection, and Sound-Block Chunking.
---

# Workflow: /generate-daily-lesson

Use this workflow to generate the 2 daily lesson files for any designated day (`day-01` to `day-05`) in a week folder (`lessons/week-<N>/`).

---

## 🎯 Target Persona & Level Constraints (Cơ Chế Phân Tầng 2 Giai Đoạn)

- **Audience**: **Bum**, a 14-year-old student (Grade 8 / 9, Secondary School / THCS chuẩn bị thi vào lớp 10 THPT).
- **Target Level (Theo giai đoạn tuần học)**:
  - 🟢 **Giai đoạn 1 (Tuần 1 – Tuần 3 - Khởi động nền tảng)**: CEFR A1–A2. Câu ngắn, từ vựng quen thuộc, bài tập nhận biết cơ bản có Word Bank trợ giúp.
  - 🚀 **Giai đoạn 2 (Tuần 4 – Tuần 10 - Bứt phá Đề thi Tuyển sinh)**: CEFR A2 → A2+ / Tiệm cận B1. Đẩy mạnh tự luận sản sinh (Productive Writing), Cấu tạo từ (Word Formation không có Word Bank), phân tích ngữ cảnh hội thoại đa lượt lời, tra cứu mục từ điển và sắp xếp câu logic theo chuẩn đề thi Hà Nội & TP.HCM mới nhất.
- **Tone**: Cool, relatable, encouraging (gaming, tech gadgets, football, friends, school life, snacks, anime).
- **Strictly Avoid**: Toddler baby talk, academic jargon, and adult corporate buzzwords.
- **Time Commitment**: 30–35 minutes total (10 mins reading knowledge, 15 mins exercises, 5–10 mins speaking with AI Buddy Leo).

---

### 🎓 4 Core Principles for Exercise Quality:
1. **Bám Sát Đề Thi Mẫu Chuẩn Hybrid (Hà Nội & TP.HCM)**:
   - Part 2 và Part 3 phải mô phỏng chính xác cấu trúc đề thi tuyển sinh vào lớp 10 chính thức từ ngân hàng câu hỏi `graduation exam/question-registry.json` (Trắc nghiệm hội thoại đời sống, Biến đổi từ loại `(CAPITALS)`, Tra cứu mục từ điển, Viết lại câu tự luận).
   - Tra cứu câu hỏi mẫu: `& "C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe" scripts/query_registry.py --category <dạng> --level A2`.
2. **Nhắc Lại Lỗi Sai Có Chọn Lọc (Targeted Error Rematch & Anti-Repetition)**:
   - Trước khi tạo bài tập, luôn kiểm tra sổ theo dõi lỗi sai [assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/assessments/MISTAKE_LOG.md).
   - **Chỉ chọn các lỗi đang có trạng thái 🔴 Active hoặc 🟡 In-Review**.
   - **TUYỆT ĐỐI KHÔNG lặp lại các lỗi đã 🟢 Mastered**: Khi Bum đã nhớ dạng bài và làm chủ kiến thức ở bài test tuần, dừng việc tạo câu hỏi phục thù cho dạng đó để tránh nhàm chán.
3. **Tránh Trùng Lặp (Context Variety)**:
   - Đảm bảo câu hỏi có ngữ cảnh mới mẻ, thay đổi tình huống giữa các ngày (ví dụ: Day 1 về thói quen buổi sáng, Day 2 về robot dọn phòng & smartwatch, Day 3 về cai doomscrolling, Day 4 về thuyết trình dự án công nghệ, Day 5 về thử thách 24h).
   - Tuyệt đối không sao chép nguyên văn câu mẫu từ phần Knowledge sang phần Bài tập.
4. **Phương Pháp Linearthinking & Sound-Block Chunking (Tư Duy Tuyến Tính & Ngắt Hơi Nhịp Điệu)**:
   - **Linearthinking Simplify**: Trong phần Ngữ pháp và Viết lại câu, luôn bóc tách khung cốt lõi `S - V - O` loại bỏ nhiễu, giúp Bum triệt tiêu thói quen dịch từng chữ (word-by-word) từ tiếng Việt.
   - **Sound-Block Chunking (`/`)**: Mọi câu ví dụ trong phần Word Power và các lời thoại đều được gắn ký hiệu ngắt nhịp `/` để hướng dẫn Bum lấy hơi theo cụm nghĩa nhịp nhàng khi nói.

---

## 📂 Exact 2-File Directory Target
For the target week `<N>` and day `<M>`, generate exactly two files:
```
lessons/week-<N>/day-<M>/
├── 01-knowledge.md      # Definitions, Target words/Word families, S-V-O Grammar bite & traps, Dialogue with Sound Blocks
└── 02-exercises.md      # Word formation, Exam-pattern builder, Practical format, S-V-O Sentence rewrite, Rematch, AI voice mission
```

---

## 📝 File 1: `01-knowledge.md` Structure

### 🔹 Dành Cho Tuần 4 Trở Đi (Giai Đoạn Bứt Phá Đề Thi):
```markdown
# Day <M>: <Engaging Teen Title with Icon> 🎮

Brief 1-sentence friendly intro explaining what the student will learn today.

---

## 1. Word Power & Word Family Tree (Từ Vựng & Bảng Họ Từ) 🌲

| Từ gốc (Base Word) | Phiên âm (IPA) | Nghĩa tiếng Việt | Họ từ liên quan (Word Family) | Ví dụ ngắt nhịp Sound-Block (`/`) |
| :--- | :---: | :--- | :--- | :--- |
| **<word 1>** *(v)* | /.../ | <nghĩa> | • **<Noun>**: <nghĩa><br>• **<Adj>**: <nghĩa> | *Eating fresh fruit / every morning / is **healthy** for your brain.* |
| **<word 2>** *(adj)* | /.../ | <nghĩa> | • **<Adv>**: <nghĩa><br>• **<Noun>**: <nghĩa> | *Bum was **careless** / and lost his game checkpoint / last night.* |
| **<word 3>** *(n)* | /.../ | <nghĩa> | • **<Adj>**: <nghĩa><br>• **<Opposite Adj>**: <nghĩa> | ... |
| **<word 4>** *(phr v)* | /.../ | <nghĩa> | • **<Collocation>**: <cụm đi kèm> | ... |
| **<word 5>** *(adj/v)* | /.../ | <nghĩa> | • **<Derived form>**: <từ phái sinh> | ... |

> 💡 **Mẹo Soi Vị Trí Từ Loại Trong Đề Thi (Part of Speech Clues)**:
> - Sau tính từ sở hữu (*my, your, their*) hoặc mạo từ (*a, an, the*) + tính từ → cần một **DANH TỪ (Noun)**.
> - Sau động từ to-be (*is, are, was, were*) hoặc động từ chỉ cảm giác (*feel, look, seem*) → cần một **TÍNH TỪ (Adj)**.
> - Đứng sau động từ thường hoặc đứng đầu/cuối câu bổ nghĩa cho cả hành động → cần một **TRẠNG TỪ (Adv đuôi -ly)**.

---

## 2. Grammar Bite: <Core Grammar Pattern> & Linearthinking Simplify ⚡

Explain the grammar rule in simple, crystal-clear terms with zero academic bloat.

### 🧠 Linearthinking Simplify (Bóc Tách Khung Xương Sống `S - V - O`):
- **Khung Cốt Lõi (`S - V - O`)**: `[Chủ ngữ S]` + `[Động từ V]` + `[Tân ngữ O]`
- **Thành Phần Bổ Bổ Sung**: `[Trạng ngữ thời gian/nơi chốn]` hoặc `[Mệnh đề quan hệ / Cụm giới từ]`
- *Ví dụ mẫu*:
  - *Câu đầy đủ*: *"My brother and I / usually play Roblox / in our bedroom / after finishing homework."*
  - *Khung cốt lõi*: `My brother and I` (S) + `play` (V) + `Roblox` (O).

### ⚠️ Watch Out! (Bẫy Đề Thi Tuyển Sinh Hay Ra):
> 💡 **Watch out**: <Chỉ rõ bẫy ngữ pháp thường gặp trong đề thi lớp 10 hoặc lỗi Bum hay mắc, ví dụ: "Sau 'look forward to' bắt buộc là V-ing chứ KHÔNG dùng V-nguyên mẫu! ❌">

---

## 3. Real-Life Teen Dialogue (Hội Thoại Đời Sống Có Ngắt Nhịp Sound Blocks) 🎧
Đoạn thoại tự nhiên giữa Bum và bạn bè/AI Leo có ký hiệu ngắt nhịp Sound-Block `/` để Bum luyện phát âm nhịp nhàng:
- **Bum**: "Hey Leo, / I still feel drowsy / even though I washed my face / five minutes ago."
- **Leo**: "Did you look at your phone screen / right after waking up, Bum?"
- **Bum**: "Yeah, guilty! / I wanted to check / my Roblox notifications."
- **Leo**: "That's a careless habit! / Looking at blue light immediately / makes your eyes exhausted."
- **Bum**: "Good point. / I'll turn off my phone screen / and do some quick stretching."
- **Leo**: "Awesome! / A disciplined morning routine / is the first step to victory!"
```

*(Nếu là Tuần 1-3: Sử dụng bảng 5 từ đơn giản nguyên bản).*

---

## 📝 File 2: `02-exercises.md` Structure

### 🔹 Dành Cho Tuần 4 Trở Đi (Chuẩn 4 Tầng Thử Thách Nâng Cấp):

```markdown
# Day <M>: Interactive Exercises & AI Mission 🚀

Hoàn thành 5 phần thử thách dưới đây để thu thập trọn vẹn 3 Ngôi Sao (⭐⭐⭐) ngày hôm nay!

---

## Part 1: Word Formation Challenge (Tự Biến Đổi Từ Loại - KHÔNG Word Bank) 🧩
*Đọc câu và biến đổi từ trong ngoặc `(IN HOA)` thành dạng Danh từ / Tính từ / Trạng từ phù hợp:*

1. Teenagers should develop __________ habits to maintain daily energy. (HEALTH)
2. We are looking forward to __________ our new robotics project next week. (PRESENT)
3. You acted __________ when you forgot to turn off the air conditioner. (CARE)
4. The cleaning robot runs __________ and saves us a lot of time. (AUTOMATIC)
5. My older brother made a sudden __________ to switch his gaming gear. (DECIDE)

---

## Part 2: Conversational Exam Builder (Trắc Nghiệm Hội Thoại & Câu Ghép) 🎯
*Chọn đáp án đúng nhất (A, B, C hoặc D) mô phỏng các câu hỏi hội thoại và câu ghép của Đề Hà Nội & TP.HCM:*

#### Question 1 (Đối thoại đời sống)
...
#### Question 2 (Cụm động từ bẫy)
...
#### Question 3 (Liên từ & Điều kiện)
...
#### Question 4 (Mệnh đề quan hệ / Đại từ)
...
#### Question 5 (Phản xạ giao tiếp xã hội)
...

---

## Part 3: Real-World Exam Formats (Biển Báo / Từ Điển / Sắp Xếp Câu) 📋
*(Luân phiên giữa các ngày: Day 1 & 2 làm Biển báo/Tin nhắn, Day 3 làm Tra cứu từ điển, Day 4 làm Sắp xếp câu).*

#### Dạng Tra Cứu Từ Điển (Mẫu Day 3 - Đề TP.HCM Q35-36):
> ### 📖 Dictionary Entry: habit /ˈhæbɪt/ (noun)
> 1. a thing that you do often and almost without thinking:
>    - It's not easy for children to **break the habit** of using digital devices while having meals.
>    - Healthy **eating habits** play an important role in overall health.

1. Bum is trying to ______________________ of staying up late to play games. (Không quá 3 từ)
2. Proper ______________________ can help students stay awake during morning classes. (Không quá 3 từ)

---

## Part 4: Open Sentence Transformation (Tự Luận Viết Lại Câu - Áp Dụng Linearthinking) ✏️
*Xác định hành động cốt lõi `S - V - O` trước khi biến đổi câu, tuyệt đối không dịch từng từ:*

1. Bum doesn't have a smartwatch, and he really wants to have one.  
   → Bum wishes _______________________________________________________________.
2. Lucie doesn't mind helping her friends with math exercises after class.  
   → It doesn't matter to Lucie to ______________________________________________.
3. Our wireless mouse has run out of battery.  
   → There is no battery left __________________________________________________.
4. *(Rematch Challenge - Lỗi 🔴 Active)*: Câu trích từ ngân hàng đề thi thật kiểm tra 1 lỗi Bum cần phục thù.

---

## Part 5: AI Voice Mission with Leo (Phản Xạ Tuyến Tính O-R-E-O & Sound Blocks) 🎙️

Mở ChatGPT Voice Mode hoặc Gemini Live và cùng Leo thảo luận về chủ đề hôm nay:
> 💬 **Your Mission Prompt**:  
> *"Hey Leo! Today I'm learning about building smart daily habits and managing screen time. Challenge me by asking why playing games late at night is bad, and I will persuade you with my new daily schedule!"*

**Speaking Checklist (Áp Dụng Sound-Block & O-R-E-O)**:
- [ ] Trả lời theo trục tuyến tính: **Trực diện (Opinion)** ➔ **Lý do (Reason)** ➔ **Ví dụ cá nhân (Example)**.
- [ ] Ngắt hơi theo các cụm âm thanh Sound Blocks (`/`), không đọc rời rạc từng từ.
- [ ] Dùng ít nhất 2 từ trong bảng Word Power (*healthy, routine, convenient, alert, habit*).
- [ ] Dùng cấu trúc ngữ pháp hôm nay (*"I wish...", "I'm looking forward to..."*).

---

<details>
<summary>Click to reveal Answer Key & Barem Chấm Điểm 🔍</summary>

### Part 1 Answers (Word Formation):
1. **healthy** *(Tính từ bổ nghĩa cho danh từ 'habits')*
2. **presenting** *(Sau 'look forward to' + V-ing)*
...

### Part 2 Answers (Conversational MCQs):
1. **B** - *Vị trí bên trong ngăn kéo dùng giới từ 'in'*
...

### Part 3 Answers (Real-World Format):
1. **break the habit**
2. **eating habits**

### Part 4 Answers (Sentence Transformation):
1. **he had a smartwatch** *(Cấu trúc wish lùi thì quá khứ)*
2. **help her friends with math exercises after class**
3. **in our wireless mouse**

</details>

---

## 🏆 Daily Scorecard
- [ ] Part 1 & 2 Complete (1 Star ⭐)
- [ ] Part 3 & 4 (Tự luận & Phục thù) Complete (1 Star ⭐)
- [ ] AI Leo Voice Mission Complete (1 Star ⭐)  
**Total Stars Earned Today**: ⭐ ⭐ ⭐ / 3
```

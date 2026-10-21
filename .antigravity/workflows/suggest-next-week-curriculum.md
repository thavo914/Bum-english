---
description: Proposes a cohesive 5-day curriculum theme, grammar blueprint, and targeted error recovery based on Grade 10 entrance exams and Bum's past test mistakes.
---

# Workflow: /suggest-next-week-curriculum

Use this workflow to plan and preview the upcoming week's curriculum for Bum (14 years old, Grade 8/9, CEFR A1–A2) before generating daily lessons.

---

## 🎯 Purpose & Scope
1. **Detect Upcoming Week**: Inspect `lessons/` to identify the next week number `<N>` (e.g. `week-03`, `week-04`).
2. **Audit Past Test Mistakes**: Check `assessments/` (e.g. [assessments/test bum.md](file:///c:/Users/Admin/source/repos/nephew-english/assessments/test%20bum.md)) and previous weeks' evaluations to extract specific errors Bum made (e.g., compound subject S-V agreement, past irregular verbs, some/any, object pronouns, prepositions).
3. **Align with Grade 10 Exam Registry**: Query `graduation exam/question-registry.json` using `py scripts/query_registry.py --bum-week week-<N>` to identify high-yield grammar patterns, vocabulary domains, and question styles tested in official entrance exams.
4. **Draft 5-Day Blueprint with Error Recovery**: Map out Monday to Friday with:
   - 1 Daily Engaging Teen Topic (Gaming, Tech, Sports, Snacks, Anime, School Clubs).
   - 1 Core A1-A2 Grammar Point aligned with entrance exams.
   - 5 High-frequency Target Words (no toddler words, no corporate jargon).
   - 1 Targeted Error Rematch (khắc phục 1 lỗi sai cụ thể từ bài test trước).
   - 1 AI Voice Scenario with Leo.
   - Day 5 Boss Battle: A 5–10 question mini-test compiled directly from real entrance exams.
5. **Output**: Write the plan to `lessons/week-<N>-<theme-slug>/week-overview.md` and present for user confirmation.

---

## 🛠️ Step-by-Step Execution Guide

### Step 1: Detect Next Week & Audit Mistake Lifecycle
1. Scan `lessons/` to find the next week index. (If `week-01` and `week-02` exist, target is `week-03`).
2. Open and inspect [assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/assessments/MISTAKE_LOG.md) cùng kết quả bài test tuần gần nhất (ví dụ: `assessments/test-week-02.md`):
   - **Lọc lỗi còn yếu**: Chỉ lấy các bẫy lỗi có trạng thái 🔴 **Active** (chưa khắc phục) hoặc 🟡 **In-Review** (cần kiểm tra lại lần 2).
   - **LOẠI BỎ các lỗi đã 🟢 Mastered**: Tuyệt đối **không lặp lại** các dạng câu hỏi mà Bum đã nhớ và làm đúng ở bài test tuần trước. Điều này giúp Bum luôn hào hứng và tập trung vào các thử thách mới.
3. Chọn ra từ 3–5 lỗi 🔴 **Active** hàng đầu để phân bổ vào 5 ngày học của tuần mới.

### Step 2: Query Real Exam Registry for Inspiration
Run the CLI tool to check real exam patterns matching the upcoming curriculum week:
```bash
py scripts/query_registry.py --bum-week week-<N> --limit 5
```
Take note of the question stems, options, and sentence transformation formats to integrate into the daily lesson designs.

### Step 3: Write `week-overview.md`
Format using the standardized template (mirroring the proven structure of `lessons/week-02-school-life-friends/week-overview.md`):

```markdown
# ⚡ Week <N>: <Engaging Teen Theme Title>
> **Target Audience**: Bum (14 tuổi – THCS Lớp 8/9)  
> **Level**: CEFR A1–A2 (Được may đo dựa trên ngân hàng đề thi lớp 10 và nhật ký lỗi sai của Bum)  
> **Goal**: <Mục tiêu 1 câu rõ ràng: Nắm vững cấu trúc mới + Khắc phục triệt để các bẫy ngữ pháp đã vấp phải>

---

## 🎯 Phân Tích Lỗ Hổng Từ Bài Test & Giải Pháp May Đo Cho Tuần <N>

| Lỗi sai trong bài Test của Bum | Bản chất bẫy ngữ pháp | Ngày học khắc phục trong Tuần <N> | Trọng tâm bài học & Đề thi mẫu |
| :--- | :--- | :---: | :--- |
| **Câu X**: <Mô tả lựa chọn sai của Bum> | <Giải thích tại sao Bum nhầm, ví dụ: nhầm thì quá khứ bất quy tắc, nhầm so sánh hơn...> | **Day 1** | **<Tên cấu trúc>** *(Tập trung bẫy đề thi hay ra)* |
| **Câu Y**: ... | ... | **Day 2** | ... |
| **Câu Z**: ... | ... | **Day 3** | ... |
| ... | ... | **Day 4** | ... |
| **Tổng hợp bẫy**: ... | ... | **Day 5** | **Boss Battle Review**: Thử sức 5 câu đề thi thật từ ngân hàng câu hỏi |

---

## 🗓️ Lịch Học 5 Ngày Chi Tiết (Daily Schedule)

| Ngày | Chủ đề (Theme) | Ngữ pháp cốt lõi (Target Grammar) | Vốn từ vựng mục tiêu (5 Target Words) | Dạng bài thi mẫu tích hợp | Nhiệm vụ nói với AI Leo (Voice Mission) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Day 1** | **...** | ... | ... | Trắc nghiệm 4 lựa chọn (A/B/C/D) | ... |
| **Day 2** | **...** | ... | ... | Viết lại câu (Sentence Transformation) | ... |
| **Day 3** | **...** | ... | ... | Đọc hiểu biển báo & tin nhắn (Signs/Notices) | ... |
| **Day 4** | **...** | ... | ... | Cấu tạo từ (Word Formation in context) | ... |
| **Day 5** | **Boss Battle Review 🏆** | Tổng ôn + Đàm thoại tự do | 5 từ chìa khóa tuần | 5 câu đề thi thật từ Question Registry | Thử thách nói 10 phút với Leo |

---

## 💡 Hướng Dẫn Tránh Trùng Lặp & Giữ Tính Hấp Dẫn
- **Ngữ cảnh mới mẻ**: Dù nhắc lại điểm ngữ pháp cũ, hãy đổi sang bối cảnh teen cuốn hút (ví dụ: nếu bài test dùng bóng đá, tuần mới dùng bối cảnh giải đấu Esports, chuyến đi dã ngoại, hoặc review đồ công nghệ).
- **Độ khó nâng dần**: Chuyển dần từ mức độ Nhận biết (A1) sang Thông hiểu & Vận dụng (A2) để Bum xây dựng sự tự tin.
```

### Step 4: User Confirmation
Present the proposed schedule and error-recovery plan to the user. Once approved, proceed to execute `/generate-daily-lesson`.

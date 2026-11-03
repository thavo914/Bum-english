---
description: Proposes a cohesive 5-day curriculum theme, grammar blueprint, and targeted error recovery based on Grade 10 entrance exams and Bum's past test mistakes (with Phase 2 Hybrid escalation from Week 4 onwards).
---

# Workflow: /suggest-next-week-curriculum

Use this workflow to plan and preview the upcoming week's curriculum for Bum (14 years old, Grade 8/9) before generating daily lessons.

---

## 🎯 Purpose & Scope (Cơ Chế Phân Tầng 2 Giai Đoạn)

1. **Detect Upcoming Week & Phase**: Inspect `lessons/` to identify the next week number `<N>`:
   - 🟢 **Giai đoạn 1 (Tuần 1 – Tuần 3)**: CEFR A1–A2. Củng cố nhận thức ngữ pháp đơn lẻ, câu ngắn, có Word Bank trợ giúp.
   - 🚀 **Giai đoạn 2 (Tuần 4 – Tuần 10)**: CEFR A2 → A2+ / Tiệm cận B1. Đột phá theo **Chuẩn Hybrid** (kết hợp trắc nghiệm logic/đọc hiểu của Đề Hà Nội và tự luận Word Formation, tra từ điển, viết lại câu của Đề TP.HCM).
2. **Audit Past Test Mistakes**: Check `assessments/` (ví dụ: [assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/assessments/MISTAKE_LOG.md) và bài test tuần gần nhất `assessments/test-week-<N-1>.md`):
   - **Chỉ lấy các lỗi 🔴 Active hoặc 🟡 In-Review**.
   - **Tuyệt đối LOẠI BỎ các lỗi đã 🟢 Mastered**: Không lặp lại để giữ sự hào hứng cho Bum.
3. **Align with Grade 10 Exam Registry**: Truy vấn ngân hàng câu hỏi `graduation exam/question-registry.json`:
   ```powershell
   & "C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe" scripts/query_registry.py --bum-week week-<N> --limit 10
   ```
4. **Draft 5-Day Blueprint with Error Recovery**:
   - 1 Daily Engaging Teen Topic (Gaming, Smart Tech, Sports, Snacks, Anime, Life Skills).
   - 1 Core Grammar / Word Family Pattern.
   - 5 Target Words có họ từ liên quan (Noun/Verb/Adj/Adv).
   - 1 Targeted Rematch Challenge (cho lỗi 🔴 Active).
   - 1 AI Voice Mission with Leo (có phản biện, đàm thoại 2 chiều).
   - Day 5 Boss Battle: Mini-test trích nguyên văn đề thi thật.
5. **Output**: Ghi vào `lessons/week-<N>-<theme-slug>/week-overview.md` và trình bày để phụ huynh/thầy cô phê duyệt.

---

## 🛠️ Step-by-Step Execution Guide

### Step 1: Detect Next Week & Audit Mistake Lifecycle
1. Quét thư mục `lessons/` để tìm số thứ tự tuần tiếp theo.
2. Mở [assessments/MISTAKE_LOG.md](file:///c:/Users/Admin/source/repos/nephew-english/assessments/MISTAKE_LOG.md):
   - Lọc ra 2-3 lỗi 🔴 **Active** ưu tiên xử lý.
   - Đảm bảo không trùng các lỗi đã 🟢 **Mastered**.

### Step 2: Query Real Exam Registry for Inspiration
Chạy CLI tra cứu câu hỏi đề thi thật thuộc chủ đề tuần tương ứng:
```powershell
& "C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe" scripts/query_registry.py --bum-week week-<N> --limit 5
```

### Step 3: Write `week-overview.md`

#### Template Chuẩn Dành Cho Tuần 4 Trở Đi (Giai Đoạn Bứt Phá Đề Thi):
```markdown
# ⚡ Week <N>: <Engaging Teen Theme Title> 🎮⌚

> **Target Audience**: Bum (14 tuổi – THCS Lớp 8/9, chuẩn bị thi vào Lớp 10 THPT)  
> **Level**: CEFR A2 → A2+ / Tiệm cận B1 (Chuẩn Hybrid: Trắc nghiệm logic Hà Nội + Tự luận sản sinh TP.HCM)  
> **Goal**: <Mục tiêu 1 câu rõ ràng về điểm ngữ pháp, cấu tạo từ và dạng bài thi tuyển sinh làm chủ>

---

## 🎯 Phân Tích Lỗ Hổng Từ Bài Test & Giải Pháp May Đo Cho Tuần <N>

| Mã lỗi | Bản chất bẫy đề thi | Lỗi Bum đã chọn / vấp phải | Ngày học khắc phục | Trọng tâm bài học & Đề thi mẫu |
| :---: | :--- | :--- | :---: | :--- |
| **ERR-XX** | ... | ... | **Day 1** | ... |
| **ERR-YY** | ... | ... | **Day 2** | ... |
| ... | ... | ... | **Day 5** | **Boss Battle Review**: Thử sức câu hỏi đề thi thật |

---

## 🗓️ Lịch Học 5 Ngày Chi Tiết (5-Day Daily Schedule)

| Ngày | Bối cảnh Teen (Teen Angle) | Ngữ pháp & Kỹ năng cốt lõi | Vốn từ vựng mục tiêu (5 Target Words) | Dạng bài thi tuyển sinh tích hợp | Thử thách nói với AI Leo (Voice Mission) |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **Day 1** | **...** | ... | ... | **TP.HCM Part I & V**: Trắc nghiệm hội thoại + Điền từ loại tự luận | ... |
| **Day 2** | **...** | ... | ... | **Hà Nội & TP.HCM**: Đọc biển báo + Viết lại câu | ... |
| **Day 3** | **...** | ... | ... | **TP.HCM Section VI**: Tra cứu mục từ điển điền cụm từ | ... |
| **Day 4** | **...** | ... | ... | **Hà Nội Q18, Q27**: Sắp xếp trật tự câu + Viết lại câu | ... |
| **Day 5** | **Boss Battle 🏆** | Tổng ôn + 10 câu đề thi thật | 5 từ chìa khóa tuần | **Mini-Exam Challenge**: Trắc nghiệm đa tầng + Tự luận | 10 phút đàm thoại phản biện cùng Leo |

---

## 🏆 Bài Kiểm Tra Cuối Tuần (Weekend Checkpoint Test - Week <N>)
- **Quy mô**: Đúng 30 câu chuẩn cấu trúc Hybrid (45 phút):
  - **Phần 1: Trắc nghiệm khách quan (20 câu)**: Ngữ âm, hội thoại đời sống, biển báo, cloze test, sắp xếp câu logic.
  - **Phần 2: Tự luận sản sinh (10 câu)**: 4 câu Word Formation không gợi ý, 2 câu tra mục từ điển, 4 câu viết lại câu hoàn chỉnh.
```

### Step 4: User Confirmation
Trình bày kế hoạch tổng quan cho người dùng. Khi được phê duyệt, sử dụng workflow `/generate-daily-lesson` để sinh từng bài học.

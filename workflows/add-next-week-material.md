---
description: Capture and organize user-suggested vocabulary, phrases, or grammar notes into the upcoming week's backlog to prioritize in daily lessons.
---

# Workflow: /add-next-week-material

Use this workflow whenever the user shares a new word, phrase, topic, or grammar question that they want included in their nephew's upcoming English lessons.

---

## 🎯 Purpose & Scope
1. **Capture Spontaneous Requests**: Examples: *"Chỉ cho cháu cách dùng like vs prefer"*, *"Cháu mới xem clip thấy từ respawn, loot"*, *"Tuần tới cho học về chủ đề bóng đá"*.
2. **Store in Target Notes**: Save as a clean markdown note in `lessons/week-<N>/notes/<topic-name>.md`.
3. **Format for A1-A2**: Keep definitions super clear, relatable for 14-year-olds, and free of complex linguistic jargon.

---

## 🛠️ Step-by-Step Execution Guide

### Step 1: Resolve Target Week
- Find the upcoming week directory `lessons/week-<N>/`.
- Create `lessons/week-<N>/notes/` if it does not exist.

### Step 2: Create Note File: `lessons/week-<N>/notes/<topic-slug>.md`
Structure the note simply:
```markdown
# Note: <Word or Grammar Point> 📝

> **Suggested for**: Week <N>  
> **Level**: CEFR A1–A2  
> **Target Audience**: 14-year-old student  

---

## 1. What does it mean? (Ý nghĩa)
- **Pronunciation (IPA)**: /.../
- **Vietnamese Meaning**: <Nghĩa tiếng Việt rõ ràng, dễ hiểu>
- **Simple English Meaning**: <1 câu tiếng Anh đơn giản>

---

## 2. Real-Life Examples (Ví dụ thực tế)
1. *<Ví dụ trong game / công nghệ / đời sống học đường>*  
   👉 *Dịch: ...*
2. *<Ví dụ khi trò chuyện với bạn bè>*  
   👉 *Dịch: ...*

---

## 3. Watch Out! (Lưu ý tránh nhầm lẫn)
❌ **Sai / Chưa tự nhiên**: ...  
✅ **Đúng chuẩn bản xứ**: ...  
💡 **Mẹo ghi nhớ**: ...
```

### Step 3: Confirm to User
Notify the user that the note is saved and will be included in the next week's lesson generation.

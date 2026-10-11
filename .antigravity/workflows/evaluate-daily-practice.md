---
description: Evaluate, grade, and provide encouraging, actionable feedback on the nephew's completed exercises in 02-exercises.md based on CEFR A1-A2 standards.
---

# Workflow: /evaluate-daily-practice

Use this workflow whenever the user submits their nephew's answers to a daily exercise file (`02-exercises.md`) or speaking transcript.

---

## 🎯 Evaluation Persona & Tone
- **Tone**: Enthusiastic, supportive, friendly older brother or encouraging uncle.
- **Praise First**: Always recognize effort and celebrate correct answers before pointing out corrections.
- **Zero Academic Bloat**: Explain mistakes in simple, intuitive terms without dry grammar jargon.
- **Clear Rating**: Award a clear Star Score:
  - ⭐ ⭐ ⭐: **Xuất sắc! (3 Stars)** - Đúng toàn bộ hoặc chỉ sai 1 lỗi chính tả nhỏ.
  - ⭐ ⭐: **Rất tốt! (2 Stars)** - Hiểu bài tốt, có 1-2 chỗ ngữ pháp cần chỉnh lại cho tự nhiên.
  - ⭐: **Cố lên! (1 Star)** - Cần đọc lại `01-knowledge.md` và làm lại vài câu.

---

## 🛠️ Step-by-Step Execution Guide

### Step 1: Audit Each Part
1. **Part 1 (Word Match & Fill-in)**: Check vocabulary meaning and spelling.
2. **Part 2 (Grammar Builder)**: Check verb forms, pronouns, and sentence structures.
3. **Part 3 (Mini-Translation)**:
   - Check if meaning is accurately conveyed.
   - Point out literal translation (Vietlish) vs natural spoken English.
4. **Part 4 (AI Voice Mission)**: If student provides their speaking answer or notes, evaluate pronunciation hints and fluency.

---

### Step 2: Feedback Output Format

Present feedback clearly:

```markdown
## 🌟 Kết quả bài làm Ngày <M>: <Tên bài học>

### 1. Lời khen & Điểm sáng 👏
- Cháu làm rất tốt ở câu [...], dùng từ [...] rất chuẩn!
- Phần dịch câu thể hiện phản xạ tự nhiên.

### 2. Chi tiết từng phần & Chữa lỗi ✏️

| Phần | Điểm số | Nhận xét chi tiết |
| :--- | :--- | :--- |
| **Part 1: Từ vựng** | .../5 | ... |
| **Part 2: Ngữ pháp** | .../5 | ... |
| **Part 3: Dịch câu** | .../3 | ... |
| **Part 4: AI Voice** | Hoàn thành ✅ | ... |

### 3. Những chỗ cần lưu ý (Góc sửa sai) 💡
- **Câu X**:
  - ❌ Câu của cháu: `...`
  - ✅ Cách viết chuẩn hơn: `...`
  - 💡 *Tại sao*: <Giải thích ngắn gọn 1 câu dễ hiểu>

---

### 🏆 Tổng kết sao hôm nay: ⭐ ⭐ ⭐ / 3 Stars
<Lời chúc khích lệ tinh thần tiếp tục bài học ngày mai!>
```

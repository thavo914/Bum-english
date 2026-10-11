---
description: Transforms a teen-friendly YouTube video transcript (gaming, science facts, life skills) into a simplified CEFR A1-A2 study guide.
---

# Workflow: /generate-youtube-lesson

Use this workflow when the user provides a transcript or link to a teen-friendly YouTube video (MrBeast challenge, gaming tutorial, tech review, science fun fact) and wants to turn it into an engaging A1-A2 study lesson.

---

## 🎯 Pedagogical Guidelines
- **Level**: CEFR A1–A2.
- **Chunking**: Break long transcripts into 3 or 4 short, manageable clips (each 2-3 sentences).
- **Focus**: Extract practical spoken words and 1 simple grammar pattern per chunk.

---

## 📝 Output Format

```markdown
# 🎬 YouTube Lesson: <Video Catchy Title>

> **Source**: <Video Title / Channel>  
> **Level**: CEFR A1–A2 • **Target Audience**: 14 Years Old  

---

## 📝 Clip 1: <Short Subtitle>
> *"[Paste 2-3 sentences of authentic transcript snippet here]"*

### 📚 Words to Know:
1. **<Word 1>**: <IPA> - <Nghĩa tiếng Việt>
2. **<Word 2>**: <IPA> - <Nghĩa tiếng Việt>

### ⚡ Grammar in Action:
- **Pattern**: `<Simple formula>`
- **Explanation**: <1-sentence clear explanation>

### 🎙️ Speak Like the YouTuber:
- Read this sentence out loud with high energy:  
  👉 *"..."*
```

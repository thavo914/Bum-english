---
description: Generates a complete 2-file daily lesson (01-knowledge.md and 02-exercises.md) for Bum (14 years old) in the A1-A2 curriculum.
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

---

## 📂 Exact 2-File Directory Target
For the target week `<N>` and day `<M>`, generate exactly two files:
```
lessons/week-<N>/day-<M>/
├── 01-knowledge.md      # Definitions, 5 target words, 1 grammar bite, mini dialogue
└── 02-exercises.md      # Puzzles, sentence builders, mini translation, AI voice mission, answers
```

---

## 📝 File 1: `01-knowledge.md` Structure

Every `01-knowledge.md` must follow this standardized template:

```markdown
# Day <M>: <Engaging Teen Title with Icon> 🎮

Brief 1-sentence friendly intro explaining what the student will learn today.

---

## 1. Word Power (5 Words for Today)

| Word | Pronunciation (IPA) | Vietnamese Meaning | Example Sentence |
| :--- | :--- | :--- | :--- |
| **<word 1>** | /.../ | <nghĩa tiếng Việt gần gũi> | *<Teen example sentence in gaming, school, or friends>* |
| **<word 2>** | /.../ | ... | ... |
| **<word 3>** | /.../ | ... | ... |
| **<word 4>** | /.../ | ... | ... |
| **<word 5>** | /.../ | ... | ... |

---

## 2. Grammar Bite: <Core Grammar Pattern> ⚡

Explain the grammar rule in simple, crystal-clear terms with zero academic bloat.

### The Rule Formula:
- **<Subject>** + **<Grammar Element>** + **<Object/Complement>**
  - *<Clear Example 1>*
  - *<Clear Example 2>*

### Watch Out! (Common Trap):
> 💡 **Watch out**: <Highlight common Vietlish or teenage mistake, e.g. "I have 14 years old" ❌ -> "I am 14 years old" ✅>

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

## Part 1: Word Match & Fill-in-the-Blank (Warm-up)
Word bank of 5 target words. 5 fill-in sentences.

---

## Part 2: Grammar Builder
5 sentences targeting today's grammar pattern (choose correct verb, unscramble, or fill in).

---

## Part 3: Mini-Translation (Teen Style)
3 natural, everyday Vietnamese sentences for the student to translate into English.

---

## Part 4: AI Voice Mission with Leo 🎙️
An interactive prompt for the student to speak with ChatGPT Voice Mode or Gemini Live Buddy Leo:
> **Your Mission Prompt**:  
> *"Hey Leo! I am 14 years old. Today I learned about [Topic]. Ask me 3 quick questions about [Topic] in simple English!"*

**Speaking Checklist**:
- [ ] Checklist item 1
- [ ] Checklist item 2

---

<details>
<summary>Click to reveal Answer Key 🔍</summary>

### Part 1 Answers:
...

### Part 2 Answers:
...

### Part 3 Suggested Translations:
...
</details>

---

## 🏆 Daily Scorecard
- [ ] Part 1 Complete (1 Star ⭐)
- [ ] Part 2 & 3 Complete (1 Star ⭐)
- [ ] AI Leo Voice Mission Complete (1 Star ⭐)  
**Total Stars Earned Today**: ⭐ ⭐ ⭐ / 3
```

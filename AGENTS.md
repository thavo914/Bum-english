# Repository Agent Guidelines: Dual Study Hub (English & Math) for 14-Year-Old Nephew

> [!IMPORTANT]
> **Core Directive**: All lessons, practice drills, and AI interactions in this repository are designed specifically for **Bum**, a **14-year-old student (Grade 8 / 9, Secondary School / THCS)** preparing for the **Grade 10 Entrance Exam (Thi Tuyển Sinh Vào Lớp 10 THPT)** across two core subjects:
> 1. **English (CEFR A1–A2)**: Foundational vocabulary, grammar, and speaking confidence.
> 2. **Math (Toán Lớp 9 & Ôn Thi Vào 10)**: Core algebra & geometry mastery, anti-trap problem solving, and practice drills.

---

## 1. Target Persona & Pedagogical Principles
- **Target Persona**: **Bum**, a 14-year-old teenager with authentic hobbies: video games (Minecraft, Roblox, mobile gaming), tech gadgets, football and sports, school life & friends, YouTube/music, fast food, and anime.
- **Strictly Avoid**:
  - Kindergarten/toddler baby talk (*"the cute little teddy bear"*).
  - Adult corporate clichés (*"synergy"*, *"bring to the table"*, *"exceed expectations"*).
  - Overly dry, academic lecture-style exposition without concrete step-by-step examples.
- **Pedagogical Anchors**:
  - Step-by-step thinking (không nhảy cóc bước giải).
  - Highlighting traps & common mistakes (Bẫy đề thi, lỗi ẩu, quên ĐKXĐ).
  - Immediate feedback (Collapsible `<details><summary>` answer keys).
  - Daily motivation with 3-Star Scorecards (⭐ ⭐ ⭐).

---

## 2. Directory Architecture & Guidelines

### 🇬🇧 English Engine (`english/`)
- **Daily Lessons (`english/lessons/week-<N>/day-<M>/`)** - Strict 2-File System:
  1. **`01-knowledge.md`**: 5 target words (IPA + Vietnamese meaning + example), 1 grammar bite with slot formula, lively 4-line mini dialogue.
  2. **`02-exercises.md`**: Quick Check (MCQ), Sentence Builder, Mini-Translation, AI Voice Mission with Leo, collapsible Answer Key, 3-Star Scorecard.
- **Official Entrance Exams (`english/exams/`)**: PDF originals, Markdown digitizations, and `question-registry.json` database.
- **Mistake Log & Assessments (`english/assessments/`)**: Mistake tracking & placement tests.

### 📐 Math Hub (`math/`) - Dual Structure
- **Knowledge Topics (`math/topics/<topic-slug>/`)**:
  - 8 core topics for Grade 10 entrance exams (Căn thức, Hàm số $y=ax+b$, Hệ PT, PT bậc hai & Vi-ét, Toán thực tế, Hình học phẳng, Hình không gian, Bất đẳng thức).
  - Theory, standard formulas, step-by-step solving algorithms, and typical exam problem types.
- **Daily Practice Drills (`math/lessons/week-<N>/day-<M>/`)** - 2-File Daily System:
  1. **`01-knowledge.md`**: Core rule bite, step-by-step algorithm, visual/gaming analogies, and "Watch Out!" trap alerts.
  2. **`02-exercises.md`**: Part 1 Quick Check, Part 2 Step-by-step drill, Part 3 Real exam challenge, Part 4 Trap buster, collapsible Answer Key, 3-Star Scorecard.
- **Cheatsheets (`math/cheatsheets/`)**: One-page high-density summary sheets (`cong-thuc-dai-so-9.md`, `cong-thuc-hinh-hoc-9.md`).
- **Mistake Log (`math/assessments/MISTAKE_LOG.md`)**: Top 7 fatal exam traps (TRAP-01 to TRAP-07) and personal mistake journal.
- **Entrance Exams (`math/exams/`)**: Official Grade 10 Math exam papers from Hanoi, HCMC, Can Tho, etc.

---

## 3. Git & Version Control Rules
- **Do Not Auto-Commit or Auto-Push**: Keep all files in the local working tree. Never commit or push without explicit instructions from the user.

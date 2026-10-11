---
description: Proposes a fun, cohesive 5-day curriculum theme, vocabulary list, and grammar blueprint for the upcoming week at CEFR A1-A2 level before generating lessons.
---

# Workflow: /suggest-next-week-curriculum

Use this workflow to plan and preview the upcoming week's curriculum for the 14-year-old nephew.

---

## 🎯 Purpose & Scope
1. **Detect Upcoming Week**: Inspect `lessons/` to identify the next week number `<N>` (e.g. `week-03`, `week-04`).
2. **Review User Notes**: Check `lessons/week-<N>/notes/` for any requests or words suggested by the user.
3. **Teen Theme Selection**: Pick an authentic, exciting theme (Gaming & Streaming, School Clubs & Sports, Fast Food & Snacks, Anime & Movies, Family Trip & Summer Plans).
4. **Draft 5-Day Blueprint**: Map out Monday to Friday with:
   - 1 Daily Topic
   - 1 Core A1-A2 Grammar Point
   - 5 High-frequency Target Words
   - 1 AI Voice Scenario with Leo
5. **Output**: Write the plan to `lessons/week-<N>/week-overview.md` and present a preview for user confirmation.

---

## 🛠️ Step-by-Step Execution Guide

### Step 1: Detect Next Week
- Scan `lessons/` directory.
- If `week-01` and `week-02` exist, target is `week-03`.
- Create folder `lessons/week-<N>-<theme-slug>/` if not present.

### Step 2: Propose the 5-Day Structure
Ensure each day covers:
- **Day 1 (Mon)**: Foundation & Key Concepts (To Be, Pronouns, Basic Nouns).
- **Day 2 (Tue)**: Gear, Tools & Describing Objects (Have got, Adjectives).
- **Day 3 (Wed)**: Actions, Abilities & Preferences (Can/Can't, Like + V-ing).
- **Day 4 (Thu)**: Daily Routines or Real-Time Actions (Present Simple or Continuous).
- **Day 5 (Fri)**: Weekly Boss Battle Review & Big Speaking Mission with Leo.

### Step 3: Write `week-overview.md`
Format using the standardized template:
```markdown
# ⚡ Week <N>: <Theme Title>
> **Target Audience**: 14-year-old student (Grade 8 / 9)  
> **Level**: CEFR A1–A2  
> **Goal**: <Clear 1-sentence goal for the week>

---

## 🗓️ Daily Schedule

| Day | Theme | Target Grammar | Core Focus |
| :--- | :--- | :--- | :--- |
| **Day 1** | **...** | ... | ... |
| **Day 2** | **...** | ... | ... |
| **Day 3** | **...** | ... | ... |
| **Day 4** | **...** | ... | ... |
| **Day 5** | **...** | ... | ... |
```

### Step 4: User Confirmation
Present the proposed schedule to the user. Once approved, proceed with `/generate-daily-lesson`.

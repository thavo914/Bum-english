---
description: Classifies, tags, and registers Grade 10 English entrance exam questions by category, CEFR level (A1-B2), Bloom taxonomy, and Bum's curriculum week into a searchable registry.
---

# Workflow: /classify-exam-questions

Use this workflow whenever new Grade 10 entrance/graduation exam papers are added to the repository, or when creating targeted practice drills, review tests, and "Boss Battle" quizzes for **Bum** (14 years old, Grade 8/9, CEFR A1–A2).

---

## 🎯 Objectives & Pedagogical Vision

1. **Systematic Classification**: Organize every single question from provincial entrance exams (Hà Nội, TP.HCM, Cần Thơ, Thừa Thiên Huế, etc.) into a normalized, searchable Question Bank.
2. **CEFR & Difficulty Leveling**: Tag every question from **A1** (Elementary foundation) to **B1/B2** (Discriminator questions) so Bum is neither overwhelmed nor unchallenged.
3. **Curriculum Alignment**: Automatically map real exam questions to Bum's 10-week themes (e.g. Present Simple, Past Adventures, Comparisons, Phrasal Verbs) so he can solve *real exam questions* right after finishing daily lessons.
4. **Permanent Reusability**: Ensure future exam PDFs can be digitized, converted to Markdown, and ingested into the registry with a single command.

---

## 📂 Architecture & Files

```
graduation exam/
├── README.md                  # Master exam index (provinces, years, page counts)
├── question-registry.json     # Primary machine-readable question database (390+ items)
├── QUESTION_REGISTRY.md       # Human-readable catalog with statistics & sample lookups
├── *.pdf                      # Official PDF exam papers
├── images/                    # Extracted signs, notices, and question illustrations
└── md/                        # Standardized Markdown exam files

scripts/
├── convert_exam_pdf_to_md.py  # PDF -> Markdown parser & image extractor
├── build_question_registry.py # Parses all md/ exams -> updates JSON & MD registry
└── query_registry.py          # Interactive CLI query & quiz generator
```

---

## 🏷️ Standardized Taxonomy

### 1. Categories & Sub-Categories

| Category | Sub-Category | Focus & Description |
| :--- | :--- | :--- |
| **`phonetics`** | `pronunciation_ed`<br>`pronunciation_s_es`<br>`pronunciation_vowel`<br>`word_stress` | Pronunciation of suffixes (`-ed`, `-s/-es`), vowels/consonants, and 2-3 syllable word stress. |
| **`grammar`** | `conditional_sentences`<br>`relative_clauses`<br>`verb_tenses`<br>`passive_voice`<br>`comparisons`<br>`conjunctions_and_linkers`<br>`prepositions`<br>`modal_verbs` | Core grammatical patterns tested in Grade 9 & entrance exams. |
| **`vocabulary`** | `phrasal_verbs`<br>`collocations`<br>`synonyms_antonyms`<br>`contextual_vocabulary`<br>`topic_environment` | Word meanings in context, common phrasal verbs (`look for`, `turn off`), and thematic vocabulary. |
| **`communication`** | `social_interaction`<br>`dialogue_ordering`<br>`making_suggestions`<br>`giving_compliments` | Everyday teen exchanges, situational replies, and conversation sequencing. |
| **`sign_notice`** | `traffic_or_public_sign`<br>`notice_or_message` | Real-world visual literacy: reading signs, school/shop notices, and SMS/chat messages. |
| **`reading`** | `cloze_test`<br>`factual_detail`<br>`main_idea_or_inference`<br>`reference_pronoun`<br>`true_false` | Reading passages, paragraph comprehension, and cloze passage fill-in-the-blanks. |
| **`word_formation`** | `standard_derivation`<br>`advanced_derivation` | Transforming base words into correct parts of speech (noun, adjective, adverb, verb). |
| **`sentence_transformation`** | `rewrite_conditional`<br>`rewrite_connectors`<br>`rewrite_wish_or_inversion`<br>`combine_relative_clause`<br>`sentence_building` | Paraphrasing sentences, combining clauses, or constructing sentences from word prompts. |

---

### 2. CEFR Leveling Rubric (Grade 8/9 Context)

| CEFR Level | Target Difficulty | Criteria & Typical Indicators |
| :---: | :---: | :--- |
| **A1** | **Easy (Cực kỳ cơ bản)** | Basic pronouns, present simple, *to be*, *can*, simple prepositions of time (`on Thursday`), basic signs (`No motorbikes`), standard polite replies (`Have a nice trip!`, `Thank you!`). |
| **A2** | **Core Standard (Chuẩn cấp 2)** | Past simple with time markers (`two days ago`), comparative adjectives, First conditional (`If you study... will...`), relative pronouns (`who/which`), basic phrasal verbs, standard word formation (`collect` -> `collection`). **~90% of exam questions belong here.** |
| **B1** | **Challenging (Phân hóa)** | Second conditional, *Wish* in present (`We wish we had...`), inverted sentence structures, complex passive with modals, advanced word derivation (`undesirable`, `amazingly`), reading inference questions. |
| **B2** | **Advanced (Chuyên biệt)** | Subtle idioms, advanced collocations, double comparative inversions (`The more... the more...`), and nuanced stylistic rephrasing. |

---

### 3. Vietnamese Exam Taxonomy (Bloom's Revised)

- **`NB` (Nhận biết)**: Direct recall of phonetic sounds, signs, simple prepositions, basic vocabulary.
- **`TH` (Thông hiểu)**: Understanding sentence meaning, dialogue matching, identifying pronoun reference in reading.
- **`VD` (Vận dụng)**: Applying grammar rules (conditionals, tenses), word formation, rewriting sentences.
- **`VDC` (Vận dụng cao)**: Complex sentence transformations, idioms, abstract reading inference.

---

### 4. Curriculum Mapping (Bum's 10-Week Journey)

| Week Tag | Weekly Theme | Target Grammar / Vocabulary in Exams |
| :---: | :--- | :--- |
| **`week-01`** | **Myself, Tech & Gaming** | Present simple, to-be, tech vocabulary, personal introductions. |
| **`week-02`** | **School Life, Friends & Fun** | Prepositions, everyday communication exchanges, dialogue ordering. |
| **`week-03`** | **Past Adventures & Stories** | Past simple, *ago*, *yesterday*, travel & storytelling sentence building. |
| **`week-04`** | **Daily Habits & Chores** | Phrasal verbs (`turn off`, `look for`), frequency adverbs, word formation. |
| **`week-05`** | **Sports, Health & Food** | Comparatives, superlatives, health & sports vocabulary. |
| **`week-06`** | **Future Plans & Predictions** | Conditional sentences (Type 1), future tense, *wish* structures. |
| **`week-07`** | **City Life vs Countryside** | Connectors (*although*, *because*, *so*), traffic signs & notices. |
| **`week-08`** | **Environment & Planet** | Passive voice, modals (*should/must*), environment cloze passages. |
| **`week-09`** | **Entertainment, Music & Cinema** | Relative clauses (*who*, *which*, *that*), movie & music topics. |
| **`week-10`** | **Review & Boss Battle Mock Exam** | Full mock exam synthesis, mixed question drills. |

---

## 🔄 Step-by-Step Execution Workflow

### Step 1: Ingest New Exam PDFs
1. Place new `.pdf` exam files into `graduation exam/`.
2. Convert all PDFs into formatted Markdown in `graduation exam/md/`:
   ```bash
   py scripts/convert_exam_pdf_to_md.py "graduation exam"
   ```

### Step 2: Update the Question Registry Database
Run the registry builder to automatically parse questions, extract answers, classify types/levels, and update both JSON and Markdown registries:
```bash
py scripts/build_question_registry.py
```

### Step 3: Verify Registry Status
Check overall counts and balance:
```bash
py scripts/query_registry.py --stats
```

---

## 💡 Practical Use Cases for Bum's Study Plan

### Use Case 1: Friday "Boss Battle" Drill
At the end of each study week (e.g., Week 6 on Conditionals), generate a real 5-question exam quiz:
```bash
py scripts/query_registry.py --bum-week week-06 --limit 5 --export-quiz "assessments/week-06-boss-battle.md"
```

### Use Case 2: Weak Spot Reinforcement (Phonetics & Signs)
If Bum struggles with `-ed` pronunciation or sign reading:
```bash
py scripts/query_registry.py --category sign_notice --limit 5
py scripts/query_registry.py --sub-category pronunciation_ed --limit 5
```

### Use Case 3: Province Comparison
Compare how Hanoi vs. TP.HCM test reading comprehension:
```bash
py scripts/query_registry.py --category reading --province "Hà Nội" --limit 5
py scripts/query_registry.py --category reading --province "TP. Hồ Chí Minh" --limit 5
```

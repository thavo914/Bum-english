"""
Exam Question Registry Builder
==============================
Parses all Markdown exam files in 'graduation exam/md/', extracts each question,
classifies it by Category, Sub-category, CEFR Level (A1, A2, B1, B2), Bloom Taxonomy
(NB, TH, VD, VDC), and Bum's Curriculum Week, then exports both:
- graduation exam/question-registry.json (Machine-readable database)
- graduation exam/QUESTION_REGISTRY.md (Human-readable catalog with filters & stats)
"""

import os
import re
import json
import sys

def parse_source_info(filename):
    """Extract Province and Year from filename."""
    fname = filename.lower()
    province = "Unknown"
    if "can-tho" in fname:
        province = "Cần Thơ"
    elif "ha-noi" in fname:
        province = "Hà Nội"
    elif "thanh-pho-ho-chi-minh" in fname or "tphcm" in fname:
        province = "TP. Hồ Chí Minh"
    elif "thua-thien-hue" in fname:
        province = "Thừa Thiên Huế"

    m_year = re.search(r'20\d\d', fname)
    year = m_year.group(0) if m_year else "2025"
    return province, year

def extract_answer_map(content):
    """Extract answer dictionary {q_num: answer_text} from markdown content."""
    ans_map = {}
    
    # 1. Answer table cells: | 1. D | 2. A |
    table_matches = re.findall(r'\|\s*(\d+)[\.:]\s*([A-D]|True|False|[a-zA-Z\s]+?)\s*(?=\|)', content)
    for q_num, ans in table_matches:
        ans_clean = ans.strip()
        if len(ans_clean) < 30 and not ans_clean.startswith('---'):
            ans_map[int(q_num)] = ans_clean

    # 2. Written questions: **1.** differently or 1. differently
    m_written = re.findall(r'^(?:\*\*)?(\d+)[\.:](?:\*\*)?\s+([a-zA-Z\s\(\)\'\’\/\-]+)$', content, re.M)
    for q_num, ans in m_written:
        qn = int(q_num)
        if qn not in ans_map and len(ans.strip()) < 120:
            ans_map[qn] = ans.strip()

    # 3. Detailed solutions: Đáp án A. / Choose C.
    sol_matches = re.findall(r'(\d+)\.\s*\([A-Z]+\).*?(?:Đáp án\s+([A-D])|Choose\s+([A-D]))', content, re.DOTALL)
    for qn, ans1, ans2 in sol_matches:
        q_idx = int(qn)
        if q_idx not in ans_map:
            ans_map[q_idx] = ans1 or ans2

    return ans_map

def classify_question(q_text, section, options_text):
    """Classify question into Category, Sub-category, CEFR Level, Bloom, Topic, and Bum Week."""
    full = (section + " " + q_text + " " + options_text).lower()

    category = "grammar"
    sub_category = "general_grammar"
    level = "A2"
    bloom = "TH"
    topic = "daily_life"
    bum_week = "week-02"

    # --- 1. PHONETICS ---
    if any(k in full for k in ['pronounced differently', 'underlined part', 'stress in', 'stress pattern', 'primary stress']):
        category = "phonetics"
        topic = "phonetics"
        bloom = "NB"
        bum_week = "week-01"
        if 'stress' in full:
            sub_category = "word_stress"
            level = "A2" if len(q_text + options_text) < 50 else "B1"
        else:
            if any(ed in full for ed in ['ed', 'played', 'watched', 'started', 'delayed']):
                sub_category = "pronunciation_ed"
                level = "A2"
            elif any(s in full for s in ['books', 'pens', 'buses', 'cats', 'dogs']):
                sub_category = "pronunciation_s_es"
                level = "A1"
            else:
                sub_category = "pronunciation_vowel"
                level = "A2"
        return category, sub_category, level, bloom, topic, bum_week

    # --- 2. SIGN & NOTICE ---
    if any(k in full for k in ['sign say', 'sign mean', 'notice say', 'notice tell', 'message mean', 'message say', 'look at the sign', 'look at the notice', 'pedro\'s pizza']):
        category = "sign_notice"
        topic = "public_signs"
        bloom = "NB"
        bum_week = "week-07"
        if 'sign' in full:
            sub_category = "traffic_or_public_sign"
            level = "A1"
        else:
            sub_category = "notice_or_message"
            level = "A2"
        return category, sub_category, level, bloom, topic, bum_week

    # --- 3. SOCIAL EXCHANGES / COMMUNICATION ---
    if any(k in full for k in ['exchange', 'dialogue', 'exchanges', 'speaking to each other', 'talking about']) or re.search(r'[A-Za-z]+:\s*".*?"', q_text):
        category = "communication"
        sub_category = "social_interaction"
        topic = "communication"
        bloom = "TH"
        bum_week = "week-02"
        if any(w in full for w in ['congratulations', 'have a nice trip', 'not at all', 'you\'re welcome', 'good idea', 'fine, thanks']):
            level = "A1"
        else:
            level = "A2"
        return category, sub_category, level, bloom, topic, bum_week

    # --- 4. SENTENCE ARRANGEMENT ---
    if 'meaningful exchange' in full or 'arrangement of utterances' in full:
        category = "communication"
        sub_category = "dialogue_ordering"
        level = "A2"
        bloom = "TH"
        topic = "conversation"
        bum_week = "week-02"
        return category, sub_category, level, bloom, topic, bum_week

    # --- 5. WORD FORMATION ---
    if any(k in full for k in ['correct forms of the words', 'correct form of the word', 'words in capitals', 'words in brackets']) or re.search(r'\([A-Z]{3,}\)', q_text):
        category = "word_formation"
        topic = "vocabulary_building"
        bloom = "VD"
        bum_week = "week-04"
        if any(w in full for w in ['amazingly', 'variety', 'unpolluted', 'undesirable', 'environmentally']):
            level = "B1"
            sub_category = "advanced_derivation"
        else:
            level = "A2"
            sub_category = "standard_derivation"
        return category, sub_category, level, bloom, topic, bum_week

    # --- 6. SENTENCE TRANSFORMATION & COMBINATION ---
    if any(k in full for k in ['same meaning as the original', 'same meaning as the first', 'closest in meaning to', 'best combines two sentences', 'rewrite each', 'meaningful sentences']) or '→' in q_text or '' in q_text:
        category = "sentence_transformation"
        topic = "sentence_structures"
        bloom = "VD"
        if 'combines two' in full:
            sub_category = "combine_relative_clause"
            level = "A2"
            bum_week = "week-09"
        elif 'meaningful sentences' in full:
            sub_category = "sentence_building"
            level = "A2"
            bum_week = "week-03"
        elif any(w in full for w in ['wish', 'wishes', 'it was not until', 'hardly', 'such a']):
            sub_category = "rewrite_wish_or_inversion"
            level = "B1"
            bloom = "VDC"
            bum_week = "week-06"
        elif any(w in full for w in ['because', 'although', 'in spite of', 'despite']):
            sub_category = "rewrite_connectors"
            level = "A2"
            bum_week = "week-07"
        elif 'if' in full or 'unless' in full:
            sub_category = "rewrite_conditional"
            level = "A2"
            bum_week = "week-06"
        else:
            sub_category = "rewrite_general"
            level = "A2"
            bum_week = "week-05"
        return category, sub_category, level, bloom, topic, bum_week

    # --- 7. READING COMPREHENSION ---
    if any(k in full for k in ['according to the passage', 'main idea of the passage', 'passage', 'best title', 'true or false', 'not true about']):
        category = "reading"
        topic = "reading_comprehension"
        bloom = "TH"
        bum_week = "week-08"
        if any(k in full for k in ['main idea', 'best title', 'inference', 'infer', 'author implies']):
            sub_category = "main_idea_or_inference"
            level = "B1"
            bloom = "VD"
        elif any(k in full for k in ['closest in meaning', 'opposite in meaning']):
            sub_category = "vocabulary_in_context"
            level = "B1"
        elif 'refers to' in full:
            sub_category = "reference_pronoun"
            level = "A2"
        else:
            sub_category = "factual_detail"
            level = "A2"
        return category, sub_category, level, bloom, topic, bum_week

    # --- 8. CLOZE TEST ---
    if 'numbered blanks' in full or re.search(r'\(\d+\)\s*_{2,}', q_text):
        category = "reading"
        sub_category = "cloze_test"
        level = "A2"
        bloom = "TH"
        topic = "cloze_passage"
        bum_week = "week-08"
        return category, sub_category, level, bloom, topic, bum_week

    # --- 9. GRAMMAR VS VOCABULARY IN MULTIPLE CHOICE ---
    # Conditional sentences
    if re.search(r'\bif\b', full) and any(w in full for w in ['will', 'would', 'rains', 'slept']):
        return "grammar", "conditional_sentences", "A2", "TH", "hypotheticals", "week-06"

    # Relative clauses
    if any(w in full for w in ['who', 'which', 'whom', 'whose', 'where']) and 'teacher' in full or 'dress' in full or 'city' in full:
        return "grammar", "relative_clauses", "A2", "TH", "people_and_things", "week-09"

    # Tenses & Aspects
    if any(w in full for w in ['yesterday', 'last night', 'last week', 'two days ago', 'at the moment', 'since 20', 'was doing', 'has gone']):
        return "grammar", "verb_tenses", "A2", "TH", "time_and_events", "week-03"

    # Comparisons
    if any(w in full for w in ['more peaceful', 'than', 'the most', 'as ... as', 'the more']):
        return "grammar", "comparisons", "A2", "TH", "describing_things", "week-05"

    # Conjunctions
    if any(w in full for w in ['although', 'because', 'however', 'therefore', 'so that']):
        return "grammar", "conjunctions_and_linkers", "A2", "TH", "logic_and_reasons", "week-07"

    # Prepositions of time / place
    if any(w in full for w in ['on thursday', 'in summer', 'at noon', 'interested in', 'fond of', 'good at']):
        return "grammar", "prepositions", "A1", "NB", "daily_activities", "week-02"

    # Phrasal Verbs
    if any(w in full for w in ['look for', 'turn off', 'turn on', 'go on', 'come in', 'carry out', 'turn down', 'give up', 'look them up']):
        return "vocabulary", "phrasal_verbs", "A2", "TH", "actions_and_habits", "week-04"

    # Environment / Nature / Society topics
    if any(w in full for w in ['environment', 'pollution', 'plastic', 'recycle', 'garbage', 'protect']):
        return "vocabulary", "topic_environment", "A2", "TH", "nature_and_planet", "week-08"

    # General vocabulary
    if any(w in full for w in ['tourist', 'destination', 'provides', 'presents', 'fluently', 'depressed', 'charity']):
        return "vocabulary", "contextual_vocabulary", "A2", "TH", "general_knowledge", "week-01"

    return category, sub_category, level, bloom, topic, bum_week

def process_all_exams():
    md_dir = r'c:\Users\Admin\source\repos\nephew-english\graduation exam\md'
    out_json = r'c:\Users\Admin\source\repos\nephew-english\graduation exam\question-registry.json'
    out_md = r'c:\Users\Admin\source\repos\nephew-english\graduation exam\QUESTION_REGISTRY.md'

    files = sorted([f for f in os.listdir(md_dir) if f.endswith('.md')])
    print(f"Indexing questions from {len(files)} exams...")

    all_questions = []
    global_id = 1

    stats = {
        'total_questions': 0,
        'by_province': {},
        'by_category': {},
        'by_level': {},
        'by_bloom': {},
        'by_bum_week': {}
    }

    for fname in files:
        fpath = os.path.join(md_dir, fname)
        province, year = parse_source_info(fname)
        
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        ans_map = extract_answer_map(content)
        parts = re.split(r'## 📖 ĐÁP ÁN & (?:HƯỚNG DẪN|LỜI GIẢI)', content)
        exam_text = parts[0]

        lines = exam_text.split('\n')
        current_q = None
        current_section = ""

        file_questions = []

        for line in lines:
            l = line.strip()
            if not l:
                continue
            if l.startswith('### ') or l.startswith('## '):
                current_section = l.lstrip('#').strip()
                continue

            # Header match
            m_q = re.match(r'^(?:\*\*)?(?:Question\s+(\d+)|Câu\s+(\d+)|(\d+)\.)(?:\*\*)?[:\.]?\s*(.*)', l, re.I)
            if m_q:
                q_num = int(m_q.group(1) or m_q.group(2) or m_q.group(3))
                q_rest = m_q.group(4).strip()
                if current_q:
                    file_questions.append(current_q)
                current_q = {
                    'number': q_num,
                    'section': current_section,
                    'stem': q_rest,
                    'options': {},
                    'raw_lines': [l]
                }
            elif current_q is not None:
                current_q['raw_lines'].append(l)
                # Option match
                m_opt = re.findall(r'([A-D])[\.:]\s+([^A-D\n]+)', l)
                if m_opt:
                    for opt_letter, opt_val in m_opt:
                        current_q['options'][opt_letter] = opt_val.strip()
                else:
                    if not current_q['stem']:
                        current_q['stem'] = l
                    else:
                        current_q['stem'] += " " + l

        if current_q:
            file_questions.append(current_q)

        # Process questions from this file
        for q in file_questions:
            q_num = q['number']
            opts_str = " ".join([f"{k}. {v}" for k, v in q['options'].items()])
            category, sub_cat, level, bloom, topic, bum_week = classify_question(q['stem'], q['section'], opts_str)
            correct_ans = ans_map.get(q_num, "")

            q_id = f"{re.sub(r'[^A-Z0-9]', '', province.upper())}_{year}_Q{q_num:02d}_{global_id:04d}"
            global_id += 1

            item = {
                'id': q_id,
                'source_file': f"md/{fname}",
                'province': province,
                'year': year,
                'question_number': q_num,
                'section': q['section'],
                'category': category,
                'sub_category': sub_cat,
                'cefr_level': level,
                'bloom_taxonomy': bloom,
                'topic': topic,
                'bum_curriculum_week': bum_week,
                'question_text': q['stem'],
                'options': q['options'],
                'correct_answer': correct_ans
            }

            all_questions.append(item)

            # Update stats
            stats['total_questions'] += 1
            stats['by_province'][province] = stats['by_province'].get(province, 0) + 1
            stats['by_category'][category] = stats['by_category'].get(category, 0) + 1
            stats['by_level'][level] = stats['by_level'].get(level, 0) + 1
            stats['by_bloom'][bloom] = stats['by_bloom'].get(bloom, 0) + 1
            stats['by_bum_week'][bum_week] = stats['by_bum_week'].get(bum_week, 0) + 1

    # Save to JSON database
    registry_data = {
        'version': '1.0.0',
        'description': "Question Bank & Taxonomy Registry for Grade 10 English Entrance Exams",
        'statistics': stats,
        'taxonomy': {
            'categories': ['phonetics', 'grammar', 'vocabulary', 'communication', 'sign_notice', 'reading', 'word_formation', 'sentence_transformation'],
            'cefr_levels': ['A1', 'A2', 'B1', 'B2'],
            'bloom_taxonomy': {'NB': 'Nhận biết', 'TH': 'Thông hiểu', 'VD': 'Vận dụng', 'VDC': 'Vận dụng cao'}
        },
        'questions': all_questions
    }

    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(registry_data, f, ensure_ascii=False, indent=2)

    print(f"-> Saved registry database: {out_json} ({len(all_questions)} questions)")

    # Save to Markdown Document
    md_lines = [
        "# 📑 Question Bank Registry (Ngân Hàng Câu Hỏi Đề Thi Vào Lớp 10)\n",
        "Tập hợp và phân loại chi tiết hơn 380 câu hỏi từ 9 đề thi tuyển sinh vào lớp 10 chính thức của Hà Nội, TP.HCM, Cần Thơ, Thừa Thiên Huế theo **Dạng bài**, **Trình độ CEFR (A1–B2)**, **Cấp độ Bloom (NB/TH/VD/VDC)** và **Chương trình học của Bum**.\n",
        "---",
        "## 📊 Thống Kê Phân Phối Câu Hỏi\n",
        "### 1. Phân loại theo Dạng bài (Category)",
        "| Dạng bài | Số lượng câu | Tỷ lệ (%) | Mô tả & Trọng tâm kiến thức |",
        "| :--- | :---: | :---: | :--- |"
    ]

    total = stats['total_questions']
    cat_desc = {
        'grammar': 'Cấu trúc câu, thì, câu điều kiện, mệnh đề quan hệ, câu bị động, liên từ',
        'vocabulary': 'Từ vựng theo chủ đề, cụm từ cố định (collocations), cụm động từ (phrasal verbs)',
        'reading': 'Đọc hiểu văn bản (Cloze test điền từ, True/False, ý chính, chi tiết)',
        'sentence_transformation': 'Viết lại câu cùng nghĩa, kết hợp câu, sắp xếp từ thành câu hoàn chỉnh',
        'word_formation': 'Biến đổi từ loại (danh - tính - động - trạng) theo ngữ cảnh',
        'phonetics': 'Phát âm đuôi (-ed, -s/es), nguyên âm và trọng âm từ 2-3 âm tiết',
        'communication': 'Giao tiếp tình huống hàng ngày, đối đáp xã hội, phản xạ ngôn ngữ',
        'sign_notice': 'Đọc hiểu biển báo giao thông, bảng tin, áp phích, tin nhắn thực tế'
    }

    for cat, cnt in sorted(stats['by_category'].items(), key=lambda x: -x[1]):
        pct = (cnt / total) * 100
        desc = cat_desc.get(cat, "")
        md_lines.append(f"| **`{cat}`** | {cnt} | {pct:.1f}% | {desc} |")

    md_lines.append("\n### 2. Phân loại theo Trình độ CEFR")
    md_lines.append("| Trình độ CEFR | Số lượng câu | Tỷ lệ (%) | Đánh giá độ khó |")
    md_lines.append("| :---: | :---: | :---: | :--- |")
    for lvl in ['A1', 'A2', 'B1', 'B2']:
        cnt = stats['by_level'].get(lvl, 0)
        pct = (cnt / total) * 100
        desc = {
            'A1': 'Cực kỳ cơ bản (nhận diện thì hiện tại, to-be, từ vựng quen thuộc)',
            'A2': 'Chuẩn cấp 2 (thì quá khứ, câu điều kiện 1, liên từ, so sánh)',
            'B1': 'Phân hóa tuyển sinh (câu ước, đảo ngữ, cấu tạo từ khó, đọc hiểu suy luận)',
            'B2': 'Vận dụng nâng cao / chuyên biệt'
        }.get(lvl, '')
        md_lines.append(f"| **`{lvl}`** | {cnt} | {pct:.1f}% | {desc} |")

    md_lines.append("\n### 3. Phân phối theo Lộ trình học 10 tuần của Bum")
    md_lines.append("| Tuần học (Theme) | Số lượng câu có thể tận dụng | Gợi ý luyện tập |")
    md_lines.append("| :--- | :---: | :--- |")
    week_names = {
        'week-01': 'Week 1: Myself, Tech & Gaming',
        'week-02': 'Week 2: School Life, Friends & Fun',
        'week-03': 'Week 3: Past Adventures & Stories',
        'week-04': 'Week 4: Daily Habits & Chores',
        'week-05': 'Week 5: Sports, Health & Food',
        'week-06': 'Week 6: Future Plans & Predictions',
        'week-07': 'Week 7: City Life vs Countryside',
        'week-08': 'Week 8: Environment & Planet',
        'week-09': 'Week 9: Entertainment, Music & Cinema',
        'week-10': 'Week 10: Review & Boss Battle Mock Exam'
    }
    for wk in sorted(stats['by_bum_week'].keys()):
        cnt = stats['by_bum_week'][wk]
        wname = week_names.get(wk, wk)
        md_lines.append(f"| **`{wname}`** | {cnt} câu | Thử thách Mini-Quiz cuối tuần |")

    md_lines.append("\n---\n")
    md_lines.append("## 🔍 Bảng Tra Cứu Câu Hỏi Nhanh (Sample Registry View)")
    md_lines.append("| ID | Tỉnh / Năm | Dạng | Sub-category | Level | Bloom | Nội dung câu hỏi (Stem) | Đáp án |")
    md_lines.append("| :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: |")

    # Sample representative questions across categories
    sample_categories = {}
    for q in all_questions:
        cat = q['category']
        if cat not in sample_categories:
            sample_categories[cat] = []
        if len(sample_categories[cat]) < 5:
            sample_categories[cat].append(q)

    for cat in sorted(sample_categories.keys()):
        for q in sample_categories[cat]:
            stem_short = (q['question_text'][:65] + "...") if len(q['question_text']) > 65 else q['question_text']
            stem_clean = stem_short.replace('|', '\\|')
            ans = q['correct_answer'] or "-"
            md_lines.append(f"| `{q['id'][:18]}` | {q['province']} {q['year']} | `{q['category']}` | `{q['sub_category']}` | **{q['cefr_level']}** | `{q['bloom_taxonomy']}` | {stem_clean} | **{ans}** |")

    md_lines.append("\n\n> [!TIP]")
    md_lines.append("> Sử dụng công cụ `py scripts/query_registry.py` để tra cứu đầy đủ 380+ câu hỏi hoặc xuất thành bài kiểm tra theo yêu cầu!")

    with open(out_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines) + '\n')

    print(f"-> Saved registry markdown catalog: {out_md}")
    return stats

if __name__ == '__main__':
    process_all_exams()

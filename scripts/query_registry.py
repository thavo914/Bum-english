"""
Question Registry Look-up & Practice Generator CLI
==================================================
Allows querying, filtering, and exporting questions from 'graduation exam/question-registry.json'.

Usage Examples:
    # 1. View statistics:
    py scripts/query_registry.py --stats

    # 2. Find 5 A2 grammar questions:
    py scripts/query_registry.py --category grammar --level A2 --limit 5

    # 3. Find questions matching Bum's current week:
    py scripts/query_registry.py --bum-week week-02 --random --limit 5

    # 4. Search questions by keyword (e.g. conditional):
    py scripts/query_registry.py --keyword "if" --limit 5

    # 5. Export a customized 10-question quiz for Bum:
    py scripts/query_registry.py --category grammar --level A2 --random --limit 10 --export-quiz "assessments/bum-a2-grammar-quiz.md"
"""

import os
import sys
import json
import random
import argparse

REGISTRY_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "graduation exam", "question-registry.json")

def load_registry():
    if not os.path.exists(REGISTRY_PATH):
        print(f"Error: Registry file not found at {REGISTRY_PATH}")
        print("Please run 'py scripts/build_question_registry.py' first!")
        sys.exit(1)
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def print_stats(registry):
    stats = registry.get('statistics', {})
    total = stats.get('total_questions', 0)
    print("\n" + "=" * 60)
    print(f"📊 QUESTION REGISTRY STATISTICS (Total Questions: {total})")
    print("=" * 60)

    print("\n1. By Category:")
    for cat, cnt in sorted(stats.get('by_category', {}).items(), key=lambda x: -x[1]):
        print(f"   - {cat:<24}: {cnt:3d} ({cnt/total*100:4.1f}%)")

    print("\n2. By CEFR Level:")
    for lvl in ['A1', 'A2', 'B1', 'B2']:
        cnt = stats.get('by_level', {}).get(lvl, 0)
        print(f"   - {lvl:<24}: {cnt:3d} ({cnt/total*100:4.1f}%)")

    print("\n3. By Province:")
    for prov, cnt in sorted(stats.get('by_province', {}).items(), key=lambda x: -x[1]):
        print(f"   - {prov:<24}: {cnt:3d} ({cnt/total*100:4.1f}%)")

    print("\n4. By Bum's Curriculum Week:")
    for wk, cnt in sorted(stats.get('by_bum_week', {}).items()):
        print(f"   - {wk:<24}: {cnt:3d}")
    print("=" * 60 + "\n")

def export_quiz(questions, output_path, title="Bum's Real Exam Challenge 🎮"):
    """Export selected questions to a clean Markdown practice test."""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    lines = [
        f"# 🏆 {title}\n",
        "> **Target**: Bum (Grade 8 / 9 - CEFR A1-A2)  ",
        f"> **Total Questions**: {len(questions)} câu hỏi từ đề thi tuyển sinh vào lớp 10 thật  ",
        "> **Time**: 15–20 phút\n",
        "---\n",
        "## 📝 Phần Làm Bài\n"
    ]

    answers = []
    for idx, q in enumerate(questions, 1):
        lines.append(f"### Câu {idx:02d} `[{q['cefr_level']}]` *({q['province']} {q['year']})*")
        lines.append(f"**{q['question_text']}**\n")
        if q.get('options'):
            for letter in ['A', 'B', 'C', 'D']:
                if letter in q['options']:
                    lines.append(f"- **{letter}.** {q['options'][letter]}")
            lines.append("")
        answers.append(f"**Câu {idx:02d}:** `{q['correct_answer'] or 'Xem lời giải'}` (*{q['category']} - {q['sub_category']}*)")

    lines.append("\n---\n")
    lines.append("## 🔍 Đáp Án & Tra Cứu\n")
    lines.append("<details>")
    lines.append("<summary><b>Click to reveal answers 🔍</b></summary>\n")
    lines.extend(answers)
    lines.append("\n</details>\n")
    lines.append("### Scorecard:")
    lines.append("- [ ] ⭐ ⭐ ⭐ (Mastered: ≥ 90%)")
    lines.append("- [ ] ⭐ ⭐ (Good Progress: 70–89%)")
    lines.append("- [ ] ⭐ (Needs Practice: < 70%)\n")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"\n-> Successfully exported quiz to: {output_path}")

def main():
    sys.stdout.reconfigure(encoding='utf-8')

    parser = argparse.ArgumentParser(description="Query and look up questions from Grade 10 exam registry.")
    parser.add_argument("--stats", action="store_true", help="Show registry statistics summary.")
    parser.add_argument("--category", "-c", help="Filter by category (grammar, vocabulary, phonetics, reading, etc.)")
    parser.add_argument("--sub-category", help="Filter by sub-category (e.g. conditional_sentences, word_stress, etc.)")
    parser.add_argument("--level", "-l", help="Filter by CEFR level (A1, A2, B1, B2)")
    parser.add_argument("--bloom", help="Filter by Bloom taxonomy (NB, TH, VD, VDC)")
    parser.add_argument("--province", "-p", help="Filter by province (Cần Thơ, Hà Nội, TP. Hồ Chí Minh, Thừa Thiên Huế)")
    parser.add_argument("--bum-week", "-w", help="Filter by Bum's curriculum week (week-01 to week-10)")
    parser.add_argument("--keyword", "-k", help="Search keyword in question text")
    parser.add_argument("--limit", "-n", type=int, default=5, help="Number of questions to display (default: 5)")
    parser.add_argument("--random", "-r", action="store_true", help="Shuffle results randomly")
    parser.add_argument("--export-quiz", "-e", help="Export filtered questions to a practice Markdown quiz file")

    args = parser.parse_args()
    registry = load_registry()

    if args.stats:
        print_stats(registry)
        return

    questions = registry.get('questions', [])

    # Filter
    if args.category:
        questions = [q for q in questions if q['category'].lower() == args.category.lower()]
    if args.sub_category:
        questions = [q for q in questions if args.sub_category.lower() in q['sub_category'].lower()]
    if args.level:
        questions = [q for q in questions if q['cefr_level'].upper() == args.level.upper()]
    if args.bloom:
        questions = [q for q in questions if q['bloom_taxonomy'].upper() == args.bloom.upper()]
    if args.province:
        questions = [q for q in questions if args.province.lower() in q['province'].lower()]
    if args.bum_week:
        questions = [q for q in questions if q['bum_curriculum_week'].lower() == args.bum_week.lower()]
    if args.keyword:
        kw = args.keyword.lower()
        questions = [q for q in questions if kw in q['question_text'].lower() or any(kw in str(v).lower() for v in q.get('options', {}).values())]

    total_matched = len(questions)
    print(f"\n🔍 Found {total_matched} matching question(s).")

    if args.random:
        random.shuffle(questions)

    selected = questions[:args.limit]

    if args.export_quiz:
        export_quiz(selected, args.export_quiz)
        return

    # Print to console
    for idx, q in enumerate(selected, 1):
        print("\n" + "-" * 60)
        print(f"[{idx:02d}] ID: {q['id']} | {q['province']} {q['year']} | Level: {q['cefr_level']} | Type: {q['category']} ({q['sub_category']})")
        print(f"Stem: {q['question_text']}")
        if q.get('options'):
            for k in ['A', 'B', 'C', 'D']:
                if k in q['options']:
                    print(f"   {k}. {q['options'][k]}")
        print(f"-> Correct Answer: {q['correct_answer'] or 'N/A'} (Bum Curriculum: {q['bum_curriculum_week']})")
    print("-" * 60 + "\n")

if __name__ == '__main__':
    main()

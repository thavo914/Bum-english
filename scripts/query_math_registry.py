"""
Math Question Registry Look-up & Quiz Generator CLI
===================================================
Allows querying, filtering by difficulty (1-5), problem type, and exporting custom practice tests for Bum.

Usage Examples:
    # 1. View statistics and distribution:
    py scripts/query_math_registry.py --stats

    # 2. Find 5 Level 2 (cơ bản) questions on Căn thức:
    py scripts/query_math_registry.py --category can_thuc --difficulty 2 --limit 5

    # 3. Find Level 5 (phân loại điểm 10) questions on Bất đẳng thức:
    py scripts/query_math_registry.py --category bat_dang_thuc_cuc_tri --difficulty 5

    # 4. Search questions by keyword (e.g. "parabol", "đèn lồng"):
    py scripts/query_math_registry.py --keyword "parabol" --limit 5

    # 5. Export a custom practice mock test for Bum at difficulty 3:
    py scripts/query_math_registry.py --difficulty 3 --limit 5 --export-quiz "math/assessments/de-luyen-tap-muc-3.md"
"""

import os
import sys
import json
import random
import argparse

REGISTRY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "math", "exams", "math-question-registry.json"
)

def load_registry():
    if not os.path.exists(REGISTRY_PATH):
        print(f"Error: Math registry file not found at {REGISTRY_PATH}")
        print("Please run 'py scripts/build_math_registry.py' first!")
        sys.exit(1)
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def print_stats(registry):
    stats = registry.get('statistics', {})
    total = stats.get('total_questions', 0)
    print("\n" + "=" * 65)
    print(f"📊 BẢNG THỐNG KÊ NGÂN HÀNG CÂU HỎI TOÁN VÀO 10 (Tổng: {total} câu)")
    print("=" * 65)

    print("\n1. Phân bố theo Dạng Bài (Category):")
    for cat, cnt in sorted(stats.get('by_category', {}).items(), key=lambda x: -x[1]):
        pct = (cnt / total) * 100 if total > 0 else 0
        print(f"   - {cat:<26}: {cnt:>2} câu ({pct:>4.1f}%)")

    print("\n2. Phân bố theo Thang Độ Khó (Difficulty 1 – 5):")
    diff_labels = {
        1: "Level 1: Nhận biết (Dễ)",
        2: "Level 2: Thông hiểu (Cơ bản)",
        3: "Level 3: Vận dụng (Khá 7.5 - 8.5đ)",
        4: "Level 4: Vận dụng cao (Giỏi 8.5 - 9.25đ)",
        5: "Level 5: Phân loại điểm 10 (Xuất sắc 9.5 - 10đ)"
    }
    for lvl in [1, 2, 3, 4, 5]:
        cnt = stats.get('by_difficulty', {}).get(str(lvl), stats.get('by_difficulty', {}).get(lvl, 0))
        pct = (cnt / total) * 100 if total > 0 else 0
        print(f"   - ⭐ {diff_labels[lvl]:<40}: {cnt:>2} câu ({pct:>4.1f}%)")

    print("\n3. Phân bố theo Tỉnh / Thành Phố:")
    for prov, cnt in sorted(stats.get('by_province', {}).items(), key=lambda x: -x[1]):
        pct = (cnt / total) * 100 if total > 0 else 0
        print(f"   - {prov:<26}: {cnt:>2} câu ({pct:>4.1f}%)")
    print("=" * 65 + "\n")

def filter_questions(questions, category=None, difficulty=None, province=None, keyword=None):
    results = []
    for q in questions:
        if category and q['category'] != category:
            continue
        if difficulty is not None and int(q['difficulty_level']) != int(difficulty):
            continue
        if province and province.lower() not in q['province'].lower():
            continue
        if keyword:
            kw = keyword.lower()
            text_full = (q['question_header'] + " " + q['question_text']).lower()
            if kw not in text_full:
                continue
        results.append(q)
    return results

def display_questions(questions, limit=10):
    print(f"\n🔍 Tìm thấy {len(questions)} câu hỏi phù hợp:")
    for idx, q in enumerate(questions[:limit], 1):
        stars = "⭐" * int(q['difficulty_level'])
        print(f"\n[{idx}] {q['id']} | {q['province']} {q['year']} | Dạng: {q['category']} | Độ khó: {stars}")
        print(f"    Tiêu đề: {q['question_header']}")
        print(f"    Nội dung: {q['question_text'][:160]}...")
        print(f"    Nguồn: math/exams/{q['source_file']}")

def export_quiz(questions, out_file, title="Đề Luyện Tập Môn Toán"):
    lines = [
        f"# 📝 {title}",
        f"\n*Tập hợp {len(questions)} câu hỏi trích từ ngân hàng đề thi vào 10 chính thức*\n",
        "---"
    ]
    for idx, q in enumerate(questions, 1):
        stars = "⭐" * int(q['difficulty_level'])
        lines.append(f"\n### Câu {idx}: ({q['question_header']}) - Độ khó: {stars}")
        lines.append(f"> **Nguồn**: {q['province']} {q['year']} | Dạng bài: `{q['category']}` / `{q['sub_category']}`\n")
        lines.append(q['question_text'] + "\n")
        lines.append(f"*Xem lời giải chi tiết tại*: [`math/exams/{q['source_file']}`]({q['source_file']})\n")
        lines.append("---")

    lines.append("\n## 🌟 Bảng Tự Đánh Giá (Scorecard)")
    lines.append("- [ ] ⭐ Đạt 5 - 6 điểm (Nắm chắc các câu Level 1 - 2)")
    lines.append("- [ ] ⭐⭐ Đạt 7 - 8 điểm (Giải đúng các câu Level 3)")
    lines.append("- [ ] ⭐⭐⭐ Đạt 9 - 10 điểm (Hoàn thành câu Level 4 - 5)")

    out_path = os.path.abspath(out_file)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
    print(f"\n-> Đã xuất bài luyện tập: {out_path} ({len(questions)} câu)")

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description="Tra cứu và xuất bài tập đề thi vào 10 môn Toán.")
    parser.add_argument("--stats", action="store_true", help="Hiển thị thống kê ngân hàng câu hỏi")
    parser.add_argument("--category", type=str, help="Lọc theo dạng bài (can_thuc, pt_bac_hai_viet, toan_thuc_te, hinh_hoc_phang, bat_dang_thuc_cuc_tri,...)")
    parser.add_argument("--difficulty", type=int, choices=[1, 2, 3, 4, 5], help="Lọc theo độ khó từ 1 đến 5")
    parser.add_argument("--province", type=str, help="Lọc theo tỉnh thành (Hà Nội, TP.HCM)")
    parser.add_argument("--keyword", type=str, help="Tìm kiếm theo từ khóa trong đề")
    parser.add_argument("--limit", type=int, default=10, help="Số lượng kết quả hiển thị tối đa (mặc định: 10)")
    parser.add_argument("--random", action="store_true", help="Trộn ngẫu nhiên kết quả")
    parser.add_argument("--export-quiz", type=str, help="Đường dẫn file markdown để xuất đề kiểm tra")

    args = parser.parse_args()
    registry = load_registry()

    if args.stats or len(sys.argv) == 1:
        print_stats(registry)
        if len(sys.argv) == 1:
            print("Gợi ý: Dùng 'py scripts/query_math_registry.py --help' để xem các tùy chọn tra cứu chi tiết!")
            return

    questions = registry.get('questions', [])
    filtered = filter_questions(questions, args.category, args.difficulty, args.province, args.keyword)

    if args.random:
        random.shuffle(filtered)

    selected = filtered[:args.limit]

    if args.export_quiz:
        export_quiz(selected, args.export_quiz, title=f"Đề Luyện Tập Môn Toán (Độ khó: Level {args.difficulty or 'Tổng hợp'})")
    else:
        display_questions(selected, limit=args.limit)

if __name__ == '__main__':
    main()

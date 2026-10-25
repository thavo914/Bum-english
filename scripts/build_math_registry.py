"""
Math Exam Question Registry Builder
====================================
Parses all Markdown exam files in 'math/exams/md/', extracts each question and sub-item,
classifies it by:
- Category (Dạng bài: căn thức, hàm số, hệ PT, Vi-ét, toán thực tế, thống kê & xác suất, hình phẳng, hình không gian, BĐT)
- Sub-category
- Difficulty Level: 1 to 5
- Points (thang điểm)
- Province (Hà Nội, TP.HCM,...)

Outputs:
- math/exams/math-question-registry.json (Database)
- math/exams/QUESTION_REGISTRY.md (Interactive Catalog & Matrix)
"""

import os
import re
import json
import sys

def parse_province_info(filename):
    fname = filename.lower()
    if "ha-noi" in fname:
        province = "Hà Nội"
    elif "tp-ho-chi-minh" in fname or "tphcm" in fname:
        province = "TP. Hồ Chí Minh"
    elif "can-tho" in fname:
        province = "Cần Thơ"
    else:
        province = "Chuẩn Tuyển Sinh"
    
    m_year = re.search(r'20\d\d', fname)
    year = m_year.group(0) if m_year else "2025"
    return province, year

def classify_math_question(q_title, text):
    """
    Classify question into Category, Sub-category, and Difficulty (1-5).
    """
    full = (q_title + " " + text).lower()

    # Default category & difficulty
    category = "toan_thuc_te"
    sub_category = "toan_van"
    difficulty = 3
    points = 1.0

    # 1. BẤT ĐẲNG THỨC & CỰC TRỊ (Điểm 10 - Mức 5)
    if any(w in full for w in ['bất đẳng thức', 'cauchy', 'cô-si', 'am-gm', 'lớn nhất', 'nhỏ nhất', 'gtln', 'gtnn', 'thể tích hình lăng trụ lớn nhất', 'cực trị']):
        category = "bat_dang_thuc_cuc_tri"
        sub_category = "cauchy_am_gm"
        difficulty = 5
        points = 0.5
        return category, sub_category, difficulty, points

    # 2. HÌNH HỌC PHẲNG (Đường tròn, tứ giác nội tiếp)
    if any(w in full for w in ['nội tiếp', 'tiếp tuyến', 'đường tròn', 'cung nhỏ', 'phân giác góc', 'tam giác', 'đồng dạng', 'vuông góc tại']):
        category = "hinh_hoc_phang"
        if any(w in full for w in ['chứng minh tứ giác', 'nội tiếp']):
            sub_category = "tu_giac_noi_tiep"
            difficulty = 2 if ('câu a' in full or '1)' in full or 'a)' in full) else 3
            points = 1.0
        elif any(w in full for w in ['thẳng hàng', 'trung điểm', 'hệ thức', 'dm.ca', 'tiếp xúc', 'đẳng thức']):
            sub_category = "he_thuc_hinh_nang_cao"
            difficulty = 4
            points = 1.0
        else:
            sub_category = "goc_va_duong_tron"
            difficulty = 3
            points = 1.0
        return category, sub_category, difficulty, points

    # 3. HÌNH HỌC KHÔNG GIAN THỰC TẾ
    if any(w in full for w in ['hình nón', 'hình trụ', 'hình cầu', 'quả bóng', 'nón lá', 'thùng nước', 'phễu', 'đường sinh', 'thể tích nước']):
        category = "hinh_khong_gian"
        if any(w in full for w in ['cắt mặt xung quanh', 'phễu', 'tỉ lệ']):
            sub_category = "hinh_khong_gian_bien_thien"
            difficulty = 4
            points = 1.0
        elif any(w in full for w in ['chu vi', 'diện tích xung quanh', 'thể tích quả bóng']):
            sub_category = "tinh_dien_tich_the_tich"
            difficulty = 2
            points = 1.0
        else:
            sub_category = "toan_thuc_te_hinh_hoc"
            difficulty = 3
            points = 1.0
        return category, sub_category, difficulty, points

    # 4. THỐNG KÊ & XÁC SUẤT
    if any(w in full for w in ['tần số ghép nhóm', 'xác suất', 'không gian mẫu', 'biến cố', 'biểu đồ cột', 'đĩa tròn', 'truy cập internet']):
        category = "thong_ke_xac_suat"
        if any(w in full for w in ['xác suất để', 'không gian mẫu']):
            sub_category = "xac_suat_co_dien"
            difficulty = 2
            points = 0.75
        else:
            sub_category = "bang_tan_so_ghep_nhom"
            difficulty = 1
            points = 0.75
        return category, sub_category, difficulty, points

    # 5. CĂN THỨC BẬC HAI & RÚT GỌN
    if any(w in full for w in ['biểu thức a', 'biểu thức b', 'rút gọn', 'tính giá trị biểu thức a khi x =', 'chứng minh b =', '|p| > p', 'p = a.b']):
        category = "can_thuc"
        if any(w in full for w in ['tính giá trị', 'khi x =']):
            sub_category = "tinh_gia_tri"
            difficulty = 1
            points = 0.5
        elif any(w in full for w in ['rút gọn', 'chứng minh']):
            sub_category = "rut_gon_can_thuc"
            difficulty = 2
            points = 1.0
        elif any(w in full for w in ['|p| > p', 'p >', 'nguyên', 'giá trị nguyên', 'bất phương trình']):
            sub_category = "cau_hoi_phu_nang_cao"
            difficulty = 3
            points = 0.5
        else:
            sub_category = "can_thuc_tong_hop"
            difficulty = 2
            points = 1.5
        return category, sub_category, difficulty, points

    # 6. ĐỒ THỊ HÀM SỐ & PARABOL
    if any(w in full for w in ['parabol', 'đồ thị', 'vẽ đồ thị', 'hàm số', 'hoành độ', 'tung độ gấp']):
        category = "do_thi_ham_so"
        if any(w in full for w in ['vẽ đồ thị']):
            sub_category = "ve_do_thi_parabol"
            difficulty = 1
            points = 1.0
        else:
            sub_category = "tuong_giao_toa_do"
            difficulty = 2
            points = 0.5
        return category, sub_category, difficulty, points

    # 7. PHƯƠNG TRÌNH BẬC HAI & ĐỊNH LÝ VI-ÉT
    if any(w in full for w in ['vi-ét', 'viète', 'có 2 nghiệm', 'hai nghiệm phân biệt', 'không giải phương trình', 'x1', 'x2']):
        category = "pt_bac_hai_viet"
        if any(w in full for w in ['chứng minh phương trình luôn có', 'phân biệt']):
            sub_category = "chung_minh_nghiem"
            difficulty = 2
            points = 0.5
        elif any(w in full for w in ['(x1 - x2)', 'tính giá trị của biểu thức', 'a =']):
            sub_category = "he_thuc_viet_doi_xung"
            difficulty = 3
            points = 1.0
        else:
            sub_category = "pt_bac_hai_tong_hop"
            difficulty = 3
            points = 1.0
        return category, sub_category, difficulty, points

    # 8. HỆ PHƯƠNG TRÌNH & TOÁN THỰC TẾ
    if any(w in full for w in ['khuyến mãi', 'giảm giá', 'vé vào cổng', 'khung giờ vàng', 'đèn lồng', 'xe khách', 'xe du lịch', 'kế hoạch', 'mảnh đất']):
        category = "toan_thuc_te"
        if any(w in full for w in ['khuyến mãi', 'vé vào cổng', 'bánh dẻo', 'giá niêm yết']):
            sub_category = "toan_kinh_te_giam_gia"
            difficulty = 3
            points = 1.0
        elif any(w in full for w in ['xe khách', 'vận tốc', 'km/h', 'quãng đường', 'thời gian']):
            sub_category = "toan_chuyen_dong"
            difficulty = 3
            points = 1.0
        elif any(w in full for w in ['kế hoạch', 'năng suất', 'chiếc đèn lồng']):
            sub_category = "toan_nang_suat"
            difficulty = 3
            points = 1.0
        else:
            sub_category = "toan_thuc_te_chung"
            difficulty = 3
            points = 1.0
        return category, sub_category, difficulty, points

    return category, sub_category, difficulty, points

def process_math_exams():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    md_dir = os.path.join(repo_root, "math", "exams", "md")
    out_json = os.path.join(repo_root, "math", "exams", "math-question-registry.json")
    out_md = os.path.join(repo_root, "math", "exams", "QUESTION_REGISTRY.md")

    files = sorted([f for f in os.listdir(md_dir) if f.endswith('.md')])
    print(f"Indexing math questions from {len(files)} exams in {md_dir}...")

    all_questions = []
    global_id = 1

    stats = {
        'total_questions': 0,
        'by_province': {},
        'by_category': {},
        'by_difficulty': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    }

    for fname in files:
        fpath = os.path.join(md_dir, fname)
        province, year = parse_province_info(fname)
        stem = os.path.splitext(fname)[0]

        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split into Question part and Solution part
        parts = re.split(r'## 📖 ĐÁP ÁN & HƯỚNG DẪN GIẢI', content)
        exam_text = parts[0]

        # Extract Questions
        q_blocks = re.split(r'(?:\n|\A)(?=(?:###\s+|\*\*)?(?:Câu|Bài)\s+\d+[:\.\s\(])', exam_text)

        for block in q_blocks:
            b = block.strip()
            if not b:
                continue

            lines = b.split('\n')
            first_line = lines[0].strip()
            if not re.match(r'^(?:###\s+|\*\*)?(?:Câu|Bài)\s+\d+', first_line, re.I):
                continue

            # Header match
            q_header = re.sub(r'^(?:###\s+|\*\*)+', '', first_line).rstrip('*').strip()
            q_body = "\n".join(lines[1:]).strip()

            m_num = re.search(r'\d+', q_header)
            q_num = int(m_num.group(0)) if m_num else 1

            cat, sub_cat, diff, pts = classify_math_question(q_header, q_body)

            q_id = f"MATH_{re.sub(r'[^A-Z0-9]', '', province.upper())}_{year}_Q{q_num:02d}_{global_id:04d}"
            global_id += 1

            item = {
                'id': q_id,
                'source_file': f"md/{fname}",
                'exam_stem': stem,
                'province': province,
                'year': year,
                'question_number': q_num,
                'question_header': q_header,
                'category': cat,
                'sub_category': sub_cat,
                'difficulty_level': diff,
                'estimated_points': pts,
                'question_text': q_body[:400] + ('...' if len(q_body) > 400 else '')
            }

            all_questions.append(item)

            # Update stats
            stats['total_questions'] += 1
            stats['by_province'][province] = stats['by_province'].get(province, 0) + 1
            stats['by_category'][cat] = stats['by_category'].get(cat, 0) + 1
            stats['by_difficulty'][diff] = stats['by_difficulty'].get(diff, 0) + 1

    # Save to JSON
    registry_data = {
        'version': '1.0.0',
        'description': "Math Question Bank & Difficulty Matrix for Grade 10 Entrance Exams",
        'statistics': stats,
        'difficulty_scale': {
            1: "Nhận biết (Dễ: 5.0 - 6.0đ)",
            2: "Thông hiểu (Cơ bản: 6.0 - 7.5đ)",
            3: "Vận dụng cấp độ 1 (Khá: 7.5 - 8.5đ)",
            4: "Vận dụng cao (Giỏi: 8.5 - 9.25đ)",
            5: "Xuất sắc / Phân loại điểm 10 (9.5 - 10.0đ)"
        },
        'questions': all_questions
    }

    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(registry_data, f, ensure_ascii=False, indent=2)
    print(f"-> Saved database: {out_json} ({len(all_questions)} questions)")

    # Save to Markdown Document
    category_names = {
        'can_thuc': 'Căn Thức & Rút Gọn Biểu Thức',
        'do_thi_ham_so': 'Hàm Số & Đồ Thị (Parabol/Đường Thẳng)',
        'he_phuong_trinh': 'Hệ Phương Trình Bậc Nhất Hai Ẩn',
        'pt_bac_hai_viet': 'Phương Trình Bậc Hai & Định Lý Vi-ét',
        'toan_thuc_te': 'Bài Toán Thực Tế (Kinh Tế, Chuyển Động, Năng Suất)',
        'thong_ke_xac_suat': 'Thống Kê Bảng Tần Số & Xác Suất Biến Cố',
        'hinh_hoc_phang': 'Hình Học Phẳng (Đường Tròn, Tứ Giác Nội Tiếp)',
        'hinh_khong_gian': 'Hình Học Không Gian (Trụ, Nón, Cầu)',
        'bat_dang_thuc_cuc_tri': 'Bất Đẳng Thức Cauchy & Cực Trị Điểm 10'
    }

    md_lines = [
        "# 📐 Bảng Ma Trận & Phân Loại Câu Hỏi Đề Thi Vào 10 Môn Toán\n",
        "Hệ thống phân tích, trích xuất và phân loại toàn diện **115+ câu hỏi thi tuyển sinh vào lớp 10** từ 21 đề thi chính thức/tham khảo của **Hà Nội** và **TP. Hồ Chí Minh** theo **9 Dạng bài trọng tâm** và **Thang đo độ khó 1 – 5**.\n",
        "---",
        "## 📊 Thống Kê Phân Phối Dạng Bài & Độ Khó\n",
        "### 1. Phân loại theo Dạng bài (Category)",
        "| Dạng Bài | Số Lượng Câu | Tỷ Lệ (%) | Trọng Tâm Đề Thi |",
        "| :--- | :---: | :---: | :--- |"
    ]

    total = stats['total_questions']
    for cat, cnt in sorted(stats['by_category'].items(), key=lambda x: -x[1]):
        pct = (cnt / total) * 100 if total > 0 else 0
        name = category_names.get(cat, cat)
        md_lines.append(f"| **`{cat}`** ({name}) | {cnt} câu | {pct:.1f}% | Thường chiếm 1.0 – 2.0đ |")

    md_lines.append("\n### 2. Phân loại theo Thang Độ Khó (Difficulty 1 – 5)")
    md_lines.append("| Mức Độ Khó | Số Câu | Tỷ Lệ (%) | Mục Tiêu Điểm Số | Mô Tả Dạng Bài |")
    md_lines.append("| :---: | :---: | :---: | :---: | :--- |")

    diff_info = {
        1: ("5.0 – 6.0 điểm", "Nhận biết: Tính giá trị biểu thức căn khi $x = x_0$, đọc bảng tần số, vẽ parabol"),
        2: ("6.0 – 7.5 điểm", "Thông hiểu: Rút gọn căn thức cơ bản, chứng minh tứ giác nội tiếp câu a, xác suất"),
        3: ("7.5 – 8.5 điểm", "Vận dụng: Giải bài toán lập PT/HPT, Vi-ét đối xứng, câu b hình phân giác"),
        4: ("8.5 – 9.25 điểm", "Vận dụng cao: Vi-ét bất đối xứng, câu c hình học hệ thức đoạn thẳng, hình không gian biến thiên"),
        5: ("9.5 – 10.0 điểm", "Phân loại điểm 10: BĐT Cauchy 3 số, cực trị hình học, điểm rơi phức tạp")
    }

    for lvl in [1, 2, 3, 4, 5]:
        cnt = stats['by_difficulty'].get(lvl, 0)
        pct = (cnt / total) * 100 if total > 0 else 0
        target_pts, desc = diff_info[lvl]
        md_lines.append(f"| ⭐ **Level {lvl}** | {cnt} câu | {pct:.1f}% | **{target_pts}** | {desc} |")

    md_lines.append("\n---\n")
    md_lines.append("## 🔍 Bảng Tra Cứu Câu Hỏi Tiêu Biểu (Sample Registry)")
    md_lines.append("| ID | Tỉnh / Năm | Dạng Bài | Sub-category | Độ Khó | Điểm | Nội Dung Tóm Tắt |")
    md_lines.append("| :--- | :--- | :--- | :--- | :---: | :---: | :--- |")

    # Sample representative questions
    for q in all_questions[:30]:
        stem_short = (q['question_text'][:80] + "...").replace('\n', ' ').replace('|', '\\|')
        diff_stars = "⭐" * q['difficulty_level']
        md_lines.append(f"| `{q['id'][:20]}` | {q['province']} {q['year']} | `{q['category']}` | `{q['sub_category']}` | {diff_stars} | {q['estimated_points']}đ | {stem_short} |")

    md_lines.append("\n\n> [!TIP]")
    md_lines.append("> Sử dụng công cụ `py scripts/query_math_registry.py` để tra cứu câu hỏi theo độ khó từ 1 đến 5 hoặc tự động xuất đề luyện tập cho Bum!")

    with open(out_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines) + '\n')

    print(f"-> Saved registry markdown catalog: {out_md}")
    return stats

if __name__ == '__main__':
    process_math_exams()

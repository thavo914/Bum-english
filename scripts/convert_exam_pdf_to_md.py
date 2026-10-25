"""
PDF to Markdown Converter for Graduation & Entrance Exams
=========================================================
Converts Grade 9-10 entrance & graduation exam PDF files into structured,
high-quality Markdown documents for Bum's English learning repository.

Features:
- Extracts question text, multiple choice options (A, B, C, D), and reading passages.
- Extracts illustration images (signs, notices, posters) into an images/ subfolder.
- Identifies and formats tables (answer keys, dictionary entries).
- Wraps answer keys & solutions into collapsible <details><summary> tags.
- Generates/updates a summary README.md table for the directory.

Usage:
    # Convert all PDFs in 'graduation exam' folder:
    py scripts/convert_exam_pdf_to_md.py

    # Convert a specific PDF:
    py scripts/convert_exam_pdf_to_md.py "graduation exam/example.pdf"

    # Convert a directory and specify custom output:
    py scripts/convert_exam_pdf_to_md.py "graduation exam" --output-dir "graduation exam"
"""

import argparse
import os
import re
import sys

try:
    import pymupdf  # type: ignore
except ImportError:
    try:
        import fitz as pymupdf  # type: ignore
    except ImportError:
        print("Error: 'pymupdf' is required. Please install it using:")
        print("    pip install pymupdf")
        sys.exit(1)


def format_markdown_table(rows):
    """Convert 2D array of rows into a GitHub Flavored Markdown table."""
    if not rows:
        return ""
    valid_rows = []
    for r in rows:
        cr = [str(c or '').replace('\n', ' ').strip() for c in r]
        if any(cr):
            valid_rows.append(cr)
    if not valid_rows:
        return ""

    max_cols = max(len(r) for r in valid_rows)
    if max_cols == 0:
        return ""

    clean_rows = []
    for r in valid_rows:
        cr = r + [''] * (max_cols - len(r))
        clean_rows.append(cr)

    header = clean_rows[0]
    sep = [':---:'] * max_cols
    md_lines = [
        '| ' + ' | '.join(header) + ' |',
        '| ' + ' | '.join(sep) + ' |'
    ]
    for r in clean_rows[1:]:
        md_lines.append('| ' + ' | '.join(r) + ' |')
    return '\n'.join(md_lines)


def is_answer_table(rows):
    """Check if table contains question answers like '1. A' or '2. D'."""
    count_ans = 0
    total = 0
    for r in rows:
        for c in r:
            if c:
                total += 1
                val = str(c).strip()
                if re.match(r'^\d+\s*[\.:]\s*[A-D]', val, re.I) or val.lower() in ['true', 'false']:
                    count_ans += 1
    return total > 0 and (count_ans / total) >= 0.35


def is_dict_table(rows):
    """Check if table is a dictionary entry (e.g., word habit definition)."""
    for r in rows:
        for c in r:
            if c and any(w in str(c).lower() for w in ['/hæbɪt/', 'noun', 'eating habits', '[countable]']):
                return True
    return False


def format_dict_table(rows):
    """Format dictionary entry table into a styled blockquote."""
    lines = ["> ### 📖 Dictionary Entry\n>"]
    for r in rows:
        for c in r:
            if c:
                text = str(c).strip()
                for line in text.split('\n'):
                    l = line.strip()
                    if l:
                        if l.startswith('o '):
                            lines.append(f"> - {l[2:]}")
                        else:
                            lines.append(f"> {l}")
    return '\n'.join(lines) + '\n'


def is_layout_table(rows):
    """Check if table is candidate registration, score grading, or exam paper header."""
    for r in rows:
        for c in r:
            if c and any(kw in str(c) for kw in ['Điểm phần', 'Giám thị', 'SỐ PHÁCH', 'Họ và tên thí sinh']):
                return True
    return False


def clean_question_text(text):
    """Format Question X and separate choices if grouped."""
    m = re.match(r'^(Question\s+\d+[:\.]|Câu\s+\d+[:\.]|\d+\.)\s*(.*)', text, re.I | re.DOTALL)
    if m:
        q_label = m.group(1).strip()
        rest = m.group(2).strip()

        m_opts = re.match(r'^(A[\.:].*)', rest)
        if m_opts:
            return f"\n**{q_label}**\n\n{m_opts.group(1)}"
        else:
            return f"\n**{q_label}** {rest}"
    return text


def convert_pdf_to_md(pdf_path, output_dir=None, extract_images=True):
    """Convert a single PDF file into a clean Markdown file."""
    pdf_dir = os.path.dirname(os.path.abspath(pdf_path))
    if output_dir is None:
        output_dir = os.path.join(pdf_dir, "md")

    os.makedirs(output_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(pdf_path))[0]
    md_path = os.path.join(output_dir, f"{stem}.md")
    doc = pymupdf.open(pdf_path)

    if output_dir:
        base_dir = os.path.dirname(os.path.abspath(output_dir))
    elif os.path.basename(pdf_dir) == "pdf":
        base_dir = os.path.dirname(pdf_dir)
    else:
        base_dir = pdf_dir

    img_dir_abs = os.path.join(base_dir, "images", stem)
    if extract_images:
        os.makedirs(img_dir_abs, exist_ok=True)

    answer_mode = False
    doc_lines = []

    for p_no in range(len(doc)):
        page = doc[p_no]

        raw_tables = page.find_tables().tables
        table_rects = []
        page_tables = []

        for t in raw_tables:
            extracted = t.extract()
            if is_dict_table(extracted):
                table_rects.append(t.bbox)
                page_tables.append((t.bbox[1], 'dict', format_dict_table(extracted)))
            elif is_answer_table(extracted):
                table_rects.append(t.bbox)
                page_tables.append((t.bbox[1], 'table', format_markdown_table(extracted)))
            elif is_layout_table(extracted):
                table_rects.append(t.bbox)
            else:
                table_rects.append(t.bbox)
                page_tables.append((t.bbox[1], 'table', format_markdown_table(extracted)))

        elements = []

        # Question illustration images
        if extract_images:
            for img in page.get_images():
                xref = img[0]
                bimg = doc.extract_image(xref)
                w, h = bimg['width'], bimg['height']
                # Skip full page backgrounds and tiny logos
                if 40 <= w <= 1200 and 40 <= h <= 1200 and not (w == 1653 and h == 2338):
                    rects = page.get_image_rects(xref)
                    if rects:
                        ext = bimg['ext']
                        img_name = f"page_{p_no+1}_img_{xref}.{ext}"
                        img_file = os.path.join(img_dir_abs, img_name)
                        with open(img_file, 'wb') as f:
                            f.write(bimg['image'])
                        img_rel = os.path.relpath(img_file, output_dir).replace('\\', '/')
                        elements.append((rects[0].y0, 'image', f"\n![Illustration]({img_rel})\n"))

        # Tables
        for y, t_type, t_content in page_tables:
            elements.append((y, t_type, f"\n{t_content}\n"))

        # Text blocks
        for b in page.get_text('blocks'):
            if b[6] != 0:
                continue
            x0, y0, x1, y1, text, bno, btype = b
            text = text.strip()
            if not text:
                continue

            # Skip layout artifacts
            if 'THÍ SINH KHÔNG ĐƯỢC VIẾT GÌ VÀO PHÁCH NÀY' in text:
                continue
            if text in ['ANSWERS', 'ANSWER']:
                continue
            if re.match(r'^(1[0-9]|2[0-9]|3[0-9]|4[0-9]|[1-9])\.\s*$', text):
                continue

            # Skip if inside layout table
            inside = False
            for tr in table_rects:
                if x0 >= tr[0] - 5 and y0 >= tr[1] - 5 and x1 <= tr[2] + 5 and y1 <= tr[3] + 5:
                    inside = True
                    break
            if inside:
                continue

            elements.append((y0, 'text', text))

        # Sort top-to-bottom
        elements.sort(key=lambda x: x[0])

        for y, etype, content in elements:
            if etype in ['image', 'table', 'dict']:
                doc_lines.append(content)
            elif etype == 'text':
                if any(kw in content.upper() for kw in ['HƯỚNG DẪN GIẢI', 'HƯỚNG DẪN CHẤM', 'ĐÁP ÁN CHI TIẾT', 'LỜI GIẢI CHI TIẾT']) and not answer_mode:
                    answer_mode = True
                    doc_lines.append("\n---\n")
                    doc_lines.append("## 📖 ĐÁP ÁN & HƯỚNG DẪN GIẢI CHI TIẾT\n")
                    doc_lines.append("<details>")
                    doc_lines.append("<summary><b>Click to reveal answers & explanations 🔍</b></summary>\n")

                lines = [l.strip() for l in content.split('\n') if l.strip()]
                joined = "\n".join(lines)

                if re.match(r'^(SỞ GIÁO DỤC|KỲ THI TUYỂN SINH|KÌ THI TUYỂN SINH|ĐỀ CHÍNH THỨC|MÔN THI|MÔN:)', joined, re.I):
                    doc_lines.append(f"**{joined}**\n")
                elif re.match(r'^(PHẦN|A\.|B\.|C\.|D\.|I\.|II\.|III\.|IV\.|V\.|VI\.|VII\.|Part \d+)\b', joined):
                    doc_lines.append(f"\n### {joined}\n")
                elif re.match(r'^(Mark the letter|Read the following|Choose the|Complete the|Circle|Write|Look at the)', joined, re.I):
                    doc_lines.append(f"\n*{joined}*\n")
                elif re.match(r'^(Question\s+\d+|Câu\s+\d+|\d+\.)', joined, re.I):
                    formatted_q = clean_question_text(joined)
                    doc_lines.append(f"\n{formatted_q}\n")
                elif re.match(r'^(Giải Question \d+|\d+\.\s*\([A-Z]+\))', joined):
                    doc_lines.append(f"\n#### {lines[0]}\n")
                    if len(lines) > 1:
                        doc_lines.append("\n".join(lines[1:]) + "\n")
                elif any(joined.startswith(pfx) for pfx in ['Kiến thức:', 'Giải thích:', 'Tạm dịch:', 'Thông tin:', 'Đáp án', 'Choose ']):
                    doc_lines.append(f"- **{joined}**\n")
                elif 'HẾT' in joined and len(joined) < 50:
                    doc_lines.append("\n\n---\n**------------------- HẾT -------------------**\n\n")
                else:
                    doc_lines.append(f"{joined}\n")

    if answer_mode:
        doc_lines.append("\n</details>\n")

    full_md = "\n".join(doc_lines)
    full_md = re.sub(r'\n{3,}', '\n\n', full_md)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(full_md)

    print(f"-> Converted: {os.path.basename(md_path)} ({len(doc)} pages, {len(full_md)} chars)")
    return md_path


def generate_readme_index(directory, md_dir=None):
    """Generate a summary README.md for the exams directory."""
    pdfs = sorted([f for f in os.listdir(directory) if f.lower().endswith('.pdf')])
    if not pdfs:
        return

    is_math = "math" in directory.lower() or "toan" in directory.lower()
    subject_title = "Toán (Math Entrance Exams)" if is_math else "Tiếng Anh (English Entrance Exams)"

    if os.path.basename(directory).lower() == "pdf":
        base_dir = os.path.dirname(directory)
        rel_pdf_dir = "pdf"
    else:
        base_dir = directory
        rel_pdf_dir = "."

    if md_dir is None:
        md_dir = os.path.join(base_dir, 'md')

    readme_path = os.path.join(base_dir, 'README.md')
    rel_md_dir = os.path.relpath(md_dir, base_dir).replace('\\', '/')

    lines = [
        f"# 📚 Bộ Đề Thi Tuyển Sinh Vào Lớp 10 Môn {subject_title}\n",
        f"Kho lưu trữ đề thi tuyển sinh vào lớp 10 THPT môn {subject_title.split(' (')[0]} chính thức & tham khảo, "
        "được số hóa và chuyển đổi định dạng chuẩn từ PDF sang Markdown để tiện học tập, ôn luyện và tra cứu.\n",
        "---",
        "## 📋 Danh Mục Đề Thi\n",
        "| STT | File Đề Thi (Markdown) | File Gốc (PDF) | Số Trang |",
        "| :---: | :--- | :--- | :---: |"
    ]

    for idx, pdf in enumerate(pdfs, 1):
        stem = os.path.splitext(pdf)[0]
        md_file = f"{stem}.md"
        md_link = f"{rel_md_dir}/{md_file}" if rel_md_dir != "." else md_file
        pdf_link = f"{rel_pdf_dir}/{pdf}" if rel_pdf_dir != "." else pdf
        pdf_path = os.path.join(directory, pdf)
        try:
            doc = pymupdf.open(pdf_path)
            page_count = len(doc)
        except Exception:
            page_count = "?"
        lines.append(f"| **{idx:02d}** | [{md_file}]({md_link}) | [{pdf}]({pdf_link}) | {page_count} |")

    lines.append("\n---\n")
    lines.append("## 💡 Hướng Dẫn Sử Dụng")
    lines.append("- Mỗi đề thi đều đã được tách câu hỏi, phương án trắc nghiệm rõ ràng.")
    lines.append("- Các hình ảnh biển báo, poster được nhúng trực tiếp ngay tại câu hỏi.")
    lines.append("- Đáp án và lời giải chi tiết được ẩn trong thẻ `<details><summary>` để học sinh tự làm bài trước khi tra cứu.")

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"-> Generated summary README: {readme_path}")


def main():
    sys.stdout.reconfigure(encoding='utf-8')

    parser = argparse.ArgumentParser(
        description="Convert graduation/entrance exam PDFs to structured Markdown."
    )
    default_exam_dir = "english/exams" if os.path.exists("english/exams") else "graduation exam"
    parser.add_argument(
        "path",
        nargs="?",
        default=default_exam_dir,
        help=f"Path to a PDF file or a directory containing PDF files (default: '{default_exam_dir}')."
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        default=None,
        help="Directory to save generated Markdown files (default: 'md/' inside target directory)."
    )
    parser.add_argument(
        "--no-images",
        action="store_true",
        help="Disable extracting question illustration images."
    )
    parser.add_argument(
        "--update-readme",
        action="store_true",
        help="Update or generate the README.md index table in the target directory."
    )

    args = parser.parse_args()
    target = os.path.abspath(args.path)

    if not os.path.exists(target):
        print(f"Error: Path not found: {target}")
        sys.exit(1)

    if os.path.isfile(target):
        if not target.lower().endswith('.pdf'):
            print(f"Error: File is not a PDF: {target}")
            sys.exit(1)
        convert_pdf_to_md(target, output_dir=args.output_dir, extract_images=not args.no_images)
    elif os.path.isdir(target):
        pdf_files = sorted([f for f in os.listdir(target) if f.lower().endswith('.pdf')])
        if not pdf_files:
            print(f"No PDF files found in {target}")
            sys.exit(0)
        if args.output_dir:
            output_dir = os.path.abspath(args.output_dir)
        elif os.path.basename(target).lower() == "pdf":
            output_dir = os.path.join(os.path.dirname(target), "md")
        else:
            output_dir = os.path.join(target, "md")
        os.makedirs(output_dir, exist_ok=True)
        print(f"Found {len(pdf_files)} PDF file(s) in {target}. Converting to {output_dir}...")
        for pdf in pdf_files:
            pdf_path = os.path.join(target, pdf)
            convert_pdf_to_md(pdf_path, output_dir=output_dir, extract_images=not args.no_images)
        if args.update_readme:
            generate_readme_index(target, md_dir=output_dir)
        print("Done!")


if __name__ == "__main__":
    main()

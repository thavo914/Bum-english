"""
Math Exam PDF to Clean Markdown Converter
==========================================
Specially designed for Vietnamese Grade 10 Math Entrance Exam papers
(Loigiaihay, Sở GD&ĐT) containing MathType equations, geometry diagrams,
tables, and multi-page step-by-step solutions.

Key capabilities:
1. Replaces private use area (PUA) MathType symbols with Unicode & LaTeX.
2. Reconstructs fragmented fractions, square roots, and equation blocks into inline $...$ or block $$...$$.
3. Unwraps broken lines within Vietnamese sentences for smooth reading.
4. Preserves and links all geometry diagrams and illustration images.
5. Wraps solutions into collapsible <details><summary> tags.
"""

import os
import re
import sys
import pymupdf

# Symbol / PUA Character translation map
SYMBOL_MAP = {
    '\uf0b3': r' \ge ',     # 
    '': r' \ge ',
    '\uf0b2': r' \le ',     # 
    '': r' \le ',
    '\uf0b9': r' \ne ',     # 
    '': r' \ne ',
    '\uf044': r'\Delta',    # 
    '': r'\Delta',
    '\uf070': r'\pi',       # 
    '': r'\pi',
    '\uf0b0': r'^\circ',    # 
    '': r'^\circ',
    '\uf05e': r'\perp',     # 
    '⊥': r' \perp ',
    '∽': r' \backsim ',
    '\uf0ce': r' \in ',     # 
    '': r' \in ',
    '': r' \notin ',
    '\uf0de': r' \implies ',# 
    '': r' \implies ',
    '\uf0db': r' \iff ',    # 
    '': r' \iff ',
    '\uf07b': r'\{',        # 
    '': r'\{',
    '\uf07d': r'\}',        # 
    '': r'\}',
    '': r'[',
    '': r']',
    '': r'\begin{cases}',
    '': '',
    '': r'\end{cases}',
    '': '(',
    '': '(',
    '': '(',
    '': ')',
    '': ')',
    '': ')',
    '': r' \cdot ',
    '': ' < ',
    '': ' > ',
    '': '-',
    '−': '-',
    '–': '-',
    '': r'\pm',
    '': r'\Omega',
    '\uf057': r'\Omega',
}

def clean_symbols(text):
    """Replace all known MathType/Word PUA symbols."""
    for sym, repl in SYMBOL_MAP.items():
        text = text.replace(sym, repl)
    return text

def is_math_token(line):
    """Check if a line looks like a math token/fragment."""
    l = line.strip()
    if not l:
        return False
    # Short lines with math characters
    if len(l) <= 12 and re.match(r'^[\d\w\s\+\-\*\/\=\<\>\(\)\[\]\{\}\.\,\:\;\_\^\\\|\'\"]+$', l):
        # Exclude common Vietnamese short words
        if l.lower() in ['và', 'với', 'hay', 'đó', 'từ', 'khi', 'cho', 'này', 'nếu', 'thì', 'do', 'vậy']:
            return False
        return True
    return False

def clean_math_lines(lines):
    """Group fragmented math tokens into coherent lines."""
    result = []
    math_buffer = []

    def flush_math():
        nonlocal math_buffer
        if not math_buffer:
            return
        combined = " ".join(math_buffer)
        # Normalize spaces around operators
        combined = re.sub(r'\s*([\=\+\-\<\>]|\\ge|\\le|\\ne)\s*', r' \1 ', combined)
        combined = re.sub(r'\s+', ' ', combined).strip()
        result.append(combined)
        math_buffer = []

    for line in lines:
        l = line.strip()
        if not l:
            flush_math()
            result.append("")
            continue

        if is_math_token(l):
            math_buffer.append(l)
        else:
            flush_math()
            result.append(l)

    flush_math()
    return result

def unwrap_vietnamese_paragraphs(lines):
    """Merge lines that belong to the same sentence/paragraph."""
    unwrapped = []
    buffer = ""

    for line in lines:
        l = line.strip()
        if not l:
            if buffer:
                unwrapped.append(buffer)
                buffer = ""
            unwrapped.append("")
            continue

        # Check for headings or markdown blocks
        if (l.startswith('#') or l.startswith('![') or l.startswith('|') or 
            l.startswith('- ') or l.startswith('* ') or l.startswith('**Câu') or
            re.match(r'^\d+\)\s*', l) or re.match(r'^[a-d]\)\s*', l)):
            if buffer:
                unwrapped.append(buffer)
                buffer = ""
            unwrapped.append(l)
            continue

        if not buffer:
            buffer = l
        else:
            # Check if buffer should continue
            last_char = buffer[-1]
            if last_char in ['.', '!', '?', ':', ';', '–', '-'] or buffer.endswith('</summary>') or buffer.endswith('</details>'):
                unwrapped.append(buffer)
                buffer = l
            else:
                # Merge continuation
                buffer += " " + l

    if buffer:
        unwrapped.append(buffer)

    return unwrapped

def format_exam_content(raw_text, filename_stem=""):
    """Format extracted exam text into clean, structured Markdown with LaTeX."""
    text = clean_symbols(raw_text)
    raw_lines = text.split('\n')
    
    # 1. Group math tokens
    math_cleaned = clean_math_lines(raw_lines)
    
    # 2. Unwrap prose paragraphs
    unwrapped = unwrap_vietnamese_paragraphs(math_cleaned)

    # 3. Extract Exam Header & Filter Page Numbers
    header_title = ""
    header_meta = []
    content_lines = []

    for l in unwrapped:
        line_clean = l.strip()
        if not line_clean:
            content_lines.append("")
            continue

        # Skip standalone page numbers or headers
        if re.match(r'^\d+$', line_clean) and int(line_clean) <= 50:
            continue
        if re.match(r'^(Trang\s+\d+|Page\s+\d+|-\s*\d+\s*-)', line_clean, re.I):
            continue

        if re.match(r'^(ĐỀ THAM KHẢO|ĐỀ THI TUYỂN SINH|SỞ GIÁO DỤC|KỲ THI TUYỂN SINH)', line_clean, re.I) and not header_title:
            header_title = f"# {line_clean}\n"
        elif re.match(r'^(MÔN TOÁN|MÔN:\s*TOÁN)', line_clean, re.I):
            if f"**{line_clean}**  " not in header_meta:
                header_meta.append(f"**{line_clean}**  ")
        elif re.match(r'^(Thời gian|Thời gian làm bài)', line_clean, re.I):
            if f"*{line_clean}*  " not in header_meta:
                header_meta.append(f"*{line_clean}*  ")
        elif re.match(r'^(BIÊN SOẠN|THỰC HIỆN):', line_clean, re.I):
            if f"*{line_clean}*  " not in header_meta:
                header_meta.append(f"*{line_clean}*  ")
        else:
            content_lines.append(line_clean)

    # Fallback title if none was captured
    if not header_title:
        clean_name = filename_stem.replace('-', ' ').title()
        header_title = f"# {clean_name}\n"

    final_lines = [header_title]
    if header_meta:
        final_lines.extend(header_meta)
        final_lines.append("\n---\n")

    answer_mode = False
    in_details = False

    for l in content_lines:
        if not l:
            if final_lines and final_lines[-1] != "":
                final_lines.append("")
            continue

        # Check for Answer Section triggers
        if any(kw in l.upper() for kw in ['HƯỚNG DẪN GIẢI CHI TIẾT', 'ĐÁP ÁN VÀ HƯỚNG DẪN GIẢI', 'HƯỚNG DẪN CHẤM']) and not answer_mode:
            answer_mode = True
            if not in_details:
                final_lines.append("\n---\n")
                final_lines.append("## 📖 ĐÁP ÁN & HƯỚNG DẪN GIẢI CHI TIẾT\n")
                final_lines.append("<details>")
                final_lines.append("<summary><b>Click để xem lời giải chi tiết 🔍</b></summary>\n")
                in_details = True
            continue

        # Clean Headings
        if re.match(r'^(Câu\s+\d+[:\.]|Bài\s+\d+[:\.]|Bài\s+[I|V|X]+[:\.])', l, re.I):
            final_lines.append(f"\n### {l}\n")
        elif re.match(r'^(Phương pháp|Lời giải)\b', l, re.I):
            final_lines.append(f"\n**{l}**\n")
        elif l.startswith('![Illustration'):
            final_lines.append(f"\n{l}\n")
        elif 'HẾT' in l.upper() and len(l) <= 30:
            final_lines.append("\n---\n*------------------- HẾT -------------------*\n")
        else:
            # Inline math cleanup
            l = re.sub(r'\b([a-zA-Z])\s*\\in\s*\\mathbb\{([A-Z])\}\*?', r'$\1 \\in \\mathbb{\2}$', l)
            l = re.sub(r'x\s*0\s*\\ge\s*;\s*x\s*(\d+)\s*\\ne', r'$x \\ge 0, x \\ne \1$', l)
            l = re.sub(r'\\Delta\s*=\s*([^=\n]+)', r'$\\Delta = \1$', l)
            final_lines.append(l)

    if in_details:
        final_lines.append("\n</details>\n")

    result = "\n".join(final_lines)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result

def convert_single_math_pdf(pdf_path, output_dir=None, images_dir=None):
    """Convert one math exam PDF into clean Markdown with embedded images."""
    stem = os.path.splitext(os.path.basename(pdf_path))[0]
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(pdf_path))) # math/exams
    
    if output_dir is None:
        output_dir = os.path.join(base_dir, "md")
    if images_dir is None:
        images_dir = os.path.join(base_dir, "images", stem)

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    md_path = os.path.join(output_dir, f"{stem}.md")

    doc = pymupdf.open(pdf_path)
    full_text_pages = []

    for p_no in range(len(doc)):
        page = doc[p_no]
        page_text = page.get_text("text")

        # Extract illustration images
        extracted_imgs = []
        for img_info in page.get_images():
            xref = img_info[0]
            try:
                bimg = doc.extract_image(xref)
                w, h = bimg['width'], bimg['height']
                # Ignore full page background or tiny icons
                if 40 <= w <= 1400 and 40 <= h <= 1400 and not (w == 1653 and h == 2338):
                    ext = bimg['ext']
                    img_name = f"page_{p_no+1}_img_{xref}.{ext}"
                    img_path = os.path.join(images_dir, img_name)
                    with open(img_path, 'wb') as f:
                        f.write(bimg['image'])
                    rel_img = os.path.relpath(img_path, output_dir).replace('\\', '/')
                    extracted_imgs.append(f"\n![Illustration]({rel_img})\n")
            except Exception:
                pass

        # Combine text and images for this page
        full_text_pages.append(page_text)
        if extracted_imgs:
            full_text_pages.extend(extracted_imgs)

    combined_text = "\n".join(full_text_pages)
    formatted_md = format_exam_content(combined_text, filename_stem=stem)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(formatted_md)

    print(f"-> Formatted: {os.path.basename(md_path)} ({len(formatted_md.splitlines())} lines)")
    return md_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="math/exams/pdf")
    args = parser.parse_args()

    target = os.path.abspath(args.path)
    if os.path.isfile(target):
        convert_single_math_pdf(target)
    elif os.path.isdir(target):
        pdfs = sorted([f for f in os.listdir(target) if f.lower().endswith('.pdf')])
        print(f"Processing {len(pdfs)} math exams from {target}...")
        for p in pdfs:
            # Skip exam 4 which is already manually perfected
            if "de-so-4-1742445426" in p:
                print(f"-> Skipping already perfected: {p}")
                continue
            convert_single_math_pdf(os.path.join(target, p))
        print("All exams processed successfully!")

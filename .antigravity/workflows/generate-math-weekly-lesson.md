---
description: Generates a complete weekly Math module (01-kien-thuc-va-phuong-phap.md and 02-bai-tap-thuc-chien.md) for Bum (14 years old), ordered from easy to hard (Level 1 to Level 4/5) with step-by-step algorithms and real exam questions.
---

# Workflow: /generate-math-weekly-lesson

Use this workflow to generate the 2 core weekly math learning and practice files for any designated week in `math/lessons/week-<N>-<topic>/`. Môn Toán không phân chia theo ngày mà tổ chức theo tuần hoàn chỉnh và **bài tập được sắp xếp theo thứ tự từ dễ lên khó**.

---

## 🎯 Target Persona & Level Constraints

- **Audience**: **Bum**, a 14-year-old student (Grade 8 / 9, Secondary School / THCS) preparing for the Grade 10 Entrance Exam.
- **Tiến trình độ khó**: Bắt buộc tuân theo thứ tự **Từ Dễ Lên Khó**:
  - **Level 1 (Nhận biết)**: Nhớ công thức, ĐKXĐ, tính nhẩm, phản xạ nhanh (5.0 – 6.0đ).
  - **Level 2 (Thông hiểu)**: Rút gọn biểu thức cơ bản, biến đổi căn số, giải phương trình/hệ phương trình căn bản (6.5 – 7.5đ).
  - **Level 3 (Vận dụng đề thi thật)**: Giải trọn vẹn câu hỏi trích từ 21 đề thi tuyển sinh vào lớp 10 Hà Nội & TP.HCM (7.5 – 8.5đ).
  - **Level 4 (Vận dụng cao)**: Câu hỏi phụ phân loại học sinh khá giỏi, tìm $x$ nguyên, cực trị BĐT Cauchy (8.5 – 9.25đ).
  - **Level 5 (Điểm 10)**: Bất đẳng thức nâng cao, cực trị hình học (dành cho các tuần nâng cao).
- **Tone**: Trực quan, khích lệ, dùng thuật toán 4 bước không nhảy cóc, kết hợp ngôn ngữ chiến thuật game (Level up, Boss fight, Khiên chống bẫy).
- **Thời lượng**: Học sinh tự chủ phân bổ làm trong tuần (khoảng 3 – 4 buổi, mỗi buổi 35 – 45 phút).

---

## 📂 Target Directory & 2-File Architecture

Mỗi tuần chỉ gồm đúng 2 file tài liệu:
```
math/lessons/week-<N>-<topic>/
├── 01-kien-thuc-va-phuong-phap.md  # Toàn bộ lý thuyết trọng tâm, công thức chuẩn, thuật toán 4 bước & bẫy thi
└── 02-bai-tap-thuc-chien.md        # Tuyển tập bài tập sắp xếp TỪ DỄ LÊN KHÓ (Level 1 -> 4) kèm đáp án
```

---

## 📝 File 1: `01-kien-thuc-va-phuong-phap.md` Template

```markdown
# ⚡ Tuần <N>: <Tên Chuyên Đề Bắt Tai Kèm Icon>
### Chuyên Đề Nền Tảng Tuyển Sinh Vào Lớp 10 – Dành Cho Bum (14 Tuổi)

> 🎯 **Mục tiêu chuyên đề tuần này**: <1 câu nêu rõ kỹ năng đạt được: ví dụ "Làm chủ toàn bộ kỹ thuật rút gọn căn thức và triệt tiêu bẫy quên ĐKXĐ">

---

## 1. Bản Chất Kiến Thức Cốt Lõi (Core Theory) 💡
Giải thích ngắn gọn các định nghĩa, định lý trọng tâm bằng ngôn ngữ dễ hiểu.
$$
<Công thức chuẩn LaTeX>
$$

## 2. Hằng Đẳng Thức & Quy Tắc Tính Nhanh ⚔️
Các công thức biến đổi cơ bản và quy tắc ghi nhớ.

## 3. Thuật Toán Chuẩn 4 Bước Trình Bày Lấy Điểm Tuyệt Đối 📋
Quy trình giải bài của giám khảo chấm thi:
- **Bước 1 (Soi ĐKXĐ)**: ...
- **Bước 2 (Quy đồng / Biến đổi)**: ...
- **Bước 3 (Thu gọn)**: ...
- **Bước 4 (Đối chiếu ĐKXĐ & Kết luận)**: ...

## 4. Bẫy Tử Thần Đề Thi Cần Né (Watch Out Traps!) ⚠️
- 🚨 **TRAP-XX**: <Mô tả bẫy thi hay gặp trong MISTAKE_LOG.md>  
  *Cách khắc phục*: <Quy tắc nhớ nhanh>
```

---

## 📝 File 2: `02-bai-tap-thuc-chien.md` Template (Xếp Từ Dễ Lên Khó)

```markdown
# ⚔️ Tuần <N>: Bộ Bài Tập Thực Chiến <Tên Chuyên Đề>
### Tuyển Tập Bài Tập Phân Hóa Từ Dễ Lên Khó (Level 1 $\rightarrow$ Level 4) – Dành Cho Bum (14 Tuổi)

---

## 🟢 PHẦN 1: CẤP ĐỘ 1 (LEVEL 1) – KHỞI ĐỘNG NHẬN BIẾT (5.0 – 6.0 ĐIỂM)
*(Mục tiêu: Thuộc công thức, tính toán nhẩm chuẩn xác, không bao giờ mất điểm câu dễ)*
- Bài 1.1: Trắc nghiệm phản xạ nhanh (10 giây/câu).
- Bài 1.2: Bài tập cơ bản thay số tính toán trực tiếp.

---

## 🟡 PHẦN 2: CẤP ĐỘ 2 (LEVEL 2) – THÔNG HIỂU & BIẾN ĐỔI CHUẨN (6.5 – 7.5 ĐIỂM)
*(Mục tiêu: Nắm vững thuật toán giải cơ bản, biến đổi thành thạo)*
- Bài 2.1: ...
- Bài 2.2: ...

---

## 🟠 PHẦN 3: CẤP ĐỘ 3 (LEVEL 3) – VẬN DỤNG ĐỀ THI VÀO 10 (7.5 – 8.5 ĐIỂM)
*(Mục tiêu: Giải trọn vẹn câu hỏi trích từ đề thi chính thức Hà Nội/TP.HCM)*
> 📌 **Nguồn**: Trích từ ngân hàng đề thi `math-question-registry.json`
- Bài 3.1: ...
- Bài 3.2: ...

---

## 🔴 PHẦN 4: CẤP ĐỘ 4 (LEVEL 4) – VẬN DỤNG CAO PHÂN HÓA (8.5 – 9.25 ĐIỂM)
*(Mục tiêu: Chinh phục câu hỏi phụ phân loại học sinh khá giỏi)*
- Bài 4.1: ...
- Bài 4.2: ...

---

## 🕵️ PHẦN 5: GÓC THỢ SĂN BẪY (TRAP BUSTER)
*(Soi lỗi sai trong bài làm mẫu giả định của bạn học sinh để rèn phản xạ chống mất điểm oan)*
- Tình huống lỗi: ...
- Nhiệm vụ của Bum: Chỉ ra lỗi sai và trình bày lại lời giải chuẩn.

---

## 🔑 ĐÁP ÁN CHI TIẾT & BAREM CHẤM ĐIỂM (ANSWER KEY)
<details>
<summary>👉 Nhấn vào đây để xem đáp án chi tiết từng bước và tự chấm điểm</summary>

*(Cung cấp lời giải đầy đủ, chi tiết từng dòng với barem 0.25đ / bước)*

</details>

---

## ⭐ BẢNG ĐÁNH GIÁ KẾT QUẢ TUẦN (3-STAR SCORECARD)
- ⭐ ⭐ ⭐: **Bậc Thầy (Xuất Sắc)** – Hoàn thành trọn vẹn Level 1, 2, 3, 4.
- ⭐ ⭐: **Chiến Binh (Rất Tốt)** – Hoàn thành tốt Level 1, 2, 3.
- ⭐: **Đang Rèn Luyện (Cố Lên)** – Mới làm xong Level 1 & 2.
```

---

## 📋 Quality Assurance Checklist

- [ ] Bài tập bắt buộc sắp xếp theo đúng thứ tự **TỪ DỄ LÊN KHÓ** (Level 1 $\rightarrow$ Level 4).
- [ ] Mọi công thức Toán sử dụng MathJax chuẩn (`$ ... $` và `$$ ... $$`).
- [ ] Phần 3 sử dụng ít nhất 1 bài trích từ `math-question-registry.json`.
- [ ] Có đầy đủ phần Thợ Săn Bẫy (Trap Buster) và Đáp án chi tiết trong `<details><summary>`.

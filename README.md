# 🚀 Bum Study Hub (Tiếng Anh & Toán Lớp 9 Ôn Thi Vào 10)

Chào mừng đến với **Bum Study Hub**!  
Kho học liệu thông minh được xây dựng riêng cho **Bum (14 tuổi)** nhằm trang bị kiến thức vững chắc và kỹ năng làm bài tự tin trước kỳ thi **Tuyển sinh vào lớp 10 THPT** với hai bộ môn trọng tâm: **Tiếng Anh** và **Toán Học**.

---

## 📂 Cấu Trúc Thư Mục Repository (Multi-Subject Architecture)

```
nephew-study/
├── english/                         # 🇬🇧 MÔN TIẾNG ANH (CEFR A1–A2)
│   ├── lessons/                     # Bài học hàng ngày (Hệ thống 2-file: Knowledge + Exercises)
│   │   ├── week-01-myself-tech-gaming/
│   │   ├── week-02-school-life-friends/
│   │   └── week-03-past-adventures-stories/
│   ├── exams/                       # Bộ đề thi vào 10 môn Tiếng Anh (PDF + Markdown + Ngân hàng câu hỏi)
│   ├── assessments/                 # Bài kiểm tra đánh giá & Sổ tay lỗi sai (MISTAKE_LOG.md)
│   └── flashcards/                  # Bộ flashcards từ vựng
│
├── math/                            # 📐 MÔN TOÁN HỌC (LỚP 9 & ÔN THI VÀO 10)
│   ├── topics/                      # 8 Chuyên đề kiến thức trọng tâm (Căn thức, Đồ thị, Hệ PT, Vi-ét, Hình 9...)
│   ├── lessons/                     # Lộ trình luyện tập Tuần/Ngày (2-File Daily Practice)
│   │   └── week-01-can-thuc-dai-so/
│   ├── exams/                       # Bộ đề thi vào 10 môn Toán (Hà Nội, TP.HCM, Cần Thơ,...)
│   ├── assessments/                 # Sổ tay bẫy tử thần (MISTAKE_LOG.md) & Bài test định kỳ
│   └── cheatsheets/                 # Sổ tay công thức 1 trang (Đại số 9 & Hình học 9)
│
├── public/                          # Web Dashboard giao diện đa môn tương tác cao
├── scripts/                         # Bộ công cụ số hóa OCR PDF, phân loại câu hỏi & tra cứu đề thi
├── server.js                        # Node.js backend phục vụ Web Dashboard & AI Voice Buddy Leo
├── Dockerfile & docker-compose.yml  # Đóng gói và chạy môi trường tự động
└── AGENTS.md                        # Quy chuẩn sư phạm & hướng dẫn dành cho AI Pair Programmer
```

---

## 🚀 Chạy Dashboard Trực Quan Trên Trình Duyệt

### Cách 1: Chạy Bằng Docker (Khuyên Dùng)
```bash
docker compose up -d --build
```
Truy cập trình duyệt: **[http://localhost:3001](http://localhost:3001)**

### Cách 2: Chạy Trực Tiếp Bằng Node.js
```bash
npm install
npm run dev
```
Truy cập trình duyệt: **[http://localhost:3000](http://localhost:3000)**

---

## 🎙️ Luyện Nói Tiếng Anh Cùng AI Buddy "Leo"
Mỗi ngày trong phần Tiếng Anh đều có **AI Voice Mission**. Bum có thể mở chế độ ChatGPT Voice hoặc nhấn kết nối AI Buddy Leo trên Web Dashboard để luyện phản xạ nói tiếng Anh ngắn gọn và tự nhiên.

---

## 📝 Công Cụ Tra Cứu Đề Thi Tuyển Sinh Vào 10
Tra cứu 390+ câu hỏi đề thi vào 10 chính thức đã được phân loại:
```bash
# Thống kê phân bố câu hỏi
py scripts/query_registry.py --stats

# Lọc câu hỏi ngữ pháp trình độ A2
py scripts/query_registry.py --category grammar --level A2 --limit 5

# Tạo bài tập trắc nghiệm ngẫu nhiên cho Bum
py scripts/query_registry.py --category grammar --level A2 --random --limit 10 --export-quiz "english/assessments/bum-quiz.md"
```

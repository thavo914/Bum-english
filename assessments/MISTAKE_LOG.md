# 🎯 Sổ Theo Dõi Lỗi Sai & Tiến Trình Làm Chủ Dạng Bài (Bum's Mistake Ledger)

> **Mục tiêu**: Theo dõi từng lỗi sai từ các bài kiểm tra tuần (`assessments/test-week-<N>.md`) và bài test đầu vào (`test bum.md`).  
> **Nguyên tắc Spaced Repetition**: 
> - 🔴 **Active (Cần khắc phục)**: Lỗi mới mắc ở bài test gần nhất -> Đưa vào Rematch Challenge trong tuần kế tiếp.
> - 🟡 **In-Review (Đang củng cố)**: Bum đã làm đúng ở bài tập ngày, cần kiểm tra lại lần cuối trong bài Boss Battle / Test tuần.
> - 🟢 **Mastered (Đã làm chủ dạng bài)**: Đã làm đúng trong Test tuần -> **Dừng lặp lại**, không đưa vào bài tập nữa để tránh nhàm chán.

---

## 📊 Bảng Theo Dõi Chi Tiết Theo Tuần

| Mã lỗi | Bài Test phát hiện | Bẫy ngữ pháp / Dạng câu hỏi | Lỗi Bum đã chọn | Trạng thái | Tuần khắc phục | Ghi chú & Đánh giá |
| :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **ERR-01** | Test đầu vào (Câu 1) | **Chủ ngữ kép & Hòa hợp S-V** | Chọn *am* trong *"My brother and I ______ fans"* | 🟢 **Mastered** | Week 2 (Day 1) | Đã làm chủ phản xạ: nhận diện 2 người -> dùng *are*. Không cần nhắc lại. |
| **ERR-02** | Test đầu vào (Câu 9) | **So sánh hơn của tính từ ngắn** | Chọn *fastest* thay vì *faster* trong *"faster than"* | 🟢 **Mastered** | Week 2 (Day 2) | Đã nắm chắc dấu hiệu *than* đi với tính từ đuôi *-er*. |
| **ERR-03** | Test đầu vào (Câu 7) | **Lượng từ: Some vs Any** | Chọn *some* thay vì *any* trong câu hỏi đồ ăn vặt | 🟢 **Mastered** | Week 2 (Day 3) | Đã phân biệt chuẩn: *any* dùng trong câu phủ định và câu hỏi. |
| **ERR-04** | Test đầu vào (Câu 2, 3) | **Hiện tại đơn đuôi -s/-es vs Tiếp diễn** | Quên thêm *-es* (*finish*) và nhầm thì tiếp diễn (*plays*) | 🟢 **Mastered** | Week 2 (Day 4) | Đã nhận diện tốt dấu hiệu *right now* vs *usually*. |
| **ERR-05** | Test đầu vào (Câu 21) | **Phản xạ giao tiếp rủ rê / lập kèo** | Chọn câu trả lời cứng nhắc *"No, it is not my game"* | 🟢 **Mastered** | Week 2 (Day 5) | Đã tự nhiên dùng *"Count me in! / Deal!"*. |
| **ERR-06** | Test đầu vào (Câu 5) | **Thì Quá khứ đơn (Động từ bất quy tắc)** | Chọn *win* thay vì *won* sau *"Yesterday afternoon"* | 🔴 **Active** | **Week 3** | Cần ưu tiên số 1 cho Tuần 3 (Chủ đề Past Adventures). |
| **ERR-07** | Test đầu vào (Câu 6) | **Đại từ tân ngữ (Object Pronouns)** | Chọn *he/his* thay vì *him* đứng sau động từ *gave* | 🔴 **Active** | **Week 3** | Vị trí tân ngữ sau verb (*gave him, told her*). |
| **ERR-08** | Test đầu vào (Câu 8) | **Giới từ thời gian & nơi chốn (In/On/At)** | Nhầm lẫn giữa *at* (giờ) và *in* (phòng học/nơi chốn) | 🔴 **Active** | **Week 3** | Cần đưa vào Rematch Challenge câu hỏi thi thật. |
| **ERR-09** | Test đầu vào (Câu 4) | **Động từ khuyết thiếu (Can / Can't)** | Chọn nhầm *don't can* / *shouldn't to* | 🟡 **In-Review** | **Week 3** | Đã hiểu *can't + V*, cần thêm 1 câu củng cố trong tuần. |
| **ERR-10** | Test đầu vào (Câu 10) | **Tương lai gần (Be going to vs Will)** | Dự đoán có dấu hiệu trước mắt (*Be careful!*) | 🔵 **Scheduled** | **Week 6** | Theo kế hoạch giáo trình sẽ học sâu ở Tuần 6. |

---

## 🔄 Quy Trình Cập Nhật Sau Mỗi Tuần

1. **Cuối mỗi tuần (Sau bài Test tuần)**:
   - Thầy cô/phụ huynh chấm bài test tuần (ví dụ: `assessments/test-week-02.md`).
   - Lỗi nào Bum đã làm đúng -> Đổi trạng thái sang 🟢 **Mastered**.
   - Lỗi nào mới phát sinh trong bài test tuần -> Thêm dòng mới với mã `ERR-XX`, trạng thái 🔴 **Active**.
2. **Khi tạo giáo trình tuần mới (`/suggest-next-week-curriculum`)**:
   - AI chỉ đọc các lỗi 🔴 **Active** và 🟡 **In-Review**.
   - **Tuyệt đối bỏ qua các lỗi 🟢 Mastered** để không làm Bum chán.
   - Phân bổ 🔴 **Active** vào từng ngày học của tuần mới.

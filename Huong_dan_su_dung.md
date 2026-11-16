# Hướng Dẫn Sử Dụng Chương Trình Thi Thử & Ôn Thi Mendix Advanced

Chương trình ôn thi trắc nghiệm chứng chỉ **Mendix Advanced Certification** được thiết kế đặc biệt nhằm phục vụ nhu cầu ôn tập nhanh, nhớ lâu: **ngay sau mỗi câu chọn sẽ hiển thị đáp án đúng, phân tích đúng/sai và chú thích giải thích chi tiết**.

---

## 🚀 Cách Mở Chương Trình
1. **Cách 1 (Nhanh nhất)**: Nhấp đúp chuột vào file **`Chay_Chuong_Trinh_Thi_Thu.bat`**.
2. **Cách 2**: Nhấp đúp chuột trực tiếp vào file **`index.html`** để mở trên bất kỳ trình duyệt nào (Chrome, Edge, Cốc Cốc, Brave, Firefox...).
3. Ứng dụng chạy hoàn toàn **Offline (Cục bộ)**, không cần kết nối internet hay cài đặt thêm bất kỳ phần mềm nào.

---

## 🎯 Các Chế Độ Ôn Luyện

### 1. 🎓 Chế độ Ôn Tập Từng Câu (Mặc định)
- **Cơ chế**: Khi bạn bấm chọn một đáp án bất kỳ:
  - Hệ thống sẽ **ngay lập tức** hiển thị đáp án của bạn là Đúng (Xanh lá) hay Sai (Đỏ).
  - Tự động đánh dấu đáp án chính xác của câu hỏi.
  - Hiển thị ngay hộp **"💡 CHÚ THÍCH & GIẢI THÍCH CHI TIẾT"** giải thích vì sao đáp án đó đúng và phân tích các phương án khác.
  - **Khóa đáp án sau khi chọn**: Một khi bạn đã chọn đáp án, hệ thống sẽ **khóa hoàn toàn các lựa chọn** (không cho phép chọn lại hoặc sửa đáp án) nhằm đảm bảo tính nghiêm túc và phản ánh đúng thực lực.
- **Tính năng nổi bật**:
  - **Tự động lưu Log câu sai**: Mọi câu trả lời sai đều được tự động lưu vào **Sổ tay Log câu sai** để bạn ôn luyện lại.
  - **Tự động xóa khỏi Log khi ôn đúng**: Khi bạn ôn tập lại và trả lời chính xác, câu hỏi đó sẽ **tự động được loại bỏ khỏi Log câu sai**.
  - Tùy chọn **"Xáo trộn ngẫu nhiên thứ tự đáp án (A, B, C, D)"**: Đảo vị trí các phương án lựa chọn, giúp hiểu bản chất kiến thức và tránh việc học vẹt / nhớ máy móc theo chữ cái A, B, C, D. Lời giải và phím tắt sẽ tự động đồng bộ theo vị trí mới.
  - Tùy chọn **"Tự động chuyển câu khi đúng"**: Nếu trả lời đúng, sau 1.2s hệ thống tự động nhảy sang câu tiếp theo.

### 2. ⏱️ Chế độ Thi Thử Bấm Giờ (Exam Mode)
- **Cơ chế**: Mô phỏng phòng thi thật với đồng hồ đếm ngược **120 phút** (50 câu hỏi, chuẩn đỗ **≥ 75%** tức từ 38/50 câu).
- **Linh hoạt**: Có sẵn tùy chọn *"Hiện đáp án & chú thích ngay trong lúc thi"* để vừa bấm giờ vừa xem giải thích sau mỗi câu, hoặc tắt đi để nộp bài xong mới xem tổng kết.

### 3. 🎯 Cơ chế Tự Động Loại Bỏ Câu Đúng & Phục Hồi Khi Đạt 100% (Mới)
- **Cơ chế**: Khi bật tùy chọn **"Loại bỏ câu đã trả lời đúng khỏi đề thi"** (mặc định BẬT):
  - **Loại bỏ câu đã đúng**: Mỗi khi bạn trả lời chính xác một câu hỏi trong bộ đề (Đề 1, Đề 2, Đề 3, Trọn bộ 111 câu, các Chuyên đề), câu hỏi đó sẽ được ghi nhận là "đã làm chủ" và tự động ẩn đi ở các lượt làm bài tiếp theo.
  - **Tập trung vào phần chưa vững**: Khi bạn mở lại đề thi đó, hệ thống chỉ hiển thị các câu bạn chưa giải đúng, giúp bạn ôn luyện đúng trọng tâm mà không phải làm lại những câu đã quá quen thuộc.
  - **Theo dõi tiến độ trực quan**: Ngay trên từng nút chọn đề ở Trang chủ, hệ thống hiển thị số lượng câu còn lại và tỷ lệ % đã đúng (ví dụ: `Còn 18/50 câu · Đúng 64%`).
  - **Tự động khôi phục 100% khi hoàn thành**: Khi bạn đã giải đúng **100% toàn bộ câu hỏi** trong bộ đề, màn hình kết quả sẽ hiển thị biểu ngữ chúc mừng vinh danh, đồng thời hệ thống **tự động đưa toàn bộ câu hỏi quay trở lại đề thi** để bạn có thể bắt đầu một vòng luyện tập mới bất cứ lúc nào!
  - **Nút ↺ Reset linh hoạt**: Bạn có thể chủ động bấm nút **`↺ Reset`** ở góc trên mỗi thẻ đề thi hoặc nút **"↺ Đưa lại toàn bộ câu hỏi"** tại Màn hình kết quả bất cứ lúc nào nếu muốn khôi phục lại đề đầy đủ ngay lập tức.

### 4. ❌ Sổ Tay & Luyện Lại Các Câu Làm Sai (Wrong Bank)
- Hệ thống tự động ghi nhớ toàn bộ những câu hỏi bạn từng làm sai vào bộ nhớ máy (`localStorage`).
- **Nút xem Sổ tay Log câu sai**: Trên thanh menu trên cùng (Topbar) và ở mục 3 trên trang chủ, bạn có thể bấm **"📋 Xem chi tiết Log các câu sai"** để xem lại danh sách câu hỏi, đáp án đúng và lời giải chi tiết.
- **Tự động đào thải khi đã thuộc**: Mỗi khi bạn làm lại một câu trong đề hoặc ở bài luyện câu sai và chọn **ĐÚNG**, hệ thống sẽ lập tức **xóa câu đó khỏi Log** và giảm số lượng câu sai cần ôn.
- Bấm vào mục **"❌ Luyện Các Câu Sai"** ở trang chủ để mở bài luyện tập riêng cho các câu bạn chưa nắm vững.

### 5. ⭐ Câu Hỏi Đã Đánh Dấu (Bookmarks)
- Trên mỗi câu hỏi có nút **⭐ Đánh dấu câu này**.
- Bạn có thể lưu lại những câu hỏi bẫy, câu khó hoặc câu muốn xem lại nhiều lần.

---

## 📚 Ngân Hàng Câu Hỏi Phong Phú (Đã cập nhật thêm 4 bộ đề mới)
- **📑 3 Đề thi chuẩn gốc**: Đề 1, Đề 2, Đề 3 (mỗi đề 50 câu có đầy đủ đáp án & giải thích).
- **🔥 4 Bộ đề mới bổ sung (Folder New - 260 câu)**:
  1. 🎯 **Practice Test I**: 50 câu trắc nghiệm chuẩn Mendix Advanced Developer.
  2. ⚡ **Practice Questions Set 1**: 30 câu trắc nghiệm chuyên sâu.
  3. 🔀 **Practice Questions Set 2**: 30 câu trắc nghiệm xáo trộn kiểm tra phản xạ.
  4. 📚 **Learning Path Quiz Bank**: 150 câu hỏi toàn diện bao quát toàn bộ lộ trình Advanced.
- **👑 Đại Ngân Hàng 314 Câu Độc Nhất**: Tổng hợp toàn bộ 314 câu hỏi không trùng lặp (111 câu gốc + 203 câu mới).
- **🌟 Trọn bộ 111 câu độc nhất gốc**: Dành cho ôn tập nhanh bộ câu hỏi trọng tâm ban đầu.
- **Ôn luyện theo 5 Chuyên đề**:
  1. 🎨 **UX & Logging** (26 câu)
  2. ⚡ **Microflows & Logic** (25 câu)
  3. 🔍 **XPath & General** (24 câu)
  4. 🔒 **Security & Access Rules** (19 câu)
  5. 🗄️ **Domain Model & Performance** (17 câu)
- **Đề ngẫu nhiên 20 câu**: Tạo bài kiểm tra nhanh ngẫu nhiên rút từ toàn bộ 314 câu hỏi.

---

## ⌨️ Phím Tắt Tiện Lợi (Keyboard Shortcuts)
- **`A`, `B`, `C`, `D`, `E`, `F`** hoặc số **`1`, `2`, `3`, `4`, `5`, `6`**: Chọn nhanh đáp án.
- **`Mũi tên phải (→)`** hoặc phím **`N`**: Sang câu tiếp theo.
- **`Mũi tên trái (←)`** hoặc phím **`P`**: Quay về câu trước.
- **Phím `S`**: Đánh dấu sao (Bookmark) câu hỏi hiện tại.

---

## 🛠️ Tiện Ích Kèm Theo
- **🔄 Đồng bộ Online & Offline với Google Sheets (Mới)**:
  - Tích hợp 2 chiều với bảng tính [Đề mendix - Google Trang tính](https://docs.google.com/spreadsheets/d/1h-DtUIyo4JRCzHHXo_4ext1L5fUsMu5bMc56Td1LLzY/edit).
  - Có sẵn file Excel hoàn chỉnh **`De_Mendix_Advanced_314_Cau_Hoi.xlsx`** (gồm 8 tab: tab tổng hợp 314 câu + 7 đề riêng) để import trực tiếp lên Google Sheets.
  - Nút **`🔄 Đồng bộ`** trên thanh công cụ giúp nạp ngay các câu hỏi hoặc sửa đổi mới nhất từ Google Sheets về ứng dụng web.
  - **Hoạt động trơn tru cả khi Offline**: Khi mất mạng, ứng dụng tự động dùng dữ liệu đã cache hoặc dữ liệu gốc tích hợp sẵn.
- **🔍 Tra cứu câu hỏi nhanh**: Tìm kiếm theo từ khóa (XPath, rollback, index, reversed, inheritance...) trong toàn bộ 314 câu hỏi và lời giải.
- **🔊 Hiệu ứng âm thanh**: Âm thanh báo Đúng / Sai sinh động (có thể bật/tắt).
- **🌙 Chế độ Sáng / Tối (Dark Mode)**: Dễ chịu cho mắt khi ôn thi vào ban đêm.
- **📊 Bảng phân tích năng lực theo từng chuyên đề**: Sau khi nộp bài, hệ thống hiển thị % chính xác của từng phần (Microflows, Security, XPath...) giúp bạn biết chính xác phần kiến thức nào cần cải thiện.
- **📥 Xuất báo cáo CSV**: Tải lịch sử các lần thi về máy tính.

---

## 🌐 Hướng Dẫn Đưa Dữ Liệu Lên Google Sheets & Đồng Bộ

### 1. Đưa 314 câu hỏi lên Google Sheets (Chỉ mất 10 giây):
1. Mở file Google Sheets của bạn: [Đề mendix - Google Trang tính](https://docs.google.com/spreadsheets/d/1h-DtUIyo4JRCzHHXo_4ext1L5fUsMu5bMc56Td1LLzY/edit).
2. Vào menu **Tệp (File)** > **Nhập (Import)** > chọn tab **Tải lên (Upload)**.
3. Kéo thả file **`De_Mendix_Advanced_314_Cau_Hoi.xlsx`** (đã tạo sẵn trong thư mục dự án) vào khung tải lên.
4. Chọn vị trí nhập là: **Thay thế trang tính hiện tại (Replace spreadsheet)** > Nhấn **Nhập dữ liệu (Import data)**.
5. Toàn bộ 8 Sheet (Master 314 câu + 7 đề thi) sẽ hiển thị đầy đủ với định dạng chuẩn, cột rõ ràng và đáp án chi tiết.

### 2. Thiết lập quyền để ứng dụng đọc được dữ liệu:
- Trên Google Sheets, nhấn nút **Chia sẻ (Share)** ở góc trên bên phải.
- Tại mục *Quyền truy cập chung*, đổi từ "Bị hạn chế" sang **"Bất kỳ ai có đường liên kết đều có thể xem" (Anyone with the link can view)** > Nhấn **Xong**.

### 3. Đồng bộ với ứng dụng web:
- Trên giao diện web thi thử (dù đang mở cục bộ offline hay qua GitHub Pages), bấm nút **`🔄 Đồng bộ`** trên thanh Topbar.
- Nhấn **"🔄 Đồng bộ ngay từ Google Sheet"**.
- Hệ thống sẽ nạp dữ liệu mới nhất, lưu vào bộ nhớ máy và tự động áp dụng cho các đề thi.
- Khi không có mạng, bạn vẫn làm bài bình thường với dữ liệu offline!



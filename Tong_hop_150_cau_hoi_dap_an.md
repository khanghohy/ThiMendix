# Tổng Hợp Đề Thi Và Đáp Án - Mendix Advanced Certification

Tài liệu ôn tập tổng hợp 3 bộ đề thi thử Mendix Advanced (tổng cộng 150 câu hỏi trắc nghiệm kèm đáp án và giải thích chi tiết).

## Mục lục
- [Đề thi thử số 1 (50 câu)](#đề-thi-thử-số-1)
- [Đề thi thử số 2 (50 câu)](#đề-thi-thử-số-2)
- [Đề thi thử số 3 (50 câu)](#đề-thi-thử-số-3)

---

## Đề thi thử số 1

### Đề 1 - Câu 1 [UX & Logging]

**Câu hỏi:** What does the UI designer focus on?

- ✅ **A.** The presentation of the product
- ⚪ B. The user's goals and desires
- ⚪ C. How it feels to use the product
- ⚪ D. Mapping out the user's journey

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): UI designer tập trung vào phần trình bày: bố cục, màu sắc, typography, thành phần giao diện. Mục tiêu, cảm nhận và hành trình user thuộc về UX.

---

### Đề 1 - Câu 2 [Microflows]

**Câu hỏi:** What will happen when there is no error handling implemented and Mendix is not able to finish a microflow transaction successfully?

- ✅ **A.** The transaction is stopped and by default Mend will show this message in the user interface: ‘Something went wrong. Please contact your administrator'
- ⚪ B. The transaction will be finished and the user won't see a message in the user interface.
- ⚪ C. The transaction is stopped and Mendix will show a default error message in the user interface.
- ⚪ D. Nothing

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Không có error handling thì Mendix rollback transaction và client hiển thị thông báo mặc định kiểu 'An error occurred, please contact your system administrator'; chi tiết lỗi ghi vào log.

---

### Đề 1 - Câu 3 [Microflows]

**Câu hỏi:** Which of the following statements is true about the [reversed()] expression?

- ✅ **A.** It can only be applied on self-references.
- ⚪ B. It can only be applied on *-* associations.
- ⚪ C. It can only be applied on 1-1 associations.
- ⚪ D. It can be applied to reverse a string attribute.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Hàm reversed() dùng trong XPath trên association tự tham chiếu (self-reference) để đi theo chiều ngược lại của association, vì hai đầu cùng là một entity.

---

### Đề 1 - Câu 4 [UX & Logging]

**Câu hỏi:** Which of the following log messages follows the best practices for a Warning log message?

- ⚪ A. “Contacting REST service.”
- ✅ **B.** “User language has not been set yet.”
- ⚪ C. “Unknown user input '129q', unable to process value.”
- ⚪ D. “REST service has returned result: 404 Not Found.”

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Theo Mendix, Warning dùng khi có điều bất thường nhưng ứng dụng vẫn tiếp tục chạy được. 'User language has not been set yet.' là tình huống như vậy. 'Contacting REST service.' là Info/Debug; lỗi input không xử lý được hay REST trả 404 là Error.

---

### Đề 1 - Câu 5 [Security]

**Câu hỏi:** When attempting to change the value of an object on a page. what will happen if the runtime identifies that you are not allowed to do this?

- ⚪ A. The change will be saved to the database and then rolled-back.
- ⚪ B. The change will be saved in the memory.
- ✅ **C.** The change will not happen and an error message willbe shown in the client and the log.
- ⚪ D. This will never happen. If you can't access the object you won't see it on the page.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Runtime luôn kiểm tra quyền khi client gửi thay đổi. Nếu không có quyền write, thay đổi bị từ chối và lỗi được hiển thị ở client và ghi log.

---

### Đề 1 - Câu 6 [XPath & General]

**Câu hỏi:** Given this Domain Model, which of the following XPath s would you choose to retrieve the Orders of the currently logged-in customer?

- ⚪ A. [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account/Name = $currentUser/Name]
- ⚪ B. [AdvancedModule.Order_Customer='[%CurrentUser%]']
- ✅ **C.** [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account='[%CurrentUser%]']
- ⚪ D. [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account/Administration.Account/id = ‘[%CurrentUsers%]']

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Đi Order, qua Customer, tới Customer_Account rồi so sánh với '[%CurrentUser%]'. Đây là cách chuẩn và hiệu quả để lấy Order của customer đang đăng nhập.

---

### Đề 1 - Câu 7 [Security]

**Câu hỏi:** Which of the three buttons New, Edit, and Delete on the page Order Overview will be visible to the user if an entity access rule specifies that the user can create, delete, read and write Orders?

- ⚪ A. Just the Edit button
- ⚪ B. Just the New and Delete buttons
- ✅ **C.** New Edit and Delete buttons
- ⚪ D. No buttons will be visible

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Entity access cho phép create, delete, read và write Order thì cả ba nút New, Edit, Delete đều hiển thị, vì Mendix ẩn nút dựa trên quyền entity.

---

### Đề 1 - Câu 8 [UX & Logging]

**Câu hỏi:** If you add widgets to the widgets folder manually in the App Directory in Explorer, how can you make them appear in the Toolbox in Mendix Studio Pro?

- ⚪ A. Restart Mendix Studio Pro,
- ✅ **B.** Synchronize the App Directory.
- ⚪ C. Import the widget via the main menu of Mendix Studio Pro, otherwise it is not possible.
- ⚪ D. Nothing, the widget will be added automatically.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Thêm widget thủ công vào thư mục widgets thì dùng App > Synchronize App Directory (F4) để Studio Pro nạp lại và hiện widget trong Toolbox.

---

### Đề 1 - Câu 9 [Microflows]

**Câu hỏi:** When an order is submitted, the Order and OrderLines will be committed to the database. Afterwards , the Customer should receive an email with the order details. Asa result. the Mendix developer adds the sub-microflow SUB_Order_SendCustomerEmail to the submit microflow. The developer wants to catch a possible error when sending an email so that the Order and OrderLines will definitely be committed. What type of error handling should the developer set on the C all microflow activity which calls the microflow SUB_Order_SendCustomerEmail?

- ✅ **A.** Custom without rollback
- ⚪ B. Continue
- ⚪ C. Custom with Rollback
- ⚪ D. Rollback

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Order và OrderLine đã commit trước khi gửi email. Đặt 'Custom without rollback' trên lời gọi SUB_Order_SendCustomerEmail để khi gửi mail lỗi thì dữ liệu đã commit không bị rollback, đồng thời vẫn bắt được lỗi để log.

---

### Đề 1 - Câu 10 [XPath & General]

**Câu hỏi:** You would like to replace an XPath that utes the logical 'and' operator with a microfiow using. two Retrieves and a List operation. Which of the following List operations should you use?

- ⚪ A. Find
- ⚪ B. Subtract
- ✅ **C.** Intersert
- ⚪ D. Union

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Toán tử 'and' nghĩa là object phải thỏa cả hai điều kiện, tức là phần giao của hai list, nên dùng list operation Intersect.

---

### Đề 1 - Câu 11 [Domain Model]

**Câu hỏi:** What is important to keep in mind when using a self-reference association?

- ⚪ A. Cascading deletes can go both ways
- ⚪ B. The number of self-reference layers has to be limited
- ⚪ C. Only 1-1 associations are allowed
- ✅ **D.** Make sure to rename the association so that both ends can be distinguished

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Self-reference có hai đầu cùng trỏ về một entity, nên cần đặt tên association (và tên hai đầu) rõ ràng để phân biệt cha/con, ví dụ Employee_Manager.

---

### Đề 1 - Câu 12 [XPath & General]

**Câu hỏi:** You want to retrieve all trainees without certificates. Which XPath should you use for this?

- ✅ **A.** [ not(Training.Trainee_CertificateType/Trainee.CertificateType) ]
- ⚪ B. [Training.Trainee_CertificateType/Trainee.CertificateType != empty]
- ⚪ C. [not(Training.Trainee_CertificateType/Trainee.CertificateType != empty)]
- ⚪ D. [not(Training.Trainee_CertificateType/Trainee.CertificateType = empty)]

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): not(association/Entity) trả về object không có liên kết nào qua association, tức là trainee chưa có certificate.

---

### Đề 1 - Câu 13 [Domain Model]

**Câu hỏi:** What type of association has the biggest data payload?

- ⚪ A. A reference “both” association (1-1)
- ✅ **B.** A reference set (*-*)
- ⚪ C. A reference association (1-*)
- ⚪ D. An association with an information entity

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Reference set (*-*) có thể chứa rất nhiều tham chiếu trên mỗi object, nên khi lấy object kèm association thì dữ liệu tải về lớn nhất.

---

### Đề 1 - Câu 14 [Domain Model]

**Câu hỏi:** Where are file or image of mendix application stored by default

- ⚪ A. As binary in the content of an attribute
- ✅ **B.** On the file server located on the application server
- ⚪ C. On the dedicated Amazon file server
- ⚪ D. On the local hard disk of the user

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Mặc định file và ảnh (FileDocument, Image) không lưu trong database mà lưu trên file storage của application server; database chỉ giữ thông tin tham chiếu tới file.

---

### Đề 1 - Câu 15 [Microflows]

**Câu hỏi:** In a sub-microflow, you want to create a string based on a DateTime parameter. The format of the string should look like this: 'Monday 23 April 2021'. Which date manipulation should you use to accomplish this?

- ⚪ A. Create a Date Variable and format the date to a string by using this expression: formatDateTime($DateTime,' EEE ddd MMMM yyyy')
- ✅ **B.** Create a String Variable and format the date to a string by using this expression: formatDateTime($DateTime,’EEEE ddd MMMM yyyy’)
- ⚪ C. Create a String Variable and format the date to a string by using this expression: formatDateTime($DateTime,’EE DD MM YYYY)
- ⚪ D. Create a String Variable and parse the date to a string by using this expression: parseDateTime($DateTime. 'EEE ddd MMMM yyyy’)

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): formatDateTime chuyển DateTime thành String. Pattern EEEE cho tên thứ đầy đủ (Monday), d là ngày, MMMM là tên tháng đầy đủ (April), yyyy là năm. parseDateTime làm ngược lại (String sang DateTime).

---

### Đề 1 - Câu 16 [XPath & General]

**Câu hỏi:** You need to retrieve the UserRole Employee in a microflow. Which XPath constraint should you use in the Retrieve from Database activity?

- ✅ **A.** [id='[%UserRole_Employee%]']
- ⚪ B. [Name = 'Employee']
- ⚪ C. [ModelGUID= '[%UserRole_Employee%]']
- ⚪ D. [Description = 'Employee']

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Mỗi user role có token [%UserRole_<Tên>%] đại diện cho id của role đó, nên dùng [id='[%UserRole_Employee%]'] để lấy chính xác role, không phụ thuộc tên hay mô tả.

---

### Đề 1 - Câu 17 [Domain Model]

**Câu hỏi:** The Order entity has an attribute OrderDate of type Date and Time. A user in the time zone Amsterdam GMT+1 creates an Order and sets the date to April 16, 1991. Which DateTime value is stored in the database?

- ⚪ A. 1991-04-16 01:00:00
- ⚪ B. 1991-04-16 00:00:00
- ✅ **C.** 1991-04-15 23:00:00
- ⚪ D. 1991-04-15 12:00:00

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Thuộc tính DateTime localized được lưu theo UTC. 16/04/1991 00:00 giờ Amsterdam (GMT+1) tương ứng 15/04/1991 23:00 UTC.

---

### Đề 1 - Câu 18 [UX & Logging]

**Câu hỏi:** You want to show a text as Heading 2. However, on this particular page you want to remove the default spacing at the bottom. What is the most efficient way to do this?

- ⚪ A. Add CSS to the style property of the text widget.
- ⚪ B. Create your own class removing the spacing and add this class to the class property of the text widget.
- ⚪ C. Add the class remove-bottomspacing to the class property of the text widget.
- ✅ **D.** Go to the properties of the text widget and set the the 'Spacing Bottom' property in Appearance to 'Outer None'.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Atlas UI có sẵn thuộc tính Spacing trong mục Appearance của widget. Chọn Spacing Bottom = Outer None là cách nhanh nhất, không cần viết CSS hay class.

---

### Đề 1 - Câu 19 [UX & Logging]

**Câu hỏi:** The default language of the app is English. United States (en_US) and Dutch. Netherlands (nl_NL) is an additional installed language. A user logs in and has the language Dutch. Netherlands (nl_NL) set as their user language. A button on a page doesn't have a caption but needs one. How should this be fixed?

- ✅ **A.** The caption must be set in the Dutch language only.
- ⚪ B. The caption must be set in the user language library and synced with the running app.
- ⚪ C. Change the conditional visibility of the button so that the caption becomes visible for users with the Dutch language.
- ⚪ D. In both English and Dutch, the caption must be set in the correct

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): User dùng tiếng Hà Lan nên caption thiếu ở bản dịch nl_NL. Chỉ cần bổ sung caption tiếng Hà Lan (Language > nl_NL), bản tiếng Anh vẫn giữ nguyên.

---

### Đề 1 - Câu 20 [Domain Model]

**Câu hỏi:** What is an index?

- ⚪ A. The unique identifier of an object
- ⚪ B. A table that contains the results of a query
- ⚪ C. A sorted duplicate of an entity table
- ✅ **D.** An extra sorted table with only the record IDs and the selected attribute

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Index là một bảng phụ được sắp xếp, chỉ chứa giá trị thuộc tính được index và id bản ghi, giúp database tìm nhanh mà không cần quét cả bảng.

---

### Đề 1 - Câu 21 [XPath & General]

**Câu hỏi:** Mendix Academy needs to retrieve all trainees with a valid RAD certificate from their customer database. Luckily, all certificates are stored in the String attribute CertificatelD and have the prefix ‘RAD’. You build a Trainee_Overview page where you add a List view with a data source Trainee by XPath. Which XPath should you specify when retrieving the Trainee entity?

- ⚪ A. [Trainee.CertificateID[starts-with('RAD')]]
- ✅ **B.** [starts-with(CertificatelD, 'RAD')]
- ⚪ C. [starts-with(Trainee.CertificatelD, RAD)]
- ⚪ D. [CertificatelD != empty and starts-with('RAD')]

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Cú pháp đúng là starts-with(attribute, 'chuỗi') đặt trong ngoặc vuông, attribute viết trực tiếp (không kèm tên entity), chuỗi đặt trong nháy đơn.

---

### Đề 1 - Câu 22 [Microflows]

**Câu hỏi:** Microflow A iterates over a list of committed OrderLines, retrieves by association the Product being ordered, then adjusts the Product Stock amount accordingly. Microflow B retrieves the whole Product list of the Order from the database, then iterates over the Product list and adjusts the Product Stock amount accordingly. Which solution would be the best approach and why?

- ✅ **A.** Microflow A, because the by association retrieve in microflow A retrieves from memory and is much faster than a database retrieve.
- ⚪ B. Microflow B. because the retrieve in microflow A might result in multiple database retrieves even when retrieved by association.
- ⚪ C. Microflow B, because a database retrieve in this case is faster than a by association retrieve.
- ⚪ D. Microflow A, because there is no difference in performance between the two and a by association retrieve is easier to maintain from a developer perspective.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Theo file gốc là Microflow A (ô tô màu vàng). ⚠ Chưa xác nhận được: tài liệu Mendix không nói retrieve by association luôn lấy từ bộ nhớ. Nếu Product chưa có trong bộ nhớ thì mỗi vòng lặp vẫn có thể là một query.

---

### Đề 1 - Câu 23 [XPath & General]

**Câu hỏi:** In a List view displaying a list of Orders, you want to add an XPath. The XPath should result in Orders where theOrderDate is within the past three years. Which XPath should you use?

- ⚪ A. [OrderDate < '[%BeginOfCurrentDay%] - 3 * [%YearLength%]']
- ✅ **B.** [OrderDate > ‘[%BeginOfCurrentDay%) - 3 * [%YearLength%]']
- ⚪ C. [addYears(OrderDate, -3)]- [OrderDate < '[%BeginOfCurrentDay%]']
- ⚪ D. [OrderDate > '[3 * [%YearLength%]- %BeginOfCurrentDay%]']

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Trong vòng 3 năm qua nghĩa là OrderDate lớn hơn (thời điểm đầu ngày hôm nay trừ 3 năm), viết bằng token: [%BeginOfCurrentDay%] - 3 * [%YearLength%].

---

### Đề 1 - Câu 24 [Security]

**Câu hỏi:** What is the Mendix Clent?

- ⚪ A. The back end of your application
- ⚪ B. A customer who has a contract with Mendix
- ✅ **C.** The front end of your application
- ⚪ D. A user who is running your app

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Mendix Client là phần front end chạy trên trình duyệt hoặc thiết bị di động, hiển thị UI và giao tiếp với Mendix Runtime (back end).

---

### Đề 1 - Câu 25 [UX & Logging]

**Câu hỏi:** The width of a layout grid can be set to Full width or Fixed width. What is the difference?

- ✅ **A.** When set to Fixed width, the total column width of this layout will be exactly the width in pixels as specified in the style sheet. Full width will be the full available width of the page.
- ⚪ B. When set to Fixed width, the input widgets width will be exactly the width in pixels as specified in the style sheet. When set to Full width the input widgets width will be the full width of the client.
- ⚪ C. When set to Fixed width, the total column width of this layout will be exactly the width in pixels as specified in the style sheet. Full width will be the full width of the client.
- ⚪ D. When set to Fixed width, the total column width of this layout will be exactly 960 pixels centered in the page. Full width will be the full available width of the enclosing container.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Fixed width giới hạn tổng chiều rộng cột theo giá trị pixel trong stylesheet (container cố định). Full width chiếm toàn bộ chiều rộng khả dụng của trang.

---

### Đề 1 - Câu 26 [XPath & General]

**Câu hỏi:** Which search function should you use to find XPath expressions that might be affecting your performance? Select the correct keyboard shortcut.

- ⚪ A. Ctrl + F
- ⚪ B. Ctrl + Space
- ✅ **C.** Ctrl + Shift + F
- ⚪ D. Shift + F

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Ctrl+Shift+F mở Find Advanced trong Studio Pro, cho phép tìm theo loại (ví dụ mọi XPath) trên toàn app để rà soát hiệu năng.

---

### Đề 1 - Câu 27 [UX & Logging]

**Câu hỏi:** You need your users to fill out a form with 40 input fields, but putting them all on one page creates a very confusing Ul. How can you simplify this form using Mendix best practices?

- ⚪ A. Add a scroll container so that each field's size can be increased
- ⚪ B. Use select pages instead of dropdown widgets
- ✅ **C.** Use a Wizard to break it into multiple pages
- ⚪ D. Reduce the size of each input widget so that more can fit on the page at once

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Form 40 trường nên chia thành nhiều bước bằng wizard để giảm tải nhận thức; user điền từng nhóm thông tin.

---

### Đề 1 - Câu 28 [Microflows]

**Câu hỏi:** When an Order is submitted, the Order Number (String) is created in a sub-microflow. What is the best way to build this sub-microflow according to Mendix best practices?

- ⚪ A. Build the OrderNumber within the End event and pass it back to the main microflow.
- ⚪ B. Build the OrderNumber in a new string variable. then change and refresh the Order object within the sub-microflow.
- ✅ **C.** Build the OrderNumber in a new string variable and pass it back to the main microflow.
- ⚪ D. Build the OrderNumber in a new string variable, then change and commit the Order object within the sub-microflow.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Sub-microflow nên chỉ làm một việc: tạo chuỗi OrderNumber và trả về. Việc change và commit Order để ở microflow chính cho dễ đọc, dễ tái sử dụng và tránh commit rải rác.

---

### Đề 1 - Câu 29 [XPath & General]

**Câu hỏi:** You would like to search for trainees in the database using their names. To speed up the search, where should you add an index?

- ⚪ A. In the ‘Search on’ settings of the List view
- ⚪ B. In a microflow by adding a Create index activity and returning the indexed list
- ✅ **C.** In the entity properties in the Domain model
- ⚪ D. In a widget downloaded from the Marketplace

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Index được khai báo trong properties của entity ở Domain Model (tab Indexes), chọn thuộc tính Name để tìm kiếm nhanh hơn.

---

### Đề 1 - Câu 30 [Domain Model]

**Câu hỏi:** You want the address of a customer to be moved from the Customer entity to a newly created Customer Address entity. When should you remove the Address attribute from the Customer entity?

- ⚪ A. You should try to avoid removing it
- ⚪ B. In the deploy that you add the Customer Address entity
- ✅ **C.** In the next deploy after you have added the CustomerAddress entity
- ⚪ D. After a predefined transfer period

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Phải giữ thuộc tính Address cũ trong lần deploy đầu để chạy migration chuyển dữ liệu sang CustomerAddress. Xóa ngay sẽ mất dữ liệu; xóa ở lần deploy sau khi dữ liệu đã chuyển xong là an toàn.

---

### Đề 1 - Câu 31 [Security]

**Câu hỏi:** Given that nanoflows always run in the context of the current user, which of the following statements is true?

- ✅ **A.** Nanoflow access is as secure as a microflow with entity access enabled.
- ⚪ B. Nanoflow access is as secure as a microflow called inside of the nanoflow
- ⚪ C. Nanoflow access is as secure as a microflow access without entity access enabled.
- ⚪ D. Nanoflow access is as secure as a microflow.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Nanoflow chạy trên client trong ngữ cảnh user hiện tại, mọi dữ liệu nó chạm tới đều chịu entity access, nên mức an toàn tương đương microflow bật 'Apply entity access'.

---

### Đề 1 - Câu 32 [Security]

**Câu hỏi:** A user with the role Employee adds a new OrderLine to an Order and selects a Product After Product selection the Employee sets a Discount of 10% What will happen when the related microflow is triggered as an on-change microflow?

- ⚪ A. The Employee will get an error message, because the Employee role doesn't have write access to the attribute LineValue
- ⚪ B. The OrderLine LineValue will not be changed and the user will not be informed.
- ✅ **C.** The OrderLine LineValue will be changed to 9.00 and the value is returned to the client
- ⚪ D. The Orderline LineValue will be changed to 9.00, though it cannot be passed to the client because the Employee role doesn't have write access to the attribute LineValue

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Microflow mặc định chạy không áp dụng entity access, nên vẫn đổi được LineValue thành 9.00 và trả object về client để hiển thị, dù role Employee không có quyền write trên thuộc tính đó.

---

### Đề 1 - Câu 33 [UX & Logging]

**Câu hỏi:** What type of design has a focus on accessibility?

- ⚪ A. UX Design
- ⚪ B. UI Design
- ✅ **C.** Usability Design
- ⚪ D. Interaction Design

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Usability design chú trọng ứng dụng dễ dùng cho mọi người, trong đó có accessibility (người khuyết tật, tương phản màu, điều hướng bằng bàn phím…).

---

### Đề 1 - Câu 34 [UX & Logging]

**Câu hỏi:** Customers can choose their desired delivery method when submitting an order in an app. This is dependent on their address, and you only want to display the delivery options that are available to their location, What is the most efficient way to achieve this?

- ✅ **A.** Use an on-change microflow to set the conditional visibility of the relevant page elements.
- ⚪ B. Use an on-leave microflow to set the conditional visibility of the relevant page elements
- ⚪ C. Use an on-change microflow to set the conditional editabilty of the relevant page elements.
- ⚪ D. Use an on-leave microflow to set the conditional editability of the relevant page elements.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Khi địa chỉ thay đổi, on-change microflow (hoặc nanoflow) tính lại các tùy chọn giao hàng phù hợp và điều khiển conditional visibility, nên chỉ những lựa chọn khả dụng được hiển thị ngay.

---

### Đề 1 - Câu 35 [Microflows]

**Câu hỏi:** The following microflow is triggered when saving a new Order. This microflow triggers a sub- microflow where the Order/Number is defined and set. This setup is not following Mendix best-practices. What should be changed to meet the best practices?

- ⚪ A. The Commit of the OrderlineList should happen before the sub- microfiow call.
- ✅ **B.** The sub-microflow should return the OrderNumber variable. The Change and Commit of the Order object should be done in the main microfiow.
- ⚪ C. The retrieve of the OrderLineList should happen after the sub-microflow call.
- ⚪ D. The retrieve of the OrderLineList and Commit of this list should be executed in a second sub-microflow.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Best practice: sub-microflow chỉ tính và trả về OrderNumber; microflow chính thực hiện Change và Commit Order. Như vậy mọi thay đổi trên Order nằm ở một chỗ và tránh commit nhiều lần.

---

### Đề 1 - Câu 36 [Domain Model]

**Câu hỏi:** In the properties of an entity, what does checking the system member 'owner' do?

- ⚪ A. The object ID of the referenced Account object is stored as the owner of the object when it is created.
- ⚪ B. The object ID of the logged-in user who retrieves the object from the database will be stored in the object for future reference.
- ⚪ C. Objects of this entity are the owner of all associations from and towards this entity.
- ✅ **D.** The object ID of the logged-in user who creates the object is stored as the owner of the object.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Bật system member 'owner' thì khi tạo object, Mendix tự lưu tham chiếu tới Account của user đang đăng nhập vào System.owner. Hay dùng cho XPath như [System.owner='[%CurrentUser%]'].

---

### Đề 1 - Câu 37 [UX & Logging]

**Câu hỏi:** What type of menu is most likely to go well with Hick's law?

- ⚪ A. A Navigation Tree
- ✅ **B.** A Simple Menu Bar
- ⚪ C. A Custom Menu
- ⚪ D. A Default Menu Bar

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Hick's law: càng nhiều lựa chọn thì user càng mất thời gian quyết định. Simple menu bar ít mục, phẳng, nên phù hợp nhất.

---

### Đề 1 - Câu 38 [Microflows]

**Câu hỏi:** Rules have some limitations compared to sub-microflow. What is one of the limitations of a Rule? Rule cannot:

- ⚪ A. have multiple End events
- ⚪ B. Return a Boolean
- ✅ **C.** Interact with the client
- ⚪ D. Have an object as an input parameter

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Rule chỉ dùng trong Decision để trả về Boolean hoặc Enumeration và không được tương tác với client (không show page, không show message, không đóng page…).

---

### Đề 1 - Câu 39 [XPath & General]

**Câu hỏi:** you need to create an Xpath query to look for customers with the company name Mendix. Which of the follwing suggestions represents a syntactically correct XPath ?

- ✅ **A.** [CustomerManagement.Customer[contains(CustomerName. ‘Mendix')]]
- ⚪ B. [CustomerManagement.Customer/(CustomerName = ‘Mendix')]
- ⚪ C. [CustomerManagement.Customer/contains(CustomerName. ‘Mendix')]
- ⚪ D. [CustomerManagement.Customer/[contains(CustomerName. ‘Mendix')]]

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Hàm contains() đặt trong cặp ngoặc vuông ràng buộc ngay sau entity: Customer[contains(CustomerName, 'Mendix')]. Các phương án còn lại đặt '/' hoặc ngoặc sai chỗ.

---

### Đề 1 - Câu 40 [Domain Model]

**Câu hỏi:** When is it likely that an index will negatively impact perfomance?

- ⚪ A. When an entity has many attributes
- ✅ **B.** When data is changed more often than it is read
- ⚪ C. When the entity exclusively has stored attributes
- ⚪ D. When there are a lot of objects for the relevant entity

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Index tăng tốc đọc nhưng mỗi lần insert/update/delete database phải cập nhật thêm bảng index. Nếu dữ liệu thay đổi nhiều hơn được đọc thì chi phí ghi lớn hơn lợi ích tìm kiếm.

---

### Đề 1 - Câu 41 [Security]

**Câu hỏi:** You want anonymous user to be able to place orders without logging in to an app. You turn on Anonymous user and configure the User role, module roles, and related access. Given the following domain model, how should you configure Anonymous user data access?

- ⚪ A. Order & OrderLine Read & Write access without XPath constraint, because an Anonymous user cannot be defined using the '[%CurrentUser%]' token. And full read access to the Product entity.
- ⚪ B. Read & Write access for Order & Orderline with the following XPath constraints: Order entity
[ADV20.Order Customer/ADV20.Customer/ADV20.Customer Account =
'[%CurrentUser%]']
OrderLine entity [ADV20.OrderLine Order/ADV20.Order/ADV20.Order Customer/ ADV20.Customer/ADV20.Customer Account='[%CurrentUser%]']
Product entity
And full read access to the Product entity.
- ⚪ C. Read & Write access for Onder & OrderLine with the following XPath constraint: [System.owner= '[%CurentUser%]'], And full read access to the Product entity.
- ✅ **D.** Mimic the Order & OrderLine entites with non-persistable entities. Grant the Anonymous user CRUD access to the non-persistable entities and full read access to the Product entity. The persistable Order and OnderLine objects are created in the microflow submitting the Order.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Anonymous user không có account cố định nên không giới hạn được bằng [%CurrentUser%]. Cách an toàn: cho anonymous thao tác trên entity non-persistable, rồi microflow submit mới tạo Order/OrderLine thật.

---

### Đề 1 - Câu 42 [Microflows]

**Câu hỏi:** When would you use the custom error handling "without rollback" on a sub-microflow call?

- ⚪ A. When you want to make sure that both the parent and sub-microflows are rolled back.
- ⚪ B. When you do not want the sub-microflow to be rolled back even if it has an error.
- ✅ **C.** When you do not want the parent microflow to be rolled back even if the sub-microflow has an error.
- ⚪ D. When additional documentation is required. Without rollback increases readability.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): 'Custom without rollback' trên lời gọi sub-microflow nghĩa là khi sub-microflow lỗi, những thay đổi trước đó của microflow cha không bị rollback và cha tiếp tục theo đường xử lý lỗi.

---

### Đề 1 - Câu 43 [UX & Logging]

**Câu hỏi:** What is the relationship between UX and UI?

- ⚪ A. UX and UI are at a core level the same thing
- ⚪ B. UX and UI are mostly unrelated
- ⚪ C. UX is a sub-category of UI
- ✅ **D.** Ul can be used to improve UX

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): UX là toàn bộ trải nghiệm của user, UI là phần giao diện. UI tốt là một phương tiện để cải thiện UX.

---

### Đề 1 - Câu 44 [Security]

**Câu hỏi:** How do you handle access to a sub-microflow in relation to the parent microflow?

- ⚪ A. When creating 3 sub-microfiow, you can choose whether you want to inherit the access rules from the parent microflow or to set it up independently.
- ✅ **B.** Access to a sub-microflow does not need to be set because itis handled by the parent microflow.
- ⚪ C. If you set the access to a sub-microflow, it overwrites access defined by the parent microflow.
- ⚪ D. Access to a sub-microflow needs to be set up independently of the access to the parent microflow.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Sub-microflow được gọi từ microflow cha chạy với quyền của cha nên không cần gán module role. Gán role còn làm lộ sub-microflow ra client API.

---

### Đề 1 - Câu 45 [Microflows]

**Câu hỏi:** The Mendix Platform uses transactions which means that every microflow, commit, and delete will occur within a database transaction. When will each transaction be initialized and when will it end?

- ✅ **A.** The transaction is initialized as soon as the microflow executes its first database action and only ends when the microflow completes.
- ⚪ B. The transaction is initialized as soon as each individual microflow action executes and ends after each individual microflow action.
- ⚪ C. The transaction is initialized as soon as the microflow executes its first database action and ends after each database action.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Một microflow chạy trong một database transaction: transaction mở khi có thao tác database đầu tiên và chỉ kết thúc (commit hoặc rollback) khi microflow hoàn tất.

---

### Đề 1 - Câu 46 [Security]

**Câu hỏi:** What does entity access affect?

- ⚪ A. What a demo user can see on a page
- ⚪ B. Which pages a user can see
- ✅ **C.** Which actions a user can execute
- ⚪ D. Which set of data a user can manipulate

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Theo file gốc là 'Which actions a user can execute'. ⚠ Nên xem lại: tài liệu Mendix nói access rule của entity quy định user được làm gì với các object của entity (create, read, write, delete, giới hạn bằng XPath). Cách diễn đạt này gần với 'Which set of data a user can manipulate' hơn.

---

### Đề 1 - Câu 47 [UX & Logging]

**Câu hỏi:** The recommended method when setting the log node name of a custom log message is to:

- ⚪ A. Create a settings entity to maintain the log node names from the runtime.
- ✅ **B.** Use an enumeration to store all log node names as an enumeration value and use the expression getCaption ModuleName.EnumerationList.CustomLogNodeNamel to set the log node name.
- ⚪ C. Use a snippet with a text widget containing a list of all custom log node names. Store this snippet in the general module as a resource.
- ⚪ D. Use string quotes around a caption Log node name

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Lưu tên log node trong enumeration và dùng getCaption(...) giúp tên thống nhất, tránh gõ sai chuỗi và dễ đổi ở một chỗ.

---

### Đề 1 - Câu 48 [XPath & General]

**Câu hỏi:** You need to write a query to retrieve all registrations associated with trainees who bought vouchers in the EMEA region and where the voucher was not used. Which of the following XPath expressions is correct?

- ⚪ A. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA'] [VoucherUsed = false ]]
- ⚪ B. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed = false ]]
- ⚪ C. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed != true ]]
- ✅ **D.** [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed = false()]]

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Hai điều kiện cùng áp lên một object nên viết chung trong một ngoặc với 'and'. Giá trị Boolean trong XPath phải viết là false() (có ngoặc).

---

### Đề 1 - Câu 49 [XPath & General]

**Câu hỏi:** In a List view displaying a list of Orders, you want to add an XPath. The result of the XPath should show Orders where the OrderDate is greater than the year 2000 and smaller than the current date and time. Which XPath should you use?

- ⚪ A. [formatdatetime(year(OrderDate) > 2000])]
[OrderDate <1%CurrentDateTime%]]
- ⚪ B. [year(OrderDate) 2000]
[OrderDate <1%CurrentDateTime%]]
- ✅ **C.** [year-from-dateTime(OrderDate) > 2000)
[OrderDate <1%CurrentDateTime%]]
- ⚪ D. [formatDateTime([%CurrentDateTime%], 'yyyy') > 2000]
[OrderDate < '[%CurrentDateTime%]']

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): year-from-dateTime() lấy năm từ thuộc tính DateTime trong XPath. Thêm ràng buộc thứ hai OrderDate < '[%CurrentDateTime%]'; hai ngoặc liền nhau tương đương 'and'.

---

### Đề 1 - Câu 50 [Microflows]

**Câu hỏi:** When is custom error handling most appropriate within a microflow?

- ⚪ A. When calling other microflows
- ✅ **B.** When Interacting with external systems
- ⚪ C. When using a JAVA action activity
- ⚪ D. When using multiple decision elements

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Gọi hệ thống bên ngoài (REST, SOAP, email…) dễ lỗi ngoài tầm kiểm soát (timeout, mất kết nối), nên cần custom error handling để log và xử lý có kiểm soát.

---

## Đề thi thử số 2

### Đề 2 - Câu 1 [Security]

**Câu hỏi:** In which of the following situations do you need to set the microflow access for a specified user?

- ⚪ A. When the microflow is set as an event handler
- ⚪ B. When the microflow is set a calculated attribute
- ⚪ C. When the microflow is a part of another parent microflow
- ✅ **D.** When the microflow is called from the navigation item

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Microflow được gọi trực tiếp từ client (navigation item, button) cần cấu hình microflow access cho role. Event handler, calculated attribute và sub-microflow được gọi nội bộ từ server nên không cần.

---

### Đề 2 - Câu 2 [Microflows]

**Câu hỏi:** In this sub-microflow, you want to return an integer/long containing the number of years between two dates. What would be the best way to calculate the number of years between two dates?

- ⚪ A. Use the ‘YearsBetween’ JAVA action available in the CommunityCommons module.
- ✅ **B.** Use the ‘calendarYearsBetween’ Date Function Call, which is available by default in Studio Pro.
- ⚪ C. Create a loop that repeatedly adds one year from the start date until the end date, then counts how many fit between the two dates.
- ⚪ D. Use the ‘yearsBetween’ Date Function Call, which is available by default in Studio Pro.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): calendarYearsBetween là hàm có sẵn, tính số năm theo lịch giữa hai ngày một cách chính xác. yearsBetween cũ tính theo số ngày chia trung bình nên có thể sai lệch.

---

### Đề 2 - Câu 3 [UX & Logging]

**Câu hỏi:** When should you use the data source type Association when displaying a list on a page?

- ✅ **A.** When you need to show all associated OrderLines of an Order and there are no additional constraints needed.
- ⚪ B. Always when you need to show all associated OrderLines of an Order in a native app.
- ⚪ C. Always when you want to show the associated OrderLines of an Order.
- ⚪ D. When you need to show all associated OrderLines of an Order with uncommitted changes.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Data source Association lấy object qua association từ object cha (kể cả object chưa commit). Dùng khi cần hiển thị toàn bộ OrderLine của Order mà không cần ràng buộc thêm; cần lọc thì dùng Database/XPath.

---

### Đề 2 - Câu 4 [Security]

**Câu hỏi:** You want to show customers only their own orders in a data grid. Which of the following ‘options is the most secure way to achieve this?

- ⚪ A. Configure conditional visibility on the page.
- ⚪ B. Set a microfiow retrieving the orders of the user as a data source of the data grid widget.
- ⚪ C. Add a data grid constraint.
- ✅ **D.** Add an XPath constraint in the entity access rule of the Order entity, restricting the access to the currently logged-in user.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): XPath trong access rule của entity được runtime áp dụng cho mọi truy vấn, nên an toàn nhất. Visibility hay constraint trên page chỉ là hiển thị và có thể bị vượt qua.

---

### Đề 2 - Câu 5 [Microflows]

**Câu hỏi:** What do you use to pass an error to a parent microflow?

- ⚪ A. Rollback
- ✅ **B.** Error End Event element
- ⚪ C. Continue element
- ⚪ D. Nothing, this is default behavior

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Error End Event kết thúc microflow con ở trạng thái lỗi, nên lỗi được ném tiếp lên microflow cha để cha xử lý.

---

### Đề 2 - Câu 6 [XPath & General]

**Câu hỏi:** A customer has write access to an OrderLine as long as the associated Order has the status "draft". How should you write an XPath to constrain the OrderLines in the entity access rule for the given Domain model?

- ⚪ A. [AdvancedModule.OrderLine Order/AdvancedModule.Order/Status = 'Draft]
JAdvancedModule.OrderLine Order/AdvancedModule.Order/
AdvancedModule.Order Customer/AdvancedModule.Customer/ System.owner '[%CurrentUser]']
- ⚪ B. [AdvancedModule.OrderLine Order/AdvancedModule.Order
[Status = 'Draft']
[AdvancedModule.Order Customer/AdvancedModule.Customer/System.owner = '[%CurrentUser%]']]
- ⚪ C. [AdvancedModule.OrderLine Order/AdvancedModule.Order/Status = "Draft'] [AdvancedModule.OrderLine Order/AdvancedModule.Order/ AdvancedModule.Order Customer/AdvancedModule.Customer/ AdvancedModule.Customer Account=%CurrentUser%]]
- ✅ **D.** [Advanced Module.OrderLine Order/AdvancedModule.Order
[Status = "Draft]
[AdvancedModule.Order Customer/AdvancedModule.Customer/
AdvancedModule.Customer Account=%CurrentUser%]]]

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Đi từ OrderLine tới Order và đặt cả hai điều kiện (Status = 'Draft' và Customer_Account = CurrentUser) trong cùng sub-constraint trên Order, để cả hai áp lên cùng một Order.

---

### Đề 2 - Câu 7 [Domain Model]

**Câu hỏi:** When a DateTime attribute is localized, the value stored in the database will be formatted in:

- ⚪ A. The client server time zone
- ⚪ B. The database server time zone
- ⚪ C. The application server time zone
- ✅ **D.** The UTC time zone

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Thuộc tính DateTime localized luôn được lưu theo UTC trong database, rồi chuyển sang múi giờ của user khi hiển thị.

---

### Đề 2 - Câu 8 [Security]

**Câu hỏi:** In which of the following cases should the Navigation setting “visible for” be set?

- ⚪ A. All the pages in the app.
- ✅ **B.** All the pages in the app excluding the role-based pages
- ⚪ C. All pages which are not marked as home or role-based pages
- ⚪ D. All the pages in the app excluding the home-web page

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): 'Visible for' của navigation item phụ thuộc page access. Các page dùng làm role-based home page đã gắn theo role nên không cần cấu hình thêm; các page còn lại cần đặt quyền tương ứng.

---

### Đề 2 - Câu 9 [XPath & General]

**Câu hỏi:** In XPath, it can be useful to define sub-constraints to further restrict the data that is being constrained. This is easily achieved by adding a sub-constraint within the brackets of the original constraint. Examine the following XPath with a sub-constraint:
 //Sales.Customer[Sales.Customer Address/Sales.Address[City = 'Rotterdam' or City
'London']]
What will this query retrieve?

- ⚪ A. One object of type SAddress: Rotterdam or London.
- ⚪ B. Two objects of type SAddress: Rotterdam and London
- ⚪ C. All customers
- ✅ **D.** All customers who live in Rotterdam or London.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Sub-constraint lọc Address theo City Rotterdam hoặc London, rồi lấy các Customer có association tới Address đó. Kết quả là các customer sống ở Rotterdam hoặc London.

---

### Đề 2 - Câu 10 [Security]

**Câu hỏi:** Which of the following statements is true?

- ✅ **A.** Entity access rules are applied on the request from the runtime to the database.
- ⚪ B. Entity access rules are applied on the request from the client to the runtime
- ⚪ C. Entity access rules are applied by the runtime after the return of the database requests.
- ⚪ D. Entity access rules are applied on the return from the runtime to the client.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): XPath của entity access được runtime thêm vào câu query gửi xuống database, nên dữ liệu user không được phép xem sẽ không bao giờ được truy vấn ra.

---

### Đề 2 - Câu 11 [UX & Logging]

**Câu hỏi:** Which of the following log messages follows the best practices for a Debug log message?

- ⚪ A. Rest service has returned 404
- ⚪ B. “Unknown user input '129q', unable to process value.”
- ✅ **C.** “User language has not been set yet.”
- ⚪ D. “Contacting REST service.”

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Theo file gốc là 'User language has not been set yet.'. ⚠ Nên xem lại: theo tài liệu Mendix, Debug là thông tin chi tiết dùng để chẩn đoán lỗi, còn Warning là khi có điều bất thường. Theo định nghĩa đó, 'Contacting REST service.' hợp với Debug hơn.

---

### Đề 2 - Câu 12 [XPath & General]

**Câu hỏi:** You need to retrieve the employee information based on the current user to display the ‘employee's information on the account overview page. Which of the following suggestions represent the correct and optimal XPath?

- ⚪ A. [Production.Customer_Account = $currentUser]
- ⚪ B. [Production.Employee_Account/Administration.Account/id = $currentUser]
- ✅ **C.** [Production.Employee_Account = '[%CurrentUsers%]']
- ⚪ D. [Production.Employee_Account/AdministrationAccount/id = '[%CurrentUsers%]']

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): So sánh trực tiếp association Employee_Account với token '[%CurrentUser%]' là ngắn gọn và tối ưu nhất. $currentUser không dùng được trong XPath của page.

---

### Đề 2 - Câu 13 [Domain Model]

**Câu hỏi:** Non-persistable entities are stored in the runtime memory and are never committed to the database. Therefore. they have no table in the database. Does it make sense to commit a non- Persistent object?

- ⚪ A. Yes, because othenwise the object cannot be retrieved over association.
- ✅ **B.** Yes. committing non-persistable entities records the current attribute values and association values in memory, allowing a rollback to revert to these values. a
- ⚪ C. No. non-persistable entities are never committed.
- ⚪ D. Yes. because Mendix will create a table in the database and store the object in the database.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Commit một object non-persistable không ghi xuống database, nhưng 'chốt' lại giá trị thuộc tính và association hiện tại trong bộ nhớ. Khi rollback, object quay về trạng thái đã commit này.

---

### Đề 2 - Câu 14 [UX & Logging]

**Câu hỏi:** Which log message component is generated only for cloud-deployed applications?

- ✅ **A.** Source
- ⚪ B. Log Node
- ⚪ C. Log Level
- ⚪ D. Timestamp

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Trên Mendix Cloud, mỗi dòng log có thêm thông tin Source (instance hoặc nguồn phát sinh log); timestamp, log level và log node thì môi trường nào cũng có.

---

### Đề 2 - Câu 15 [Microflows]

**Câu hỏi:** Why would you use two identical database retrieves in one microflow?

- ⚪ A. When speed and memory usage are not a concern.
- ✅ **B.** To optimize both retrieves if they are followed immediately by Aggregate list activities.
- ⚪ C. For readability. The second retrieve will not result in a database call.
- ⚪ D. To free up memory between the first retrieve and the second.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Khi Retrieve from database theo sau ngay là Aggregate list (Count, Sum…) và list không dùng vào việc khác, Mendix gộp thành một câu query aggregate. Hai retrieve giống nhau cho hai aggregate khác nhau thì cả hai đều được tối ưu.

---

### Đề 2 - Câu 16 [XPath & General]

**Câu hỏi:** You would like to replace an XPath that utes the logical 'or' operator with a microfiow using. two Retrieves and a List operation. Which of the following List operations should you use?

- ⚪ A. Find
- ✅ **B.** Union
- ⚪ C. Subtract
- ⚪ D. Intersert

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Toán tử 'or' nghĩa là object thỏa ít nhất một điều kiện, tức là hợp hai list, nên dùng list operation Union.

---

### Đề 2 - Câu 17 [Domain Model]

**Câu hỏi:** In an app,a user can create orders. It is required that each order gets a unique order number.The order number is constructed from the customer number and the date when ordered.When should you determine the order number value and store it?

- ⚪ A. In a before commit event on the Order entity.
- ⚪ B. In the microflow which commits the Order afterthe Order is entered.
- ⚪ C. In an after create event on the Order entity.
- ✅ **D.** In the microflow which creates the order object and opens the Order_New page.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Số đơn hàng ghép từ mã khách hàng và ngày đặt, cả hai đã có ngay lúc tạo Order. Gán giá trị trong microflow tạo Order (trước khi mở trang Order_New) giúp logic rõ ràng, tránh dùng event handler chạy ngầm mỗi lần commit.

---

### Đề 2 - Câu 18 [UX & Logging]

**Câu hỏi:** You are building a responsive web page where you only want some of the existing columns to be visible on tablets. How can you use bootstrap to achieve this?

- ✅ **A.** By using the visible-sm and hidden-sm helper classes
- ⚪ B. By using conditional visibility based on device type
- ⚪ C. By creating a tablet specific page
- ⚪ D. By adding the col-sm-0 helper class to the columns you want to hide

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Bootstrap có helper class visible-*/hidden-* theo kích thước màn hình (sm = tablet) để ẩn/hiện cột mà không cần trang riêng.

---

### Đề 2 - Câu 19 [XPath & General]

**Câu hỏi:** We have five trainees: two without registrations, one with a discount of 30, and two with discounts of 50. How many trainee objects will the following XPath return? [not(Training.Registration_Trainee/Training.Registration/Discount = 30)]

- ⚪ A. 5 trainees
- ⚪ B. 1 trainees
- ✅ **C.** 4 trainees
- ⚪ D. 2 trainees

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): not(... = 30) lấy mọi trainee KHÔNG có registration discount 30, gồm cả trainee không có registration. Vậy 5 - 1 = 4 trainee.

---

### Đề 2 - Câu 20 [Security]

**Câu hỏi:** Is the following statement True or False and why?
"Every microflow in the app must be assigned at least one allowed role, including unused microflows and sub-microflows."

- ✅ **A.** False-When you add a module role to an unused microflow. this microflow is accessible through the server API because it specifies allowed roles. This is unnecessary because the microflow is not used from navigation, a page or published service. Sub microflows do not need assigned allowed roles because they inherit this from the parent microflow.
- ⚪ B. True-You only need to assign allowed roles to unused microflows to make sure they are safe, you don't need to assign allowed roles to sub microflows because they inhent this from the parent microflow
- ⚪ C. True-When you add a module role to an unused microflow this Microflow is accessible through the server API because it specifies allowed roles. This is unnecessary because the microflow is not used from navigation a page or published service. Sub microflows need assigned allowed roles because they inherit this from the parent microflow
- ⚪ D. True-This way you can be sure that your application is safe, so it is good to assign both unused microflows and sub-microflows to allowed
roles

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): ✎ Đã sửa so với file gốc. Câu phát biểu là SAI. Tài liệu Mendix (Module Security): allowed roles chỉ được kiểm tra khi microflow được gọi từ client, và microflow gọi microflow khác thì không kiểm tra role. Vậy sub-microflow không cần role; gán role cho microflow không dùng chỉ làm nó bị lộ qua API.

---

### Đề 2 - Câu 21 [Domain Model]

**Câu hỏi:** Which statement is true about localized DateTime attributes?

- ✅ **A.** Use non-localized attributes if you are not interested in the time component or if you want a date to look exactly the same all over the world.
- ⚪ B. Use non-localized attributes if you are interested in the time component (for example, birthdays) or if you want a date to look exactly the same all over the world.
- ⚪ C. It doesn’t matter if you localize a DateTime Attribute because the end user will never see the difference. The difference is only visible in the backend.
- ⚪ D. Use localized attributes if you are interested in the time component (for example, birthdays) or if you want a date to look exactly the same all over the world.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): ✎ Đã sửa so với file gốc. Tài liệu Mendix (Attributes > Localize): nếu KHÔNG quan tâm phần giờ và muốn ngày giống hệt nhau ở mọi nơi trên thế giới (ví dụ ngày sinh) thì tắt Localize, tức là dùng non-localized.

---

### Đề 2 - Câu 22 [UX & Logging]

**Câu hỏi:** What is one method of applying typographical hierarchy to a page?

- ⚪ A. Ordering multiple languages appropriately in settings
- ⚪ B. Creating a sticky footer
- ✅ **C.** Changing text size
- ⚪ D. Adding sort constraints

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Typographic hierarchy là dùng kích thước, độ đậm và kiểu chữ khác nhau (ví dụ H1, H2, body) để thể hiện mức độ quan trọng của nội dung.

---

### Đề 2 - Câu 23 [UX & Logging]

**Câu hỏi:** How are logs stored in the Mendix Cloud?

- ⚪ A. Within multiple log files organized by log level
- ✅ **B.** Within multiple log files organized by time periods
- ⚪ C. Within multiple log files capped at a particular file size
- ⚪ D. Within a single log file that is cleared periodically

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Mendix Cloud lưu log thành nhiều file theo khoảng thời gian (theo ngày), có thể tải về theo ngày trong Developer Portal.

---

### Đề 2 - Câu 24 [Domain Model]

**Câu hỏi:** Is it preferable to use one-to-one associations or inheritance in a system with a high transaction volume? (Multiple changes or creates per second)

- ⚪ A. There is no preference because they will both have the same performance.
- ⚪ B. Inheritance, because writing and updating a single table is faster than updating records in multiple tables.
- ⚪ C. Both a one-to-one association and inheritance in the same entity.
- ✅ **D.** One-to-one associations, because writing and updating records in tables with inheritance is slower than just updating a single table.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): ✎ Đã sửa so với file gốc. Tài liệu Mendix (Generalization vs One-to-One Associations) nói rõ: ghi và cập nhật bản ghi trong bảng có kế thừa chậm hơn chỉ cập nhật một bảng, vì kế thừa ghi vào cả bảng cha lẫn bảng con. Với nhiều thay đổi mỗi giây thì nên chọn association 1-1.

---

### Đề 2 - Câu 25 [XPath & General]

**Câu hỏi:** You need a list of all products which have been ordered once by the customer or on the ‘Favorites’ list of that customer. The following XPath is used in a microflow to retrieve that list from the database. How can you optimize this XPath to increase the performance of the app?

- ✅ **A.** By executing the comparison on the Customer object in a subquery, [Product [AdvancedModule. OrderLine_Product/AdvancedModule OrderLine/ AdvancedModule.Orderline_Order/AdvancedModule.order [AdvancedModule.Customer = SCustomer or AdvancedModule.Customer_ProductFavorite = $Customer])
- ⚪ B. By executing the comparison on the Customer object in a subquery, the or statement can be changed to an and statement. which is better performing. //Product [AdvancedModule. OrderLine_Product/AdvancedModule Ordertine/ AdvancedModule.Ordertine Order [AdvancedModule.Order_Customer = SCustomer and AdvancedModule.Customer_ProductFavorite = $Customer)
- ⚪ C. By retrieving all Products from the database without a constraint. iterating through this list ProductList and retrieving the Customers who have the IteratorProduct on their favorite list and have ordered it. Check if this CustomerList contains the affected Customer, If itis 2 part of the CustomerList. then add the product on the ProductFinal list. f not. continue with the next IteratorProduct.
- ⚪ D. By retrieving a list of already ordered products Productlist_Ordered and a list of favorite products ProductList_ Favorite separately, and joining them into a single list ProductList_Total. The ProductList_Ordered is achieved via the Retrieve from database activity with XPath: IADV20.0rderLine_Product/ADV20.0rderLine/ADV20.Ordertine_Order/ ADV20.0rder/ADV20.0rder_Customer= SCustomer] . The ProductList_Favorite is achieved via the Retrieve from database activity with XPath {ADV20.Customer_ProductFavorite = SCustomer). The ProductList_Total is obtained using the Union List operation applied to the ProductList_ Ordered and ProductList Favorite lists.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Gom điều kiện về Customer vào một subquery trên đường association giúp database xử lý trong một câu query, thay vì nhiều nhánh truy vấn riêng.

---

### Đề 2 - Câu 26 [XPath & General]

**Câu hỏi:** You need a list of all products which are not on the current Order. The following XPath is used in a microflow to retrieve that list from the database. How can you optimize this XPath to increase the performance of the app?
//Product[not(AdvancedModule Orderline Product/AdvancedModule Ordertine /AdvancedModule OrderLine Order SOrder)]

- ✅ **A.** By adding a sub-query in your XPath to check the id of the Order object
//Product
[not(AdvancedModule OrderLine Product/AdvancedModule OrderLine/AdvancedModule OrderLine Order/AdvancedModule [ id=$Order])]
- ⚪ B. By retrieving the list of all products ProductList All retrieving the list of OrderLines of the affected Order, iterating over the Orderline list, retrieving the Product of each OrderLine, and removing it from the initial list ProductList All
- ⚪ C. By changing the XPath by using the != comparison instead of the not function:
//Product [AdvancedModule.OrderLine_Product/AdvancedModule.OrderLine/AdvancedModule.OrderLine_Order != $Order]
- ⚪ D. By separately retrieving two lists ProductList All and ProductList Referenced from database, and subtracting one from
the other to the ProductList_Final
Where the ProductList All is a list of all Products retrieved from
the database without constraints.
The ProductList Referenced is obtained by retrieving from
database the list of all referenced Products associated to the OrderLines of the affected Order by
XPath(AdvancedModule.OrderLine Product/AdvancedModule.Or derline/AdvancedModule.OrderLine Order = $Order]
ProductList Final is achieved by applying the Subtract list operation to subtract the ProductList Referenced from ProductList All

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): So sánh theo id của Order trong sub-query ([id = $Order]) giúp database dùng khóa chính để lọc, hiệu quả hơn so sánh association trực tiếp trong not().

---

### Đề 2 - Câu 27 [XPath & General]

**Câu hỏi:** You want to constrain a list of objects retrieved from the database using an XPath where the ReleaseDate is more than a year from now. Which XPath expression should you use to check this?

- ⚪ A. [ReleaseDate >='%YearLength%']
- ⚪ B. [ReleaseDate >= addYears([%CurrentDateTime%], 1)]
- ⚪ C. [ReleaseDate >='[% YearLength%]']
- ✅ **D.** [ReleaseDate >= ('[%CurrentDateTime%] + [%YearLength%]')]

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Thời điểm sau một năm tính bằng '[%CurrentDateTime%] + [%YearLength%]' (token cộng thời gian trong XPath). Hàm addYears không dùng được trong XPath constraint.

---

### Đề 2 - Câu 28 [XPath & General]

**Câu hỏi:** To be admitted to the Solution Architecture workshop, trainees should have either an Intermediate or Advanced certificate. You have created an enumeration with values ‘RAD’, ‘INT” and ‘ADV’ of String data type, representing Rapid. Intermediate and Advanced certificates respectively. Each Trainee has a Badge attribute of the String data type. which stores the latest attained certificate type, You created a page with a List view, where the Data source is set to Training.Trainee by XPath. How should you write an XPath constraint to limit admissions of trainees only to the Intermediate and Advanced certificates?

- ⚪ A. [ Badge = (INT or ADV) ]
- ⚪ B. ..
- ⚪ C. not[Badge = 'RAD']
- ✅ **D.** [ Badge = ‘INT’ or Badge = ‘ADV’ ]

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Badge là String nên so sánh với giá trị trong nháy và nối bằng 'or': [Badge = 'INT' or Badge = 'ADV'].

---

### Đề 2 - Câu 29 [Microflows]

**Câu hỏi:** In Mendix, commits in loop should be avoided. What is the best way to improve this microflow?

- ⚪ A. Create a list Orders ToBeCommitted before the loop. Add changed objects within the loop to Orders ToBeCommitted. Commit the OrdersToBeCommitted list after the loop.
- ⚪ B. Add a Commit activity after the loop to commit the OrderList list.
- ✅ **C.** Uncheck Commit within the Change Object activity. Add a Commit activity, and nothing else, after the loop to commit the OrderList list.
- ⚪ D. Create a list OrdersToBeCommitted before the loop. Add changed objects within the loop to Orders ToBeCommitted. Commit the OrderList list after the loop.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Bỏ chọn Commit trong Change Object trong vòng lặp, sau vòng lặp commit cả OrderList một lần. Làm vậy chỉ tốn một lần ghi theo lô thay vì commit từng object.

---

### Đề 2 - Câu 30 [XPath & General]

**Câu hỏi:** We have five trainees: two without registrations. one with a discount of 30, and two with discounts of 50. How many trainee objects will the following XPath retuin? [Training.Registration_Trainee/Trainin.Registration/Discount != 30]

- ⚪ A. 4 trainee
- ✅ **B.** 2 trainee
- ⚪ C. 1 trainee
- ⚪ D. 5 trainee

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): '!= 30' qua association chỉ đúng khi tồn tại một registration có discount khác 30. Trainee không có registration và trainee có discount 30 bị loại, còn 2 trainee có discount 50.

---

### Đề 2 - Câu 31 [Security]

**Câu hỏi:** Imagine that in the Domain Model of your app, there is a cascading delete configured between two entities. What happens if you are not allowed to delete all of the objects you've planned to delete?

- ✅ **A.** All the objects will be deleted besides the conflicted ones
- ⚪ B. An error message will be shown in the Console log
- ⚪ C. All the objects will remain unaffected.
- ⚪ D. The cascading delete will e rolled-back

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Theo file gốc (ô tô màu vàng): các object được phép xóa vẫn bị xóa, chỉ object không có quyền thì được giữ lại. ⚠ Tài liệu chính thức không mô tả trường hợp này, nên giảng viên cần tự kiểm chứng.

---

### Đề 2 - Câu 32 [Microflows]

**Câu hỏi:** When is it advised to apply custom error handling?

- ✅ **A.** With Rest integration activities
- ⚪ B. When committing a list with more than 10 objects
- ⚪ C. When creating an object with a population of members
- ⚪ D. Before commit event handlers

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Tích hợp REST phụ thuộc hệ thống ngoài nên có thể lỗi bất kỳ lúc nào. Custom error handling giúp bắt lỗi, log và thông báo thay vì làm hỏng cả transaction.

---

### Đề 2 - Câu 33 [UX & Logging]

**Câu hỏi:** How does Sass help with styling?

- ⚪ A. It is a more capable styling language than CSS.
- ⚪ B. It simplifies security rules which hide UI elements.
- ✅ **C.** It processes CSS to avoid repetitive work.
- ⚪ D. It directly formats HTML content for better UX.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Sass là bộ tiền xử lý CSS: có biến, mixin, nesting, import… giúp tránh lặp code, rồi được biên dịch ra CSS thường.

---

### Đề 2 - Câu 34 [Microflows]

**Câu hỏi:** Which variable is predefined with error information within a microflow?

- ⚪ A. System.EventStatus
- ⚪ B. $CurrentSession
- ✅ **C.** $latestError
- ⚪ D. System.EventStatus

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Trong error handler, biến $latestError (kiểu System.Error) có sẵn và chứa thông tin lỗi (message, stacktrace). Với lỗi web service còn có $latestSoapFault, với REST có $latestHttpResponse.

---

### Đề 2 - Câu 35 [UX & Logging]

**Câu hỏi:** Customers can receive up to 3 samples with their order out of 5 options. What would be the most intuitive widget to use for their selection?

- ⚪ A. The enumeration widget
- ✅ **B.** The check box widget
- ⚪ C. The radio buttons widget
- ⚪ D. The drop-down widget

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Chọn tối đa 3 trong 5 mẫu là chọn nhiều, nên dùng check box (mỗi lựa chọn một ô). Radio button và drop-down chỉ chọn được một.

---

### Đề 2 - Câu 36 [XPath & General]

**Câu hỏi:** On the Product_Overview page, you have placed the List view widget and configured the Data source as the entity Production.Product by XPath [Production.ProductReview_Product/ProductReview]. What data do you expect to be listed on this page once previewing the app?

- ⚪ A. A list of all product reviews
- ✅ **B.** A list of products associated to product review
- ⚪ C. A list of all products
- ⚪ D. A list of products with a review

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Ràng buộc [ProductReview_Product/ProductReview] chỉ giữ Product có ít nhất một ProductReview liên kết, nên trang liệt kê các product có review.

---

### Đề 2 - Câu 37 [UX & Logging]

**Câu hỏi:** You have a microflow that calls a REST service. You update that microflow with new activities and it stops working. Which Log Node should you use to investigate?

- ⚪ A. REST Consume
- ⚪ B. REST Publish
- ⚪ C. ConnectionBus Retrieve
- ✅ **D.** MicroflowEngine

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Lỗi xuất hiện sau khi sửa các activity trong microflow, nên đặt log node MicroflowEngine lên Debug/Trace để theo dõi microflow chạy từng bước.

---

### Đề 2 - Câu 38 [Microflows]

**Câu hỏi:** What is the behavior of the list operation Head?

- ⚪ A. The first object on the list will be removed. and all other objects returned.
- ✅ **B.** It returns the first object of the sorted list.
- ⚪ C. All objects will be removed from the list except the last one which will be retuned.
- ⚪ D. It returns all objects of a sorted list except the last one.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): List operation Head trả về object đầu tiên của list (theo thứ tự sắp xếp nếu có), kết quả là một object chứ không phải list.

---

### Đề 2 - Câu 39 [Domain Model]

**Câu hỏi:** You want to use a List view to display all products as well as their specialized attributes. Is this possible?

- ⚪ A. No. but it is possible with a data grid.
- ✅ **B.** Yes, the widget will allow you to create a specific template for each specialization.
- ⚪ C. No, you will only be able to display the general attributes.
- ⚪ D. Yes, but you will have to set visibilities to avoid irrelevant attributes from being shown.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): List view hỗ trợ template riêng cho từng specialization: khi data source là entity cha, có thể thêm template cho Book, Music… để hiển thị thuộc tính riêng của từng loại.

---

### Đề 2 - Câu 40 [UX & Logging]

**Câu hỏi:** What is one of the 4 main phases of the UX project process?

- ✅ **A.** User Journey
- ⚪ B. Mock-up
- ⚪ C. Realize
- ⚪ D. Feedback

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Theo file gốc (ô tô màu vàng): User Journey là một trong các giai đoạn chính của quy trình UX, giúp hiểu hành trình và nhu cầu user trước khi thiết kế.

---

### Đề 2 - Câu 41 [UX & Logging]

**Câu hỏi:** Throughout an entire app, you want to display the values of DateTime attributes for users with the language English, United States (en_US) as M-dd-yyy (4/23/2018), and for users with the language Dutch, Netherlands (nl_NL) as dd-M-yyy (23-4-2018), What is the best way to achieve this?

- ⚪ A. This isn’t possible: each language has a predefined fixed default date and time format.
- ⚪ B. Set the date format in the system settings.
- ⚪ C. Set the date format in the text widget captions per language.
- ✅ **D.** Set the date format in the language settings.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Định dạng ngày giờ được cấu hình theo từng ngôn ngữ trong App Settings > Languages, nên áp dụng cho toàn app tùy ngôn ngữ của user.

---

### Đề 2 - Câu 42 [Microflows]

**Câu hỏi:** In addition to a Published REST Service, what other Mendix document type is required to set up a POST method?

- ⚪ A. Published web service
- ⚪ B. Data set
- ⚪ C. Java action
- ✅ **D.** Import mapping

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Phương thức POST nhận JSON/XML trong body, nên cần Import mapping để chuyển payload thành object Mendix.

---

### Đề 2 - Câu 43 [Microflows]

**Câu hỏi:** When handling errors, how should system-triggered and user-triggered microflows be handled?

- ⚪ A. Both should only be shown in a user visible message when Trace debugging is implemented.
- ✅ **B.** System-triggered microflow errors should be logged and user-triggered microflow errors should be shown in a user visible message
- ⚪ C. System-triggered microflows should have a Custom with Rollback error handling implemented and user-triggered microflows should have Custom without Rollback.
- ⚪ D. System-triggered microflow errors don't require error handling but user-triggered microflows do.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Microflow do hệ thống chạy (scheduled event, after startup…) không có user nhìn thấy, nên lỗi cần được log. Microflow do user bấm nên hiện thông báo dễ hiểu cho user.

---

### Đề 2 - Câu 44 [Microflows]

**Câu hỏi:** You have a list of Order objects and you need the sum of their amounts. As seen below, you could do this with either a variable and loop, or with an aggregate list activity. Why is the aggregate list method the preferred best practice in this situation?

- ✅ **A.** The loop method has worse performance.
- ⚪ B. The loop method could cause dirty writes.
- ⚪ C. The aggregate list activity is easier to configure.
- ⚪ D. The aggregate list method is more readable.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Aggregate list sau retrieve được Mendix tối ưu thành một câu SUM chạy trên database. Vòng lặp phải tải mọi object vào bộ nhớ rồi cộng từng cái, nên chậm hơn.

---

### Đề 2 - Câu 45 [Security]

**Câu hỏi:** To ensure that the right information is shown on a page. you have different options when it comes to differences between security and usability. Which of the following statements is true?

- ⚪ A. Only what is secure will eventually be usable and accessible from the Mendix Client.
- ✅ **B.** Usability is not security. adding a conditional visibility on a page does not result in a secure app.
- ⚪ C. What is accessible from the Mendix client is by definition secure.
- ⚪ D. Usability is secunty, adding a conditional visibility on a page results in a secure app.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Usability khác security: conditional visibility chỉ ẩn trên giao diện, dữ liệu vẫn có thể lấy qua API. Bảo mật phải đặt ở entity access, page access và microflow access.

---

### Đề 2 - Câu 46 [Security]

**Câu hỏi:** Sometimes the module security matrix highlights cells in yellow Why is this?

- ✅ **A.** Yellow cells indicate microfiows that have module roles assigned to them but are never used in the client API
- ⚪ B. Yellow cells indicate microflows that have no module roles assigned to them, but the microflow is used in the client API
- ⚪ C. The yellow cells indicate that these microflows have a completed security configuration
- ⚪ D. Yellow cells indicate microflows that have a module role assigned that is not linked to a User Role.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Ô vàng trong security matrix cảnh báo microflow đã được gán module role nhưng không được dùng ở client (page, navigation…). Microflow như vậy bị lộ qua API mà không cần thiết, nên bỏ role.

---

### Đề 2 - Câu 47 [UX & Logging]

**Câu hỏi:** Which statement about building blocks is true?

- ⚪ A. A building block can be selected as a template when you create a new page.
- ⚪ B. A building block is a widget which can be downloaded from the Mendix Marketplace.
- ⚪ C. A building block is a page element which can be maintained on a single location, and all changes will be automatically applied to all locations where this building block is used.
- ✅ **D.** A building block is a collection of widgets styled with CSS classes in a way that suits a specific use case.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): ✎ Đã sửa so với file gốc. Tài liệu Mendix (Pages): building block là bộ widget đã tạo kiểu sẵn, xuất hiện trong toolbox để tái sử dụng. Mô tả 'sửa một chỗ, áp dụng mọi nơi' là của snippet, không phải building block.

---

### Đề 2 - Câu 48 [Domain Model]

**Câu hỏi:** What is the owner of an association?

- ✅ **A.** It is the entity from which the association is created.
- ⚪ B. It is the user that created the association.
- ⚪ C. It is the entity in which the association is stored,
- ⚪ D. It is the user that set the association,

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Owner của association là entity mà association được vẽ từ đó (phía 'parent' trong domain model). Phía owner là phía giữ và thay đổi tham chiếu, không phải một user.

---

### Đề 2 - Câu 49 [Domain Model]

**Câu hỏi:** You want every product to have an image. Which of the following statements is true?

- ✅ **A.** Using a specialization of the Image entity allows for a more specific security setup.
- ⚪ B. You can add new attributes to the Image entity.
- ⚪ C. The Image entity is a generalization of the Document entity.
- ⚪ D. It is impossible to create an association to the Image entity,

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Tạo entity riêng kế thừa System.Image (ví dụ ProductImage) cho phép đặt access rule riêng cho ảnh sản phẩm. Không sửa được System.Image; Image là specialization của FileDocument chứ không phải ngược lại.

---

### Đề 2 - Câu 50 [Microflows]

**Câu hỏi:** How can you ensure that a certain microflow is always called when a user logs in to an application?

- ⚪ A. Set this microflow as the After Startup microflow.
- ⚪ B. This is not possible. You must place a button on the homepage to be pressed manually by the user every time they log in.
- ✅ **C.** In the App Navigation, choose a microflow as the default home page.
- ⚪ D. Call this microflow from an After Commit Event Handler in the Administration.Account entity.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Đặt một microflow làm home page (default hoặc theo role) trong Navigation thì microflow đó chạy mỗi khi user đăng nhập. After Startup chỉ chạy một lần khi ứng dụng khởi động.

---

## Đề thi thử số 3

### Đề 3 - Câu 1 [UX & Logging]

**Câu hỏi:** The recommended method when setting the log node name of a custom log message is to:

- ⚪ A. Create a settings entity to maintain the log node names from the runtime.
- ⚪ B. Use string quotes around a caption Log node name
- ⚪ C. Use a snippet with a text widget containing a list of all custom log node names. Store this snippet in the general module as a resource.
- ✅ **D.** Use an enumeration to store all log node names as an enumeration value and use the expression getCaption ModuleName.EnumerationList.CustomLogNodeNamel to set the log node name.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Lưu tên log node trong enumeration và dùng getCaption(...) giúp tên thống nhất, tránh gõ sai chuỗi và dễ đổi ở một chỗ.

---

### Đề 3 - Câu 2 [Domain Model]

**Câu hỏi:** Given the following Domain model, how will objects of the Book entity be stored in the database?

- ✅ **A.** Some information will be stored in the Product table and some in the Book table.
- ⚪ B. All information will be stored in the general Product table.
- ⚪ C. All information will be stored in a specific Book table.
- ⚪ D. All information will be stored in a table for specializations.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Với kế thừa (generalization), thuộc tính chung lưu ở bảng Product, thuộc tính riêng của Book lưu ở bảng Book; hai bản ghi dùng chung một id.

---

### Đề 3 - Câu 3 [Domain Model]

**Câu hỏi:** When is it likely that an index will negatively impact perfomance?

- ⚪ A. When there are a lot of objects for the relevant entity
- ⚪ B. When an entity has many attributes
- ✅ **C.** When data is changed more often than it is read
- ⚪ D. When the entity exclusively has stored attributes

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Index tăng tốc đọc nhưng mỗi lần insert/update/delete database phải cập nhật thêm bảng index. Nếu dữ liệu thay đổi nhiều hơn được đọc thì chi phí ghi lớn hơn lợi ích tìm kiếm.

---

### Đề 3 - Câu 4 [Security]

**Câu hỏi:** When attempting to change the value of an object on a page. what will happen if the runtime identifies that you are not allowed to do this?

- ⚪ A. This will never happen. If you can't access the object you won't see it on the page.
- ✅ **B.** The change will not happen and an error message willbe shown in the client and the log.
- ⚪ C. The change will be saved in the memory.
- ⚪ D. The change will be saved to the database and then rolled-back.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Runtime luôn kiểm tra quyền khi client gửi thay đổi. Nếu không có quyền write, thay đổi bị từ chối và lỗi được hiển thị ở client và ghi log.

---

### Đề 3 - Câu 5 [XPath & General]

**Câu hỏi:** Which of these data sources is not supported in offine applications?

- ⚪ A. Listen to widget
- ✅ **B.** Microflow
- ⚪ C. Nanoflow
- ⚪ D. Context

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Ứng dụng offline-first chạy trên thiết bị, không gọi server được, nên data source Microflow không được hỗ trợ; dùng Nanoflow, Database (local), Context, Listen to widget.

---

### Đề 3 - Câu 6 [Microflows]

**Câu hỏi:** Rules have some limitations compared to sub-microflow. What is one of the limitations of a Rule? Rule cannot:

- ⚪ A. Have an object as an input parameter
- ✅ **B.** Interact with the client
- ⚪ C. Return a Boolean
- ⚪ D. have multiple End events

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Rule chỉ dùng trong Decision để trả về Boolean hoặc Enumeration và không được tương tác với client (không show page, không show message, không đóng page…).

---

### Đề 3 - Câu 7 [XPath & General]

**Câu hỏi:** A Customer should only be allowed to Read and Write their own Orders. Which XPath (if any) should be added to the r access rule in the domain model below?

- ⚪ A. [ADV20.Order_Customer/ADV20.Customer/ADV20.Customer_Account/Administration.Account/id = '{%CurrentUser%}]
- ⚪ B. [ADV20.Order_Customer/ADV20.Customers = '[%CurrentUser%]']
- ⚪ C. Since the Order is linked to Customer. there is no need to add an XPath constraint in the Access Rule for the user role Customer in the ‘Order entity. The data is not accessible to other users.
- ✅ **D.** [ADV20.Order_Customer/ADV20 Customer/ADV20.Customer_Account='[%CurrentUser%]']

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Order nối Customer, Customer nối Account. So sánh association Customer_Account trực tiếp với '[%CurrentUser%]' là đúng cú pháp và hiệu quả, không cần đi tới /id.

---

### Đề 3 - Câu 8 [Domain Model]

**Câu hỏi:** What type of association has the biggest data payload?

- ⚪ A. An association with an information entity
- ⚪ B. A reference “both” association (1-1)
- ⚪ C. A reference association (1-*)
- ✅ **D.** A reference set (*-*)

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Reference set (*-*) có thể chứa rất nhiều tham chiếu trên mỗi object, nên khi lấy object kèm association thì dữ liệu tải về lớn nhất.

---

### Đề 3 - Câu 9 [UX & Logging]

**Câu hỏi:** You want to show a text as Heading 2. However, on this particular page you want to remove the default spacing at the bottom. What is the most efficient way to do this?

- ✅ **A.** Go to the properties of the text widget and set the the 'Spacing Bottom' property in Appearance to 'Outer None'.
- ⚪ B. Add the class remove-bottomspacing to the class property of the text widget.
- ⚪ C. Add CSS to the style property of the text widget.
- ⚪ D. Create your own class removing the spacing and add this class to the class property of the text widget.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Atlas UI có sẵn thuộc tính Spacing trong mục Appearance của widget. Chọn Spacing Bottom = Outer None là cách nhanh nhất, không cần viết CSS hay class.

---

### Đề 3 - Câu 10 [Microflows]

**Câu hỏi:** Microflow A iterates over a list of committed OrderLines, retrieves by association the Product being ordered, then adjusts the Product Stock amount accordingly. Microflow B retrieves the whole Product list of the Order from the database, then iterates over the Product list and adjusts the Product Stock amount accordingly. Which solution would be the best approach and why?

- ⚪ A. Microflow B. because the retrieve in microflow A might result in multiple database retrieves even when retrieved by association.
- ⚪ B. Microflow B, because a database retrieve in this case is faster than a by association retrieve.
- ✅ **C.** Microflow A, because the by association retrieve in microflow A retrieves from memory and is much faster than a database retrieve.
- ⚪ D. Microflow A, because there is no difference in performance between the two and a by association retrieve is easier to maintain from a developer perspective.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Theo file gốc là Microflow A (ô tô màu vàng). ⚠ Chưa xác nhận được: tài liệu Mendix không nói retrieve by association luôn lấy từ bộ nhớ. Nếu Product chưa có trong bộ nhớ thì mỗi vòng lặp vẫn có thể là một query.

---

### Đề 3 - Câu 11 [XPath & General]

**Câu hỏi:** Which search function should you use to find XPath expressions that might be affecting your performance? Select the correct keyboard shortcut.

- ⚪ A. Ctrl + Space
- ⚪ B. Ctrl + F
- ⚪ C. Shift + F
- ✅ **D.** Ctrl + Shift + F

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Ctrl+Shift+F mở Find Advanced trong Studio Pro, cho phép tìm theo loại (ví dụ mọi XPath) trên toàn app để rà soát hiệu năng.

---

### Đề 3 - Câu 12 [XPath & General]

**Câu hỏi:** You would like to search for trainees in the database using their names. To speed up the search, where should you add an index?

- ⚪ A. In a widget downloaded from the Marketplace
- ✅ **B.** In the entity properties in the Domain model
- ⚪ C. In a microflow by adding a Create index activity and returning the indexed list
- ⚪ D. In the ‘Search on’ settings of the List view

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Index được khai báo trong properties của entity ở Domain Model (tab Indexes), chọn thuộc tính Name để tìm kiếm nhanh hơn.

---

### Đề 3 - Câu 13 [Domain Model]

**Câu hỏi:** Where are file or image of mendix application stored by default

- ⚪ A. On the dedicated Amazon file server
- ⚪ B. On the local hard disk of the user
- ✅ **C.** On the file server located on the application server
- ⚪ D. As binary in the content of an attribute

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Mặc định file và ảnh (FileDocument, Image) không lưu trong database mà lưu trên file storage của application server; database chỉ giữ thông tin tham chiếu tới file.

---

### Đề 3 - Câu 14 [UX & Logging]

**Câu hỏi:** What type of menu is most likely to go well with Hick's law?

- ✅ **A.** A Simple Menu Bar
- ⚪ B. A Navigation Tree
- ⚪ C. A Default Menu Bar
- ⚪ D. A Custom Menu

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Hick's law: càng nhiều lựa chọn thì user càng mất thời gian quyết định. Simple menu bar ít mục, phẳng, nên phù hợp nhất.

---

### Đề 3 - Câu 15 [UX & Logging]

**Câu hỏi:** Customers can choose their desired delivery method when submitting an order in an app. This is dependent on their address, and you only want to display the delivery options that are available to their location, What is the most efficient way to achieve this?

- ⚪ A. Use an on-leave microflow to set the conditional visibility of the relevant page elements
- ⚪ B. Use an on-leave microflow to set the conditional editability of the relevant page elements.
- ✅ **C.** Use an on-change microflow to set the conditional visibility of the relevant page elements.
- ⚪ D. Use an on-change microflow to set the conditional editabilty of the relevant page elements.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Khi địa chỉ thay đổi, on-change microflow (hoặc nanoflow) tính lại các tùy chọn giao hàng phù hợp và điều khiển conditional visibility, nên chỉ những lựa chọn khả dụng được hiển thị ngay.

---

### Đề 3 - Câu 16 [Microflows]

**Câu hỏi:** When is custom error handling most appropriate within a microflow?

- ⚪ A. When calling other microflows
- ✅ **B.** When Interacting with external systems
- ⚪ C. When using a JAVA action activity
- ⚪ D. When using multiple decision elements

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Gọi hệ thống bên ngoài (REST, SOAP, email…) dễ lỗi ngoài tầm kiểm soát (timeout, mất kết nối), nên cần custom error handling để log và xử lý có kiểm soát.

---

### Đề 3 - Câu 17 [Security]

**Câu hỏi:** A user with the role Employee adds a new OrderLine to an Order and selects a Product After Product selection the Employee sets a Discount of 10% What will happen when the related microflow is triggered as an on-change microflow?

- ⚪ A. The OrderLine LineValue will not be changed and the user will not be informed.
- ⚪ B. The Employee will get an error message, because the Employee role doesn't have write access to the attribute LineValue
- ✅ **C.** The OrderLine LineValue will be changed to 9.00 and the value is returned to the client
- ⚪ D. The Orderline LineValue will be changed to 9.00, though it cannot be passed to the client because the Employee role doesn't have write access to the attribute LineValue

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Microflow mặc định chạy không áp dụng entity access, nên vẫn đổi được LineValue thành 9.00 và trả object về client để hiển thị, dù role Employee không có quyền write trên thuộc tính đó.

---

### Đề 3 - Câu 18 [Microflows]

**Câu hỏi:** When an Order is submitted, the Order Number (String) is created in a sub-microflow. What is the best way to build this sub-microflow according to Mendix best practices?

- ✅ **A.** Build the OrderNumber in a new string variable and pass it back to the main microflow.
- ⚪ B. Build the OrderNumber within the End event and pass it back to the main microflow.
- ⚪ C. Build the OrderNumber in a new string variable. then change and refresh the Order object within the sub-microflow.
- ⚪ D. Build the OrderNumber in a new string variable, then change and commit the Order object within the sub-microflow.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Sub-microflow nên chỉ làm một việc: tạo chuỗi OrderNumber và trả về. Việc change và commit Order để ở microflow chính cho dễ đọc, dễ tái sử dụng và tránh commit rải rác.

---

### Đề 3 - Câu 19 [Domain Model]

**Câu hỏi:** What is an index?

- ⚪ A. A table that contains the results of a query
- ⚪ B. The unique identifier of an object
- ✅ **C.** An extra sorted table with only the record IDs and the selected attribute
- ⚪ D. A sorted duplicate of an entity table

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Index là một bảng phụ được sắp xếp, chỉ chứa giá trị thuộc tính được index và id bản ghi, giúp database tìm nhanh mà không cần quét cả bảng.

---

### Đề 3 - Câu 20 [Domain Model]

**Câu hỏi:** You want the address of a customer to be moved from the Customer entity to a newly created Customer Address entity. When should you remove the Address attribute from the Customer entity?

- ⚪ A. After a predefined transfer period
- ⚪ B. You should try to avoid removing it
- ✅ **C.** In the next deploy after you have added the CustomerAddress entity
- ⚪ D. In the deploy that you add the Customer Address entity

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Phải giữ thuộc tính Address cũ trong lần deploy đầu để chạy migration chuyển dữ liệu sang CustomerAddress. Xóa ngay sẽ mất dữ liệu; xóa ở lần deploy sau khi dữ liệu đã chuyển xong là an toàn.

---

### Đề 3 - Câu 21 [UX & Logging]

**Câu hỏi:** What part of a page remains if you navigate between two pages with the same layout?

- ⚪ A. Mendix is optimized to change as little as possible
- ✅ **B.** Everything that is not in a placeholder
- ⚪ C. The menu bar and footer
- ⚪ D. Nothing, it's a different page with different content

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Khi chuyển giữa hai page cùng layout, Mendix chỉ thay nội dung trong placeholder; phần ngoài placeholder (header, menu, footer…) giữ nguyên.

---

### Đề 3 - Câu 22 [XPath & General]

**Câu hỏi:** You need to write a query to retrieve all registrations associated with trainees who bought vouchers in the EMEA region and where the voucher was not used. Which of the following XPath expressions is correct?

- ⚪ A. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA'] [VoucherUsed = false ]]
- ✅ **B.** [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed = false()]]
- ⚪ C. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed = false ]]
- ⚪ D. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed != true ]]

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Hai điều kiện cùng áp lên một object nên viết chung trong một ngoặc với 'and'. Giá trị Boolean trong XPath phải viết là false() (có ngoặc).

---

### Đề 3 - Câu 23 [XPath & General]

**Câu hỏi:** Mendix Academy needs to retrieve all trainees with a valid RAD certificate from their customer database. Luckily, all certificates are stored in the String attribute CertificatelD and have the prefix ‘RAD’. You build a Trainee_Overview page where you add a List view with a data source Trainee by XPath. Which XPath should you specify when retrieving the Trainee entity?

- ✅ **A.** [starts-with(CertificatelD, 'RAD')]
- ⚪ B. [Trainee.CertificateID[starts-with('RAD')]]
- ⚪ C. [starts-with(Trainee.CertificatelD, RAD)]
- ⚪ D. [CertificatelD != empty and starts-with('RAD')]

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Cú pháp đúng là starts-with(attribute, 'chuỗi') đặt trong ngoặc vuông, attribute viết trực tiếp (không kèm tên entity), chuỗi đặt trong nháy đơn.

---

### Đề 3 - Câu 24 [Security]

**Câu hỏi:** In an app consisting of two modules, each of which has two module roles, what is the minimal number of module roles that can be linked to a user role defined in the app security?

- ⚪ A. Four, indicating that a user role is linked to each module role in both modules
- ⚪ B. None, indicating that a user role does not have to be linked to a module role in each available module.
- ⚪ C. Two, indicating that a user role is linked to exactly one module role in each module
- ✅ **D.** One, indicating that a user role is linked to at least one module role in at least one of the available modules

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Một user role chỉ cần gắn tối thiểu 1 module role (ở ít nhất một module). Không bắt buộc gắn module role ở mọi module.

---

### Đề 3 - Câu 25 [Microflows]

**Câu hỏi:** In a sub-microflow, you want to create a string based on a DateTime parameter. The format of the string should look like this: 'Monday 23 April 2021'. Which date manipulation should you use to accomplish this?

- ✅ **A.** Create a String Variable and format the date to a string by using this expression: formatDateTime($DateTime,’EEEE ddd MMMM yyyy’)
- ⚪ B. Create a String Variable and format the date to a string by using this expression: formatDateTime($DateTime,’EE DD MM YYYY)
- ⚪ C. Create a String Variable and parse the date to a string by using this expression: parseDateTime($DateTime. 'EEE ddd MMMM yyyy’)
- ⚪ D. Create a Date Variable and format the date to a string by using this expression: formatDateTime($DateTime,' EEE ddd MMMM yyyy')

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): formatDateTime chuyển DateTime thành String. Pattern EEEE cho tên thứ đầy đủ (Monday), d là ngày, MMMM là tên tháng đầy đủ (April), yyyy là năm. parseDateTime làm ngược lại (String sang DateTime).

---

### Đề 3 - Câu 26 [UX & Logging]

**Câu hỏi:** When a Customer marks a Product as favorite, the heart empty icon is replaced by the heart icon. This is achieved by two separated link buttons, with icon set and an empty caption. By applying conditional visibility either the heart or heart empty icon is displayed. The heart icon also has an orange color, instead of the default link button color style. Which out-of-the-box class can be used to achieve this?

- ⚪ A. btn-warning
- ✅ **B.** text-warning
- ⚪ C. text-orange
- ⚪ D. text-color: #f99b1d:

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): ✎ Đã sửa so với file gốc. Tài liệu Mendix (Implement Classes): Atlas có sẵn helper class text-warning (màu warning của theme, mặc định là cam). 'text-color: #f99b1d' là CSS chứ không phải class.

---

### Đề 3 - Câu 27 [Microflows]

**Câu hỏi:** What will happen when there is no error handling implemented and Mendix is not able to finish a microflow transaction successfully?

- ⚪ A. Nothing
- ✅ **B.** The transaction is stopped and by default Mend will show this message in the user interface: ‘Something went wrong. Please contact your administrator'
- ⚪ C. The transaction is stopped and Mendix will show a default error message in the user interface.
- ⚪ D. The transaction will be finished and the user won't see a message in the user interface.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Không có error handling thì Mendix rollback transaction và client hiển thị thông báo mặc định kiểu 'An error occurred, please contact your system administrator'; chi tiết lỗi ghi vào log.

---

### Đề 3 - Câu 28 [UX & Logging]

**Câu hỏi:** What does the UI designer focus on?

- ✅ **A.** The presentation of the product
- ⚪ B. Mapping out the user's journey
- ⚪ C. The user's goals and desires
- ⚪ D. How it feels to use the product

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): UI designer tập trung vào phần trình bày: bố cục, màu sắc, typography, thành phần giao diện. Mục tiêu, cảm nhận và hành trình user thuộc về UX.

---

### Đề 3 - Câu 29 [Domain Model]

**Câu hỏi:** In the properties of an entity, what does checking the system member 'owner' do?

- ⚪ A. The object ID of the referenced Account object is stored as the owner of the object when it is created.
- ⚪ B. Objects of this entity are the owner of all associations from and towards this entity.
- ✅ **C.** The object ID of the logged-in user who creates the object is stored as the owner of the object.
- ⚪ D. The object ID of the logged-in user who retrieves the object from the database will be stored in the object for future reference.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Bật system member 'owner' thì khi tạo object, Mendix tự lưu tham chiếu tới Account của user đang đăng nhập vào System.owner. Hay dùng cho XPath như [System.owner='[%CurrentUser%]'].

---

### Đề 3 - Câu 30 [UX & Logging]

**Câu hỏi:** Which of the following log messages follows the best practices for a Warning log message?

- ⚪ A. “User language has not been set yet.”
- ✅ **B.** “REST service has returned result: 404 Not Found.”
- ⚪ C. “Unknown user input '129q', unable to process value.”
- ⚪ D. “Contacting REST service.”

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Theo file gốc là 'REST service has returned result: 404 Not Found.'. ⚠ Nên xem lại: tài liệu Mendix định nghĩa Warning là có điều bất thường nhưng ứng dụng vẫn chạy, còn Error là không thực hiện được một chức năng. Lỗi 404 có thể được xếp vào Error; 'User language has not been set yet.' cũng là ứng viên cho Warning.

---

### Đề 3 - Câu 31 [Security]

**Câu hỏi:** What does entity access affect?

- ✅ **A.** Which actions a user can execute
- ⚪ B. What a demo user can see on a page
- ⚪ C. Which pages a user can see
- ⚪ D. Which set of data a user can manipulate

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Theo file gốc là 'Which actions a user can execute'. ⚠ Nên xem lại: tài liệu Mendix nói access rule của entity quy định user được làm gì với các object của entity (create, read, write, delete, giới hạn bằng XPath). Cách diễn đạt này gần với 'Which set of data a user can manipulate' hơn.

---

### Đề 3 - Câu 32 [XPath & General]

**Câu hỏi:** Given this Domain Model, which of the following XPath s would you choose to retrieve the Orders of the currently logged-in customer?

- ⚪ A. [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account/Name = $currentUser/Name]
- ⚪ B. [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account/Administration.Account/id = ‘[%CurrentUsers%]']
- ✅ **C.** [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account='[%CurrentUser%]']
- ⚪ D. [AdvancedModule.Order_Customer='[%CurrentUser%]']

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Đi Order, qua Customer, tới Customer_Account rồi so sánh với '[%CurrentUser%]'. Đây là cách chuẩn và hiệu quả để lấy Order của customer đang đăng nhập.

---

### Đề 3 - Câu 33 [XPath & General]

**Câu hỏi:** You would like to replace an XPath that utes the logical 'and' operator with a microfiow using. two Retrieves and a List operation. Which of the following List operations should you use?

- ✅ **A.** Intersert
- ⚪ B. Union
- ⚪ C. Subtract
- ⚪ D. Find

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Toán tử 'and' nghĩa là object phải thỏa cả hai điều kiện, tức là phần giao của hai list, nên dùng list operation Intersect.

---

### Đề 3 - Câu 34 [Security]

**Câu hỏi:** Which of the three buttons New, Edit, and Delete on the page Order Overview will be visible to the user if an entity access rule specifies that the user can create, delete, read and write Orders?

- ⚪ A. Just the New and Delete buttons
- ⚪ B. No buttons will be visible
- ✅ **C.** New Edit and Delete buttons
- ⚪ D. Just the Edit button

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Entity access cho phép create, delete, read và write Order thì cả ba nút New, Edit, Delete đều hiển thị, vì Mendix ẩn nút dựa trên quyền entity.

---

### Đề 3 - Câu 35 [Microflows]

**Câu hỏi:** When an order is submitted, the Order and OrderLines will be committed to the database. Afterwards , the Customer should receive an email with the order details. Asa result. the Mendix developer adds the sub-microflow SUB_Order_SendCustomerEmail to the submit microflow. The developer wants to catch a possible error when sending an email so that the Order and OrderLines will definitely be committed. What type of error handling should the developer set on the C all microflow activity which calls the microflow SUB_Order_SendCustomerEmail?

- ⚪ A. Continue
- ⚪ B. Rollback
- ⚪ C. Custom with Rollback
- ✅ **D.** Custom without rollback

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Order và OrderLine đã commit trước khi gửi email. Đặt 'Custom without rollback' trên lời gọi SUB_Order_SendCustomerEmail để khi gửi mail lỗi thì dữ liệu đã commit không bị rollback, đồng thời vẫn bắt được lỗi để log.

---

### Đề 3 - Câu 36 [UX & Logging]

**Câu hỏi:** What is the relationship between UX and UI?

- ⚪ A. UX is a sub-category of UI
- ⚪ B. UX and UI are mostly unrelated
- ⚪ C. UX and UI are at a core level the same thing
- ✅ **D.** Ul can be used to improve UX

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): UX là toàn bộ trải nghiệm của user, UI là phần giao diện. UI tốt là một phương tiện để cải thiện UX.

---

### Đề 3 - Câu 37 [UX & Logging]

**Câu hỏi:** The width of a layout grid can be set to Full width or Fixed width. What is the difference?

- ✅ **A.** When set to Fixed width, the total column width of this layout will be exactly the width in pixels as specified in the style sheet. Full width will be the full available width of the page.
- ⚪ B. When set to Fixed width, the total column width of this layout will be exactly the width in pixels as specified in the style sheet. Full width will be the full width of the client.
- ⚪ C. When set to Fixed width, the total column width of this layout will be exactly 960 pixels centered in the page. Full width will be the full available width of the enclosing container.
- ⚪ D. When set to Fixed width, the input widgets width will be exactly the width in pixels as specified in the style sheet. When set to Full width the input widgets width will be the full width of the client.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Fixed width giới hạn tổng chiều rộng cột theo giá trị pixel trong stylesheet (container cố định). Full width chiếm toàn bộ chiều rộng khả dụng của trang.

---

### Đề 3 - Câu 38 [Microflows]

**Câu hỏi:** When handling an error, what is the most appropriate use of a Continue element?

- ⚪ A. Within a “while” loop
- ⚪ B. Within a “for each” loop
- ⚪ C. After completing a loop
- ✅ **D.** When no rollback is needed

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Theo file gốc là 'When no rollback is needed'. ⚠ Chưa chắc: tài liệu Mendix nói Continue chỉ dùng được trên lời gọi microflow hoặc trong vòng lặp, và các thay đổi trong lần lặp hoặc lời gọi bị lỗi VẪN bị rollback. Đáp án hợp lý hơn có thể là dùng trong vòng lặp 'for each' để bỏ qua phần tử lỗi.

---

### Đề 3 - Câu 39 [Security]

**Câu hỏi:** How do you handle access to a sub-microflow in relation to the parent microflow?

- ⚪ A. If you set the access to a sub-microflow, it overwrites access defined by the parent microflow.
- ⚪ B. When creating 3 sub-microfiow, you can choose whether you want to inherit the access rules from the parent microflow or to set it up independently.
- ✅ **C.** Access to a sub-microflow does not need to be set because itis handled by the parent microflow.
- ⚪ D. Access to a sub-microflow needs to be set up independently of the access to the parent microflow.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Sub-microflow được gọi từ microflow cha chạy với quyền của cha nên không cần gán module role. Gán role còn làm lộ sub-microflow ra client API.

---

### Đề 3 - Câu 40 [Security]

**Câu hỏi:** When specifying entity access rules. what does “Limited access” mean?

- ⚪ A. The conditional visibility on a page is set to limit the access for the given user.
- ✅ **B.** At least one member is not allowed to be accessed by the user with a given module role.
- ⚪ C. A user that is assigned multiple user roles is limited to view only data corresponding to the currently logged in user.
- ⚪ D. The user with a given module role has no access to the data set.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): ✎ Đã sửa so với file gốc. Tài liệu Mendix: 'Limited access' nghĩa là có ít nhất một ràng buộc hoặc một phần không được phép truy cập; 'No access' mới là không có quyền gì. Phương án đúng là có ít nhất một member user không được truy cập.

---

### Đề 3 - Câu 41 [Microflows]

**Câu hỏi:** Which of the following statements is true about the [reversed()] expression?

- ⚪ A. It can only be applied on *-* associations.
- ⚪ B. It can only be applied on 1-1 associations.
- ⚪ C. It can be applied to reverse a string attribute.
- ✅ **D.** It can only be applied on self-references.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Hàm reversed() dùng trong XPath trên association tự tham chiếu (self-reference) để đi theo chiều ngược lại của association, vì hai đầu cùng là một entity.

---

### Đề 3 - Câu 42 [Microflows]

**Câu hỏi:** Why is it a Mendix best practice to use Decisions instead of if-then-else expressions?

- ✅ **A.** It increases readability and documentation.
- ⚪ B. It is faster than typing expressions.
- ⚪ C. It allows faster duplication of existing processes.
- ⚪ D. Decisions have better multilingual support.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Decision hiển thị nhánh logic trực quan trên sơ đồ microflow, dễ đọc và tự mô tả hơn biểu thức if-then-else lồng nhau.

---

### Đề 3 - Câu 43 [XPath & General]

**Câu hỏi:** In a List view displaying a list of Orders, you want to add an XPath. The XPath should result in Orders where theOrderDate is within the past three years. Which XPath should you use?

- ✅ **A.** [OrderDate > ‘[%BeginOfCurrentDay%) - 3 * [%YearLength%]']
- ⚪ B. [OrderDate > '[3 * [%YearLength%]- %BeginOfCurrentDay%]']
- ⚪ C. [OrderDate < '[%BeginOfCurrentDay%] - 3 * [%YearLength%]']
- ⚪ D. [addYears(OrderDate, -3)]- [OrderDate < '[%BeginOfCurrentDay%]']

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Trong vòng 3 năm qua nghĩa là OrderDate lớn hơn (thời điểm đầu ngày hôm nay trừ 3 năm), viết bằng token: [%BeginOfCurrentDay%] - 3 * [%YearLength%].

---

### Đề 3 - Câu 44 [XPath & General]

**Câu hỏi:** In a List view displaying a list of Orders, you want to add an XPath. The result of the XPath should show Orders where the OrderDate is greater than the year 2000 and smaller than the current date and time. Which XPath should you use?

- ⚪ A. [formatDateTime([%CurrentDateTime%], 'yyyy') > 2000]
[OrderDate < '[%CurrentDateTime%]']
- ⚪ B. [year(OrderDate) 2000]
[OrderDate <1%CurrentDateTime%]]
- ✅ **C.** [year-from-dateTime(OrderDate) > 2000)
[OrderDate <1%CurrentDateTime%]]
- ⚪ D. [formatdatetime(year(OrderDate) > 2000])]
[OrderDate <1%CurrentDateTime%]]

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): year-from-dateTime() lấy năm từ thuộc tính DateTime trong XPath. Thêm ràng buộc thứ hai OrderDate < '[%CurrentDateTime%]'; hai ngoặc liền nhau tương đương 'and'.

---

### Đề 3 - Câu 45 [UX & Logging]

**Câu hỏi:** The default language of the app is English. United States (en_US) and Dutch. Netherlands (nl_NL) is an additional installed language. A user logs in and has the language Dutch. Netherlands (nl_NL) set as their user language. A button on a page doesn't have a caption but needs one. How should this be fixed?

- ⚪ A. Change the conditional visibility of the button so that the caption becomes visible for users with the Dutch language.
- ⚪ B. The caption must be set in the user language library and synced with the running app.
- ⚪ C. In both English and Dutch, the caption must be set in the correct
- ✅ **D.** The caption must be set in the Dutch language only.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): User dùng tiếng Hà Lan nên caption thiếu ở bản dịch nl_NL. Chỉ cần bổ sung caption tiếng Hà Lan (Language > nl_NL), bản tiếng Anh vẫn giữ nguyên.

---

### Đề 3 - Câu 46 [XPath & General]

**Câu hỏi:** You need to retrieve the UserRole Employee in a microflow. Which XPath constraint should you use in the Retrieve from Database activity?

- ⚪ A. [Description = 'Employee']
- ⚪ B. [ModelGUID= '[%UserRole_Employee%]']
- ⚪ C. [Name = 'Employee']
- ✅ **D.** [id='[%UserRole_Employee%]']

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Mỗi user role có token [%UserRole_<Tên>%] đại diện cho id của role đó, nên dùng [id='[%UserRole_Employee%]'] để lấy chính xác role, không phụ thuộc tên hay mô tả.

---

### Đề 3 - Câu 47 [Microflows]

**Câu hỏi:** In microflows, there are various security settings that can affect the creation of objects. Which of these statements about creating objects is true?

- ✅ **A.** A user can create an object with a microflow even if ‘Allow creating new ‘objects’ is disabled for them in the access rules of the entity.
- ⚪ B. A user will not be able to see any buttons that call microflows which create a particular object if ‘Allow creating new objects’ is tured off for their module role in the access rules of the entity.
- ⚪ C. An object can be created with a microflow if ‘Apply entity access’ is set to ‘Yes’ even if ‘Allow creating new objects’ is disabled for the user's module role in the access rules of the entity.
- ⚪ D. An object can only be created with a microfiow if ‘Apply entity access’ is set to ‘No’.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): ✎ Đã sửa so với file gốc. Tài liệu Mendix (Microflow Properties): mặc định microflow không áp dụng entity access, khi đó mọi thao tác đều được phép. Vì vậy user vẫn tạo được object qua microflow dù access rule tắt 'Allow creating new objects'.

---

### Đề 3 - Câu 48 [Security]

**Câu hỏi:** A Customer is only allowed to view their own orders because of the following XPath. Where should you apply this XPath? 
[ADV20.Order_Customer/ADV20.Customer/ADV20.Customer_Account = '[%CurrentUser%]']

- ⚪ A. The data source for all lists widgets should be converted to a microflow, which retrieves the orders from the database using this XPath constraint.
- ⚪ B. At the page level on List widgets where orders are displayed
- ✅ **C.** On the access rule of the entity Orders for the Customer role
- ⚪ D. At the page level on List widgets where orders are displayed and on the access rule of the entity Orders for the
customer role

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): XPath giới hạn dữ liệu phải đặt ở access rule của entity Order cho role Customer. Đặt ở đó thì mọi nơi truy cập Order đều bị giới hạn, không phụ thuộc từng widget.

---

### Đề 3 - Câu 49 [Domain Model]

**Câu hỏi:** The Order entity has an attribute OrderDate of type Date and Time. A user in the time zone Amsterdam GMT+1 creates an Order and sets the date to April 16, 1991. Which DateTime value is stored in the database?

- ⚪ A. 1991-04-15 12:00:00
- ✅ **B.** 1991-04-15 23:00:00
- ⚪ C. 1991-04-16 00:00:00
- ⚪ D. 1991-04-16 01:00:00

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Thuộc tính DateTime localized được lưu theo UTC. 16/04/1991 00:00 giờ Amsterdam (GMT+1) tương ứng 15/04/1991 23:00 UTC.

---

### Đề 3 - Câu 50 [UX & Logging]

**Câu hỏi:** What type of design has a focus on accessibility?

- ⚪ A. UX Design
- ✅ **B.** Usability Design
- ⚪ C. UI Design
- ⚪ D. Interaction Design

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Usability design chú trọng ứng dụng dễ dùng cho mọi người, trong đó có accessibility (người khuyết tật, tương phản màu, điều hướng bằng bàn phím…).

---

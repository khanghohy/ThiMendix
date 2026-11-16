# Đề Thi Thử Mendix Advanced - Đề Số 1

- **Số lượng câu hỏi:** 50 câu
- **Thời gian làm bài quy định:** 120 phút
- **Tiêu chuẩn đạt:** Từ 75% (38/50 câu đúng)

---

### Câu 1 [UX & Logging]

**Câu hỏi:** What does the UI designer focus on?

- ✅ **A.** The presentation of the product
- ⚪ B. The user's goals and desires
- ⚪ C. How it feels to use the product
- ⚪ D. Mapping out the user's journey

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): UI designer tập trung vào phần trình bày: bố cục, màu sắc, typography, thành phần giao diện. Mục tiêu, cảm nhận và hành trình user thuộc về UX.

---

### Câu 2 [Microflows]

**Câu hỏi:** What will happen when there is no error handling implemented and Mendix is not able to finish a microflow transaction successfully?

- ✅ **A.** The transaction is stopped and by default Mend will show this message in the user interface: ‘Something went wrong. Please contact your administrator'
- ⚪ B. The transaction will be finished and the user won't see a message in the user interface.
- ⚪ C. The transaction is stopped and Mendix will show a default error message in the user interface.
- ⚪ D. Nothing

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Không có error handling thì Mendix rollback transaction và client hiển thị thông báo mặc định kiểu 'An error occurred, please contact your system administrator'; chi tiết lỗi ghi vào log.

---

### Câu 3 [Microflows]

**Câu hỏi:** Which of the following statements is true about the [reversed()] expression?

- ✅ **A.** It can only be applied on self-references.
- ⚪ B. It can only be applied on *-* associations.
- ⚪ C. It can only be applied on 1-1 associations.
- ⚪ D. It can be applied to reverse a string attribute.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Hàm reversed() dùng trong XPath trên association tự tham chiếu (self-reference) để đi theo chiều ngược lại của association, vì hai đầu cùng là một entity.

---

### Câu 4 [UX & Logging]

**Câu hỏi:** Which of the following log messages follows the best practices for a Warning log message?

- ⚪ A. “Contacting REST service.”
- ✅ **B.** “User language has not been set yet.”
- ⚪ C. “Unknown user input '129q', unable to process value.”
- ⚪ D. “REST service has returned result: 404 Not Found.”

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Theo Mendix, Warning dùng khi có điều bất thường nhưng ứng dụng vẫn tiếp tục chạy được. 'User language has not been set yet.' là tình huống như vậy. 'Contacting REST service.' là Info/Debug; lỗi input không xử lý được hay REST trả 404 là Error.

---

### Câu 5 [Security]

**Câu hỏi:** When attempting to change the value of an object on a page. what will happen if the runtime identifies that you are not allowed to do this?

- ⚪ A. The change will be saved to the database and then rolled-back.
- ⚪ B. The change will be saved in the memory.
- ✅ **C.** The change will not happen and an error message willbe shown in the client and the log.
- ⚪ D. This will never happen. If you can't access the object you won't see it on the page.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Runtime luôn kiểm tra quyền khi client gửi thay đổi. Nếu không có quyền write, thay đổi bị từ chối và lỗi được hiển thị ở client và ghi log.

---

### Câu 6 [XPath & General]

**Câu hỏi:** Given this Domain Model, which of the following XPath s would you choose to retrieve the Orders of the currently logged-in customer?

- ⚪ A. [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account/Name = $currentUser/Name]
- ⚪ B. [AdvancedModule.Order_Customer='[%CurrentUser%]']
- ✅ **C.** [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account='[%CurrentUser%]']
- ⚪ D. [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account/Administration.Account/id = ‘[%CurrentUsers%]']

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Đi Order, qua Customer, tới Customer_Account rồi so sánh với '[%CurrentUser%]'. Đây là cách chuẩn và hiệu quả để lấy Order của customer đang đăng nhập.

---

### Câu 7 [Security]

**Câu hỏi:** Which of the three buttons New, Edit, and Delete on the page Order Overview will be visible to the user if an entity access rule specifies that the user can create, delete, read and write Orders?

- ⚪ A. Just the Edit button
- ⚪ B. Just the New and Delete buttons
- ✅ **C.** New Edit and Delete buttons
- ⚪ D. No buttons will be visible

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Entity access cho phép create, delete, read và write Order thì cả ba nút New, Edit, Delete đều hiển thị, vì Mendix ẩn nút dựa trên quyền entity.

---

### Câu 8 [UX & Logging]

**Câu hỏi:** If you add widgets to the widgets folder manually in the App Directory in Explorer, how can you make them appear in the Toolbox in Mendix Studio Pro?

- ⚪ A. Restart Mendix Studio Pro,
- ✅ **B.** Synchronize the App Directory.
- ⚪ C. Import the widget via the main menu of Mendix Studio Pro, otherwise it is not possible.
- ⚪ D. Nothing, the widget will be added automatically.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Thêm widget thủ công vào thư mục widgets thì dùng App > Synchronize App Directory (F4) để Studio Pro nạp lại và hiện widget trong Toolbox.

---

### Câu 9 [Microflows]

**Câu hỏi:** When an order is submitted, the Order and OrderLines will be committed to the database. Afterwards , the Customer should receive an email with the order details. Asa result. the Mendix developer adds the sub-microflow SUB_Order_SendCustomerEmail to the submit microflow. The developer wants to catch a possible error when sending an email so that the Order and OrderLines will definitely be committed. What type of error handling should the developer set on the C all microflow activity which calls the microflow SUB_Order_SendCustomerEmail?

- ✅ **A.** Custom without rollback
- ⚪ B. Continue
- ⚪ C. Custom with Rollback
- ⚪ D. Rollback

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Order và OrderLine đã commit trước khi gửi email. Đặt 'Custom without rollback' trên lời gọi SUB_Order_SendCustomerEmail để khi gửi mail lỗi thì dữ liệu đã commit không bị rollback, đồng thời vẫn bắt được lỗi để log.

---

### Câu 10 [XPath & General]

**Câu hỏi:** You would like to replace an XPath that utes the logical 'and' operator with a microfiow using. two Retrieves and a List operation. Which of the following List operations should you use?

- ⚪ A. Find
- ⚪ B. Subtract
- ✅ **C.** Intersert
- ⚪ D. Union

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Toán tử 'and' nghĩa là object phải thỏa cả hai điều kiện, tức là phần giao của hai list, nên dùng list operation Intersect.

---

### Câu 11 [Domain Model]

**Câu hỏi:** What is important to keep in mind when using a self-reference association?

- ⚪ A. Cascading deletes can go both ways
- ⚪ B. The number of self-reference layers has to be limited
- ⚪ C. Only 1-1 associations are allowed
- ✅ **D.** Make sure to rename the association so that both ends can be distinguished

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Self-reference có hai đầu cùng trỏ về một entity, nên cần đặt tên association (và tên hai đầu) rõ ràng để phân biệt cha/con, ví dụ Employee_Manager.

---

### Câu 12 [XPath & General]

**Câu hỏi:** You want to retrieve all trainees without certificates. Which XPath should you use for this?

- ✅ **A.** [ not(Training.Trainee_CertificateType/Trainee.CertificateType) ]
- ⚪ B. [Training.Trainee_CertificateType/Trainee.CertificateType != empty]
- ⚪ C. [not(Training.Trainee_CertificateType/Trainee.CertificateType != empty)]
- ⚪ D. [not(Training.Trainee_CertificateType/Trainee.CertificateType = empty)]

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): not(association/Entity) trả về object không có liên kết nào qua association, tức là trainee chưa có certificate.

---

### Câu 13 [Domain Model]

**Câu hỏi:** What type of association has the biggest data payload?

- ⚪ A. A reference “both” association (1-1)
- ✅ **B.** A reference set (*-*)
- ⚪ C. A reference association (1-*)
- ⚪ D. An association with an information entity

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Reference set (*-*) có thể chứa rất nhiều tham chiếu trên mỗi object, nên khi lấy object kèm association thì dữ liệu tải về lớn nhất.

---

### Câu 14 [Domain Model]

**Câu hỏi:** Where are file or image of mendix application stored by default

- ⚪ A. As binary in the content of an attribute
- ✅ **B.** On the file server located on the application server
- ⚪ C. On the dedicated Amazon file server
- ⚪ D. On the local hard disk of the user

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Mặc định file và ảnh (FileDocument, Image) không lưu trong database mà lưu trên file storage của application server; database chỉ giữ thông tin tham chiếu tới file.

---

### Câu 15 [Microflows]

**Câu hỏi:** In a sub-microflow, you want to create a string based on a DateTime parameter. The format of the string should look like this: 'Monday 23 April 2021'. Which date manipulation should you use to accomplish this?

- ⚪ A. Create a Date Variable and format the date to a string by using this expression: formatDateTime($DateTime,' EEE ddd MMMM yyyy')
- ✅ **B.** Create a String Variable and format the date to a string by using this expression: formatDateTime($DateTime,’EEEE ddd MMMM yyyy’)
- ⚪ C. Create a String Variable and format the date to a string by using this expression: formatDateTime($DateTime,’EE DD MM YYYY)
- ⚪ D. Create a String Variable and parse the date to a string by using this expression: parseDateTime($DateTime. 'EEE ddd MMMM yyyy’)

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): formatDateTime chuyển DateTime thành String. Pattern EEEE cho tên thứ đầy đủ (Monday), d là ngày, MMMM là tên tháng đầy đủ (April), yyyy là năm. parseDateTime làm ngược lại (String sang DateTime).

---

### Câu 16 [XPath & General]

**Câu hỏi:** You need to retrieve the UserRole Employee in a microflow. Which XPath constraint should you use in the Retrieve from Database activity?

- ✅ **A.** [id='[%UserRole_Employee%]']
- ⚪ B. [Name = 'Employee']
- ⚪ C. [ModelGUID= '[%UserRole_Employee%]']
- ⚪ D. [Description = 'Employee']

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Mỗi user role có token [%UserRole_<Tên>%] đại diện cho id của role đó, nên dùng [id='[%UserRole_Employee%]'] để lấy chính xác role, không phụ thuộc tên hay mô tả.

---

### Câu 17 [Domain Model]

**Câu hỏi:** The Order entity has an attribute OrderDate of type Date and Time. A user in the time zone Amsterdam GMT+1 creates an Order and sets the date to April 16, 1991. Which DateTime value is stored in the database?

- ⚪ A. 1991-04-16 01:00:00
- ⚪ B. 1991-04-16 00:00:00
- ✅ **C.** 1991-04-15 23:00:00
- ⚪ D. 1991-04-15 12:00:00

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Thuộc tính DateTime localized được lưu theo UTC. 16/04/1991 00:00 giờ Amsterdam (GMT+1) tương ứng 15/04/1991 23:00 UTC.

---

### Câu 18 [UX & Logging]

**Câu hỏi:** You want to show a text as Heading 2. However, on this particular page you want to remove the default spacing at the bottom. What is the most efficient way to do this?

- ⚪ A. Add CSS to the style property of the text widget.
- ⚪ B. Create your own class removing the spacing and add this class to the class property of the text widget.
- ⚪ C. Add the class remove-bottomspacing to the class property of the text widget.
- ✅ **D.** Go to the properties of the text widget and set the the 'Spacing Bottom' property in Appearance to 'Outer None'.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Atlas UI có sẵn thuộc tính Spacing trong mục Appearance của widget. Chọn Spacing Bottom = Outer None là cách nhanh nhất, không cần viết CSS hay class.

---

### Câu 19 [UX & Logging]

**Câu hỏi:** The default language of the app is English. United States (en_US) and Dutch. Netherlands (nl_NL) is an additional installed language. A user logs in and has the language Dutch. Netherlands (nl_NL) set as their user language. A button on a page doesn't have a caption but needs one. How should this be fixed?

- ✅ **A.** The caption must be set in the Dutch language only.
- ⚪ B. The caption must be set in the user language library and synced with the running app.
- ⚪ C. Change the conditional visibility of the button so that the caption becomes visible for users with the Dutch language.
- ⚪ D. In both English and Dutch, the caption must be set in the correct

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): User dùng tiếng Hà Lan nên caption thiếu ở bản dịch nl_NL. Chỉ cần bổ sung caption tiếng Hà Lan (Language > nl_NL), bản tiếng Anh vẫn giữ nguyên.

---

### Câu 20 [Domain Model]

**Câu hỏi:** What is an index?

- ⚪ A. The unique identifier of an object
- ⚪ B. A table that contains the results of a query
- ⚪ C. A sorted duplicate of an entity table
- ✅ **D.** An extra sorted table with only the record IDs and the selected attribute

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Index là một bảng phụ được sắp xếp, chỉ chứa giá trị thuộc tính được index và id bản ghi, giúp database tìm nhanh mà không cần quét cả bảng.

---

### Câu 21 [XPath & General]

**Câu hỏi:** Mendix Academy needs to retrieve all trainees with a valid RAD certificate from their customer database. Luckily, all certificates are stored in the String attribute CertificatelD and have the prefix ‘RAD’. You build a Trainee_Overview page where you add a List view with a data source Trainee by XPath. Which XPath should you specify when retrieving the Trainee entity?

- ⚪ A. [Trainee.CertificateID[starts-with('RAD')]]
- ✅ **B.** [starts-with(CertificatelD, 'RAD')]
- ⚪ C. [starts-with(Trainee.CertificatelD, RAD)]
- ⚪ D. [CertificatelD != empty and starts-with('RAD')]

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Cú pháp đúng là starts-with(attribute, 'chuỗi') đặt trong ngoặc vuông, attribute viết trực tiếp (không kèm tên entity), chuỗi đặt trong nháy đơn.

---

### Câu 22 [Microflows]

**Câu hỏi:** Microflow A iterates over a list of committed OrderLines, retrieves by association the Product being ordered, then adjusts the Product Stock amount accordingly. Microflow B retrieves the whole Product list of the Order from the database, then iterates over the Product list and adjusts the Product Stock amount accordingly. Which solution would be the best approach and why?

- ✅ **A.** Microflow A, because the by association retrieve in microflow A retrieves from memory and is much faster than a database retrieve.
- ⚪ B. Microflow B. because the retrieve in microflow A might result in multiple database retrieves even when retrieved by association.
- ⚪ C. Microflow B, because a database retrieve in this case is faster than a by association retrieve.
- ⚪ D. Microflow A, because there is no difference in performance between the two and a by association retrieve is easier to maintain from a developer perspective.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Theo file gốc là Microflow A (ô tô màu vàng). ⚠ Chưa xác nhận được: tài liệu Mendix không nói retrieve by association luôn lấy từ bộ nhớ. Nếu Product chưa có trong bộ nhớ thì mỗi vòng lặp vẫn có thể là một query.

---

### Câu 23 [XPath & General]

**Câu hỏi:** In a List view displaying a list of Orders, you want to add an XPath. The XPath should result in Orders where theOrderDate is within the past three years. Which XPath should you use?

- ⚪ A. [OrderDate < '[%BeginOfCurrentDay%] - 3 * [%YearLength%]']
- ✅ **B.** [OrderDate > ‘[%BeginOfCurrentDay%) - 3 * [%YearLength%]']
- ⚪ C. [addYears(OrderDate, -3)]- [OrderDate < '[%BeginOfCurrentDay%]']
- ⚪ D. [OrderDate > '[3 * [%YearLength%]- %BeginOfCurrentDay%]']

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Trong vòng 3 năm qua nghĩa là OrderDate lớn hơn (thời điểm đầu ngày hôm nay trừ 3 năm), viết bằng token: [%BeginOfCurrentDay%] - 3 * [%YearLength%].

---

### Câu 24 [Security]

**Câu hỏi:** What is the Mendix Clent?

- ⚪ A. The back end of your application
- ⚪ B. A customer who has a contract with Mendix
- ✅ **C.** The front end of your application
- ⚪ D. A user who is running your app

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Mendix Client là phần front end chạy trên trình duyệt hoặc thiết bị di động, hiển thị UI và giao tiếp với Mendix Runtime (back end).

---

### Câu 25 [UX & Logging]

**Câu hỏi:** The width of a layout grid can be set to Full width or Fixed width. What is the difference?

- ✅ **A.** When set to Fixed width, the total column width of this layout will be exactly the width in pixels as specified in the style sheet. Full width will be the full available width of the page.
- ⚪ B. When set to Fixed width, the input widgets width will be exactly the width in pixels as specified in the style sheet. When set to Full width the input widgets width will be the full width of the client.
- ⚪ C. When set to Fixed width, the total column width of this layout will be exactly the width in pixels as specified in the style sheet. Full width will be the full width of the client.
- ⚪ D. When set to Fixed width, the total column width of this layout will be exactly 960 pixels centered in the page. Full width will be the full available width of the enclosing container.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Fixed width giới hạn tổng chiều rộng cột theo giá trị pixel trong stylesheet (container cố định). Full width chiếm toàn bộ chiều rộng khả dụng của trang.

---

### Câu 26 [XPath & General]

**Câu hỏi:** Which search function should you use to find XPath expressions that might be affecting your performance? Select the correct keyboard shortcut.

- ⚪ A. Ctrl + F
- ⚪ B. Ctrl + Space
- ✅ **C.** Ctrl + Shift + F
- ⚪ D. Shift + F

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Ctrl+Shift+F mở Find Advanced trong Studio Pro, cho phép tìm theo loại (ví dụ mọi XPath) trên toàn app để rà soát hiệu năng.

---

### Câu 27 [UX & Logging]

**Câu hỏi:** You need your users to fill out a form with 40 input fields, but putting them all on one page creates a very confusing Ul. How can you simplify this form using Mendix best practices?

- ⚪ A. Add a scroll container so that each field's size can be increased
- ⚪ B. Use select pages instead of dropdown widgets
- ✅ **C.** Use a Wizard to break it into multiple pages
- ⚪ D. Reduce the size of each input widget so that more can fit on the page at once

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Form 40 trường nên chia thành nhiều bước bằng wizard để giảm tải nhận thức; user điền từng nhóm thông tin.

---

### Câu 28 [Microflows]

**Câu hỏi:** When an Order is submitted, the Order Number (String) is created in a sub-microflow. What is the best way to build this sub-microflow according to Mendix best practices?

- ⚪ A. Build the OrderNumber within the End event and pass it back to the main microflow.
- ⚪ B. Build the OrderNumber in a new string variable. then change and refresh the Order object within the sub-microflow.
- ✅ **C.** Build the OrderNumber in a new string variable and pass it back to the main microflow.
- ⚪ D. Build the OrderNumber in a new string variable, then change and commit the Order object within the sub-microflow.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Sub-microflow nên chỉ làm một việc: tạo chuỗi OrderNumber và trả về. Việc change và commit Order để ở microflow chính cho dễ đọc, dễ tái sử dụng và tránh commit rải rác.

---

### Câu 29 [XPath & General]

**Câu hỏi:** You would like to search for trainees in the database using their names. To speed up the search, where should you add an index?

- ⚪ A. In the ‘Search on’ settings of the List view
- ⚪ B. In a microflow by adding a Create index activity and returning the indexed list
- ✅ **C.** In the entity properties in the Domain model
- ⚪ D. In a widget downloaded from the Marketplace

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Index được khai báo trong properties của entity ở Domain Model (tab Indexes), chọn thuộc tính Name để tìm kiếm nhanh hơn.

---

### Câu 30 [Domain Model]

**Câu hỏi:** You want the address of a customer to be moved from the Customer entity to a newly created Customer Address entity. When should you remove the Address attribute from the Customer entity?

- ⚪ A. You should try to avoid removing it
- ⚪ B. In the deploy that you add the Customer Address entity
- ✅ **C.** In the next deploy after you have added the CustomerAddress entity
- ⚪ D. After a predefined transfer period

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Phải giữ thuộc tính Address cũ trong lần deploy đầu để chạy migration chuyển dữ liệu sang CustomerAddress. Xóa ngay sẽ mất dữ liệu; xóa ở lần deploy sau khi dữ liệu đã chuyển xong là an toàn.

---

### Câu 31 [Security]

**Câu hỏi:** Given that nanoflows always run in the context of the current user, which of the following statements is true?

- ✅ **A.** Nanoflow access is as secure as a microflow with entity access enabled.
- ⚪ B. Nanoflow access is as secure as a microflow called inside of the nanoflow
- ⚪ C. Nanoflow access is as secure as a microflow access without entity access enabled.
- ⚪ D. Nanoflow access is as secure as a microflow.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Nanoflow chạy trên client trong ngữ cảnh user hiện tại, mọi dữ liệu nó chạm tới đều chịu entity access, nên mức an toàn tương đương microflow bật 'Apply entity access'.

---

### Câu 32 [Security]

**Câu hỏi:** A user with the role Employee adds a new OrderLine to an Order and selects a Product After Product selection the Employee sets a Discount of 10% What will happen when the related microflow is triggered as an on-change microflow?

- ⚪ A. The Employee will get an error message, because the Employee role doesn't have write access to the attribute LineValue
- ⚪ B. The OrderLine LineValue will not be changed and the user will not be informed.
- ✅ **C.** The OrderLine LineValue will be changed to 9.00 and the value is returned to the client
- ⚪ D. The Orderline LineValue will be changed to 9.00, though it cannot be passed to the client because the Employee role doesn't have write access to the attribute LineValue

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Microflow mặc định chạy không áp dụng entity access, nên vẫn đổi được LineValue thành 9.00 và trả object về client để hiển thị, dù role Employee không có quyền write trên thuộc tính đó.

---

### Câu 33 [UX & Logging]

**Câu hỏi:** What type of design has a focus on accessibility?

- ⚪ A. UX Design
- ⚪ B. UI Design
- ✅ **C.** Usability Design
- ⚪ D. Interaction Design

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Usability design chú trọng ứng dụng dễ dùng cho mọi người, trong đó có accessibility (người khuyết tật, tương phản màu, điều hướng bằng bàn phím…).

---

### Câu 34 [UX & Logging]

**Câu hỏi:** Customers can choose their desired delivery method when submitting an order in an app. This is dependent on their address, and you only want to display the delivery options that are available to their location, What is the most efficient way to achieve this?

- ✅ **A.** Use an on-change microflow to set the conditional visibility of the relevant page elements.
- ⚪ B. Use an on-leave microflow to set the conditional visibility of the relevant page elements
- ⚪ C. Use an on-change microflow to set the conditional editabilty of the relevant page elements.
- ⚪ D. Use an on-leave microflow to set the conditional editability of the relevant page elements.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Khi địa chỉ thay đổi, on-change microflow (hoặc nanoflow) tính lại các tùy chọn giao hàng phù hợp và điều khiển conditional visibility, nên chỉ những lựa chọn khả dụng được hiển thị ngay.

---

### Câu 35 [Microflows]

**Câu hỏi:** The following microflow is triggered when saving a new Order. This microflow triggers a sub- microflow where the Order/Number is defined and set. This setup is not following Mendix best-practices. What should be changed to meet the best practices?

- ⚪ A. The Commit of the OrderlineList should happen before the sub- microfiow call.
- ✅ **B.** The sub-microflow should return the OrderNumber variable. The Change and Commit of the Order object should be done in the main microfiow.
- ⚪ C. The retrieve of the OrderLineList should happen after the sub-microflow call.
- ⚪ D. The retrieve of the OrderLineList and Commit of this list should be executed in a second sub-microflow.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Best practice: sub-microflow chỉ tính và trả về OrderNumber; microflow chính thực hiện Change và Commit Order. Như vậy mọi thay đổi trên Order nằm ở một chỗ và tránh commit nhiều lần.

---

### Câu 36 [Domain Model]

**Câu hỏi:** In the properties of an entity, what does checking the system member 'owner' do?

- ⚪ A. The object ID of the referenced Account object is stored as the owner of the object when it is created.
- ⚪ B. The object ID of the logged-in user who retrieves the object from the database will be stored in the object for future reference.
- ⚪ C. Objects of this entity are the owner of all associations from and towards this entity.
- ✅ **D.** The object ID of the logged-in user who creates the object is stored as the owner of the object.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Bật system member 'owner' thì khi tạo object, Mendix tự lưu tham chiếu tới Account của user đang đăng nhập vào System.owner. Hay dùng cho XPath như [System.owner='[%CurrentUser%]'].

---

### Câu 37 [UX & Logging]

**Câu hỏi:** What type of menu is most likely to go well with Hick's law?

- ⚪ A. A Navigation Tree
- ✅ **B.** A Simple Menu Bar
- ⚪ C. A Custom Menu
- ⚪ D. A Default Menu Bar

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Hick's law: càng nhiều lựa chọn thì user càng mất thời gian quyết định. Simple menu bar ít mục, phẳng, nên phù hợp nhất.

---

### Câu 38 [Microflows]

**Câu hỏi:** Rules have some limitations compared to sub-microflow. What is one of the limitations of a Rule? Rule cannot:

- ⚪ A. have multiple End events
- ⚪ B. Return a Boolean
- ✅ **C.** Interact with the client
- ⚪ D. Have an object as an input parameter

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Rule chỉ dùng trong Decision để trả về Boolean hoặc Enumeration và không được tương tác với client (không show page, không show message, không đóng page…).

---

### Câu 39 [XPath & General]

**Câu hỏi:** you need to create an Xpath query to look for customers with the company name Mendix. Which of the follwing suggestions represents a syntactically correct XPath ?

- ✅ **A.** [CustomerManagement.Customer[contains(CustomerName. ‘Mendix')]]
- ⚪ B. [CustomerManagement.Customer/(CustomerName = ‘Mendix')]
- ⚪ C. [CustomerManagement.Customer/contains(CustomerName. ‘Mendix')]
- ⚪ D. [CustomerManagement.Customer/[contains(CustomerName. ‘Mendix')]]

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Hàm contains() đặt trong cặp ngoặc vuông ràng buộc ngay sau entity: Customer[contains(CustomerName, 'Mendix')]. Các phương án còn lại đặt '/' hoặc ngoặc sai chỗ.

---

### Câu 40 [Domain Model]

**Câu hỏi:** When is it likely that an index will negatively impact perfomance?

- ⚪ A. When an entity has many attributes
- ✅ **B.** When data is changed more often than it is read
- ⚪ C. When the entity exclusively has stored attributes
- ⚪ D. When there are a lot of objects for the relevant entity

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Index tăng tốc đọc nhưng mỗi lần insert/update/delete database phải cập nhật thêm bảng index. Nếu dữ liệu thay đổi nhiều hơn được đọc thì chi phí ghi lớn hơn lợi ích tìm kiếm.

---

### Câu 41 [Security]

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

### Câu 42 [Microflows]

**Câu hỏi:** When would you use the custom error handling "without rollback" on a sub-microflow call?

- ⚪ A. When you want to make sure that both the parent and sub-microflows are rolled back.
- ⚪ B. When you do not want the sub-microflow to be rolled back even if it has an error.
- ✅ **C.** When you do not want the parent microflow to be rolled back even if the sub-microflow has an error.
- ⚪ D. When additional documentation is required. Without rollback increases readability.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): 'Custom without rollback' trên lời gọi sub-microflow nghĩa là khi sub-microflow lỗi, những thay đổi trước đó của microflow cha không bị rollback và cha tiếp tục theo đường xử lý lỗi.

---

### Câu 43 [UX & Logging]

**Câu hỏi:** What is the relationship between UX and UI?

- ⚪ A. UX and UI are at a core level the same thing
- ⚪ B. UX and UI are mostly unrelated
- ⚪ C. UX is a sub-category of UI
- ✅ **D.** Ul can be used to improve UX

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): UX là toàn bộ trải nghiệm của user, UI là phần giao diện. UI tốt là một phương tiện để cải thiện UX.

---

### Câu 44 [Security]

**Câu hỏi:** How do you handle access to a sub-microflow in relation to the parent microflow?

- ⚪ A. When creating 3 sub-microfiow, you can choose whether you want to inherit the access rules from the parent microflow or to set it up independently.
- ✅ **B.** Access to a sub-microflow does not need to be set because itis handled by the parent microflow.
- ⚪ C. If you set the access to a sub-microflow, it overwrites access defined by the parent microflow.
- ⚪ D. Access to a sub-microflow needs to be set up independently of the access to the parent microflow.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Sub-microflow được gọi từ microflow cha chạy với quyền của cha nên không cần gán module role. Gán role còn làm lộ sub-microflow ra client API.

---

### Câu 45 [Microflows]

**Câu hỏi:** The Mendix Platform uses transactions which means that every microflow, commit, and delete will occur within a database transaction. When will each transaction be initialized and when will it end?

- ✅ **A.** The transaction is initialized as soon as the microflow executes its first database action and only ends when the microflow completes.
- ⚪ B. The transaction is initialized as soon as each individual microflow action executes and ends after each individual microflow action.
- ⚪ C. The transaction is initialized as soon as the microflow executes its first database action and ends after each database action.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Một microflow chạy trong một database transaction: transaction mở khi có thao tác database đầu tiên và chỉ kết thúc (commit hoặc rollback) khi microflow hoàn tất.

---

### Câu 46 [Security]

**Câu hỏi:** What does entity access affect?

- ⚪ A. What a demo user can see on a page
- ⚪ B. Which pages a user can see
- ✅ **C.** Which actions a user can execute
- ⚪ D. Which set of data a user can manipulate

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Theo file gốc là 'Which actions a user can execute'. ⚠ Nên xem lại: tài liệu Mendix nói access rule của entity quy định user được làm gì với các object của entity (create, read, write, delete, giới hạn bằng XPath). Cách diễn đạt này gần với 'Which set of data a user can manipulate' hơn.

---

### Câu 47 [UX & Logging]

**Câu hỏi:** The recommended method when setting the log node name of a custom log message is to:

- ⚪ A. Create a settings entity to maintain the log node names from the runtime.
- ✅ **B.** Use an enumeration to store all log node names as an enumeration value and use the expression getCaption ModuleName.EnumerationList.CustomLogNodeNamel to set the log node name.
- ⚪ C. Use a snippet with a text widget containing a list of all custom log node names. Store this snippet in the general module as a resource.
- ⚪ D. Use string quotes around a caption Log node name

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Lưu tên log node trong enumeration và dùng getCaption(...) giúp tên thống nhất, tránh gõ sai chuỗi và dễ đổi ở một chỗ.

---

### Câu 48 [XPath & General]

**Câu hỏi:** You need to write a query to retrieve all registrations associated with trainees who bought vouchers in the EMEA region and where the voucher was not used. Which of the following XPath expressions is correct?

- ⚪ A. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA'] [VoucherUsed = false ]]
- ⚪ B. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed = false ]]
- ⚪ C. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed != true ]]
- ✅ **D.** [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed = false()]]

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Hai điều kiện cùng áp lên một object nên viết chung trong một ngoặc với 'and'. Giá trị Boolean trong XPath phải viết là false() (có ngoặc).

---

### Câu 49 [XPath & General]

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

### Câu 50 [Microflows]

**Câu hỏi:** When is custom error handling most appropriate within a microflow?

- ⚪ A. When calling other microflows
- ✅ **B.** When Interacting with external systems
- ⚪ C. When using a JAVA action activity
- ⚪ D. When using multiple decision elements

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Gọi hệ thống bên ngoài (REST, SOAP, email…) dễ lỗi ngoài tầm kiểm soát (timeout, mất kết nối), nên cần custom error handling để log và xử lý có kiểm soát.

---

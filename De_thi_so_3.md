# Đề Thi Thử Mendix Advanced - Đề Số 3

- **Số lượng câu hỏi:** 50 câu
- **Thời gian làm bài quy định:** 120 phút
- **Tiêu chuẩn đạt:** Từ 75% (38/50 câu đúng)

---

### Câu 1 [UX & Logging]

**Câu hỏi:** The recommended method when setting the log node name of a custom log message is to:

- ⚪ A. Create a settings entity to maintain the log node names from the runtime.
- ⚪ B. Use string quotes around a caption Log node name
- ⚪ C. Use a snippet with a text widget containing a list of all custom log node names. Store this snippet in the general module as a resource.
- ✅ **D.** Use an enumeration to store all log node names as an enumeration value and use the expression getCaption ModuleName.EnumerationList.CustomLogNodeNamel to set the log node name.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Lưu tên log node trong enumeration và dùng getCaption(...) giúp tên thống nhất, tránh gõ sai chuỗi và dễ đổi ở một chỗ.

---

### Câu 2 [Domain Model]

**Câu hỏi:** Given the following Domain model, how will objects of the Book entity be stored in the database?

- ✅ **A.** Some information will be stored in the Product table and some in the Book table.
- ⚪ B. All information will be stored in the general Product table.
- ⚪ C. All information will be stored in a specific Book table.
- ⚪ D. All information will be stored in a table for specializations.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Với kế thừa (generalization), thuộc tính chung lưu ở bảng Product, thuộc tính riêng của Book lưu ở bảng Book; hai bản ghi dùng chung một id.

---

### Câu 3 [Domain Model]

**Câu hỏi:** When is it likely that an index will negatively impact perfomance?

- ⚪ A. When there are a lot of objects for the relevant entity
- ⚪ B. When an entity has many attributes
- ✅ **C.** When data is changed more often than it is read
- ⚪ D. When the entity exclusively has stored attributes

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Index tăng tốc đọc nhưng mỗi lần insert/update/delete database phải cập nhật thêm bảng index. Nếu dữ liệu thay đổi nhiều hơn được đọc thì chi phí ghi lớn hơn lợi ích tìm kiếm.

---

### Câu 4 [Security]

**Câu hỏi:** When attempting to change the value of an object on a page. what will happen if the runtime identifies that you are not allowed to do this?

- ⚪ A. This will never happen. If you can't access the object you won't see it on the page.
- ✅ **B.** The change will not happen and an error message willbe shown in the client and the log.
- ⚪ C. The change will be saved in the memory.
- ⚪ D. The change will be saved to the database and then rolled-back.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Runtime luôn kiểm tra quyền khi client gửi thay đổi. Nếu không có quyền write, thay đổi bị từ chối và lỗi được hiển thị ở client và ghi log.

---

### Câu 5 [XPath & General]

**Câu hỏi:** Which of these data sources is not supported in offine applications?

- ⚪ A. Listen to widget
- ✅ **B.** Microflow
- ⚪ C. Nanoflow
- ⚪ D. Context

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Ứng dụng offline-first chạy trên thiết bị, không gọi server được, nên data source Microflow không được hỗ trợ; dùng Nanoflow, Database (local), Context, Listen to widget.

---

### Câu 6 [Microflows]

**Câu hỏi:** Rules have some limitations compared to sub-microflow. What is one of the limitations of a Rule? Rule cannot:

- ⚪ A. Have an object as an input parameter
- ✅ **B.** Interact with the client
- ⚪ C. Return a Boolean
- ⚪ D. have multiple End events

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Rule chỉ dùng trong Decision để trả về Boolean hoặc Enumeration và không được tương tác với client (không show page, không show message, không đóng page…).

---

### Câu 7 [XPath & General]

**Câu hỏi:** A Customer should only be allowed to Read and Write their own Orders. Which XPath (if any) should be added to the r access rule in the domain model below?

- ⚪ A. [ADV20.Order_Customer/ADV20.Customer/ADV20.Customer_Account/Administration.Account/id = '{%CurrentUser%}]
- ⚪ B. [ADV20.Order_Customer/ADV20.Customers = '[%CurrentUser%]']
- ⚪ C. Since the Order is linked to Customer. there is no need to add an XPath constraint in the Access Rule for the user role Customer in the ‘Order entity. The data is not accessible to other users.
- ✅ **D.** [ADV20.Order_Customer/ADV20 Customer/ADV20.Customer_Account='[%CurrentUser%]']

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Order nối Customer, Customer nối Account. So sánh association Customer_Account trực tiếp với '[%CurrentUser%]' là đúng cú pháp và hiệu quả, không cần đi tới /id.

---

### Câu 8 [Domain Model]

**Câu hỏi:** What type of association has the biggest data payload?

- ⚪ A. An association with an information entity
- ⚪ B. A reference “both” association (1-1)
- ⚪ C. A reference association (1-*)
- ✅ **D.** A reference set (*-*)

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Reference set (*-*) có thể chứa rất nhiều tham chiếu trên mỗi object, nên khi lấy object kèm association thì dữ liệu tải về lớn nhất.

---

### Câu 9 [UX & Logging]

**Câu hỏi:** You want to show a text as Heading 2. However, on this particular page you want to remove the default spacing at the bottom. What is the most efficient way to do this?

- ✅ **A.** Go to the properties of the text widget and set the the 'Spacing Bottom' property in Appearance to 'Outer None'.
- ⚪ B. Add the class remove-bottomspacing to the class property of the text widget.
- ⚪ C. Add CSS to the style property of the text widget.
- ⚪ D. Create your own class removing the spacing and add this class to the class property of the text widget.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Atlas UI có sẵn thuộc tính Spacing trong mục Appearance của widget. Chọn Spacing Bottom = Outer None là cách nhanh nhất, không cần viết CSS hay class.

---

### Câu 10 [Microflows]

**Câu hỏi:** Microflow A iterates over a list of committed OrderLines, retrieves by association the Product being ordered, then adjusts the Product Stock amount accordingly. Microflow B retrieves the whole Product list of the Order from the database, then iterates over the Product list and adjusts the Product Stock amount accordingly. Which solution would be the best approach and why?

- ⚪ A. Microflow B. because the retrieve in microflow A might result in multiple database retrieves even when retrieved by association.
- ⚪ B. Microflow B, because a database retrieve in this case is faster than a by association retrieve.
- ✅ **C.** Microflow A, because the by association retrieve in microflow A retrieves from memory and is much faster than a database retrieve.
- ⚪ D. Microflow A, because there is no difference in performance between the two and a by association retrieve is easier to maintain from a developer perspective.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Theo file gốc là Microflow A (ô tô màu vàng). ⚠ Chưa xác nhận được: tài liệu Mendix không nói retrieve by association luôn lấy từ bộ nhớ. Nếu Product chưa có trong bộ nhớ thì mỗi vòng lặp vẫn có thể là một query.

---

### Câu 11 [XPath & General]

**Câu hỏi:** Which search function should you use to find XPath expressions that might be affecting your performance? Select the correct keyboard shortcut.

- ⚪ A. Ctrl + Space
- ⚪ B. Ctrl + F
- ⚪ C. Shift + F
- ✅ **D.** Ctrl + Shift + F

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Ctrl+Shift+F mở Find Advanced trong Studio Pro, cho phép tìm theo loại (ví dụ mọi XPath) trên toàn app để rà soát hiệu năng.

---

### Câu 12 [XPath & General]

**Câu hỏi:** You would like to search for trainees in the database using their names. To speed up the search, where should you add an index?

- ⚪ A. In a widget downloaded from the Marketplace
- ✅ **B.** In the entity properties in the Domain model
- ⚪ C. In a microflow by adding a Create index activity and returning the indexed list
- ⚪ D. In the ‘Search on’ settings of the List view

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Index được khai báo trong properties của entity ở Domain Model (tab Indexes), chọn thuộc tính Name để tìm kiếm nhanh hơn.

---

### Câu 13 [Domain Model]

**Câu hỏi:** Where are file or image of mendix application stored by default

- ⚪ A. On the dedicated Amazon file server
- ⚪ B. On the local hard disk of the user
- ✅ **C.** On the file server located on the application server
- ⚪ D. As binary in the content of an attribute

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Mặc định file và ảnh (FileDocument, Image) không lưu trong database mà lưu trên file storage của application server; database chỉ giữ thông tin tham chiếu tới file.

---

### Câu 14 [UX & Logging]

**Câu hỏi:** What type of menu is most likely to go well with Hick's law?

- ✅ **A.** A Simple Menu Bar
- ⚪ B. A Navigation Tree
- ⚪ C. A Default Menu Bar
- ⚪ D. A Custom Menu

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Hick's law: càng nhiều lựa chọn thì user càng mất thời gian quyết định. Simple menu bar ít mục, phẳng, nên phù hợp nhất.

---

### Câu 15 [UX & Logging]

**Câu hỏi:** Customers can choose their desired delivery method when submitting an order in an app. This is dependent on their address, and you only want to display the delivery options that are available to their location, What is the most efficient way to achieve this?

- ⚪ A. Use an on-leave microflow to set the conditional visibility of the relevant page elements
- ⚪ B. Use an on-leave microflow to set the conditional editability of the relevant page elements.
- ✅ **C.** Use an on-change microflow to set the conditional visibility of the relevant page elements.
- ⚪ D. Use an on-change microflow to set the conditional editabilty of the relevant page elements.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Khi địa chỉ thay đổi, on-change microflow (hoặc nanoflow) tính lại các tùy chọn giao hàng phù hợp và điều khiển conditional visibility, nên chỉ những lựa chọn khả dụng được hiển thị ngay.

---

### Câu 16 [Microflows]

**Câu hỏi:** When is custom error handling most appropriate within a microflow?

- ⚪ A. When calling other microflows
- ✅ **B.** When Interacting with external systems
- ⚪ C. When using a JAVA action activity
- ⚪ D. When using multiple decision elements

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Gọi hệ thống bên ngoài (REST, SOAP, email…) dễ lỗi ngoài tầm kiểm soát (timeout, mất kết nối), nên cần custom error handling để log và xử lý có kiểm soát.

---

### Câu 17 [Security]

**Câu hỏi:** A user with the role Employee adds a new OrderLine to an Order and selects a Product After Product selection the Employee sets a Discount of 10% What will happen when the related microflow is triggered as an on-change microflow?

- ⚪ A. The OrderLine LineValue will not be changed and the user will not be informed.
- ⚪ B. The Employee will get an error message, because the Employee role doesn't have write access to the attribute LineValue
- ✅ **C.** The OrderLine LineValue will be changed to 9.00 and the value is returned to the client
- ⚪ D. The Orderline LineValue will be changed to 9.00, though it cannot be passed to the client because the Employee role doesn't have write access to the attribute LineValue

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Microflow mặc định chạy không áp dụng entity access, nên vẫn đổi được LineValue thành 9.00 và trả object về client để hiển thị, dù role Employee không có quyền write trên thuộc tính đó.

---

### Câu 18 [Microflows]

**Câu hỏi:** When an Order is submitted, the Order Number (String) is created in a sub-microflow. What is the best way to build this sub-microflow according to Mendix best practices?

- ✅ **A.** Build the OrderNumber in a new string variable and pass it back to the main microflow.
- ⚪ B. Build the OrderNumber within the End event and pass it back to the main microflow.
- ⚪ C. Build the OrderNumber in a new string variable. then change and refresh the Order object within the sub-microflow.
- ⚪ D. Build the OrderNumber in a new string variable, then change and commit the Order object within the sub-microflow.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Sub-microflow nên chỉ làm một việc: tạo chuỗi OrderNumber và trả về. Việc change và commit Order để ở microflow chính cho dễ đọc, dễ tái sử dụng và tránh commit rải rác.

---

### Câu 19 [Domain Model]

**Câu hỏi:** What is an index?

- ⚪ A. A table that contains the results of a query
- ⚪ B. The unique identifier of an object
- ✅ **C.** An extra sorted table with only the record IDs and the selected attribute
- ⚪ D. A sorted duplicate of an entity table

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Index là một bảng phụ được sắp xếp, chỉ chứa giá trị thuộc tính được index và id bản ghi, giúp database tìm nhanh mà không cần quét cả bảng.

---

### Câu 20 [Domain Model]

**Câu hỏi:** You want the address of a customer to be moved from the Customer entity to a newly created Customer Address entity. When should you remove the Address attribute from the Customer entity?

- ⚪ A. After a predefined transfer period
- ⚪ B. You should try to avoid removing it
- ✅ **C.** In the next deploy after you have added the CustomerAddress entity
- ⚪ D. In the deploy that you add the Customer Address entity

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Phải giữ thuộc tính Address cũ trong lần deploy đầu để chạy migration chuyển dữ liệu sang CustomerAddress. Xóa ngay sẽ mất dữ liệu; xóa ở lần deploy sau khi dữ liệu đã chuyển xong là an toàn.

---

### Câu 21 [UX & Logging]

**Câu hỏi:** What part of a page remains if you navigate between two pages with the same layout?

- ⚪ A. Mendix is optimized to change as little as possible
- ✅ **B.** Everything that is not in a placeholder
- ⚪ C. The menu bar and footer
- ⚪ D. Nothing, it's a different page with different content

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Khi chuyển giữa hai page cùng layout, Mendix chỉ thay nội dung trong placeholder; phần ngoài placeholder (header, menu, footer…) giữ nguyên.

---

### Câu 22 [XPath & General]

**Câu hỏi:** You need to write a query to retrieve all registrations associated with trainees who bought vouchers in the EMEA region and where the voucher was not used. Which of the following XPath expressions is correct?

- ⚪ A. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA'] [VoucherUsed = false ]]
- ✅ **B.** [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed = false()]]
- ⚪ C. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed = false ]]
- ⚪ D. [Training.Registration_Trainee/Training.Trainee/Training.Trainee_EventRegion/Training.EventRegion[EventRegionCode = 'EMEA' and VoucherUsed != true ]]

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Hai điều kiện cùng áp lên một object nên viết chung trong một ngoặc với 'and'. Giá trị Boolean trong XPath phải viết là false() (có ngoặc).

---

### Câu 23 [XPath & General]

**Câu hỏi:** Mendix Academy needs to retrieve all trainees with a valid RAD certificate from their customer database. Luckily, all certificates are stored in the String attribute CertificatelD and have the prefix ‘RAD’. You build a Trainee_Overview page where you add a List view with a data source Trainee by XPath. Which XPath should you specify when retrieving the Trainee entity?

- ✅ **A.** [starts-with(CertificatelD, 'RAD')]
- ⚪ B. [Trainee.CertificateID[starts-with('RAD')]]
- ⚪ C. [starts-with(Trainee.CertificatelD, RAD)]
- ⚪ D. [CertificatelD != empty and starts-with('RAD')]

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Cú pháp đúng là starts-with(attribute, 'chuỗi') đặt trong ngoặc vuông, attribute viết trực tiếp (không kèm tên entity), chuỗi đặt trong nháy đơn.

---

### Câu 24 [Security]

**Câu hỏi:** In an app consisting of two modules, each of which has two module roles, what is the minimal number of module roles that can be linked to a user role defined in the app security?

- ⚪ A. Four, indicating that a user role is linked to each module role in both modules
- ⚪ B. None, indicating that a user role does not have to be linked to a module role in each available module.
- ⚪ C. Two, indicating that a user role is linked to exactly one module role in each module
- ✅ **D.** One, indicating that a user role is linked to at least one module role in at least one of the available modules

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Một user role chỉ cần gắn tối thiểu 1 module role (ở ít nhất một module). Không bắt buộc gắn module role ở mọi module.

---

### Câu 25 [Microflows]

**Câu hỏi:** In a sub-microflow, you want to create a string based on a DateTime parameter. The format of the string should look like this: 'Monday 23 April 2021'. Which date manipulation should you use to accomplish this?

- ✅ **A.** Create a String Variable and format the date to a string by using this expression: formatDateTime($DateTime,’EEEE ddd MMMM yyyy’)
- ⚪ B. Create a String Variable and format the date to a string by using this expression: formatDateTime($DateTime,’EE DD MM YYYY)
- ⚪ C. Create a String Variable and parse the date to a string by using this expression: parseDateTime($DateTime. 'EEE ddd MMMM yyyy’)
- ⚪ D. Create a Date Variable and format the date to a string by using this expression: formatDateTime($DateTime,' EEE ddd MMMM yyyy')

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): formatDateTime chuyển DateTime thành String. Pattern EEEE cho tên thứ đầy đủ (Monday), d là ngày, MMMM là tên tháng đầy đủ (April), yyyy là năm. parseDateTime làm ngược lại (String sang DateTime).

---

### Câu 26 [UX & Logging]

**Câu hỏi:** When a Customer marks a Product as favorite, the heart empty icon is replaced by the heart icon. This is achieved by two separated link buttons, with icon set and an empty caption. By applying conditional visibility either the heart or heart empty icon is displayed. The heart icon also has an orange color, instead of the default link button color style. Which out-of-the-box class can be used to achieve this?

- ⚪ A. btn-warning
- ✅ **B.** text-warning
- ⚪ C. text-orange
- ⚪ D. text-color: #f99b1d:

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): ✎ Đã sửa so với file gốc. Tài liệu Mendix (Implement Classes): Atlas có sẵn helper class text-warning (màu warning của theme, mặc định là cam). 'text-color: #f99b1d' là CSS chứ không phải class.

---

### Câu 27 [Microflows]

**Câu hỏi:** What will happen when there is no error handling implemented and Mendix is not able to finish a microflow transaction successfully?

- ⚪ A. Nothing
- ✅ **B.** The transaction is stopped and by default Mend will show this message in the user interface: ‘Something went wrong. Please contact your administrator'
- ⚪ C. The transaction is stopped and Mendix will show a default error message in the user interface.
- ⚪ D. The transaction will be finished and the user won't see a message in the user interface.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Không có error handling thì Mendix rollback transaction và client hiển thị thông báo mặc định kiểu 'An error occurred, please contact your system administrator'; chi tiết lỗi ghi vào log.

---

### Câu 28 [UX & Logging]

**Câu hỏi:** What does the UI designer focus on?

- ✅ **A.** The presentation of the product
- ⚪ B. Mapping out the user's journey
- ⚪ C. The user's goals and desires
- ⚪ D. How it feels to use the product

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): UI designer tập trung vào phần trình bày: bố cục, màu sắc, typography, thành phần giao diện. Mục tiêu, cảm nhận và hành trình user thuộc về UX.

---

### Câu 29 [Domain Model]

**Câu hỏi:** In the properties of an entity, what does checking the system member 'owner' do?

- ⚪ A. The object ID of the referenced Account object is stored as the owner of the object when it is created.
- ⚪ B. Objects of this entity are the owner of all associations from and towards this entity.
- ✅ **C.** The object ID of the logged-in user who creates the object is stored as the owner of the object.
- ⚪ D. The object ID of the logged-in user who retrieves the object from the database will be stored in the object for future reference.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Bật system member 'owner' thì khi tạo object, Mendix tự lưu tham chiếu tới Account của user đang đăng nhập vào System.owner. Hay dùng cho XPath như [System.owner='[%CurrentUser%]'].

---

### Câu 30 [UX & Logging]

**Câu hỏi:** Which of the following log messages follows the best practices for a Warning log message?

- ⚪ A. “User language has not been set yet.”
- ✅ **B.** “REST service has returned result: 404 Not Found.”
- ⚪ C. “Unknown user input '129q', unable to process value.”
- ⚪ D. “Contacting REST service.”

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Theo file gốc là 'REST service has returned result: 404 Not Found.'. ⚠ Nên xem lại: tài liệu Mendix định nghĩa Warning là có điều bất thường nhưng ứng dụng vẫn chạy, còn Error là không thực hiện được một chức năng. Lỗi 404 có thể được xếp vào Error; 'User language has not been set yet.' cũng là ứng viên cho Warning.

---

### Câu 31 [Security]

**Câu hỏi:** What does entity access affect?

- ✅ **A.** Which actions a user can execute
- ⚪ B. What a demo user can see on a page
- ⚪ C. Which pages a user can see
- ⚪ D. Which set of data a user can manipulate

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Theo file gốc là 'Which actions a user can execute'. ⚠ Nên xem lại: tài liệu Mendix nói access rule của entity quy định user được làm gì với các object của entity (create, read, write, delete, giới hạn bằng XPath). Cách diễn đạt này gần với 'Which set of data a user can manipulate' hơn.

---

### Câu 32 [XPath & General]

**Câu hỏi:** Given this Domain Model, which of the following XPath s would you choose to retrieve the Orders of the currently logged-in customer?

- ⚪ A. [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account/Name = $currentUser/Name]
- ⚪ B. [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account/Administration.Account/id = ‘[%CurrentUsers%]']
- ✅ **C.** [AdvancedModule.Order_Customer/AdvancedModule.Customer/AdvancedModule.Customer_Account='[%CurrentUser%]']
- ⚪ D. [AdvancedModule.Order_Customer='[%CurrentUser%]']

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Đi Order, qua Customer, tới Customer_Account rồi so sánh với '[%CurrentUser%]'. Đây là cách chuẩn và hiệu quả để lấy Order của customer đang đăng nhập.

---

### Câu 33 [XPath & General]

**Câu hỏi:** You would like to replace an XPath that utes the logical 'and' operator with a microfiow using. two Retrieves and a List operation. Which of the following List operations should you use?

- ✅ **A.** Intersert
- ⚪ B. Union
- ⚪ C. Subtract
- ⚪ D. Find

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Toán tử 'and' nghĩa là object phải thỏa cả hai điều kiện, tức là phần giao của hai list, nên dùng list operation Intersect.

---

### Câu 34 [Security]

**Câu hỏi:** Which of the three buttons New, Edit, and Delete on the page Order Overview will be visible to the user if an entity access rule specifies that the user can create, delete, read and write Orders?

- ⚪ A. Just the New and Delete buttons
- ⚪ B. No buttons will be visible
- ✅ **C.** New Edit and Delete buttons
- ⚪ D. Just the Edit button

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Entity access cho phép create, delete, read và write Order thì cả ba nút New, Edit, Delete đều hiển thị, vì Mendix ẩn nút dựa trên quyền entity.

---

### Câu 35 [Microflows]

**Câu hỏi:** When an order is submitted, the Order and OrderLines will be committed to the database. Afterwards , the Customer should receive an email with the order details. Asa result. the Mendix developer adds the sub-microflow SUB_Order_SendCustomerEmail to the submit microflow. The developer wants to catch a possible error when sending an email so that the Order and OrderLines will definitely be committed. What type of error handling should the developer set on the C all microflow activity which calls the microflow SUB_Order_SendCustomerEmail?

- ⚪ A. Continue
- ⚪ B. Rollback
- ⚪ C. Custom with Rollback
- ✅ **D.** Custom without rollback

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Order và OrderLine đã commit trước khi gửi email. Đặt 'Custom without rollback' trên lời gọi SUB_Order_SendCustomerEmail để khi gửi mail lỗi thì dữ liệu đã commit không bị rollback, đồng thời vẫn bắt được lỗi để log.

---

### Câu 36 [UX & Logging]

**Câu hỏi:** What is the relationship between UX and UI?

- ⚪ A. UX is a sub-category of UI
- ⚪ B. UX and UI are mostly unrelated
- ⚪ C. UX and UI are at a core level the same thing
- ✅ **D.** Ul can be used to improve UX

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): UX là toàn bộ trải nghiệm của user, UI là phần giao diện. UI tốt là một phương tiện để cải thiện UX.

---

### Câu 37 [UX & Logging]

**Câu hỏi:** The width of a layout grid can be set to Full width or Fixed width. What is the difference?

- ✅ **A.** When set to Fixed width, the total column width of this layout will be exactly the width in pixels as specified in the style sheet. Full width will be the full available width of the page.
- ⚪ B. When set to Fixed width, the total column width of this layout will be exactly the width in pixels as specified in the style sheet. Full width will be the full width of the client.
- ⚪ C. When set to Fixed width, the total column width of this layout will be exactly 960 pixels centered in the page. Full width will be the full available width of the enclosing container.
- ⚪ D. When set to Fixed width, the input widgets width will be exactly the width in pixels as specified in the style sheet. When set to Full width the input widgets width will be the full width of the client.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Fixed width giới hạn tổng chiều rộng cột theo giá trị pixel trong stylesheet (container cố định). Full width chiếm toàn bộ chiều rộng khả dụng của trang.

---

### Câu 38 [Microflows]

**Câu hỏi:** When handling an error, what is the most appropriate use of a Continue element?

- ⚪ A. Within a “while” loop
- ⚪ B. Within a “for each” loop
- ⚪ C. After completing a loop
- ✅ **D.** When no rollback is needed

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Theo file gốc là 'When no rollback is needed'. ⚠ Chưa chắc: tài liệu Mendix nói Continue chỉ dùng được trên lời gọi microflow hoặc trong vòng lặp, và các thay đổi trong lần lặp hoặc lời gọi bị lỗi VẪN bị rollback. Đáp án hợp lý hơn có thể là dùng trong vòng lặp 'for each' để bỏ qua phần tử lỗi.

---

### Câu 39 [Security]

**Câu hỏi:** How do you handle access to a sub-microflow in relation to the parent microflow?

- ⚪ A. If you set the access to a sub-microflow, it overwrites access defined by the parent microflow.
- ⚪ B. When creating 3 sub-microfiow, you can choose whether you want to inherit the access rules from the parent microflow or to set it up independently.
- ✅ **C.** Access to a sub-microflow does not need to be set because itis handled by the parent microflow.
- ⚪ D. Access to a sub-microflow needs to be set up independently of the access to the parent microflow.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Sub-microflow được gọi từ microflow cha chạy với quyền của cha nên không cần gán module role. Gán role còn làm lộ sub-microflow ra client API.

---

### Câu 40 [Security]

**Câu hỏi:** When specifying entity access rules. what does “Limited access” mean?

- ⚪ A. The conditional visibility on a page is set to limit the access for the given user.
- ✅ **B.** At least one member is not allowed to be accessed by the user with a given module role.
- ⚪ C. A user that is assigned multiple user roles is limited to view only data corresponding to the currently logged in user.
- ⚪ D. The user with a given module role has no access to the data set.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): ✎ Đã sửa so với file gốc. Tài liệu Mendix: 'Limited access' nghĩa là có ít nhất một ràng buộc hoặc một phần không được phép truy cập; 'No access' mới là không có quyền gì. Phương án đúng là có ít nhất một member user không được truy cập.

---

### Câu 41 [Microflows]

**Câu hỏi:** Which of the following statements is true about the [reversed()] expression?

- ⚪ A. It can only be applied on *-* associations.
- ⚪ B. It can only be applied on 1-1 associations.
- ⚪ C. It can be applied to reverse a string attribute.
- ✅ **D.** It can only be applied on self-references.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Hàm reversed() dùng trong XPath trên association tự tham chiếu (self-reference) để đi theo chiều ngược lại của association, vì hai đầu cùng là một entity.

---

### Câu 42 [Microflows]

**Câu hỏi:** Why is it a Mendix best practice to use Decisions instead of if-then-else expressions?

- ✅ **A.** It increases readability and documentation.
- ⚪ B. It is faster than typing expressions.
- ⚪ C. It allows faster duplication of existing processes.
- ⚪ D. Decisions have better multilingual support.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Decision hiển thị nhánh logic trực quan trên sơ đồ microflow, dễ đọc và tự mô tả hơn biểu thức if-then-else lồng nhau.

---

### Câu 43 [XPath & General]

**Câu hỏi:** In a List view displaying a list of Orders, you want to add an XPath. The XPath should result in Orders where theOrderDate is within the past three years. Which XPath should you use?

- ✅ **A.** [OrderDate > ‘[%BeginOfCurrentDay%) - 3 * [%YearLength%]']
- ⚪ B. [OrderDate > '[3 * [%YearLength%]- %BeginOfCurrentDay%]']
- ⚪ C. [OrderDate < '[%BeginOfCurrentDay%] - 3 * [%YearLength%]']
- ⚪ D. [addYears(OrderDate, -3)]- [OrderDate < '[%BeginOfCurrentDay%]']

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Trong vòng 3 năm qua nghĩa là OrderDate lớn hơn (thời điểm đầu ngày hôm nay trừ 3 năm), viết bằng token: [%BeginOfCurrentDay%] - 3 * [%YearLength%].

---

### Câu 44 [XPath & General]

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

### Câu 45 [UX & Logging]

**Câu hỏi:** The default language of the app is English. United States (en_US) and Dutch. Netherlands (nl_NL) is an additional installed language. A user logs in and has the language Dutch. Netherlands (nl_NL) set as their user language. A button on a page doesn't have a caption but needs one. How should this be fixed?

- ⚪ A. Change the conditional visibility of the button so that the caption becomes visible for users with the Dutch language.
- ⚪ B. The caption must be set in the user language library and synced with the running app.
- ⚪ C. In both English and Dutch, the caption must be set in the correct
- ✅ **D.** The caption must be set in the Dutch language only.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): User dùng tiếng Hà Lan nên caption thiếu ở bản dịch nl_NL. Chỉ cần bổ sung caption tiếng Hà Lan (Language > nl_NL), bản tiếng Anh vẫn giữ nguyên.

---

### Câu 46 [XPath & General]

**Câu hỏi:** You need to retrieve the UserRole Employee in a microflow. Which XPath constraint should you use in the Retrieve from Database activity?

- ⚪ A. [Description = 'Employee']
- ⚪ B. [ModelGUID= '[%UserRole_Employee%]']
- ⚪ C. [Name = 'Employee']
- ✅ **D.** [id='[%UserRole_Employee%]']

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Mỗi user role có token [%UserRole_<Tên>%] đại diện cho id của role đó, nên dùng [id='[%UserRole_Employee%]'] để lấy chính xác role, không phụ thuộc tên hay mô tả.

---

### Câu 47 [Microflows]

**Câu hỏi:** In microflows, there are various security settings that can affect the creation of objects. Which of these statements about creating objects is true?

- ✅ **A.** A user can create an object with a microflow even if ‘Allow creating new ‘objects’ is disabled for them in the access rules of the entity.
- ⚪ B. A user will not be able to see any buttons that call microflows which create a particular object if ‘Allow creating new objects’ is tured off for their module role in the access rules of the entity.
- ⚪ C. An object can be created with a microflow if ‘Apply entity access’ is set to ‘Yes’ even if ‘Allow creating new objects’ is disabled for the user's module role in the access rules of the entity.
- ⚪ D. An object can only be created with a microfiow if ‘Apply entity access’ is set to ‘No’.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): ✎ Đã sửa so với file gốc. Tài liệu Mendix (Microflow Properties): mặc định microflow không áp dụng entity access, khi đó mọi thao tác đều được phép. Vì vậy user vẫn tạo được object qua microflow dù access rule tắt 'Allow creating new objects'.

---

### Câu 48 [Security]

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

### Câu 49 [Domain Model]

**Câu hỏi:** The Order entity has an attribute OrderDate of type Date and Time. A user in the time zone Amsterdam GMT+1 creates an Order and sets the date to April 16, 1991. Which DateTime value is stored in the database?

- ⚪ A. 1991-04-15 12:00:00
- ✅ **B.** 1991-04-15 23:00:00
- ⚪ C. 1991-04-16 00:00:00
- ⚪ D. 1991-04-16 01:00:00

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Thuộc tính DateTime localized được lưu theo UTC. 16/04/1991 00:00 giờ Amsterdam (GMT+1) tương ứng 15/04/1991 23:00 UTC.

---

### Câu 50 [UX & Logging]

**Câu hỏi:** What type of design has a focus on accessibility?

- ⚪ A. UX Design
- ✅ **B.** Usability Design
- ⚪ C. UI Design
- ⚪ D. Interaction Design

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Usability design chú trọng ứng dụng dễ dùng cho mọi người, trong đó có accessibility (người khuyết tật, tương phản màu, điều hướng bằng bàn phím…).

---

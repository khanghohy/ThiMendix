# Đề Thi Thử Mendix Advanced - Đề Số 2

- **Số lượng câu hỏi:** 50 câu
- **Thời gian làm bài quy định:** 120 phút
- **Tiêu chuẩn đạt:** Từ 75% (38/50 câu đúng)

---

### Câu 1 [Security]

**Câu hỏi:** In which of the following situations do you need to set the microflow access for a specified user?

- ⚪ A. When the microflow is set as an event handler
- ⚪ B. When the microflow is set a calculated attribute
- ⚪ C. When the microflow is a part of another parent microflow
- ✅ **D.** When the microflow is called from the navigation item

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Microflow được gọi trực tiếp từ client (navigation item, button) cần cấu hình microflow access cho role. Event handler, calculated attribute và sub-microflow được gọi nội bộ từ server nên không cần.

---

### Câu 2 [Microflows]

**Câu hỏi:** In this sub-microflow, you want to return an integer/long containing the number of years between two dates. What would be the best way to calculate the number of years between two dates?

- ⚪ A. Use the ‘YearsBetween’ JAVA action available in the CommunityCommons module.
- ✅ **B.** Use the ‘calendarYearsBetween’ Date Function Call, which is available by default in Studio Pro.
- ⚪ C. Create a loop that repeatedly adds one year from the start date until the end date, then counts how many fit between the two dates.
- ⚪ D. Use the ‘yearsBetween’ Date Function Call, which is available by default in Studio Pro.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): calendarYearsBetween là hàm có sẵn, tính số năm theo lịch giữa hai ngày một cách chính xác. yearsBetween cũ tính theo số ngày chia trung bình nên có thể sai lệch.

---

### Câu 3 [UX & Logging]

**Câu hỏi:** When should you use the data source type Association when displaying a list on a page?

- ✅ **A.** When you need to show all associated OrderLines of an Order and there are no additional constraints needed.
- ⚪ B. Always when you need to show all associated OrderLines of an Order in a native app.
- ⚪ C. Always when you want to show the associated OrderLines of an Order.
- ⚪ D. When you need to show all associated OrderLines of an Order with uncommitted changes.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Data source Association lấy object qua association từ object cha (kể cả object chưa commit). Dùng khi cần hiển thị toàn bộ OrderLine của Order mà không cần ràng buộc thêm; cần lọc thì dùng Database/XPath.

---

### Câu 4 [Security]

**Câu hỏi:** You want to show customers only their own orders in a data grid. Which of the following ‘options is the most secure way to achieve this?

- ⚪ A. Configure conditional visibility on the page.
- ⚪ B. Set a microfiow retrieving the orders of the user as a data source of the data grid widget.
- ⚪ C. Add a data grid constraint.
- ✅ **D.** Add an XPath constraint in the entity access rule of the Order entity, restricting the access to the currently logged-in user.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): XPath trong access rule của entity được runtime áp dụng cho mọi truy vấn, nên an toàn nhất. Visibility hay constraint trên page chỉ là hiển thị và có thể bị vượt qua.

---

### Câu 5 [Microflows]

**Câu hỏi:** What do you use to pass an error to a parent microflow?

- ⚪ A. Rollback
- ✅ **B.** Error End Event element
- ⚪ C. Continue element
- ⚪ D. Nothing, this is default behavior

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Error End Event kết thúc microflow con ở trạng thái lỗi, nên lỗi được ném tiếp lên microflow cha để cha xử lý.

---

### Câu 6 [XPath & General]

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

### Câu 7 [Domain Model]

**Câu hỏi:** When a DateTime attribute is localized, the value stored in the database will be formatted in:

- ⚪ A. The client server time zone
- ⚪ B. The database server time zone
- ⚪ C. The application server time zone
- ✅ **D.** The UTC time zone

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Thuộc tính DateTime localized luôn được lưu theo UTC trong database, rồi chuyển sang múi giờ của user khi hiển thị.

---

### Câu 8 [Security]

**Câu hỏi:** In which of the following cases should the Navigation setting “visible for” be set?

- ⚪ A. All the pages in the app.
- ✅ **B.** All the pages in the app excluding the role-based pages
- ⚪ C. All pages which are not marked as home or role-based pages
- ⚪ D. All the pages in the app excluding the home-web page

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): 'Visible for' của navigation item phụ thuộc page access. Các page dùng làm role-based home page đã gắn theo role nên không cần cấu hình thêm; các page còn lại cần đặt quyền tương ứng.

---

### Câu 9 [XPath & General]

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

### Câu 10 [Security]

**Câu hỏi:** Which of the following statements is true?

- ✅ **A.** Entity access rules are applied on the request from the runtime to the database.
- ⚪ B. Entity access rules are applied on the request from the client to the runtime
- ⚪ C. Entity access rules are applied by the runtime after the return of the database requests.
- ⚪ D. Entity access rules are applied on the return from the runtime to the client.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): XPath của entity access được runtime thêm vào câu query gửi xuống database, nên dữ liệu user không được phép xem sẽ không bao giờ được truy vấn ra.

---

### Câu 11 [UX & Logging]

**Câu hỏi:** Which of the following log messages follows the best practices for a Debug log message?

- ⚪ A. Rest service has returned 404
- ⚪ B. “Unknown user input '129q', unable to process value.”
- ✅ **C.** “User language has not been set yet.”
- ⚪ D. “Contacting REST service.”

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Theo file gốc là 'User language has not been set yet.'. ⚠ Nên xem lại: theo tài liệu Mendix, Debug là thông tin chi tiết dùng để chẩn đoán lỗi, còn Warning là khi có điều bất thường. Theo định nghĩa đó, 'Contacting REST service.' hợp với Debug hơn.

---

### Câu 12 [XPath & General]

**Câu hỏi:** You need to retrieve the employee information based on the current user to display the ‘employee's information on the account overview page. Which of the following suggestions represent the correct and optimal XPath?

- ⚪ A. [Production.Customer_Account = $currentUser]
- ⚪ B. [Production.Employee_Account/Administration.Account/id = $currentUser]
- ✅ **C.** [Production.Employee_Account = '[%CurrentUsers%]']
- ⚪ D. [Production.Employee_Account/AdministrationAccount/id = '[%CurrentUsers%]']

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): So sánh trực tiếp association Employee_Account với token '[%CurrentUser%]' là ngắn gọn và tối ưu nhất. $currentUser không dùng được trong XPath của page.

---

### Câu 13 [Domain Model]

**Câu hỏi:** Non-persistable entities are stored in the runtime memory and are never committed to the database. Therefore. they have no table in the database. Does it make sense to commit a non- Persistent object?

- ⚪ A. Yes, because othenwise the object cannot be retrieved over association.
- ✅ **B.** Yes. committing non-persistable entities records the current attribute values and association values in memory, allowing a rollback to revert to these values. a
- ⚪ C. No. non-persistable entities are never committed.
- ⚪ D. Yes. because Mendix will create a table in the database and store the object in the database.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Commit một object non-persistable không ghi xuống database, nhưng 'chốt' lại giá trị thuộc tính và association hiện tại trong bộ nhớ. Khi rollback, object quay về trạng thái đã commit này.

---

### Câu 14 [UX & Logging]

**Câu hỏi:** Which log message component is generated only for cloud-deployed applications?

- ✅ **A.** Source
- ⚪ B. Log Node
- ⚪ C. Log Level
- ⚪ D. Timestamp

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Trên Mendix Cloud, mỗi dòng log có thêm thông tin Source (instance hoặc nguồn phát sinh log); timestamp, log level và log node thì môi trường nào cũng có.

---

### Câu 15 [Microflows]

**Câu hỏi:** Why would you use two identical database retrieves in one microflow?

- ⚪ A. When speed and memory usage are not a concern.
- ✅ **B.** To optimize both retrieves if they are followed immediately by Aggregate list activities.
- ⚪ C. For readability. The second retrieve will not result in a database call.
- ⚪ D. To free up memory between the first retrieve and the second.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Khi Retrieve from database theo sau ngay là Aggregate list (Count, Sum…) và list không dùng vào việc khác, Mendix gộp thành một câu query aggregate. Hai retrieve giống nhau cho hai aggregate khác nhau thì cả hai đều được tối ưu.

---

### Câu 16 [XPath & General]

**Câu hỏi:** You would like to replace an XPath that utes the logical 'or' operator with a microfiow using. two Retrieves and a List operation. Which of the following List operations should you use?

- ⚪ A. Find
- ✅ **B.** Union
- ⚪ C. Subtract
- ⚪ D. Intersert

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Toán tử 'or' nghĩa là object thỏa ít nhất một điều kiện, tức là hợp hai list, nên dùng list operation Union.

---

### Câu 17 [Domain Model]

**Câu hỏi:** In an app,a user can create orders. It is required that each order gets a unique order number.The order number is constructed from the customer number and the date when ordered.When should you determine the order number value and store it?

- ⚪ A. In a before commit event on the Order entity.
- ⚪ B. In the microflow which commits the Order afterthe Order is entered.
- ⚪ C. In an after create event on the Order entity.
- ✅ **D.** In the microflow which creates the order object and opens the Order_New page.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Số đơn hàng ghép từ mã khách hàng và ngày đặt, cả hai đã có ngay lúc tạo Order. Gán giá trị trong microflow tạo Order (trước khi mở trang Order_New) giúp logic rõ ràng, tránh dùng event handler chạy ngầm mỗi lần commit.

---

### Câu 18 [UX & Logging]

**Câu hỏi:** You are building a responsive web page where you only want some of the existing columns to be visible on tablets. How can you use bootstrap to achieve this?

- ✅ **A.** By using the visible-sm and hidden-sm helper classes
- ⚪ B. By using conditional visibility based on device type
- ⚪ C. By creating a tablet specific page
- ⚪ D. By adding the col-sm-0 helper class to the columns you want to hide

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Bootstrap có helper class visible-*/hidden-* theo kích thước màn hình (sm = tablet) để ẩn/hiện cột mà không cần trang riêng.

---

### Câu 19 [XPath & General]

**Câu hỏi:** We have five trainees: two without registrations, one with a discount of 30, and two with discounts of 50. How many trainee objects will the following XPath return? [not(Training.Registration_Trainee/Training.Registration/Discount = 30)]

- ⚪ A. 5 trainees
- ⚪ B. 1 trainees
- ✅ **C.** 4 trainees
- ⚪ D. 2 trainees

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): not(... = 30) lấy mọi trainee KHÔNG có registration discount 30, gồm cả trainee không có registration. Vậy 5 - 1 = 4 trainee.

---

### Câu 20 [Security]

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

### Câu 21 [Domain Model]

**Câu hỏi:** Which statement is true about localized DateTime attributes?

- ✅ **A.** Use non-localized attributes if you are not interested in the time component or if you want a date to look exactly the same all over the world.
- ⚪ B. Use non-localized attributes if you are interested in the time component (for example, birthdays) or if you want a date to look exactly the same all over the world.
- ⚪ C. It doesn’t matter if you localize a DateTime Attribute because the end user will never see the difference. The difference is only visible in the backend.
- ⚪ D. Use localized attributes if you are interested in the time component (for example, birthdays) or if you want a date to look exactly the same all over the world.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): ✎ Đã sửa so với file gốc. Tài liệu Mendix (Attributes > Localize): nếu KHÔNG quan tâm phần giờ và muốn ngày giống hệt nhau ở mọi nơi trên thế giới (ví dụ ngày sinh) thì tắt Localize, tức là dùng non-localized.

---

### Câu 22 [UX & Logging]

**Câu hỏi:** What is one method of applying typographical hierarchy to a page?

- ⚪ A. Ordering multiple languages appropriately in settings
- ⚪ B. Creating a sticky footer
- ✅ **C.** Changing text size
- ⚪ D. Adding sort constraints

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Typographic hierarchy là dùng kích thước, độ đậm và kiểu chữ khác nhau (ví dụ H1, H2, body) để thể hiện mức độ quan trọng của nội dung.

---

### Câu 23 [UX & Logging]

**Câu hỏi:** How are logs stored in the Mendix Cloud?

- ⚪ A. Within multiple log files organized by log level
- ✅ **B.** Within multiple log files organized by time periods
- ⚪ C. Within multiple log files capped at a particular file size
- ⚪ D. Within a single log file that is cleared periodically

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Mendix Cloud lưu log thành nhiều file theo khoảng thời gian (theo ngày), có thể tải về theo ngày trong Developer Portal.

---

### Câu 24 [Domain Model]

**Câu hỏi:** Is it preferable to use one-to-one associations or inheritance in a system with a high transaction volume? (Multiple changes or creates per second)

- ⚪ A. There is no preference because they will both have the same performance.
- ⚪ B. Inheritance, because writing and updating a single table is faster than updating records in multiple tables.
- ⚪ C. Both a one-to-one association and inheritance in the same entity.
- ✅ **D.** One-to-one associations, because writing and updating records in tables with inheritance is slower than just updating a single table.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): ✎ Đã sửa so với file gốc. Tài liệu Mendix (Generalization vs One-to-One Associations) nói rõ: ghi và cập nhật bản ghi trong bảng có kế thừa chậm hơn chỉ cập nhật một bảng, vì kế thừa ghi vào cả bảng cha lẫn bảng con. Với nhiều thay đổi mỗi giây thì nên chọn association 1-1.

---

### Câu 25 [XPath & General]

**Câu hỏi:** You need a list of all products which have been ordered once by the customer or on the ‘Favorites’ list of that customer. The following XPath is used in a microflow to retrieve that list from the database. How can you optimize this XPath to increase the performance of the app?

- ✅ **A.** By executing the comparison on the Customer object in a subquery, [Product [AdvancedModule. OrderLine_Product/AdvancedModule OrderLine/ AdvancedModule.Orderline_Order/AdvancedModule.order [AdvancedModule.Customer = SCustomer or AdvancedModule.Customer_ProductFavorite = $Customer])
- ⚪ B. By executing the comparison on the Customer object in a subquery, the or statement can be changed to an and statement. which is better performing. //Product [AdvancedModule. OrderLine_Product/AdvancedModule Ordertine/ AdvancedModule.Ordertine Order [AdvancedModule.Order_Customer = SCustomer and AdvancedModule.Customer_ProductFavorite = $Customer)
- ⚪ C. By retrieving all Products from the database without a constraint. iterating through this list ProductList and retrieving the Customers who have the IteratorProduct on their favorite list and have ordered it. Check if this CustomerList contains the affected Customer, If itis 2 part of the CustomerList. then add the product on the ProductFinal list. f not. continue with the next IteratorProduct.
- ⚪ D. By retrieving a list of already ordered products Productlist_Ordered and a list of favorite products ProductList_ Favorite separately, and joining them into a single list ProductList_Total. The ProductList_Ordered is achieved via the Retrieve from database activity with XPath: IADV20.0rderLine_Product/ADV20.0rderLine/ADV20.Ordertine_Order/ ADV20.0rder/ADV20.0rder_Customer= SCustomer] . The ProductList_Favorite is achieved via the Retrieve from database activity with XPath {ADV20.Customer_ProductFavorite = SCustomer). The ProductList_Total is obtained using the Union List operation applied to the ProductList_ Ordered and ProductList Favorite lists.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Gom điều kiện về Customer vào một subquery trên đường association giúp database xử lý trong một câu query, thay vì nhiều nhánh truy vấn riêng.

---

### Câu 26 [XPath & General]

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

### Câu 27 [XPath & General]

**Câu hỏi:** You want to constrain a list of objects retrieved from the database using an XPath where the ReleaseDate is more than a year from now. Which XPath expression should you use to check this?

- ⚪ A. [ReleaseDate >='%YearLength%']
- ⚪ B. [ReleaseDate >= addYears([%CurrentDateTime%], 1)]
- ⚪ C. [ReleaseDate >='[% YearLength%]']
- ✅ **D.** [ReleaseDate >= ('[%CurrentDateTime%] + [%YearLength%]')]

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Thời điểm sau một năm tính bằng '[%CurrentDateTime%] + [%YearLength%]' (token cộng thời gian trong XPath). Hàm addYears không dùng được trong XPath constraint.

---

### Câu 28 [XPath & General]

**Câu hỏi:** To be admitted to the Solution Architecture workshop, trainees should have either an Intermediate or Advanced certificate. You have created an enumeration with values ‘RAD’, ‘INT” and ‘ADV’ of String data type, representing Rapid. Intermediate and Advanced certificates respectively. Each Trainee has a Badge attribute of the String data type. which stores the latest attained certificate type, You created a page with a List view, where the Data source is set to Training.Trainee by XPath. How should you write an XPath constraint to limit admissions of trainees only to the Intermediate and Advanced certificates?

- ⚪ A. [ Badge = (INT or ADV) ]
- ⚪ B. ..
- ⚪ C. not[Badge = 'RAD']
- ✅ **D.** [ Badge = ‘INT’ or Badge = ‘ADV’ ]

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Badge là String nên so sánh với giá trị trong nháy và nối bằng 'or': [Badge = 'INT' or Badge = 'ADV'].

---

### Câu 29 [Microflows]

**Câu hỏi:** In Mendix, commits in loop should be avoided. What is the best way to improve this microflow?

- ⚪ A. Create a list Orders ToBeCommitted before the loop. Add changed objects within the loop to Orders ToBeCommitted. Commit the OrdersToBeCommitted list after the loop.
- ⚪ B. Add a Commit activity after the loop to commit the OrderList list.
- ✅ **C.** Uncheck Commit within the Change Object activity. Add a Commit activity, and nothing else, after the loop to commit the OrderList list.
- ⚪ D. Create a list OrdersToBeCommitted before the loop. Add changed objects within the loop to Orders ToBeCommitted. Commit the OrderList list after the loop.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Bỏ chọn Commit trong Change Object trong vòng lặp, sau vòng lặp commit cả OrderList một lần. Làm vậy chỉ tốn một lần ghi theo lô thay vì commit từng object.

---

### Câu 30 [XPath & General]

**Câu hỏi:** We have five trainees: two without registrations. one with a discount of 30, and two with discounts of 50. How many trainee objects will the following XPath retuin? [Training.Registration_Trainee/Trainin.Registration/Discount != 30]

- ⚪ A. 4 trainee
- ✅ **B.** 2 trainee
- ⚪ C. 1 trainee
- ⚪ D. 5 trainee

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): '!= 30' qua association chỉ đúng khi tồn tại một registration có discount khác 30. Trainee không có registration và trainee có discount 30 bị loại, còn 2 trainee có discount 50.

---

### Câu 31 [Security]

**Câu hỏi:** Imagine that in the Domain Model of your app, there is a cascading delete configured between two entities. What happens if you are not allowed to delete all of the objects you've planned to delete?

- ✅ **A.** All the objects will be deleted besides the conflicted ones
- ⚪ B. An error message will be shown in the Console log
- ⚪ C. All the objects will remain unaffected.
- ⚪ D. The cascading delete will e rolled-back

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Theo file gốc (ô tô màu vàng): các object được phép xóa vẫn bị xóa, chỉ object không có quyền thì được giữ lại. ⚠ Tài liệu chính thức không mô tả trường hợp này, nên giảng viên cần tự kiểm chứng.

---

### Câu 32 [Microflows]

**Câu hỏi:** When is it advised to apply custom error handling?

- ✅ **A.** With Rest integration activities
- ⚪ B. When committing a list with more than 10 objects
- ⚪ C. When creating an object with a population of members
- ⚪ D. Before commit event handlers

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Tích hợp REST phụ thuộc hệ thống ngoài nên có thể lỗi bất kỳ lúc nào. Custom error handling giúp bắt lỗi, log và thông báo thay vì làm hỏng cả transaction.

---

### Câu 33 [UX & Logging]

**Câu hỏi:** How does Sass help with styling?

- ⚪ A. It is a more capable styling language than CSS.
- ⚪ B. It simplifies security rules which hide UI elements.
- ✅ **C.** It processes CSS to avoid repetitive work.
- ⚪ D. It directly formats HTML content for better UX.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Sass là bộ tiền xử lý CSS: có biến, mixin, nesting, import… giúp tránh lặp code, rồi được biên dịch ra CSS thường.

---

### Câu 34 [Microflows]

**Câu hỏi:** Which variable is predefined with error information within a microflow?

- ⚪ A. System.EventStatus
- ⚪ B. $CurrentSession
- ✅ **C.** $latestError
- ⚪ D. System.EventStatus

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Trong error handler, biến $latestError (kiểu System.Error) có sẵn và chứa thông tin lỗi (message, stacktrace). Với lỗi web service còn có $latestSoapFault, với REST có $latestHttpResponse.

---

### Câu 35 [UX & Logging]

**Câu hỏi:** Customers can receive up to 3 samples with their order out of 5 options. What would be the most intuitive widget to use for their selection?

- ⚪ A. The enumeration widget
- ✅ **B.** The check box widget
- ⚪ C. The radio buttons widget
- ⚪ D. The drop-down widget

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Chọn tối đa 3 trong 5 mẫu là chọn nhiều, nên dùng check box (mỗi lựa chọn một ô). Radio button và drop-down chỉ chọn được một.

---

### Câu 36 [XPath & General]

**Câu hỏi:** On the Product_Overview page, you have placed the List view widget and configured the Data source as the entity Production.Product by XPath [Production.ProductReview_Product/ProductReview]. What data do you expect to be listed on this page once previewing the app?

- ⚪ A. A list of all product reviews
- ✅ **B.** A list of products associated to product review
- ⚪ C. A list of all products
- ⚪ D. A list of products with a review

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Ràng buộc [ProductReview_Product/ProductReview] chỉ giữ Product có ít nhất một ProductReview liên kết, nên trang liệt kê các product có review.

---

### Câu 37 [UX & Logging]

**Câu hỏi:** You have a microflow that calls a REST service. You update that microflow with new activities and it stops working. Which Log Node should you use to investigate?

- ⚪ A. REST Consume
- ⚪ B. REST Publish
- ⚪ C. ConnectionBus Retrieve
- ✅ **D.** MicroflowEngine

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Lỗi xuất hiện sau khi sửa các activity trong microflow, nên đặt log node MicroflowEngine lên Debug/Trace để theo dõi microflow chạy từng bước.

---

### Câu 38 [Microflows]

**Câu hỏi:** What is the behavior of the list operation Head?

- ⚪ A. The first object on the list will be removed. and all other objects returned.
- ✅ **B.** It returns the first object of the sorted list.
- ⚪ C. All objects will be removed from the list except the last one which will be retuned.
- ⚪ D. It returns all objects of a sorted list except the last one.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): List operation Head trả về object đầu tiên của list (theo thứ tự sắp xếp nếu có), kết quả là một object chứ không phải list.

---

### Câu 39 [Domain Model]

**Câu hỏi:** You want to use a List view to display all products as well as their specialized attributes. Is this possible?

- ⚪ A. No. but it is possible with a data grid.
- ✅ **B.** Yes, the widget will allow you to create a specific template for each specialization.
- ⚪ C. No, you will only be able to display the general attributes.
- ⚪ D. Yes, but you will have to set visibilities to avoid irrelevant attributes from being shown.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): List view hỗ trợ template riêng cho từng specialization: khi data source là entity cha, có thể thêm template cho Book, Music… để hiển thị thuộc tính riêng của từng loại.

---

### Câu 40 [UX & Logging]

**Câu hỏi:** What is one of the 4 main phases of the UX project process?

- ✅ **A.** User Journey
- ⚪ B. Mock-up
- ⚪ C. Realize
- ⚪ D. Feedback

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Theo file gốc (ô tô màu vàng): User Journey là một trong các giai đoạn chính của quy trình UX, giúp hiểu hành trình và nhu cầu user trước khi thiết kế.

---

### Câu 41 [UX & Logging]

**Câu hỏi:** Throughout an entire app, you want to display the values of DateTime attributes for users with the language English, United States (en_US) as M-dd-yyy (4/23/2018), and for users with the language Dutch, Netherlands (nl_NL) as dd-M-yyy (23-4-2018), What is the best way to achieve this?

- ⚪ A. This isn’t possible: each language has a predefined fixed default date and time format.
- ⚪ B. Set the date format in the system settings.
- ⚪ C. Set the date format in the text widget captions per language.
- ✅ **D.** Set the date format in the language settings.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Định dạng ngày giờ được cấu hình theo từng ngôn ngữ trong App Settings > Languages, nên áp dụng cho toàn app tùy ngôn ngữ của user.

---

### Câu 42 [Microflows]

**Câu hỏi:** In addition to a Published REST Service, what other Mendix document type is required to set up a POST method?

- ⚪ A. Published web service
- ⚪ B. Data set
- ⚪ C. Java action
- ✅ **D.** Import mapping

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): Phương thức POST nhận JSON/XML trong body, nên cần Import mapping để chuyển payload thành object Mendix.

---

### Câu 43 [Microflows]

**Câu hỏi:** When handling errors, how should system-triggered and user-triggered microflows be handled?

- ⚪ A. Both should only be shown in a user visible message when Trace debugging is implemented.
- ✅ **B.** System-triggered microflow errors should be logged and user-triggered microflow errors should be shown in a user visible message
- ⚪ C. System-triggered microflows should have a Custom with Rollback error handling implemented and user-triggered microflows should have Custom without Rollback.
- ⚪ D. System-triggered microflow errors don't require error handling but user-triggered microflows do.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Microflow do hệ thống chạy (scheduled event, after startup…) không có user nhìn thấy, nên lỗi cần được log. Microflow do user bấm nên hiện thông báo dễ hiểu cho user.

---

### Câu 44 [Microflows]

**Câu hỏi:** You have a list of Order objects and you need the sum of their amounts. As seen below, you could do this with either a variable and loop, or with an aggregate list activity. Why is the aggregate list method the preferred best practice in this situation?

- ✅ **A.** The loop method has worse performance.
- ⚪ B. The loop method could cause dirty writes.
- ⚪ C. The aggregate list activity is easier to configure.
- ⚪ D. The aggregate list method is more readable.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Aggregate list sau retrieve được Mendix tối ưu thành một câu SUM chạy trên database. Vòng lặp phải tải mọi object vào bộ nhớ rồi cộng từng cái, nên chậm hơn.

---

### Câu 45 [Security]

**Câu hỏi:** To ensure that the right information is shown on a page. you have different options when it comes to differences between security and usability. Which of the following statements is true?

- ⚪ A. Only what is secure will eventually be usable and accessible from the Mendix Client.
- ✅ **B.** Usability is not security. adding a conditional visibility on a page does not result in a secure app.
- ⚪ C. What is accessible from the Mendix client is by definition secure.
- ⚪ D. Usability is secunty, adding a conditional visibility on a page results in a secure app.

> **Đáp án đúng:** **B**  
> **Giải thích:** Giải thích (B): Usability khác security: conditional visibility chỉ ẩn trên giao diện, dữ liệu vẫn có thể lấy qua API. Bảo mật phải đặt ở entity access, page access và microflow access.

---

### Câu 46 [Security]

**Câu hỏi:** Sometimes the module security matrix highlights cells in yellow Why is this?

- ✅ **A.** Yellow cells indicate microfiows that have module roles assigned to them but are never used in the client API
- ⚪ B. Yellow cells indicate microflows that have no module roles assigned to them, but the microflow is used in the client API
- ⚪ C. The yellow cells indicate that these microflows have a completed security configuration
- ⚪ D. Yellow cells indicate microflows that have a module role assigned that is not linked to a User Role.

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Ô vàng trong security matrix cảnh báo microflow đã được gán module role nhưng không được dùng ở client (page, navigation…). Microflow như vậy bị lộ qua API mà không cần thiết, nên bỏ role.

---

### Câu 47 [UX & Logging]

**Câu hỏi:** Which statement about building blocks is true?

- ⚪ A. A building block can be selected as a template when you create a new page.
- ⚪ B. A building block is a widget which can be downloaded from the Mendix Marketplace.
- ⚪ C. A building block is a page element which can be maintained on a single location, and all changes will be automatically applied to all locations where this building block is used.
- ✅ **D.** A building block is a collection of widgets styled with CSS classes in a way that suits a specific use case.

> **Đáp án đúng:** **D**  
> **Giải thích:** Giải thích (D): ✎ Đã sửa so với file gốc. Tài liệu Mendix (Pages): building block là bộ widget đã tạo kiểu sẵn, xuất hiện trong toolbox để tái sử dụng. Mô tả 'sửa một chỗ, áp dụng mọi nơi' là của snippet, không phải building block.

---

### Câu 48 [Domain Model]

**Câu hỏi:** What is the owner of an association?

- ✅ **A.** It is the entity from which the association is created.
- ⚪ B. It is the user that created the association.
- ⚪ C. It is the entity in which the association is stored,
- ⚪ D. It is the user that set the association,

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Owner của association là entity mà association được vẽ từ đó (phía 'parent' trong domain model). Phía owner là phía giữ và thay đổi tham chiếu, không phải một user.

---

### Câu 49 [Domain Model]

**Câu hỏi:** You want every product to have an image. Which of the following statements is true?

- ✅ **A.** Using a specialization of the Image entity allows for a more specific security setup.
- ⚪ B. You can add new attributes to the Image entity.
- ⚪ C. The Image entity is a generalization of the Document entity.
- ⚪ D. It is impossible to create an association to the Image entity,

> **Đáp án đúng:** **A**  
> **Giải thích:** Giải thích (A): Tạo entity riêng kế thừa System.Image (ví dụ ProductImage) cho phép đặt access rule riêng cho ảnh sản phẩm. Không sửa được System.Image; Image là specialization của FileDocument chứ không phải ngược lại.

---

### Câu 50 [Microflows]

**Câu hỏi:** How can you ensure that a certain microflow is always called when a user logs in to an application?

- ⚪ A. Set this microflow as the After Startup microflow.
- ⚪ B. This is not possible. You must place a button on the homepage to be pressed manually by the user every time they log in.
- ✅ **C.** In the App Navigation, choose a microflow as the default home page.
- ⚪ D. Call this microflow from an After Commit Event Handler in the Administration.Account entity.

> **Đáp án đúng:** **C**  
> **Giải thích:** Giải thích (C): Đặt một microflow làm home page (default hoặc theo role) trong Navigation thì microflow đó chạy mỗi khi user đăng nhập. After Startup chỉ chạy một lần khi ứng dụng khởi động.

---

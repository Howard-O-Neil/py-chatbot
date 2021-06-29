## Xây dựng chatbot hỗ trợ doanh nghiệp phần mềm
## Thành viên:
  - Trần Minh Khôi &emsp;&emsp;&emsp;&ensp; 18520947
  - Phạm Thăng Long &emsp;&emsp; 18521051

## Tổng quan đồ án

#### Bối cảnh
- Trong tình hình công nghệ phát triển như hiện nay, việc xây dựng một môi trường, văn hóa làm việc hiện đại, đổi mới và minh bạch là một nhu cầu thiết yếu của các công ty, tập đoàn mưu cầu sự phát triển bền vững.
- Chúng ta bàn về doanh nghiệp phát triển phần mềm. Tiếp nhận yêu cầu, tầm nhìn và chiến lược từ khách hàng; triển khai sản phẩm phần mềm phù hợp với `UserStory` của khách hàng; là một trong những việc mang lại nhiều lợi nhuận nhất cho công ty phần mềm. Thế nhưng để có được lợi nhuận tối ưu nhất cho cả 2 bên, ta cần phải deal được giá tốt với khách hàng.
- Đây là vấn đề đã không mấy xa lạ với các doanh nghiệp gia công phần mềm. Ta có thể thấy cụm từ `OT` trong ngành phần mềm được đề cập khá phổ biến. Khi ước tính giá cả thấp hơn so với chi phí phần mềm thực tế, việc các nhân viên phải `làm thêm giờ` để kịp tiến độ phần mềm là điều không hiếm gặp.
- Để ra được giá cả tối ưu với khách hàng, ta phải ước tính được chi phí để gia công phần mềm; làm phần mềm này hết bao nhiêu thời gian; chi phí thuê máy chủ, hosting hết bao nhiêu tiền. Vấn đề về tiền bạc trong quá trình phát triển phần mềm khá là dễ ước lượng; nhưng việc ước lượng thời gian gia công phần mềm là điều không hề dễ. Việc này phụ thuộc rất nhiều vào yếu tố con người, vốn là một việc khó dự đoán.
- Các công ty thường quản lý dự án theo các `Project-Management Framework` ví dụ như là `Scrum`, `WaterFall`, `XPM`... Trong các framework quản lý dự án, điển hình là `Scrum`; framework quản lý được sử dụng trong công ty; framework chia project thành các `Sprint` kéo dài 2 tuần, mỗi Sprint sẽ có 1 số lượng `Backlog` (việc cần làm) nhất định, mỗi Backlog có nhiều `Task` (tác vụ). Mục tiêu của 1 Sprint trong Scrum là team `Deliver` được hết các Backlog. Câu hỏi đặt ra bây giờ là project này sẽ lên `UAT` (User Acceptance Testing) trong bao nhiêu `Sprint` ?
- Để ước tính được số `Sprint`, phân bổ `Backlog` hợp lý cho mỗi Sprint. Trong quản trị dự án bằng `Scrum` chúng ta có một khái niệm đó là `Metrics`. Metrics là dữ liệu thu thập được trong quá trình làm dự án; Metrics giúp ước lượng chi phí dự án chính xác hơn; càng nhiều Metrics, Metrics càng chính xác, ước lượng chi phí dự án sẽ sát với thực tế hơn. Ở mỗi công ty ứng dụng các Framework khác nhau có cách định nghĩa Metrics khác nhau, tùy theo chiến lược của công ty; khái quát chung, Metrics có thể được đặc trưng bởi các thành phần sau
  - `Logwork`: Thời gian hoàn thành 1 `Task` của 1 người trong team
  - `Velocity`: Số giờ trung bình của team để deliver 1 `Point`; Velocity lý tưởng của 1 dự án thường là 1 (trong 1h deliver được 1 `Point`)
    - `Point` có thể hiểu là điểm của 1 Backlog. 1 Backlog bao gồm Point và Task. Lí tưởng nhất theo [pmi.org](https://www.pmi.org/), một Point nên tương đương với 1 giờ; nghĩa là nếu ta ước lượng 1 Backlog là 5 points, ta đang giả định team có thể làm xong backlog đó trong 5 tiếng.
  - `Workload`: Số giờ 1 người trong team **cam kết** làm việc trong 1 `Project-Working Week` (tuần của dự án)
    - tuần dự án khác tuần thông thường; 1 tuần thông thường bắt đầu từ thứ 2, kết thúc vào thứ 7, tuần dự án có thể bắt đầu thứ 7, kết thúc thứ 6. Một số trường hợp đặc biệt, tuần dự án chỉ có 4 ngày thay vì 7, tuy nhiên case này khá là hiếm gặp.
  - `Review tuần`: Mỗi người team tự review lại `Project-Working Week` của mình. Có gì tốt, có gì xấu diễn ra trong tuần dự án vừa rồi
- Tạo ra một hệ thống phần mềm để thực thi quản trị `Scrum` là cần thiết, nhưng vấn đề đặt ra là: làm sao để nhân viên làm quen với cách quản trị dự án bằng `Scrum`; làm sao để nhân viên chủ động hơn, thoải mái hơn trong chuyện `Logwork`, `Tracking Team's Velocity`, `Update Workload`, `Review tuần`. Nhân viên cũ còn chưa chắc đã làm đúng, nhân viên mới lại càng khó hơn.
- Ta có nhiều cách để giải quyết vấn đề, một trong những cách thú vị và hay ho đó là sử dụng `Chatbot`. Ý tưởng là ta tạo một con Chatbot tích hợp với các flatform nhắn tin (Ex: Facebook Messenger) để tương tác với nhân viên; nhân viên có thể ra lệnh cho Chatbot (Ex: `Logwork`); Chatbot có thể thông báo, cập nhật thông tin cho nhân viên (Ex: `Velocity` của team cao quá).
- Việc xây dựng `Chatbot` không những giúp doanh nghiệp xây dựng được văn hóa làm việc hiện đại, sống động, bên cạnh đó còn giúp nhân viên chủ động hơn trong việc thực thi `Scrum` để quản lý công việc. Càng về lâu, về dài, `Metrics` thu thập được càng nhiều, ước lượng chi phí phần mềm sẽ chính xác hơn. 

#### Hạ tầng hệ thống (System Infrastructure)

![py-chatbot-architecture](https://i.imgur.com/691PwEj.png)

##### <u>chú thích</u>
- **Application** là `Container` chứa các `Business Logic` của công ty, phục vụ cho mục đích thực thi `Scrum` để quản trị dự án
- **AWS EC2** là dịch vụ `Hosting` được cung cấp để host các service, website...
- **Dialogflow** là engine sử dụng `AI` để xây dựng một `NLP model`
  - `NLP model` bản chất là một con bot có khả năng chiết xuất được `Intent` (ý định) từ input của người dùng, từ đó thực hiện `Action` (hành động) tương ứng với Intent đó
  - `Intent` và `Action` là do mình thiết kế và đưa vào Chatbot
  - Mỗi `Intent` ứng với một tập các input và một `Action`; ta tổng hợp các input phổ biến và đưa và train cho con bot; con bot sẽ tự nhận biết Input từ người dùng là thuộc Intent nào, từ đó thực hiện Action tương ứng

#### Tiến độ

###### Đã hoàn thành
|Epics|
|-|
|Setup Application với Flask và Map thư viện vào VirtualENV
|Thiết kế  và cài đặt hạ tầng ứng dụng với Docker
|Thiết kế  và cài đặt Database Migration Cli với SqlAlchemy
|Thiết kế  và cài đặt cấu trúc Database
|Thiết kế cấu trúc Application's source-code
|Setup Team-Working Space trong DialogFlow
|Thiết kế Intent cho DialogFlow Bot
|Setup tích hợp các WebHooks trong DialogFlow Bot

###### Cần phải thực hiện

|Epics|
|-|
|Tích hợp Facebook Messenger
|Tích hợp DialogFlow Bot giao tiếp với Application
|Application cài đặt thêm cấu trúc bảo mật cấp key theo request từ DialogFlow Agent 

###### Sản phẩm đến hiện tại
- phần Application trong kiến trúc hệ thống đã hoàn thành được 70%:
  - bảo mật các API bằng token JWT
  - cache token bằng sessionID, lưu ở máy client
  - Database Schema
  - Database Migration
  - Các API để tích hợp với DialogFlow
  - Các tool CLI ứng với API phục vụ Seed-Data, Operate hệ thống
  - Deploy lên AWS
- Phần NLP Engine trong kiến trúc hệ thống
  - Chatbot có thể phản hội dựa theo input đầu vào
  - Chiết xuất Chatbot để tự host bằng VPS cá nhân trên AWS


#### Xin cảm ơn
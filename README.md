# DEC04_SQL-NoSQL1. Lấy **toàn bộ** sản phẩm đang hiển thị trên các danh mục của website tiki.vn. Dữ liệu lấy về sẽ lưu trong MongoDB
2. Tạo một bản sao lưu data gửi cho Coach để có thể Restore dữ liệu trên một hệ thống MongoDB khác
3. Trích xuất các trường thông tin sau và lưu vào MySQL để cho team khác sử dụng:
    1. Product name: Tên sản phẩm 
    2. Short description: Mô tả ngắn của sản phẩm
    3. Description: Mô tả chi tiết sản phẩm. Yêu cầu: **clean dữ liệu, lọc bỏ những tag html thừa trong mô tả**
    4. URL: Link sản phẩm
    5. Rating: Đánh giá trung bình về sản phẩm
    6. Số lượng bán
    7. Giá sản phẩm
    8. Category ID: ID của danh mục sản phẩm
    9. day_ago_created 
4. Thống kê:
    1. Mỗi category (bao gồm cả sub-category) có bao nhiêu sản phẩm
    2. Tạo biểu đồ thống kê xuất xứ của các sản phẩm. Ví dụ từ biểu đồ có thể biết: Có bao nhiêu sản phẩm xuất xứ từ Trung Quốc. Từ đó so sánh tỉ lệ xuất xứ của các sản phẩm
    3. Top 10 sản phẩm được bán nhiều nhất, có rating cao nhất và giá thấp nhất
5. Lấy tất cả sản phẩm mà có thông tin “thành phần” trong mô tả. Lưu các thông tin dưới dạng CSV: product_id, ingredient.
Lưu ý, chỉ trích chọn ra thông tin miêu tả “Thành phần” trong Description, những thông tin khác không lấy. Thời gian truy vấn ra các sản phẩm có “Thành phần” trong Description phải nhanh nhất có thể




# Data Engineering Project README
## Introduction
Welcome to the Data Engineering project! This repository contains documentation and code for various aspects of data engineering, focusing on addressing pain points and ensuring the smooth operation of data-related tasks.

## Getting Started
Prerequisites : MongoDb , Mysql , Python

# Pain Points
## 1. Investigating Data
Objective: Investigate data using Postman to evaluate API parameters and estimate processing time for a large dataset (approximately 1.6 million records).

### Actions:

Use Postman to test API endpoints with different parameter configurations.
Measure response times for varying parameters to estimate processing time.
Store documentation in 'Code' directory 

## 2. Monitoring
Objective: Implement robust logging and error handling mechanisms to ensure the reliability of data processes.

### Actions:

Design and implement a comprehensive logging strategy.
Develop error handling routines to gracefully manage unexpected scenarios.
Store documentation in 'Code' directory and in the 'Log' directory.


## 3. Migration
Objective: Address weaknesses in data migration, particularly in terms of load timing, by implementing query paging on a NoSQL database.

### Actions recommended:

Identify the NoSQL database in use.
Design and implement query paging strategies to optimize data migration.


## 4. Statistics
Objective: Gather and analyze data to understand the needs of stakeholders.

### Actions:

Identify key stakeholders and their data requirements.
Develop scripts or queries to extract relevant statistics and insights.
Present findings in a user-friendly format (notebook visualization)
Store documentation in 'Code' directory and reports in the 'Outcome' directory.


# License
DEC community

# Contact Information
Email:hazelhan2002@gmail.com
Phone : +84862469454

# Conclusion
Feel free to reach out if you have any questions or need assistance with any aspect of this project. Happy data engineering!

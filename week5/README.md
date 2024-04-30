# Assignment - Week 5
### Task2: Create database and table in MySQL server
- Create a new database named website.
  ```sql
  CREATE DATABASE `website`;
- Create a new table named member, in the website database, designed as below:
  ![]()
  ```sql
  USE `website`;
  CREATE TABLE `member`(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,  
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count INT UNSIGNED NOT NULL DEFAULT O,
    time DATETIME NOT NULL DEFAULT CURRENT TIMESTAMP
  );
  ```
### Task3: SQL CRUD
- INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
  ```sql
  
- SELECT all rows from the member table.
  ```sql
  
- SELECT all rows from the member table, in descending order of time.
  ```sql
  
- SELECT total 3 rows, second to fourth, from the member table, in descending order of time.
  ```sql
  
- SELECT rows where username equals to test.
  ```sql
  
- SELECT rows where name includes the es keyword.
  ```sql
  
- SELECT rows where both username and password equal to test.
  ```sql
  
- UPDATE data in name column to test2 where username equals to test.
  ```sql
  
### Task4: SQL Aggregation Functions
- SELECT how many rows from the member table.
  ```sql
  
- SELECT the sum of follower_count of all the rows from the member table.
  ```sql
  
- SELECT the average of follower_count of all the rows from the member table.
  ```sql
  
- SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
  ```sql
  
### Task5: SQL JOIN
- Create a new table named message, in the website database. designed as below:
  ```sql
  
- SELECT all messages, including sender names. We have to JOIN the member table to get that.
  ```sql
  
- SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
  ```sql
  
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
  ```sql
  
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
  ```sql
  

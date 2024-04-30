# Assignment - Week 5
### Task2: Create database and table in MySQL server
- Create a new database named website.
  ```sql
  CREATE DATABASE `website`;
- Create a new table named member, in the website database, designed as below:
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/c5ed449733aaa9d38988d7ef75b6c6611f9c62d8/week5/images/task2.jpg)
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
  ![Executing Result of Task2](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task2-1.2-2.jpg)
### Task3: SQL CRUD
- INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-1.jpg)
- SELECT all rows from the member table.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-2.jpg)
- SELECT all rows from the member table, in descending order of time.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-3.jpg)
- SELECT total 3 rows, second to fourth, from the member table, in descending order of time.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-4.jpg)
- SELECT rows where username equals to test.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-5.jpg)
- SELECT rows where name includes the es keyword.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-6.jpg)
- SELECT rows where both username and password equal to test.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-7.jpg)
- UPDATE data in name column to test2 where username equals to test.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-8.jpg)
### Task4: SQL Aggregation Functions
- SELECT how many rows from the member table.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task4-1.jpg)
- SELECT the sum of follower_count of all the rows from the member table.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task4-2.jpg)
- SELECT the average of follower_count of all the rows from the member table.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task4-3.jpg)
- SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task4-4.jpg)
### Task5: SQL JOIN
- Create a new table named message, in the website database. designed as below:
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5.jpg)
  ```sql
  
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-1.1.jpg)
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-1.2.jpg)
- SELECT all messages, including sender names. We have to JOIN the member table to get that.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-2.jpg)
- SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-3.jpg)
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-4.jpg)
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
  ```sql
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-5.jpg)  

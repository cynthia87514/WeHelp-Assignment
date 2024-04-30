# Assignment - Week 5
### Task2: Create database and table in MySQL server
- Create a new database named website.
  ```sql
  CREATE DATABASE `website`;
  ```
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
  INSERT INTO `member` (name, username, password, follower_count, time) VALUES
  ("test", "test", "test", 300, "2024-04-09 13:00:20"),
  ("Amy", "amy0101", "AMY0101", 100, "2024-04-01 09:50:00"),
  ("Betty", "betty0202", "BETTY0202", 400, "2024-04-15 23:00:08"),
  ("Celine", "celine0303", "CELINEO303", 500, "2024-04-27 19:00:45"),
  ("Dennis", "dennis0404", "DENNIS0404", 200, "2024-04-21 16:35:50");
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-1.jpg)
- SELECT all rows from the member table.
  ```sql
  SELECT * FROM `member`;
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-2.jpg)
- SELECT all rows from the member table, in descending order of time.
  ```sql
  SELECT * FROM `member` ORDER BY time DESC;
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-3.jpg)
- SELECT total 3 rows, second to fourth, from the member table, in descending order of time.
  ```sql
  SELECT * FROM (
  SELECT * FROM `member` ORDER BY time DESC
  ) AS subquery LIMIT 1,3;
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-4.jpg)
- SELECT rows where username equals to test.
  ```sql
  SELECT * FROM `member` WHERE username = "test";
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-5.jpg)
- SELECT rows where name includes the es keyword.
  ```sql
  SELECT * FROM `member` WHERE name LIKE "%es%";
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-6.jpg)
- SELECT rows where both username and password equal to test.
  ```sql
  SELECT * FROM `member` WHERE username = "test" AND password = "test";
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-7.jpg)
- UPDATE data in name column to test2 where username equals to test.
  ```sql
  UPDATE `member` SET name = "test2" WHERE username = "test";
  SELECT * FROM `member`;
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task3-8.jpg)
### Task4: SQL Aggregation Functions
- SELECT how many rows from the member table.
  ```sql
  SELECT COUNT(*) FROM `member`;
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task4-1.jpg)
- SELECT the sum of follower_count of all the rows from the member table.
  ```sql
  SELECT SUM(follower_count) FROM `member`;
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task4-2.jpg)
- SELECT the average of follower_count of all the rows from the member table.
  ```sql
  SELECT AVG(follower_count) FROM `member`;
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task4-3.jpg)
- SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
  ```sql
  SELECT AVG(follower_count) FROM(
  SELECT * FROM `member` ORDER BY follower_count DESC LIMIT 2
  )AS subquery;
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task4-4.jpg)
### Task5: SQL JOIN
- Create a new table named message, in the website database. designed as below:
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5.jpg)
  ```sql
  CREATE TABLE `message`(
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  member_id BIGINT NOT NULL,
  content VARCHAR(255) NOT NULL,
  like_count INT UNSIGNED NOT NULL DEFAULT O,
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (member_id) REFERENCES `member`(id)
  );
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-1.1.jpg)
  ```sql
  INSERT INTO `message` (id, member_id, content, like_count, time) VALUES
  (001, 3, "WHAT glorious weather! Not a cloud in the sky!", 50, "2024-04-16 12:00:10"),
  (002, 4, "I have just completed my first half marathon in my life!", 350, "2024-04-28 10:10:00"),
  (003, 2, "I really love this kind of dessert!", 220, "2024-04-08 15:30:24"),
  (004, 5, "I plan to adopt three cats within six months.", 120, "2024-04-29 16:50:30"),
  (005, 1, "I have been learning coding recently.", 95, "2024-04-30 15:40:20");
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-1.2.jpg)
- SELECT all messages, including sender names. We have to JOIN the member table to get that.
  ```sql
  SELECT `message`.*, `member`.name AS sender name
  FROM `message`
  JOIN `member`
  ON `message`.member_id = `member`.id;
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-2.jpg)
- SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
  ```sql
  SELECT `message`.*, `member`.name AS sender_name
  FROM `message`
  JOIN `member`
  ON `message`.member_id = `member`.id;
  WHERE `member`.username = "test";
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-3.jpg)
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
  ```sql
  SELECT AVG(`message`.like_count) AS average_like_count
  FROM `message`
  JOIN `member`
  ON `message`.member_id = `member`.id;
  WHERE `member`.username = "test";
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-4.jpg)
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
  ```sql
  SELECT `member`.username AS sender_name, AVG(`message`.like_count) AS average_like_count
  FROM `message`
  JOIN `member`
  ON `message`.member_id = `member`.id;
  GROUP BY `member`.username;
  ```
  ![](https://github.com/cynthia87514/WeHelp-Assignment/blob/d6663d3a8b809595c9f689200b8d1d5a024db6a1/week5/images/task5-5.jpg)  

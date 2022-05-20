

mysql -u anabig11425 -p


use anabig11425;
show databases;
show tables; 


drop table if exists my_depts;
drop table if exists my_dept_emp;
drop table if exists my_dept_mng;
drop table if exists my_emp;
drop table if exists my_sal;
drop table if exists my_emp_title;


CREATE TABLE my_depts (dept_no VARCHAR(20),dept_name VARCHAR(20));
CREATE TABLE my_dept_emp (emp_no VARCHAR(20),dept_no VARCHAR(20));
CREATE TABLE my_dept_mng (dept_no VARCHAR(20), emp_no VARCHAR(20));
CREATE TABLE my_emp (emp_no VARCHAR(20),emp_title_id VARCHAR(20),birth_date VARCHAR(20),first_name VARCHAR(20),last_name VARCHAR(20),sex VARCHAR(20),hire_date VARCHAR(20),no_of_projects VARCHAR(20),Last_performance_rating VARCHAR(20),left_ VARCHAR(20),last_date VARCHAR(20));
CREATE TABLE my_sal (emp_no VARCHAR(20),salary VARCHAR(20));
CREATE TABLE my_emp_title (title_id VARCHAR(20),title VARCHAR(20));




LOAD DATA LOCAL INFILE '/home/anabig11425/Data/departments.csv' INTO TABLE my_depts FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;
LOAD DATA LOCAL INFILE '/home/anabig11425/Data/dept_emp.csv' INTO TABLE my_dept_emp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;
LOAD DATA LOCAL INFILE '/home/anabig11425/Data/dept_manager.csv' INTO TABLE my_dept_mng FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;
LOAD DATA LOCAL INFILE '/home/anabig11425/Data/employees.csv' INTO TABLE my_emp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;
LOAD DATA LOCAL INFILE '/home/anabig11425/Data/salaries.csv' INTO TABLE my_sal FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;
LOAD DATA LOCAL INFILE '/home/anabig11425/Data/titles.csv' INTO TABLE my_emp_title FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;



select * from my_depts limit 5;
select * from my_dept_emp limit 5;
select * from my_dept_mng limit 5;
select * from my_emp limit 5;
select * from my_sal limit 5;
select * from my_emp_title limit 5;


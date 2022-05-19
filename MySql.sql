

mysql -u anabig11425 -p


use anabig11425;
show databases;
show tables; 


drop table if exists departments;
drop table if exists dept_emp;
drop table if exists dept_manager;
drop table if exists employees;
drop table if exists salaries;
drop table if exists titles;


CREATE TABLE departments (dept_no VARCHAR(20),dept_name VARCHAR(20));
CREATE TABLE dept_emp (emp_no VARCHAR(20),dept_no VARCHAR(20));
CREATE TABLE dept_manager (dept_no VARCHAR(20), emp_no VARCHAR(20));
CREATE TABLE employees (emp_no VARCHAR(20),emp_title_id VARCHAR(20),birth_date VARCHAR(20),first_name VARCHAR(20),last_name VARCHAR(20),sex VARCHAR(20),hire_date VARCHAR(20),no_of_projects VARCHAR(20),Last_performance_rating VARCHAR(20),left_ VARCHAR(20),last_date VARCHAR(20));
CREATE TABLE salaries (emp_no VARCHAR(20),salary VARCHAR(20));
CREATE TABLE titles (title_id VARCHAR(20),title VARCHAR(20));




LOAD DATA LOCAL INFILE '/home/anabig11425/Data_final/departments.csv' INTO TABLE departments FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;
LOAD DATA LOCAL INFILE '/home/anabig11425/Data_final/dept_emp.csv' INTO TABLE dept_emp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;
LOAD DATA LOCAL INFILE '/home/anabig11425/Data_final/dept_manager.csv' INTO TABLE dept_manager FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;
LOAD DATA LOCAL INFILE '/home/anabig11425/Data_final/employees.csv' INTO TABLE employees FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;
LOAD DATA LOCAL INFILE '/home/anabig11425/Data_final/salaries.csv' INTO TABLE salaries FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;
LOAD DATA LOCAL INFILE '/home/anabig11425/Data_final/titles.csv' INTO TABLE titles FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' ignore 1 rows;



select * from departments limit 5;
select * from dept_emp limit 5;
select * from dept_manager limit 5;
select * from employees limit 5;
select * from salaries limit 5;
select * from titles limit 5;


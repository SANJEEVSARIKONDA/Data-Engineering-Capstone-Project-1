CREATE EXTERNAL TABLE dept_manager
STORED AS AVRO LOCATION 'hdfs:///user/anabig11425/hive/warehouse/my_dept_mng'
TBLPROPERTIES ('avro.schema.url'='/user/anabig11425/my_dept_mng.avsc');

select * from dept_manager ;

--########################


CREATE EXTERNAL TABLE dept_emp
STORED AS AVRO LOCATION 'hdfs:///user/anabig11425/hive/warehouse/my_dept_emp '
TBLPROPERTIES ('avro.schema.url'='/user/anabig11425/my_dept_emp.avsc');


--##########

CREATE EXTERNAL TABLE departments
STORED AS AVRO LOCATION 'hdfs:///user/anabig11425/hive/warehouse/my_depts'
TBLPROPERTIES ('avro.schema.url'='/user/anabig11425/my_depts.avsc');

--###############

CREATE EXTERNAL TABLE employees
STORED AS AVRO LOCATION 'hdfs:///user/anabig11425/hive/warehouse/my_emp'
TBLPROPERTIES ('avro.schema.url'='/user/anabig11425/my_emp.avsc');

--############

CREATE EXTERNAL TABLE titles
STORED AS AVRO LOCATION 'hdfs:///user/anabig11425/hive/warehouse/my_emp_title'
TBLPROPERTIES ('avro.schema.url'='/user/anabig11425/my_emp_title.avsc');

--##################

CREATE EXTERNAL TABLE salaries
STORED AS AVRO LOCATION 'hdfs:///user/anabig11425/hive/warehouse/my_sal'
TBLPROPERTIES ('avro.schema.url'='/user/anabig11425/my_sal.avsc');

--###################
-- Data Analysis --
-- 1--

SELECT employees.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary
FROM employees
JOIN salaries
ON employees.emp_no = salaries.emp_no;

--2--
--SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN '1986-01-01' AND '1987-01-01';

select first_name,last_name,hire_date,date_format(from_unixtime(unix_timestamp(cast(hire_date as string),'MM/dd/yyyy')),'yyyy-MM-dd') as hire_date1
from employees where date_format(from_unixtime(unix_timestamp(cast(hire_date as string),'MM/dd/yyyy')),'yyyy') = '1986' ;

--3--

SELECT departments.dept_no, departments.dept_name, dept_manager.emp_no, employees.last_name, employees.first_name
FROM departments
JOIN dept_manager
ON departments.dept_no = dept_manager.dept_no
JOIN employees
ON dept_manager.emp_no = employees.emp_no;

-- 4--
--SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name FROM dept_emp JOIN employees ON dept_emp.emp_no = employees.emp_no JOIN departments ON dept_emp.dept_no = departments.dept_no;


select employees.emp_no, employees.last_name, employees.first_name, departments.dept_name 
from  departments
inner join  dept_emp on departments.dept_no = dept_emp.dept_no
inner join employees on dept_emp.emp_no = employees.emp_no


-- 5 --
SELECT first_name, last_name,sex
FROM employees
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%';

-- 6 --
--SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name FROM dept_emp JOIN employees ON dept_emp.emp_no = employees.emp_no JOIN departments ON dept_emp.dept_no = departments.dept_no WHERE departments.dept_name = 'Sales';

select employees.emp_no, employees.last_name, employees.first_name, departments.dept_name 
from  departments
inner join  dept_emp on departments.dept_no = dept_emp.dept_no
inner join employees on dept_emp.emp_no = employees.emp_no
where dept_name = 'Sales';



-- 7 --
--SELECT dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name FROM dept_emp JOIN employees ON dept_emp.emp_no = employees.emp_no JOIN departments ON dept_emp.dept_no = departments.dept_no WHERE departments.dept_name = 'Sales'  OR departments.dept_name = 'Development';

select employees.emp_no, employees.last_name, employees.first_name, departments.dept_name 
from  departments
inner join  dept_emp on departments.dept_no = dept_emp.dept_no
inner join employees on dept_emp.emp_no = employees.emp_no
where departments.dept_name = 'Sales' or departments.dept_name = 'development';

-- 8 --

select last_name,count(last_name) count_ from employees group by last_name order by count_ desc;

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SQLContext
from pyspark import SparkContext
sc = SparkContext('local','Spark SQL')
Sqlcontext = SQLContext(sc)


# In[2]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("DataframeExercise").getOrCreate()


# In[3]:


# Loading the data 
department = Sqlcontext.read.parquet("hdfs://nameservice1/user/anabig11425/hive/warehouse2/my_depts/dd059383-bc33-4247-a1c7-c023fa662212.parquet")
dept_emp = Sqlcontext.read.parquet("hdfs://nameservice1/user/anabig11425/hive/warehouse2/my_dept_emp/ed3a77e9-b61b-4d82-8750-a80595d561f9.parquet")
dept_manager = Sqlcontext.read.parquet("hdfs://nameservice1/user/anabig11425/hive/warehouse2/my_dept_mng/f9b87af2-69ac-4392-b2bf-ce0cc235e5fd.parquet")
employees = Sqlcontext.read.parquet("hdfs://nameservice1/user/anabig11425/hive/warehouse2/my_emp/e8404f4e-a039-4ed3-8dbf-35c69d29e9a3.parquet")
salaries = Sqlcontext.read.parquet("hdfs://nameservice1/user/anabig11425/hive/warehouse2/my_sal/e2a0b33e-f0b7-42f9-b4d1-8d7a568b3e35.parquet")
titles = Sqlcontext.read.parquet("hdfs://nameservice1/user/anabig11425/hive/warehouse2/my_emp_title/ff932837-adb6-4975-97e6-848403be68a7.parquet")


# In[4]:


department.show(10)


# In[5]:


dept_emp.show(10)


# In[6]:


dept_manager.show(10)


# In[7]:


employees.show(10)


# In[8]:


titles.show(10)


# In[9]:


salaries.show(10)


# In[10]:


department.createTempView("departments_sql")
dept_emp.createTempView("dept_emp_sql")
dept_manager.createTempView("dept_manager_sql") 
employees.createTempView("employees_sql") 
salaries.createTempView("salaries_sql") 
titles.createTempView("titles_sql")


# In[11]:


# 1. A list showing employee number, last name, first name, sex, and salary for each employee
spark.sql('select t1.emp_no,t2.emp_no,last_name,first_name,sex,t2.salary from employees_sql t1 inner join salaries_sql t2 on t1.emp_no=t2.emp_no ').show()


# In[12]:


# 2. A list showing first name, last name, and hire date for employees who were hired in 1986.
spark.sql("select first_name,last_name,hire_date,date_format(from_unixtime(unix_timestamp(cast(hire_date as string),'MM/dd/yyyy')),'yyyy-MM-dd') as hire_date1 from employees_sql where date_format(from_unixtime(unix_timestamp(cast(hire_date as string),'MM/dd/yyyy')),'yyyy') = '1986'").show()


# In[13]:


# 3. A list showing the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
spark.sql("SELECT departments_sql.dept_no, departments_sql.dept_name, dept_manager_sql.emp_no, employees_sql.last_name, employees_sql.first_name FROM departments_sql JOIN dept_manager_sql ON departments_sql.dept_no = dept_manager_sql.dept_no JOIN employees_sql ON dept_manager_sql.emp_no = employees_sql.emp_no").show()


# In[14]:


# 4. A list showing the department of each employee with the following information: employee number, last name, first name, and department name.
spark.sql("select employees_sql.emp_no, employees_sql.last_name, employees_sql.first_name, departments_sql.dept_name from  departments_sql inner join  dept_emp_sql on departments_sql.dept_no = dept_emp_sql.dept_no inner join employees_sql on dept_emp_sql.emp_no = employees_sql.emp_no").show()


# In[15]:


# 5. A list showing first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B.“
spark.sql("select first_name,last_name,sex from employees_sql where first_name = 'Hercules' and last_name like 'B%'").show()


# In[16]:


# 6. A list showing all employees in the Sales department, including their employee number, last name, first name, and department name.
spark.sql("select employees_sql.emp_no, employees_sql.last_name, employees_sql.first_name, departments_sql.dept_name from  departments_sql inner join  dept_emp_sql on departments_sql.dept_no = dept_emp_sql.dept_no inner join employees_sql on dept_emp_sql.emp_no = employees_sql.emp_no where dept_name like '%Sales%'").show()


# In[17]:


# 7. A list showing all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
spark.sql("select employees_sql.emp_no, employees_sql.last_name, employees_sql.first_name, departments_sql.dept_name from  departments_sql inner join  dept_emp_sql on departments_sql.dept_no = dept_emp_sql.dept_no inner join employees_sql on dept_emp_sql.emp_no = employees_sql.emp_no where dept_name like '%Sales%' or dept_name like '%development%'").show()


# In[18]:


# 8. A list showing the frequency count of employee last names, in descending order. ( i.e., how many employees share each last name
spark.sql("select last_name,count(last_name) count_ from employees_sql group by last_name order by count_ desc").show()


# In[19]:


# 9. Histogram to show the salary distribution among the employees
spark.sql("select t1.emp_no,t2.emp_no,last_name,first_name,sex,t2.salary from employees_sql t1 inner join salaries_sql t2 on t1.emp_no=t2.emp_no  ").show()


# In[20]:


# 10. Bar graph to show the Average salary per title (designation)
spark.sql("select t1.title, avg(t3.salary) as avg_salary from titles_sql t1 inner join employees_sql t2 on t1.title_id = t2.emp_title_id inner join salaries_sql t3 on t2.emp_no=t3.emp_no group by t1.title").show()


# In[21]:


# 11. Calculate employee tenure & show the tenure distribution among the employees


# In[22]:


# 12. Perform your own Analysis (based on the data understanding) – At least 5 additional analysis


# In[23]:


#data_all =spark.sql("select * from  departments_sql t1 inner join  dept_emp_sql t2 on t1.dept_no = t2.dept_no inner join employees_sql t3 on t2.emp_no = t3.emp_no inner join salaries_sql t4 on t4.emp_no = t3.emp_no inner join titles_sql t5 on t5.title_id = t3.emp_title_id")


# In[25]:


#here loading data into table as t1,t2,t3
data_all =spark.sql("select t1.dept_name,t2.dept_no,t3.birth_date,t3.emp_no,t3.emp_title_id,t3.first_name,t3.hire_date,t3.last_date,t3.last_name,t3.last_performance_rating,t3.left_company,t3.no_of_projects,t3.sex,t4.salary,t5.title from  departments_sql t1 inner join  dept_emp_sql t2 on t1.dept_no = t2.dept_no inner join employees_sql t3 on t2.emp_no = t3.emp_no inner join salaries_sql t4 on t4.emp_no = t3.emp_no inner join titles_sql t5 on t5.title_id = t3.emp_title_id")


# In[26]:


data_all.show()


# In[27]:


data_all.columns


# In[28]:


final = data_all
for col in data_all.columns:
 final = data_all.withColumnRenamed(col,col.replace(" ", "_"))


# In[29]:


final.show()


# In[30]:


final.createTempView("final_sql")


# In[32]:


#spark.sql('select * from final_sql').show()


# In[33]:


spark.sql('select distinct left_company from final_sql').show()


# In[34]:


final = final.withColumn("no_of_projects", final.no_of_projects.cast('int'))
final = final.withColumn("salary", final.no_of_projects.cast('int'))
final = final.withColumn("left_company", final.left_company.cast('int'))


# In[35]:


final.printSchema()


# In[36]:


continuous_features = [
 'no_of_projects',
 'salary']
final.show()
categorical_features = ['dept_name',
 'last_performance_rating',
 'sex',
 'title']
y = ['left_company']


# In[37]:


# Encoding all categorical columns(one hot encoding)
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler, PolynomialExpansion, VectorIndexer


# In[38]:


final.columns


# In[ ]:





# In[ ]:


#final.select('emp_no','dept_no','dept_name','emp_title_id','sex','no_of_projects','Last_performance_rating','left_company','salary').show()


# In[39]:


# create object of StringIndexer(lable encodeing) class and specify input and output column
SI_dept_name = StringIndexer(inputCol='dept_name',outputCol='dept_name_Index')
SI_last_performance_rating = StringIndexer(inputCol='last_performance_rating',outputCol='last_performance_rating_Index')
SI_sex = StringIndexer(inputCol='sex',outputCol='sex_Index')
SI_title = StringIndexer(inputCol='title',outputCol='title_Index')


# In[40]:


# transforming the data
final = SI_dept_name.fit(final).transform(final)
final = SI_last_performance_rating.fit(final).transform(final)
final = SI_sex.fit(final).transform(final)
final = SI_title.fit(final).transform(final)


# In[41]:


# transformed data
final.select('dept_name', 'dept_name_Index', 'last_performance_rating', 'last_performance_rating_Index', 'sex', 'sex_Index','title','title_Index').show(10)


# In[42]:


# Vector assesmbler
assesmble=VectorAssembler(inputCols=['no_of_projects',
 'salary',
 'dept_name_Index',
 'last_performance_rating_Index',
 'sex_Index',
 'title_Index'],outputCol='features')


# In[43]:


final1=assesmble.transform(final)
final1.show()


# In[45]:


# Training and Testing data 
df=final1.select('features','left_company')
df.printSchema()


# In[46]:


(train, test) = df.randomSplit([.7,.3])
train.show(2)
test.show(2)


# In[47]:


from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator, BinaryClassificationEvaluator
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


# In[50]:


#  RandomForestClassifier Supervised Learning (Classification Alogrithm)
rf = RandomForestClassifier(labelCol='left_company', 
                            featuresCol='features',
                            maxDepth=5)
model = rf.fit(train)
rf_predictions = model.transform(test)
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
multi_evaluator = MulticlassClassificationEvaluator(labelCol = 'left_company', metricName = 'accuracy')
print('RandomForest Accuracy:', multi_evaluator.evaluate(rf_predictions))


# In[51]:


## LogisticRegression Supervised Learning (Classificaton Alogrithm)
lr = LogisticRegression(featuresCol ='features', labelCol ='left_company', maxIter=10)
lrModel = lr.fit(train)
lr_predictions = lrModel.transform(test)
log_multi_evaluator = MulticlassClassificationEvaluator(labelCol = 'left_company', metricName = 'accuracy')
print('LogisticRegression Accuracy:', log_multi_evaluator.evaluate(lr_predictions))


# In[ ]:


spark.stop()


# In[ ]:





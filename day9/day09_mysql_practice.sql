
mysql> CREATE TABLE Shan;

mysql> CREATE TABLE Shan(
    -> id INT,
    -> name VARCHAR(50),
    -> rollno INT
    -> );

mysql> Select * from Shan

mysql> Insert into Shan values(2,"arun",12);

mysql> insert into Shan values(3,"hafan",13);

mysql> select * from Shan order by rollno asc;

mysql> select avg(rollno) from Shan;

mysql> select count(*) from shan

mysql> select max(rollno) from Shan;

mysql> ALTER TABLE Shan
    -> ADD marks INT;

mysql> update Shan
    -> set marks = 85
    -> where rollno = 44;

mysql> update Shan
    -> set marks = 100
    -> where rollno = 12;
mysql> update Shan
    -> set marks = 92
    -> where rollno = 13;
mysql> drop Students

truncate table Students;

mysql> select * from Shan;
mysql> create table candidate(
    -> id INT,
    -> age INT,
    -> course VARCHAR(100),
    -> name VARCHAR(50),
    -> Marks INT
    -> );
mysql> select * from candidate;
mysql> insert into candidate values(
    -> 1,23,"python","shan",85),
    -> 2,21,"SQL","haneen",80),
    -> 3,22,"python","hafan",88),
    -> 4,21,"java","hafesh",92);
mysql> select course,age,avg(Marks),max(Marks) from candidate group by course,age;
mysql> select avg(age),min(Marks) from candidate group by name,id;
mysql> select id,name,avg(age),min(marks) from candidate group by name,id;

mysql>  CREATE TABLE employees (
    ->     emp_id INT,
    ->     emp_name VARCHAR(50),
    ->     department VARCHAR(30),
    ->     gender VARCHAR(10),
    ->     city VARCHAR(30),
    ->     salary INT,
    ->     experience INT
    -> );
mysql> INSERT INTO employees VALUES
    -> (1, 'Rahul', 'IT', 'Male', 'Delhi', 70000, 5),
    -> (2, 'Anita', 'HR', 'Female', 'Mumbai', 50000, 4),
    -> (3, 'Aman', 'IT', 'Male', 'Delhi', 90000, 8),
    -> (4, 'Neha', 'Finance', 'Female', 'Pune', 60000, 6),
    -> (5, 'Rohit', 'IT', 'Male', 'Mumbai', 75000, 5),
    -> (6, 'Priya', 'HR', 'Female', 'Delhi', 48000, 3),
    -> (7, 'Vikas', 'Finance', 'Male', 'Pune', 65000, 7),
    -> (8, 'Sneha', 'IT', 'Female', 'Bangalore', 85000, 6),
    -> (9, 'Arjun', 'HR', 'Male', 'Mumbai', 52000, 4),
    -> (10,'Kavya', 'Finance', 'Female', 'Delhi', 72000, 8);

mysql> select * from employees;
mysql> select department ,avg(salary) from employees group by department;
mysql> select city,sum(salary)from employees group by city,salary;
mysql> select city,sum(salary)from employees group by city;
mysql> select department,count(*) from employees where salary > 60000 group by department;
mysql> select department,count(*) as count_emp from employees where salary>60000 group by department;
mysql> select department,city,avg(salary)
    -> as Avg_salary
    -> from employees
    -> group by department,city;
mysql> select department,city,avg(salary)
    -> as Avg_salary
    -> from employees
    -> group by department,city;
mysql> select department,count(*) as male_count from employees where gender = 'Male' group by department;




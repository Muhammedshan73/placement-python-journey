-- Day 10: MySQL Constraints, Foreign Keys & Joins Practice

USE school;

-- ===============================
-- Table with Constraints
-- ===============================
CREATE TABLE xyz (
    id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    phone_num BIGINT UNIQUE
);

INSERT INTO xyz VALUES
(1,'shan',7306469703),
(2,'hafan',9846990404),
(3,'hanin',9400651431);

ALTER TABLE xyz ADD marks INT;

UPDATE xyz
SET marks = CASE id
    WHEN 1 THEN 90
    WHEN 2 THEN 80
    WHEN 3 THEN 95
END
WHERE id IN (1,2,3);

ALTER TABLE xyz ADD course VARCHAR(20) DEFAULT 'python';

INSERT INTO xyz VALUES
(4,'harsh',7736176142,75,'java'),
(5,'zii',8723702942,99,''),
(6,'aroo',7854320976,99,NULL);

-- ===============================
-- Foreign Key Example
-- ===============================
CREATE TABLE abc (
    id INT,
    age INT,
    FOREIGN KEY (id) REFERENCES xyz(id)
);

INSERT INTO abc VALUES
(1,25),
(2,22),
(2,45);

-- INNER JOIN
SELECT xyz.name, xyz.marks, abc.age
FROM xyz
INNER JOIN abc
ON xyz.id = abc.id;

-- ===============================
-- One-to-Many Relationship
-- ===============================
CREATE TABLE table1 (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

CREATE TABLE table2 (
    student_id INT,
    course VARCHAR(50),
    duration INT,
    FOREIGN KEY (student_id) REFERENCES table1(student_id)
);

INSERT INTO table1 VALUES
(1,'shan',21),
(2,'hafan',22),
(3,'hanin',21);

INSERT INTO table2 VALUES
(1,'python',140),
(2,'java',130),
(3,'python',120);

SELECT table1.student_id, table1.name, table1.age,
       table2.course, table2.duration
FROM table1
INNER JOIN table2
ON table1.student_id = table2.student_id;

-- ===============================
-- Employee & Department Join
-- ===============================
CREATE TABLE one (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(20) UNIQUE,
    emp_city VARCHAR(30) NOT NULL
);

CREATE TABLE two (
    department_id INT PRIMARY KEY,
    emp_id INT,
    department VARCHAR(20),
    salary INT,
    FOREIGN KEY (emp_id) REFERENCES one(emp_id)
);

INSERT INTO one VALUES
(1,'shan','kozhikode'),
(2,'hanin','wayanad'),
(3,'hafan','kannur');

INSERT INTO two VALUES
(101,1,'computer',50000),
(102,2,'electrical',40000),
(103,3,'aerospace',30000);

SELECT o.emp_name, t.salary
FROM one o
JOIN two t
ON o.emp_id = t.emp_id;

-- ===============================
-- Customers & Orders (Joins)
-- ===============================
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50),
    amount INT
);

INSERT INTO customers VALUES
(1,'Aman','Delhi'),
(2,'Riya','Mumbai'),
(3,'Kabir','Delhi'),
(4,'Neha','Pune'),
(5,'Arjun','Bangalore'),
(6,'Simran','Mumbai'),
(7,'Rahul','Delhi'),
(8,'Pooja','Chennai'),
(9,'Vikas','Pune'),
(10,'Anita','Bangalore');

INSERT INTO orders VALUES
(101,1,'Laptop',60000),
(102,1,'Mouse',1500),
(103,2,'Mobile',30000),
(104,3,'Keyboard',2500),
(105,3,'Monitor',12000),
(106,5,'Tablet',20000),
(107,6,'Laptop',65000),
(108,7,'Mobile',28000),
(109,7,'Earphones',2000),
(110,11,'Camera',40000);

-- INNER JOIN
SELECT c.customer_name, o.product, o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;

-- LEFT JOIN
SELECT c.customer_name, o.product
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

-- RIGHT JOIN
SELECT c.customer_name, o.product
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

-- Orders without matching customers
SELECT o.*
FROM orders o
LEFT JOIN customers c
ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- FULL JOIN (Using UNION)
SELECT c.customer_name, o.product
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
UNION
SELECT c.customer_name, o.product
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

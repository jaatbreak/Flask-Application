CREATE DATABASE employee_db;

USE employee_db;

CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    employee_id VARCHAR(50),
    company_name VARCHAR(100),
    designation VARCHAR(100),
    contact_no VARCHAR(20)
);

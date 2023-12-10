-- SQLite

-- DDL: Data Definition Language

CREATE TABLE  employees(
  employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
  employees_name VARCHAR(100) NOT NULL,
  employees_designation VARCHAR(45) NULL,
  company VARCHAR(100) NULL,
  apoint_date DATETIME NOT NULL
);


-- DML: Data Manipulation Language
INSERT INTO employees (employees_name, employees_designation, company, apoint_date)
VALUES
  ('John Doe', 'Software Engineer', 'ABC Corp', '2023-01-15 09:00:00'),
  ('Jane Smith', 'Project Manager', 'XYZ Inc', '2023-02-20 14:30:00'),
  ('Bob Johnson', 'Data Analyst', '123 Company', '2023-03-10 11:45:00');


UPDATE  employees SET company = 'nordiac', apoint_date = '2023-05-01 09:00:00' WHERE employee_id = 1

DELETE FROM employees WHERE employee_id = 3  


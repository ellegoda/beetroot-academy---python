SELECT 
    e.first_name AS 'First Name', 
    e.last_name AS 'Last Name',
    d.department_name AS 'Deparment Name', 
    e.department_id AS 'Department Number' 
FROM employees AS e
INNER JOIN department AS d ON e.department_id = d.department_id;

SELECT 
    e.first_name AS 'First Name', 
    e.last_name AS 'Last Name',
    d.department_name AS 'Deparment Name', 
    l.city AS 'City', 
    l.state_province AS 'State Province' 
FROM employees AS e
INNER JOIN department AS d ON e.department_id = d.department_id
INNER JOIN locations AS l ON d.location_id = l.location_id;

SELECT 
    e.first_name AS 'First Name', 
    e.last_name AS 'Last Name',
    d.department_name AS 'Deparment Name', 
    e.department_id AS 'Department Number'
FROM employees AS e
INNER JOIN department AS d ON e.department_id = d.department_id
WHERE e.department_id IN (40, 80);

SELECT 
    d.department_id AS 'Department Id', 
    d.department_name AS 'Department Name', 
    e.first_name AS 'First Name', 
    e.last_name AS 'Last Name' 
FROM department as d
LEFT JOIN employees e ON d.department_id = e.department_id;

SELECT 
    e.first_name AS 'Employee Name', 
    m.first_name AS 'Manager Name' 
FROM employees e
INNER JOIN employees m ON e.manager_id = m.employee_id;

SELECT
    (e.first_name || " " || e.last_name) AS 'Full Name',
    j.job_title AS 'Job Title',
    j.max_salary AS 'Max Salary',
    e.salary AS 'Current Salary',
    (j.max_salary - e.salary ) AS 'Salary Differance'
FROM employees e
INNER JOIN jobs j ON e.job_id = j.job_id;


SELECT
    j.job_title AS 'Job Title',
    AVG(e.salary) AS 'Average Salary'
FROM employees e
INNER JOIN jobs j ON e.job_id = j.job_id
GROUP BY e.job_id;


SELECT
    (e.first_name || " " || e.last_name) AS 'Full Name'
FROM employees e
INNER JOIN department d ON e.department_id = d.department_id
INNER JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'London';


SELECT
    d.department_name AS 'Department Name',
    COUNT(*) AS 'Number of Employees'
FROM employees e 
INNER JOIN department d ON e.department_id = d.department_id
GROUP BY e.department_id;







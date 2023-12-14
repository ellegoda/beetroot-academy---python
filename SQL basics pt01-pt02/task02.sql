SELECT first_name AS 'First Name', last_name AS 'Last Name' FROM employees

SELECT DISTINCT department_id FROM employees 

SELECT department_id FROM employees GROUP BY department_id

SELECT * FROM employees ORDER BY first_name DESC

SELECT first_name, last_name, salary, (salary * 0.12) AS PF FROM employees 

SELECT MIN(salary) AS 'Minimum Salary', MAX(salary) AS 'Maximum salary' FROM employees

SELECT employee_id, first_name, last_name, ROUND(salary, 2) FROM employees 
-- Question 181

SELECT name AS Employee 
FROM Employee AS empl 
WHERE salary > (SELECT salary 
    FROM Employee AS mang 
    WHERE empl.managerId = mang.id)
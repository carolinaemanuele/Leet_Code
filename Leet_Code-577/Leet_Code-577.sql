-- Question 577

SELECT name, bonus
FROM Employee AS emp
LEFT OUTER JOIN
Bonus AS bn
ON emp.empId = bn.empId 
WHERE bn.bonus < 1000 OR bn.bonus IS NULL
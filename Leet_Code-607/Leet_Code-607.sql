-- Question 607

SELECT NAME 
FROM SalesPerson 
WHERE sales_id 
NOT IN (
    SELECT sales_id 
    FROM Orders 
    WHERE com_id 
    IN (
        SELECT com_id 
        FROM Company 
        WHERE name = 'RED'))
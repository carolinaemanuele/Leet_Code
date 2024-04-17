-- Question 586

SELECT customer_number
FROM Orders
GROUP BY customer_number
HAVING COUNT(customer_number) = (
    SELECT MAX(number_order)
    FROM (
        SELECT COUNT(customer_number) AS number_order 
        FROM Orders
        GROUP BY customer_number) AS frequency)
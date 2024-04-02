-- Question 183

SELECT name AS Customers FROM Customers WHERE id NOT IN (SELECT customerID FROM Orders)
-- Question 175

SELECT p.firstName, p.lastName, 
       (SELECT a.city FROM Address a WHERE a.personId = p.personId) AS city,
       (SELECT a.state FROM Address a WHERE a.personId = p.personId) AS state
FROM Person p;
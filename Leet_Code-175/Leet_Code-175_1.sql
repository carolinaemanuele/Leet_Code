-- Question 175

SELECT pers.firstName, pers.lastName, addr.city, addr.state
FROM Person pers
LEFT JOIN Address addr ON pers.personId = addr.personId;
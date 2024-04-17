-- Question 620

SELECT *
FROM Cinema
WHERE description != "boring" AND id % 2 = 1
ORDER BY rating DESC
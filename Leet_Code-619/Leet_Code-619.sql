-- Question 619

SELECT MAX(single) AS num
FROM (
    SELECT num AS single
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS single_numbers
-- Question 610

SELECT *,
    CASE
        WHEN ABS(x) + ABS(y) > ABS(z)
            AND ABS(x) + ABS(z) > ABS(y)
            AND ABS(z) + ABS(y) > ABS(x)
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle
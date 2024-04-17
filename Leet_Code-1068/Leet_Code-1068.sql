-- Question 1068

SELECT pd.product_name, sl.year, sl.price
FROM Product pd
INNER JOIN Sales sl
ON pd.product_id = sl.product_id
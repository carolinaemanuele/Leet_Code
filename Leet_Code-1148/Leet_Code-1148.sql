-- Question 1148

SELECT DISTINCT author_id AS id
FROM Views vs
WHERE  vs.author_id = vs.viewer_id
ORDER BY author_id ASC
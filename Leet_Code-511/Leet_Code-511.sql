-- Question 511

SELECT actv.player_id, MIN(ac.event_date) AS first_login
FROM Activity AS actv
INNER JOIN Activity AS ac ON actv.player_id = ac.player_id
GROUP BY actv.player_id;
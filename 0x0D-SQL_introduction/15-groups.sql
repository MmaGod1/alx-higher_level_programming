-- Lists the number of records with the same score in the table second_table in my MySQL server.
-- Records are ordered by descending count.
SELECT score, COUNT(score) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY number DESC;

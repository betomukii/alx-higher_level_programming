-- script that lists the number of record with the same score in the table
-- second_table of the database hbtn_0c_0 in MYSQL server
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;

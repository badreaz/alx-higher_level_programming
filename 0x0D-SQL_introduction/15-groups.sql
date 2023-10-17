-- lists the number of records with the same score inn the table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;

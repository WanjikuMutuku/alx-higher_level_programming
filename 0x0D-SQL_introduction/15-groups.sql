-- lists the number of records with the same score in the table second_table
-- results should display the score under the label number, desc order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

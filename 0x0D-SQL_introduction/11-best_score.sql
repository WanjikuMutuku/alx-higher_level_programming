--  lists all records with a score >= 10 in the table second_table
--  Results should display both the score and the name, top first
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

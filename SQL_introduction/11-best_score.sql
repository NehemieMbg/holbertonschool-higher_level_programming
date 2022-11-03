-- Lists all records with a score >= 10
SELECT second_table.score, second_table.name FROM second_table ORDER BY DESC WHERE score >= 10;

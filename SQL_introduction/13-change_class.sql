-- Removes all records with a score less than 6
DELETE second_table.score, second_table.name, second_table.id
FROM second_table WHERE score <= 5;

-- Creates a table sceond_table
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table(id, name, score)
VALUES('1', 'Jhon', '10')
VALUES('2', 'Alex', '3')
VALUES('3', 'Bob', '14')
VALUES('4', 'George', '8')
#!/usr/bin/node
'use strict';

const size = process.argv[2];

function printSquare(num) {
	if (!Number.isInteger(Number(num))) return console.log('Not a number');

	for (let i = 0; i < Number(num); i++) {
		for (let j = 0; j < Number(num); j++) {
			process.stdout.write('#');
		}
		console.log();
	}
	return;
}

printSquare(size);

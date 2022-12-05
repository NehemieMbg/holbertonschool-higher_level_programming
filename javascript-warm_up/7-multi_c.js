#!/usr/bin/node
'use strict';

const n = process.argv[2];

if (n > 1) {
	for (let i = 0; i < n; i++) {
		console.log('C is fun');
	}
	return;
}
else console.log('Missing number of occurrences');
return;

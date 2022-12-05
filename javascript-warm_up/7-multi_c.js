#!/usr/bin/node
'use strict';

if (Number.isInteger(Number(process.argv[2]))) {
  const n = process.argv[2];
  for (let i = 0; i < Number(n); i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurrences');

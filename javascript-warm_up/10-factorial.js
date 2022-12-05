#!/usr/bin/node
'use strict';

const n = process.argv[2];

function printFactorial (num) {
  if (!Number.isInteger(Number(num))) return console.log('NaN');
  if (Number(num) <= 0) return 1;
  return Number(num) * printFactorial(Number(num) - 1);
}

console.log(printFactorial(n));

#!/usr/bin/node
'use strict';

const n1 = process.argv[2];
const n2 = process.argv[3];

const add = (a, b) => {
  if (!Number.isInteger(Number(a)) || !Number.isInteger(Number(b))) { return console.log('NaN'); }

  return console.log(Number(a) + Number(b));
};

add(n1, n2);

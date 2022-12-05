#!/usr/bin/node
'use strict';

const arr = [];
for (let i = 2; i < process.argv.length; i++) {
  arr.push(Number(process.argv[i]));
}

if (arr.length > 0) console.log(Math.max(...arr) - 1);
else console.log(0);

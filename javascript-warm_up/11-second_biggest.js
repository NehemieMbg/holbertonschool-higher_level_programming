#!/usr/bin/node
'use strict';

const arr = [];
for (let i = 2; i < process.argv.length; i++) {
  arr.push(Number(process.argv[i]));
}

console.log(Math.max(...arr));

#!/usr/bin/node
'use strict';

const num = Number(process.argv[2]);
Number.isInteger(num) ? console.log(`My number: ${num}`) : console.log('Not a number');

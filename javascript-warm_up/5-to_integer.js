#!/usr/bin/node
'use strict';

const num = process.argv[2];
typeof +num === 'number' ? console.log(`My number: ${num}`) : console.log('Not a number');

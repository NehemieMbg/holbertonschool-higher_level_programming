#!/usr/bin/node
'use strict';

if (!process.argv.length > 0) console.log('No arguments');
else if (process.argv.length === 1) console.log('Argument found');
else console.log('Arguments found');

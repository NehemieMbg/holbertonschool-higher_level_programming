#!/usr/bin/node

const coucou = require('request');
const merciAlain = {
  method: 'GET',
  url: process.argv[2]
};
coucou(merciAlain, function (_, response) {
  console.log(`code: ${response.statusCode}`);
});

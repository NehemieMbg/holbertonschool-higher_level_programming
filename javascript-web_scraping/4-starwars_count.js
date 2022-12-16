#!/usr/bin/node
const request = require('request');
const api = process.argv[2];
let count = 0;
request.get(api, function (err, _, body) {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body).results;
    for (const items of res) {
      for (const actor of items.characters) {
        if (actor.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

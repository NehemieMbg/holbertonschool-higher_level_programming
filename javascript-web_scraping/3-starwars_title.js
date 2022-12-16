#!/usr/bin/node
'use strict';

const request = require('request');
const id = process.argv[2];

request.get(
  `https://swapi-api.hbtn.io/api/films/${id}`,
  function (err, _, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).title);
    }
  }
);

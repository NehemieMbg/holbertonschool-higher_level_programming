#!/usr/bin/node
'use strict';

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, _, body) {
  if (err) { console.log(err); } else {
    fs.writeFile(process.argv[3], body, err => {
      if (err) { console.log(err); }
    });
  }
});

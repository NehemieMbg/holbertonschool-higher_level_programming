#!/usr/bin/node
'use strict'

const request = require('request');

request.get(process.argv[2], function (err, _, body) {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body);
    const workersDict = {};
    for (let i = 0; i < res.length; i++) {
      if (res[i].completed === true) {
        if (workersDict[res[i].userId] === undefined) {
          workersDict[res[i].userId] = 1;
        } else {
          workersDict[res[i].userId]++;
        }
      }
    }
    console.log(workersDict);
  }
});

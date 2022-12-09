#!/usr/bin/node
'use strict';

const arr = [];
exports.esrever = function (list) {
  for (let i = list.length - 1; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};

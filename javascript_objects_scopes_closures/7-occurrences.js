#!/usr/bin/node
'use strict';

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, cur) => cur === searchElement ? count + 1 : count, 0);
};

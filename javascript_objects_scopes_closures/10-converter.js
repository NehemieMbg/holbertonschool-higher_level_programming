#!/usr/bin/node
'use strict';

exports.converter = function (base) {
  return function conversion (str) {
    return str.toString(base);
  };
};

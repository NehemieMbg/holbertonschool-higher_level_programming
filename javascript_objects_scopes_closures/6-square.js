#!/usr/bin/node
'use strict';
const OldSquare = require('./5-square.js');

module.exports = class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const letter = !c ? 'X' : 'C';
    for (let i = 0; i < this.width; i++) {
      console.log(letter.repeat(this.width));
    }
  }
};

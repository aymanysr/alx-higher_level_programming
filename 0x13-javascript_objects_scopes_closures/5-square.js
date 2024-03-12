#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Call the parent class constructor
    super(size, size);
  }
}

module.exports = Square;

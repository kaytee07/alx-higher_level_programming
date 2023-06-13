#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let box = '';
      for (let j = 0; j < this.width; j++) {
        box += c || 'X';
      }
      console.log(box);
    }
  }
}
module.exports = Square;

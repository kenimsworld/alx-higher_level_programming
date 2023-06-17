#!/usr/bin/node
const Square01 = require('./5-square');

class Square extends Square01 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let m = 0; m < this.height; m++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;

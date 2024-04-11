const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;

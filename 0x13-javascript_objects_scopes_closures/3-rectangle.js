#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const row = this.height;
    const column = this.width;
    for (let x = 0; x < row; x++) {
      let tmpStr = '';
      for (let y = 0; y < column; y++) {
        tmpStr += 'X';
      }
      console.log(tmpStr);
    }
  }
}

module.exports = Rectangle;

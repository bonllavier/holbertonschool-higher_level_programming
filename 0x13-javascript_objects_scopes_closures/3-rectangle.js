#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    let h = 0;
    let w = 0;
    for (; h < this.height; h++) {
      for (; w < this.width; w++) {
        x = x + 'X';
      }
      console.log(x);
    }
  }
};

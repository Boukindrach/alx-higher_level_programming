#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let box = '';
      for (let j = 0; j < this.width; j++) box += 'X';
      console.log(box);
    }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
};

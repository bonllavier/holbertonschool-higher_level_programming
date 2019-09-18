#!/usr/bin/node
const array = process.argv.slice(2);
let string = '';
let i = 0;
let y = 0;
if (isNaN(array[0])) {
  console.log('Missing size');
} else {
  for (i = 0; i < array[0]; i++) {
    for (y = 0; y < array[0]; y++) {
      string = string + 'X';
    }
    if ((array[0] - 1) !== i) {
      string = string + '\n';
    }
  }
  console.log(string);
}

#!/usr/bin/node
const array = process.argv.slice(2);
let fmax = 0;
const array2 = [];
let i = 0;
let cont2 = 0;
if (array[0] === undefined) {
  console.log(0);
} else if (array.length === 1) {
  console.log(0);
} else {
  fmax = Math.max.apply(Math, array);
  for (i = 0; i < (array.length - 1); i++) {
    if (parseInt(array[i]) !== fmax) {
      array2[cont2] = array[i];
      cont2 = cont2 + 1;
    }
  }
  console.log(Math.max.apply(Math, array2));
}

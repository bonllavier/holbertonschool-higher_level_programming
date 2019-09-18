#!/usr/bin/node
const array = process.argv.slice(2);
add(array[0], array[1]);
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

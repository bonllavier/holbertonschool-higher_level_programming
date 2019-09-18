#!/usr/bin/node
const array = process.argv.slice(2);
const times = array[0];
let i = 0;
if (times === 0 || times === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < times; i++) {
    console.log('C is fun');
  }
}

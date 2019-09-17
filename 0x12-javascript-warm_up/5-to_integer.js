#!/usr/bin/node
const array = process.argv.slice(2);
if (isNaN(array[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(array[0]));
}

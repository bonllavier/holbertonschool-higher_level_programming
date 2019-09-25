#!/usr/bin/node
const array = process.argv.slice(2);
const fs = require('fs');
fs.readFile(array[0], 'utf-8', function read (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

#!/usr/bin/node
const array = process.argv.slice(2);
const fs = require('fs');
const content = array[1];
try {
  fs.writeFileSync(array[0], content);
} catch (err) {
  console.error(err);
}

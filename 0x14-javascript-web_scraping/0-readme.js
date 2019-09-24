#!/usr/bin/node
const array = process.argv.slice(2);
const fs = require('fs');
try {
  const data = fs.readFileSync(array[0], 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}

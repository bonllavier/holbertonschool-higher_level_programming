#!/usr/bin/node
const array = process.argv.slice(2);
const request = require('request');
const fs = require('fs');
request(array[0], function (err, res, body) {
  if (err) {
  }
  try {
    fs.writeFileSync(array[1], body);
  } catch (err) {
    console.error(err);
  }
});

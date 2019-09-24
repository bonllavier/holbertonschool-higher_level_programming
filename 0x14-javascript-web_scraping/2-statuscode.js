#!/usr/bin/node
const array = process.argv.slice(2);
const request = require('request');
request(array[0], function (err, res, body) {
  if (err) {
  }
  console.log('code: ' + res.statusCode);
});

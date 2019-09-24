#!/usr/bin/node
const array = process.argv.slice(2);
const request = require('request');
let x = 0;
const dict = {};
let cont = 0;
let userant = 0;
let result = [];
request(array[0], function (err, res, body) {
  if (err) {
  }
  result = JSON.parse(body);
  for (x = 0; x < result.length; x++) {
    if (userant !== result[x].userId) {
      cont = 0;
    }
    if (result[x].completed === true) {
      cont = cont + 1;
      dict[result[x].userId.toString()] = cont;
    }
    userant = result[x].userId;
  }
  console.log(dict);
});

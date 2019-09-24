#!/usr/bin/node
const array = process.argv.slice(2);
const request = require('request');
let x = 0;
let y = 0;
let result = [];
let cont = 0;
request(array[0], function (err, res, body) {
  if (err) {
  }
  result = JSON.parse(body).results;
  for (x = 0; x < result.length; x++) {
    for (y = 0; y < result[x].characters.length; y++) {
      if (result[x].characters[y].includes('18') === true) {
        cont = cont + 1;
      }
    }
  }
  console.log(cont);
});

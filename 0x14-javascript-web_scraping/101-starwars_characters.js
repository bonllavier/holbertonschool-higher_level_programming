#!/usr/bin/node
const array = process.argv.slice(2);
const request = require('request');
const request2 = require('request');
const url = 'https://swapi.co/api/films/';
let x = 0;
let result = {};
let result2 = {};
request(url + array[0], function (err, res, body) {
  result = JSON.parse(body);
  if (err) {
    console.log(err);
  } else {
    for (x = 0; x < result.characters.length; x++) {
      request2(result.characters[x], function (err2, res2, body2) {
        result2 = JSON.parse(body2);
        console.log(result2.name);
      });
    }
  }
});

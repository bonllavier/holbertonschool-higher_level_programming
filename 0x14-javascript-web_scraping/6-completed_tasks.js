#!/usr/bin/node
const array = process.argv.slice(2);
const request = require('request');
let x = 0;
const dict = {};
let cont = 0;
let result = [];
let k2 = '';
request(array[0], function (err, res, body) {
  if (err) {
  } else {
    result = JSON.parse(body);
    for (x = 0; x < result.length; x++) {
      dict[result[x].userId.toString()] = 0;
    }
    for (let key in dict) {
      cont = 0;
      for (x = 0; x < result.length; x++) {
        k2 = result[x].userId.toString();
        if (key === k2 && result[x].completed === true) {
          cont = cont + 1;
          dict[result[x].userId.toString()] = cont;
        }
      }
    }
    console.log(dict);
  }
});

#!/usr/bin/node
const array = process.argv.slice(2);
const request = require('request');
let x = 0;
const dict = {};
const dict2 = {};
let cont = 0;
let result = [];
let k2 = '';
/* const fs = require('fs');
const data = fs.readFileSync(array[0], 'utf8');
*/
request(array[0], function (err, res, body) {
  result = JSON.parse(body);
  result = JSON.parse(body);
  if (err) {
    console.log(err);
  } else {
    for (x = 0; x < result.length; x++) {
      dict[result[x].userId.toString()] = 0;
    }
    for (const key in dict) {
      cont = 0;
      for (x = 0; x < result.length; x++) {
        k2 = result[x].userId.toString();
        if (key === k2 && result[x].completed === true) {
          cont = cont + 1;
          dict2[result[x].userId.toString()] = cont;
        }
      }
    }
    console.log(dict2);
  }
});

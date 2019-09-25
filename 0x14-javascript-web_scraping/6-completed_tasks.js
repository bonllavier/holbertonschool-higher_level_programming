#!/usr/bin/node
const array = process.argv.slice(2);
const request = require('request');
let x = 0;
const dict = {};
let cont = 0;
let result = [];
request(array[0], function (err, res, body) {
  if (err) {
  } else {
    try {
      result = JSON.parse(body);
      for (x = 0; x < result.length; x++) {
        dict[result[x].userId.toString()] = 0;
      }
      for (var key in dict) {
        cont = 0;
        for (x = 0; x < result.length; x++) {
          if (key === result[x].userId.toString() &&
result[x].completed === true) {
            cont = cont + 1;
            dict[result[x].userId.toString()] = cont;
          }
        }
      }
      console.log(dict);
    } catch (e) {
      console.log(e);
    }
  }
});

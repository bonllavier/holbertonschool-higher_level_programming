#!/usr/bin/node
const array = process.argv.slice(2);
const url = 'http://swapi.co/api/films/';
const request = require('request');
request(url + array[0], function (err, res, body) {
  if (err) {
  }
  console.log(JSON.parse(body).title);
});

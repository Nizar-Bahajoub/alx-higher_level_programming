#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];

const output = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  fs.writeFile(output, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});

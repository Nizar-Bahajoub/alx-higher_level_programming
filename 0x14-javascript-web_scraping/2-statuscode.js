#!/usr/bin/node
// Display status code of Get Request

const request = require('request');

request.get(process.argv[2], (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});

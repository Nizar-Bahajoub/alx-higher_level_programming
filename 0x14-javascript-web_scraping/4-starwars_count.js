#!/usr/bin/node
const request = require('request');

const url = `${process.argv[2]}/people/18`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const filmdata = JSON.parse(body);
  console.log(filmdata.films.length);
});

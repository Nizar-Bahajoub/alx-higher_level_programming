#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  for (const filmIndex in films) {
    const filmChars = films[filmIndex].characters;

    for (const charIndex in filmChars) {
      if (filmChars[charIndex].includes('18')) {
        count++;
      }
    }
  }

  console.log(count);
});

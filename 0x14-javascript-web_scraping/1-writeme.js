#!/usr/bin/node
const fs = require('fs');

const content = process.argv[3];

const filepath = process.argv[2];

fs.writeFile(filepath, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});

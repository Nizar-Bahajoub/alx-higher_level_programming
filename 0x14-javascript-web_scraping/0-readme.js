#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 2) {
  console.log('Please proide the file path as an argument.');
  process.exit(1);
}

const filepath = process.argv[2];

fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

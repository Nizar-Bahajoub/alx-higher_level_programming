#!/usr/bin/node

const intValue = parseInt(process.argv[2]);
if (!isNaN(intValue)) { console.log('My number: ' + parseInt(process.argv[2])); } else { console.log('Not a number'); }

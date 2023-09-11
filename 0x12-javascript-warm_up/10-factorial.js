#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }

  return n * factorial(n - 1);
}

const input = parseInt(process.argv[2]);
const result = factorial(input);

console.log(result);

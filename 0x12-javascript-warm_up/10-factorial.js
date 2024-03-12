#!/usr/bin/node

function factorial (n) {
  // Base case: factorial of 0 or NaN is 1
  if (isNaN(n) || n === 0) {
    return 1;
  }
  // Recursive case: compute factorial recursively
  return n * factorial(n - 1);
}

const firstArg = process.argv[2];
const num = parseInt(firstArg);

console.log(factorial(num));

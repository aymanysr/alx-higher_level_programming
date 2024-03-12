#!/usr/bin/node

function factorial (n) {
  // Base case: factorial of 0 or NaN is 1
  if (isNaN(n) || n === 0) {
    return 1;
  }
  // Recursive case: compute factorial recursively
  return n * factorial(n - 1);
}

// Retrieve the command-line argument and compute its factorial
const num = parseInt(process.argv[2]);
const result = factorial(num);

console.log(result);

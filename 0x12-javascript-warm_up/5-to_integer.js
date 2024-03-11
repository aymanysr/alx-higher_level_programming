#!/usr/bin/node

const myArgs = process.argv;

console.log(parseInt(myArgs[2]) || 'Not a number');

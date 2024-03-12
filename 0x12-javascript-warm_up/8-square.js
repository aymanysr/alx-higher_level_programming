#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
  process.exit(1); // Exit the program
}

let i = 0;
while (i < size) {
  let line = '';
  let j = 0;
  while (j < size) {
    line += 'X';
    j++;
  }
  console.log(line);
  i++;
}

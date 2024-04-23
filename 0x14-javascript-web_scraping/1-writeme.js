#!/usr/bin/node

// write a string to a file

const filesys = require('fs');

filesys.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (error) {
    if (error) {
      console.log(error);
    }
  });

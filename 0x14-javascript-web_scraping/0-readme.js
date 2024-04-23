#!/usr/bin/node

// read the content of a file

const filesys = require('fs');
filesys.readFile(process.argv[2], 'utf-8',
  function (error, data) {
    if (error) {
      console.log(error);
      return;
    }
    console.log(data);
  });

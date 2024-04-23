#!/usr/bin/node

// Number of movies with the given character ID

const request = require('request');
let num = 0;

request.get(process.argv[2], (error, _response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(18)) {
          num += 1;
        }
      });
    });
    console.log(num);
  }
});

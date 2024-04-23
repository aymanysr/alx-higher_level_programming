#!/usr/bin/node

// web scrappcomputes the number of tasks completed by user id.

const request = require('request');

request.get(process.argv[2], { json: true }, (error, _response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const completedTasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 1;
      } else {
        completedTasks[todo.userId] += 1;
      }
    }
  });
  console.log(completedTasks);
});

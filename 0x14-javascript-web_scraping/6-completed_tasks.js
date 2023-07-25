#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const timeoutInMilliseconds = 10 * 1000;
const option = {
  url,
  timeout: timeoutInMilliseconds
};

request(option, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }

  const completed = {};
  const newbody = JSON.parse(body);
  for (const index in newbody) {
    const todo = newbody[index];
    const user = newbody[index].userId;
    if (todo.completed) {
      if (!completed[user]) {
        completed[user] = 1;
      } else {
        completed[user]++;
      }
    } else {
	console.log('An error occured')
    }
  }

  console.log(completed);
});

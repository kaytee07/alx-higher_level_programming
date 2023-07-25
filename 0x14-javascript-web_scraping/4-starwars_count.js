#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const findme = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

const timeoutInMilliseconds = 10 * 1000;
const options = {
  url,
  timeout: timeoutInMilliseconds
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(res.body);
  for (const index in data.results) {
    for (const ind in data.results[index].characters) {
      if (data.results[index].characters[ind] === findme) {
        count++;
      }
    }
  }

  console.log(count);
});

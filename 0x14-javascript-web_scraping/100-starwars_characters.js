#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const timeoutInMilliseconds = 10 * 1000;
const option = {
  url,
  timeout: timeoutInMilliseconds
};

request(option, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  for (const index in characters) {
    request(characters[index], function (err, res, body) {
      if (err) {
        console.log(err);
      }
      const chars = JSON.parse(body).name;
      console.log(chars);
    });
  }
});

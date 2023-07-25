#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
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
  const obj = JSON.parse(res.body);
  console.log(obj.title);
});

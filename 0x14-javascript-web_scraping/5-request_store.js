#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

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
  fs.writeFile(file, body, 'utf8', err => {
    if (err) {
      console.log(err);
    }
  });
});

#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const timeoutInMilliseconds = 10 * 1000;
const options = {
  url,
  timeout: timeoutInMilliseconds
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  }

  const statusCode = res.statusCode;
  console.log('code: ' + statusCode);
});

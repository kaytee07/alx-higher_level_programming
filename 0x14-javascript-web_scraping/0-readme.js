#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, info) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(info);
});
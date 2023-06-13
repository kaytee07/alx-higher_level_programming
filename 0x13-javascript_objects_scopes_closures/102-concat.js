#!/usr/bin/node
const fs = require('fs');
const fileC1 = fs.readFileSync(process.argv[2], toString());
const fileC2 = fs.readFileSync(process.argv[3], toString());
fs.writeFileSync(process.argv[4], fileC1 + fileC2);

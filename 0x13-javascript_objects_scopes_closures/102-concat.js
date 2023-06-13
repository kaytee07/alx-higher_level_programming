#!/usr/bin/node
const fs = require('fs');
const fileC1 = fs.readFileSync(process.argv[2], 'utf8');
const fileC2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], fileC1 + '\n' + fileC2 + '\n', 'utf8');

#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
let newList = list.map((val, index) => val * index);
console.log(newList);

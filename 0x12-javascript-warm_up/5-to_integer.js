#!/usr/bin/node
if (Number(process.argv[2])) {
  console.log(Number(process.argv[2]));
} else {
  console.log('Not a number');
}

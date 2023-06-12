#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arrOfNums = [];
  for (let i = 2; i < process.argv.length; i++) {
    arrOfNums.push(process.argv[i]);
    arrOfNums.sort((a, b) => a - b);
  }
  console.log(arrOfNums[arrOfNums.length - 2]);
}

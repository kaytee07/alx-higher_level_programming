#!/usr/bin/node
if (process.argv.length <= 2 || !Number(process.argv[3])) {
  console.log(1);
} else {
  let factorial = 1;
  for (let i = Number(process.argv[2]); i > 0; i--) {
    factorial *= i;
  }
  console.log(factorial);
}

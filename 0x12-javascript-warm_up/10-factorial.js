#!/usr/bin/node
const computeFactorial = (n) => {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0) {
    return 1;
  }

  return n * computeFactorial(n - 1);
};
const number = parseInt(process.argv[2]);
const factorial = computeFactorial(number);
console.log(factorial);

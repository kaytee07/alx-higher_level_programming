#!/usr/bin/node
if (process.argv.length === 2 || !Number(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    let arg = '';
    for (let j = 0; j < process.argv[2]; j++) {
      arg += 'X';
    }
    console.log(arg);
  }
}

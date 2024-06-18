#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('1');
} else {
  let factorial = 1;
  while (process.argv[2] !== 0) {
    factorial *= process.argv[2];
    process.argv[2] = process.argv[2] - 1;
  }
  console.log(factorial);
}

#!/usr/bin/node

if (process.argv.length === 2) {
	let x = 1;
	console.log(x);
} else {
  let factorial = 1;
  while (process.argv[2] != 0) {
    factorial *= process.argv[2];
    process.argv[2] = process.argv[2] - 1;
  }
  console.log(factorial)
}

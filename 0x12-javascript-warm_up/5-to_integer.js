#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('Not a number');
} else if (process.argv.length === 3) {
  if (!isNaN(parseFloat(process.argv[2])) && isFinite(process.argv[2])) {
    console.log(process.argv[2]);
  } else {
    console.log('Not a number');
  }
}

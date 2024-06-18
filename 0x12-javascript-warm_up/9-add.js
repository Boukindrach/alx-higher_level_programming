#!/usr/bin/node

function add(a, b) {
  return a + b;
}

if (process.argv.length <= 3){
  console.log('NaN');
} else {
  let sum = 0;
  for (let i = 2; i < process.argv.length; i++) {
    sum += Number(process.argv[i]);
  }
  console.log(sum)
}

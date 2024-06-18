#!/usr/bin/node

function Factorial (number) {
  let factorial = 1;
  while (number !== 0) {
    factorial *= number;
    number = number - 1;
  }
  return factorial;
}

if (isNaN(process.argv[2])) {
  console.log(Factorial(1));
} else {
  console.log(Factorial(Number(process.argv[2])));
}

#!/usr/bin/python3

if __name__ == "__main__":

from calculator_1 import add, mul, div, sub
import sys

x = len(sys.argv) - 1
a = int(sys.argv[1])
b = int(sys.argv[x])
operator = sys.argv[x - 1]
operators = {"+", "*", "-", "/"}

if x < 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")

else:
    if operator in operators:
        if operator == '+':
            print(add(a, b))

        elif operator == '*':
            print(mul(a, b))

        elif operator == '-':
            print(sub(a, b))

        elif operator == '/':
            print(div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")

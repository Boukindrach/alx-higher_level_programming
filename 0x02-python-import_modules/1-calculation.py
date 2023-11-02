#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul
    a = 10
    b = 5
    x = add(a, b)
    c = "{}".format(x)
    print(f"{a} + {b} = {c}")

    x = sub(a, b)
    c = "{}".format(x)
    print(f"{a} - {b} = {c}")

    x = mul(a, b)
    c = "{}".format(x)
    print(f"{a} * {b} = {c}")

    x = div(a, b)
    c = "{}".format(x)
    print(f"{a} / {b} = {c}")

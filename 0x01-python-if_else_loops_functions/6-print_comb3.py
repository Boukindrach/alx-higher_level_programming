#!/usr/bin/python3
num = ""
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i != 8 or j != 9:
            num += "{}{}, ".format(i, j)
        else:
            num += "{}{}".format(i, j)

print(num)

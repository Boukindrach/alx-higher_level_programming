#!/usr/bin/python3
num = ""
for i in range(0, 100):
    if i < 10:
        num += '0{}'.format(i)
    else:
        num += '{}'.format(i)

    if i < 99:
        num += ", "
print(num)

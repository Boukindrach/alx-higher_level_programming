#!/usr/bin/python3
num = ""
for i in range(0, 80):
    num += "{}".format(i)

    if i < 79:
        num += ", "
    else:
        num += ", 89"
print(num)

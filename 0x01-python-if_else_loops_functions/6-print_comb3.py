#!/usr/bin/python3
num = ""
for i in range(0, 80):
    if i < 10:
        num += "0{}".format(i)
    else:
        num += "{}".format(i)

    if i < 79:
        num += ", "
    else:
        num += ", 89"
print(num)

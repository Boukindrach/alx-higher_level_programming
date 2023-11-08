#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    x = 0
    y = 0
    for a in my_list:
        x += (a[0] * a[1])
        y += a[1]
    return x / y

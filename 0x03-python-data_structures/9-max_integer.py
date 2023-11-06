#!/usr/bin/python3
def max_integer(my_list=[]):
    x = len(my_list)
    if x == 0:
        return None
    else:
        max_ = my_list[0]
        for a in range(x):
            if my_list[a] > max_:
                max_ = my_list[a]
    return max_

#!/usr/bin/python3
def element_at(my_list, idx):
    x = len(my_list)
    if idx < 0:
        return None
    for i in range(x):
        if i == idx:
            return my_list[i]

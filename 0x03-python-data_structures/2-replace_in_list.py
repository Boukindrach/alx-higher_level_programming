#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    x = len(my_list)
    if idx < 0 and idx < element:
        return None
    for i in range(x):
        if i == idx:
            my_list[i] = element
            return my_list

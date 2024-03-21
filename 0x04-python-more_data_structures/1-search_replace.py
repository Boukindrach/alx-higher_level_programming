#!/usr/bin/python3
def search_replace(my_list, search, replace):
    x = len(my_list)
    new_list = my_list[:]
    for i in range(x):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list

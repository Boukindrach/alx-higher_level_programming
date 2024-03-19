#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    x = len(my_list)
    if idx < 0 and idx < element:
        return None
    else:
        my_list[idx] = element
        return my_list

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not isinstance(my_list, list):
        return
    reversed_list = list(reversed(my_list))
    for i in reversed_list:
        print("{:d}".format(i))

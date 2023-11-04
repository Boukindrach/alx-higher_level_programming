#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list)
    if my_list:
       # my_list.reverse()
        for a in my_list[::-1]:
            print("{:d}".format(a))

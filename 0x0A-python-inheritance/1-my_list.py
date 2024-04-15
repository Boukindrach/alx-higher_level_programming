#!/usr/bin/python3

"""Defines a class that inherits from the 'list' class"""


class MyList(list):
    """Subclass of 'list' class"""
    def print_sorted(self):
        """Sorts and prints the list"""
        sorted_list = (sorted(self[:]))
        print(sorted_list)

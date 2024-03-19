#!/usr/bin/python3
def no_c(my_string):
    filter_chars = [char for char in my_string if char not in 'cC']
    return ''.join(filter_chars)

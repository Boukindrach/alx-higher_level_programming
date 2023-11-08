#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for a in sorted(a_dictionary):
        print(f"{a}: {a_dictionary[a]}")

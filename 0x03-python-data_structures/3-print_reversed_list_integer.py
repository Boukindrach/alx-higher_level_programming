#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list)
    for a in range(x-1, -1, -1):
            print("{:d}".format(my_list[a]))


if __name__ == "__main__":
    print_reversed_list_integer()

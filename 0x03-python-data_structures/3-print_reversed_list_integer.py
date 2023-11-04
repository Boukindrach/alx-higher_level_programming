#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list)
    if my_list:
        my_list.reverse()
        for a in range(x):
            print("{:d}".format(my_list[a]))


if __name__ == "__main__":
    print_reversed_list_integer()

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list)
    for a in range(x):
        if x > 0:
            print("{:d}".format(my_list[x - 1]))
            x -= 1


if __name__ == "__main__":
    print_reversed_list_integer()

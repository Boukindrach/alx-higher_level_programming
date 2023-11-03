#!/usr/bin/python3
def print_list_integer(my_list=[]):
    x = len(my_list)
    for a in range(0, x):
        print("{}".format(my_list[a]))

if __name__ == "__main__":
    print_list_integer()

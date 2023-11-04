#!/usr/bin/python3
def no_c(my_string):
    x = len(my_string)
    str_1 = ""
    for a in range(0, x):
        if my_string[a] == 'c' or my_string[a] == 'C':
            continue
        else:
            str_1 += "{}".format(my_string[a])
    return str_1


if __name__ == "__main__":
    no_c()

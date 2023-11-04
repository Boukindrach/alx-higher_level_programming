#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = len(my_list)
    if idx < 0:
        return my_list

    if x <= idx:
        return my_list

    my_new_list = list(my_list)
    my_new_list[idx] = element
    return my_new_list


if __name__ == "__main__":
    new_in_list()

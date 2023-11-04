#!/usr/bin/python3
def element_at(my_list, idx):
    x = len(my_list)
    if idx < 0:
        return None
    elif x <= idx:
        return None
    else:
        return my_list[idx]


if __name__ == "__main__":
    element_at()

#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = 0
    num_of_args = len(sys.argv)
    for i in range(1, num_of_args):
        a = a + int(sys.argv[i])
    print("{}".format(a))

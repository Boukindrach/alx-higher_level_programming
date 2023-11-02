#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1
    if x == 0:
        print(f"{x} arguments.")
    elif x == 1:
        print(f"{x} argument:")
        print(f"{x}: {sys.argv[x]}")
    else:
        print(f"{x} arguments:")
        for a in range(1, x + 1):
            print(f"{a}: {sys.argv[a]}")

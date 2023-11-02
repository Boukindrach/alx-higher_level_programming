#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = 0
    x = len(sys.argv) - 1
    for a in range(1, x + 1):
        c += int(sys.argv[a])
    print(c)

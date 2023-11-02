#!/usr/bin/python3
import sys
x = len(sys.argv) - 1
if x == 0:
    print(f"{x} arguments.")
else:
    print(f"{x} arguments:")
    for a in range (1, x + 1):
        print(f"{a}: {sys.argv[a]}")

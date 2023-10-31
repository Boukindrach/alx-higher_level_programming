#!/usr/bin/python3
def uppercase(str):
    got = ""
    for i in str:
        if 'a' <= i <= 'z':
            got += chr(ord(i) - 32)
        else:
            got += i
    print(got)

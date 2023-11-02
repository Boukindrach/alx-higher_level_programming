#!/usr/bin/python3
def print_alphabet(letter):
    print(letter, end='') if letter < 'Z' else print()
    print_alphabet(chr(ord(letter) + 1)) if letter < 'Z' else None

print_alphabet('A')

#!/usr/bin/python3
"""Defines a function for reading text files."""


def read_file(filename=""):
    """Prints UTF-8 encoded text file to the standard output."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

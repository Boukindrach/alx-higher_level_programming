#!/usr/bin/python3
"""Defines a function for reading text files."""


def read_file(filename=""):
    """Prints the content of a UTF-8 encoded text file 
		to the standard output.

    Args:
        filename (str, optional): The name of the file to read.
		Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

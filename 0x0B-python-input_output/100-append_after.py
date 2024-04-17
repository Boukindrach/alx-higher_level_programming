#!/usr/bin/python3

"""Defines a function to insert text after lines with a specified string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each occurrence of a string in a file's lines.

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for in file lines.
        new_string (str): String to insert after found occurrences.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

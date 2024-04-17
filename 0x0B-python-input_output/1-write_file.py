#!/usr/bin/python3

"""Defines a function for writing to text files."""


def write_file(filename="", text=""):
    """Write the provided text to a UTF-8 encoded file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text content to write to the file.
        
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

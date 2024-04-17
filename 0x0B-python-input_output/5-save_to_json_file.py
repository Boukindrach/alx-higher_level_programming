#!/usr/bin/python3

"""Defines a function for saving objects to JSON files."""
import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a JSON-formatted text file.

    Args:
        my_obj (any): The object to save to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)

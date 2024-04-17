#!/usr/bin/python3

"""Defines a function for loading objects from JSON files."""
import json


def load_from_json_file(filename):
    """Load a Python object from a JSON-formatted text file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        any: The Python object loaded from the JSON file.
    """
    with open(filename) as file:
        return json.load(file)

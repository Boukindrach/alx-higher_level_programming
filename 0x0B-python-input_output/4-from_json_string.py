#!/usr/bin/python3

"""Defines a function for converting JSON strings to Python objects."""
import json


def from_json_string(my_str):
    """Converts a JSON-formatted string to a Python object.

    Args:
        my_str (str): The JSON-formatted string to convert.

    Returns:
        any: The Python object representation of the JSON string.
    """
    return json.loads(my_str)

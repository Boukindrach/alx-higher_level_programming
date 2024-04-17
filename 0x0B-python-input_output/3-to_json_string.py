#!/usr/bin/python3

"""Defines a function for converting objects to JSON strings."""
import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON-formatted string.

    Args:
        my_obj (any): The object to convert to JSON.

    Returns:
        str: The JSON-formatted string representation of my_obj.
    """
    return json.dumps(my_obj)

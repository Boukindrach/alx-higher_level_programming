#!/usr/bin/python3

"""Converts a class instance to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Convert an object instance to a dictionary of its attributes

    Args:
        obj (object): The object to convert.

    Returns:
        dict: Dictionary representation of the object's attributes.
    """
    return obj.__dict__

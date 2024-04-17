#!/usr/bin/python3

"""Defines a function for converting a class 
	instance to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Convert a class instance to a dictionary
		representing its instance variables.

    Args:
        obj (object): The object (instance of a class) to convert.

    Returns:
        dict: A dictionary representation of the object's
		instance variables.
    """
    return obj.__dict__

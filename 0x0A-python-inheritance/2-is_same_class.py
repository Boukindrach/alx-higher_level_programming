#!/usr/bin/python3

"""Defines a function to check object class."""


def is_same_class(obj, a_class):
    """Verify if an object is an instance 
		of a specific class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare 
		against the type of obj.
        
    Returns:
        True if obj is an instance of a_class
		otherwise False.
    """
    return type(obj) == a_class

#!/usr/bin/python3

"""Defines a function to check object class or inheritance."""


def is_kind_of_class(obj, a_class):

    """Verify if an object is an inherited instance of a specific class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against the type of obj.
     
    Returns:
        True if obj is an inherited instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class):
        return True
    return False

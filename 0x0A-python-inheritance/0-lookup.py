#!/usr/bin/python3

"""Return a list of an object's available attributes."""


def lookup(obj):
    """Retrieve a list of attributes available for an object."""
    return (dir(obj))

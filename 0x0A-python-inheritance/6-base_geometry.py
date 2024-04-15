#!/usr/bin/python3

"""Defines a BaseGeometry class for geometry calculations."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raises an exception for unimplemented area calculation."""
        raise Exception("area() is not implemented")

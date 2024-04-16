#!/usr/bin/python3

"""Defines a BaseGeometry class for geometric operations."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raises an exception for unimplemented area calculation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""Represent a square."""


class Square:
    """A square."""

    def __init__(self, size=0):
        """Initialize a new Square with the specified size.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size should be an integer")

        elif size < 0:
            raise ValueError("size should be >= 0")
        self.__size = size

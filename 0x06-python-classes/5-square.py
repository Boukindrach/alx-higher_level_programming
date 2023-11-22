#!/usr/bin/python3
"""Represent a square."""


class Square:
    """A square."""

    def __init__(self, size):
        """Initialize a new Square

        Args:
            size (int): The size of the new square.
        """
        self._size = size

    @property
    def size(self):
        """Get or set the current size of the square."""

        
    return self._size
    @size.setter

    
    def size(self, value):
        """Set the current size of the square, validating the input."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be non-negative")

        self._size = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self._size * self._size

    def my_print(self):
        """Print the square using the '#' character."""
        if not self._size:
            print("")
            return

        for _ in range(self._size):
            for _ in range(self._size):
                print("#", end="")

            print()

#!/usr/bin/python3
"""Define a MagicClass representing a circle."""

import math


class MagicClass:
    """Represent a circle with specified radius."""

    def __init__(self, radius=0):
        """Initialize a MagicClass with the specified radius.

        Args:
            radius (float or int): The radius of the new MagicClass. Default is 0.
        """
        self._radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number (integer or float).")

        self._radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self._radius ** 2

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self._radius

#!/usr/bin/python3

"""Function that prints a square"""


def print_square(size):
	"""Prints a square of '#' characters with the specified size.

    Args:
        size (int): The size of the square. Must be a non-negative integer.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """
	if not isinstance(size, int):
		raise TypeError("size must be an integer")
	if size < 0:
		raise ValueError("size must be >= 0")

	for i in range(size):
		[print("#", end="") for j in range(size)]
		print("")

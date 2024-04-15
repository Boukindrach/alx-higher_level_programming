#!/usr/bin/python3

"""function that adds 2 integers."""


def add_integer(a, b=98):
	"""Return the integer addition of two numbers.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or a float.

    Returns:
        int: The sum of a and b, casted to an integer.
    """
	if ((not isinstance(a, int) and not isinstance(a, float))):
		raise TypeError("a must be an integer")
	if ((not isinstance(b, int) and not isinstance(b, float))):
		raise TypeError("b must be an integer")
	return (int(a) + int(b))

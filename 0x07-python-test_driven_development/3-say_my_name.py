#!/usr/bin/python3

""" A function name-printing"""


def say_my_name(first_name, last_name=""):
	"""Prints a formatted name using the provided first name and optional last name.

    Args:
        first_name (str): The first name to include in the formatted name.
        last_name (str, optional): The last name to include in the formatted name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
	if not isinstance(first_name, str):
		raise TypeError("first_name must be a string")
	if not isinstance(last_name, str):
		raise TypeError("last_name must be a string")
	print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
	"""Represent a rectangle."""
	def __init__(self, width=0, height=0):
		"""Initialize a new Rectangle.

		Args:
		width (int): The width of the new rectangle. Default is 0.
		height (int): The height of the new rectangle. Default is 0.
		"""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""Get or set the width of the Rectangle."""
		return (self.__width)

	@width.setter
	def width(self, value):
		"""Set the width of the Rectangle."""
		self._validate_dimension(value, "width")
		self.__width = value

	@property
	def height(self):
		"""Get or set the height of the Rectangle."""
		return (self.__height)

	@height.setter
	def height(self, value):
		"""Set the height of the Rectangle."""
		self._validate_dimension(value, "height")
		self.__height = value

	def _validate_dimension(self, value, dimension_name):
		"""Validate if the dimension is a positive integer."""
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")

	def area(self):
		"""Return the area of the Rectangle."""
		return self.__width * self.__height

	def perimeter(self):
		"""Return the perimeter of the Rectangle."""
		if self.__width == 0 or self.__height == 0:
			return (0)
		return ((self.__width * 2) + (self.__height * 2))

	def __str__(self):
		"""Return the printable representation of the Rectangle.

		Represents the rectangle with the # character.
		"""
		if self.__width == 0 or self.__height == 0:
			return ("")

		r = []
		for i in range(self.__height):
			r.extend(['#' for j in range(self.__width)])
			if i != self.__height - 1:
				r.append("\n")
		return ("".join(r))

	def __repr__(self):
		"""Return the string representation of the Rectangle."""
		return "Rectangle({}, {})".format(self.__width, self.__height)

	def __del__(self):
		"""Print a message for every deletion of a Rectangle."""
		print("Bye rectangle...")


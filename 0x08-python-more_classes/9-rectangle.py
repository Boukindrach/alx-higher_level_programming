#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
	"""Represent a rectangle."""
	
	print_symbol = "#"
	number_of_instances = 0

	def __init__(self, width=0, height=0):
		"""Initialize a new Rectangle.

		Args:
		width (int): The width of the new rectangle. Default is 0.
		height (int): The height of the new rectangle. Default is 0.
		"""
		type(self).number_of_instances += 1
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
			[r.extend(str(self.print_symbol)) for j in range(self.__width)]
			if i != self.__height - 1:
				r.append("\n")
		return ("".join(r))

	def __repr__(self):
		"""Return the string representation of the Rectangle."""
		return "Rectangle({}, {})".format(self.__width, self.__height)

	def __del__(self):
		"""Print a message for every deletion of a Rectangle."""
		type(self).number_of_instances -= 1
		print("Bye rectangle...")
	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		"""Return the Rectangle with the greater area.

		Args:
		rect_1 (Rectangle): The first Rectangle.
		rect_2 (Rectangle): The second Rectangle.
		Raises:
		TypeError: If either of rect_1 or rect_2 is not a Rectangle.
		"""
		if not isinstance(rect_1, Rectangle):
			raise TypeError("rect_1 must be an instance of Rectangle")
		if not isinstance(rect_2, Rectangle):
			raise TypeError("rect_2 must be an instance of Rectangle")
		return rect_1 if rect_1.area() >= rect_2.area() else rect_2
	@classmethod
	def square(cls, size=0):
		"""Return a new Rectangle with width and height equal to size.

		Args:
		size (int): The width and height of the new Rectangle.
		"""
		return cls(size, size)

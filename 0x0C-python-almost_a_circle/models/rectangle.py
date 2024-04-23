#!/usr/bin/python3

"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self._y = value

    def area(self):
        """Return area of the rectangle"""
        return self._height * self._width

    def display(self):
        """Prints size of rectangle using #"""
        for y in range(0, self._y):
            print("")
        for height in range(self._height):
            for x in range(self._x):
                print(" ", end="")
            for width in range(self._width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle"""
        count = 0
        if args:
            for arg in args:
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self._x = arg
                elif count == 4:
                    self._y = arg
                count += 1
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self._width = value
                if key == "height":
                    self._height = value
                if key == "x":
                    self._x = value
                if key == "y":
                    self._y = value

    def __str__(self):
        """Return the print() and str() representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self._x,
                self._y,
                self._width,
                self._height
                )

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }

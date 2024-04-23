#!/usr/usr/python3

"""Defines a square class."""
from models.rectangle import Rectangle
from models.base import Base

class Square(Rectangle):

    """Represent a square."""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

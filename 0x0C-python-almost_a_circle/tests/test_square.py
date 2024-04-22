#!/usr/bin/python3

from io import StringIO
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_default_initialization(self):
        square = Square(size=5)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_custom_initialization(self):
        square = Square(size=5, x=2, y=3, id=10)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 10)

    def test_inheritance(self):
        self.assertTrue(issubclass(Square, Rectangle))


class TestSquareStrMethod(unittest.TestCase):

    def test_str_representation(self):
        square = Square(size=5, x=2, y=3, id=10)
        expected_str = "[Square] (10) 2/3 - 5"
        self.assertEqual(str(square), expected_str)


class TestSquare_setter(unittest.TestCase):

    def test_size_property(self):
        square = Square(size=5)
        self.assertEqual(square.size, 5)

    def test_set_size(self):
        square = Square(size=5)
        square.size = 10
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)


class TestSquare_update(unittest.TestCase):

    def test_update_with_args(self):
        rect = Square(size=10)
        rect.update(5, 15, 2, 3)
        self.assertEqual(rect.size, 15)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 5)

    def test_update_with_kwargs(self):
        rect = Square(size=10)
        rect.update(id=5, size=15, x=2, y=3)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.size, 15)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)


class TestSquare_To_DictionaryMethod(unittest.TestCase):

    def test_to_dictionary(self):
        square = Square(size=5, x=2, y=3, id=10)
        expected_dict = {'id': 10, 'x': 2, 'size': 5, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()

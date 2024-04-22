#!/usr/bin/python3

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_stdout:

    @staticmethod
    def capture_stdout(obj, method_name, *args, **kwargs):
        captured_output = StringIO()
        sys.stdout = captured_output

        getattr(obj, method_name)(*args, **kwargs)

        sys.stdout = sys.__stdout__
        return captured_output


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init_with_id(self):
        rect = Rectangle(width=10, height=20, id=5)
        self.assertEqual(rect.id, 5)

    def test_init_without_id(self):
        rect1 = Rectangle(width=10, height=20)
        rect2 = Rectangle(width=15, height=25)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 2)

    def test_init_attributes(self):
        rect = Rectangle(width=10, height=20, x=5, y=10)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 10)

    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))


class TestRectangle_width(unittest.TestCase):

    def test_get_width(self):
        rect = Rectangle(width=10, height=20)
        self.assertEqual(rect.width, 10)

    def test_set_width_valid(self):
        rect = Rectangle(width=10, height=20)
        self.assertEqual(rect.width, 10)

    def test_set_width_valid(self):
        rect = Rectangle(width=10, height=20)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_set_width_non_integer(self):
        rect = Rectangle(width=10, height=20)
        with self.assertRaises(TypeError):
            rect.width = 'invalid'

    def test_set_width_zero_or_negative(self):
        rect = Rectangle(width=10, height=20)
        with self.assertRaises(ValueError):
            rect.width = 0

        with self.assertRaises(ValueError):
            rect.width = -5


class TestRectangle_height(unittest.TestCase):

    def test_get_height(self):
        rect = Rectangle(width=10, height=20)
        self.assertEqual(rect.width, 10)

    def test_set_height_valid(self):
        rect = Rectangle(width=10, height=20)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_set_height_non_integer(self):
        rect = Rectangle(width=10, height=20)
        with self.assertRaises(TypeError):
            rect.width = 'invalid'

    def test_set_height_zero_or_negative(self):
        rect = Rectangle(width=10, height=20)
        with self.assertRaises(ValueError):
            rect.width = 0

        with self.assertRaises(ValueError):
            rect.width = -5


class TestRectangle_x(unittest.TestCase):

    def test_get_x(self):
        rect = Rectangle(width=10, height=20, x=5)
        self.assertEqual(rect.x, 5)

    def test_set_x_valid(self):
        rect = Rectangle(width=10, height=20)
        rect.x = 15
        self.assertEqual(rect.x, 15)

    def test_set_x_non_integer(self):
        rect = Rectangle(width=10, height=20)
        with self.assertRaises(TypeError):
            rect.x = 'invalid'

    def test_set_x_negative(self):
        rect = Rectangle(width=10, height=20)
        with self.assertRaises(ValueError):
            rect.x = -5


class TestRectangle_y(unittest.TestCase):

    def test_get_y(self):
        rect = Rectangle(width=10, height=20, y=5)
        self.assertEqual(rect.y, 5)

    def test_set_y_valid(self):
        rect = Rectangle(width=10, height=20)
        rect.y = 15
        self.assertEqual(rect.y, 15)

    def test_set_y_non_integer(self):
        rect = Rectangle(width=10, height=20)
        with self.assertRaises(TypeError):
            rect.y = 'invalid'

    def test_set_y_negative(self):
        rect = Rectangle(width=10, height=20)
        with self.assertRaises(ValueError):
            rect.y = -5


class TestRectangle_area(unittest.TestCase):

    def test_area(self):
        rect = Rectangle(width=10, height=20)
        self.assertEqual(rect.area(), 200)


class TestRectangle_display(unittest.TestCase):

    def test_display(self):
        rect = Rectangle(width=4, height=3, x=1, y=2)
        captured_output = TestRectangle_stdout.capture_stdout(rect, "display")
        self.assertEqual(captured_output.getvalue(), "\n\n ####\n ####\n ####\n")


class TestRectangle_args_kwargs(unittest.TestCase):

    def test_update_with_args(self):
        rect = Rectangle(width=10, height=20)
        rect.update(5, 15, 25, 2, 3)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_update_with_kwargs(self):
        rect = Rectangle(width=10, height=20)
        rect.update(id=5, width=15, height=25, x=2, y=3)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)


if __name__ == '__main__':
    unittest.main()

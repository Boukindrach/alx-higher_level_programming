#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_nb_objects_counter(self):
        Base._Base__nb_objects = 0
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)


if __name__ == '__main__':
    unittest.main()

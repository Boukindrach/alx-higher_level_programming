#!/usr/bin/python3

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os


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

class Test_JsonString_Function_Rectangle(unittest.TestCase):

    def test_to_json_string_with_list(self):
        list_dicts = [{'id': 1, 'height': 20}, {'id': 2, 'width': 10, 'x': 0, 'y': 6}]
        expected_json_str = '[{"id": 1, "height": 20}, {"id": 2, "width": 10, "x": 0, "y": 6}]'
        self.assertEqual(Rectangle.to_json_string(list_dicts), expected_json_str)

    def test_to_json_string_with_empty_list(self):
        self.assertEqual(Rectangle.to_json_string([]), "[]")

    def test_to_json_string_with_none(self):
        self.assertEqual(Rectangle.to_json_string(None), "[]")

class Test_JsonString_Function_Square(unittest.TestCase):

    def test_to_json_string_with_list(self):
        list_dicts = [{'id': 1, 'size': 15}, {'id': 2, 'size': 20, 'x': 1}]
        expected_json_str = '[{"id": 1, "size": 15}, {"id": 2, "size": 20, "x": 1}]'
        self.assertEqual(Square.to_json_string(list_dicts), expected_json_str)

    def test_to_json_string_with_empty_list(self):
        self.assertEqual(Square.to_json_string([]), "[]")

    def test_to_json_string_with_none(self):
        self.assertEqual(Square.to_json_string(None), "[]")

class TestSaveToFileFunction(unittest.TestCase):

    class TestClass:
        def __init__(self, id=None, width=None):
            self.id = id
            self.width = width

        def to_dictionary(self):
            return {'id': self.id, 'width': self.width}

    def test_save_to_file_with_objects(self):
        obj1 = self.TestClass(id=1, width=10)
        obj2 = self.TestClass(id=2, width=15)
        Square.save_to_file([obj1, obj2])
        
        with open("TestClass.json", "w") as file:
            content = file.read()
            expected_content = '[{"id": 1, "width": 10}]', '[{"id": 2, "width": 15}]'
            self.assertEqual(content, expected_content)

    def test_save_to_file_with_empty_list(self):
        Square.save_to_file([])
        
        with open("TestClass.json", "w") as file:
            content = file.read()
            self.assertEqual(content, "[]")

if __name__ == '__main__':
    unittest.main()

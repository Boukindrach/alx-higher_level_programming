#!/user/bin/python3

import unittest
from models.square import Square
from models.rectangle import Rectangle

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square1 = Square(5)
        self.square2 = Square(3, 2, 3, 10)

    def test_init(self):
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square1.width, 5)
        self.assertEqual(self.square1.height, 5)
        self.assertEqual(self.square1.x, 0)
        self.assertEqual(self.square1.y, 0)
        self.assertEqual(self.square1.id, 23)

        self.assertEqual(self.square2.size, 3)
        self.assertEqual(self.square2.width, 3)
        self.assertEqual(self.square2.height, 3)
        self.assertEqual(self.square2.x, 2)
        self.assertEqual(self.square2.y, 3)
        self.assertEqual(self.square2.id, 10)

    def test_size_property(self):
        self.square1.size = 7
        self.assertEqual(self.square1.size, 7)
        self.assertEqual(self.square1.width, 7)
        self.assertEqual(self.square1.height, 7)

    def test_update(self):
        self.square1.update(2, 10, 1, 1)
        self.assertEqual(self.square1.id, 2)
        self.assertEqual(self.square1.size, 10)
        self.assertEqual(self.square1.x, 1)
        self.assertEqual(self.square1.y, 1)

        self.square2.update(size=4, y=7, id=8)
        self.assertEqual(self.square2.id, 8)
        self.assertEqual(self.square2.size, 4)
        self.assertEqual(self.square2.y, 7)

    def test_to_dictionary(self):
        dict_square1 = self.square1.to_dictionary()
        self.assertEqual(dict_square1, {'id': 26, 'size': 5, 'x': 0, 'y': 0})

        dict_square2 = self.square2.to_dictionary()
        self.assertEqual(dict_square2, {'id': 10, 'size': 3, 'x': 2, 'y': 3})

    def test_str(self):
        self.assertEqual(str(self.square1), "[Square] (25) 0/0 - 5")
        self.assertEqual(str(self.square2), "[Square] (10) 2/3 - 3")

if __name__ == '__main__':
    unittest.main()

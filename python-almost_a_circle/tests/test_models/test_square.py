#!/usr/bin/python3
"""
This is the "test_square" module
Thes test_square module supplies a class to test class Square
"""

from re import S
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os.path import exists
import io
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """
    test classe square
    """

    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass

    def test_correct_values(self):
        r1 = Square(2, 4, 6)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 1)

        r2 = Square(2, 4, 6, 50)
        self.assertEqual(r2.size, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 6)
        self.assertEqual(r2.id, 50)

        r3 = Square(2)
        self.assertEqual(r3.size, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 2)

    def test_priority_width_height(self):
        with self.assertRaises(ValueError):
            r1 = Square(-2, -6, -4)
            r2 = Square("str", "str", 3, None)
            r3 = Square("str", -2, 3, None)
            r4 = Square(-1, -2, 3, None)
            r5 = Square(-1, "str", 3, None)

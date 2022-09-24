#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for max at the end"""
    def test_maxAtTheEnd(self):
        self.assertEqual(test_MaxAtTheEnd([1, 2 , 5, 10], 10))

    """Test for max at the beginning"""
    def test_maxAtTheBeginning(self):
        self.assertEqual(test_maxAtTheBeginning([10, 4, 3, 1], 10))

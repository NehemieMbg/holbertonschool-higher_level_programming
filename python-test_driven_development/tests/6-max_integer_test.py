#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_maxAtTheEnd(self):
        """Test for max at the end"""
        self.assertEqual(max_integer([1, 2 , 5, 10], 10))

    def test_maxAtTheBeginning(self):
        """Test for max at the beginning"""
        self.assertEqual(max_integer([10, 4, 3, 1], 10))

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for max at the end"""
    def test_MaxAtTheEnd(self):
        self.assertEqual.test_MaxAtTheEnd(([1, 2 , 5, 10], 10))

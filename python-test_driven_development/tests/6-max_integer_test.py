#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_maxAtTheEnd(self):
        """Test for max at the end"""
        self.assertEqual(max_integer([1, 2 , 5, 10]), 10)

    def test_maxAtTheBeginning(self):
        """Test for max at the beginning"""
        self.assertEqual(max_integer([10, 4, 3, 1]), 10)
    
    def test_maxInTheMiddle(self):
        """Test for max in the middle"""
        self.assertEqual(max_integer([2, 3, 10, 5, 8]), 10)
    
    def test_oneNegativeNumber(self):
        """Test for one negative number"""
        self.assertEqual(max_integer([6, -3, 7, 8]), 8)
    
    def test_onlyNegativeNum(self):
        """Test for only negative number"""
        self.assertEqual(max_integer([-100, -85, -69, -24]), -24)
    
    def test_listOfElement(self):
        """Test for list of one element"""
        elem = [74]
        self.assertEqual(max_integer(elem), 74)

    def test_emptyList(self):
        """Test for an empty list"""
        elem = []
        self.assertEqual(max_integer(elem), None)

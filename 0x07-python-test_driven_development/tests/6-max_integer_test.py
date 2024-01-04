#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        """Test with a regular list."""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unsorted_list(self):
        """Test with an unsorted list."""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test with an empty list."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        result = max_integer([-5, -3, -8, -1])
        self.assertEqual(result, -1)

    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers."""
        result = max_integer([2, 2, 2, 2])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

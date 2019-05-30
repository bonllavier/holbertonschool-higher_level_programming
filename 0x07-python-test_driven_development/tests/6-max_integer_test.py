#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        """
        simple cases
        """
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test2(self):
        """
        simple cases2
        """
        result = max_integer([])
        self.assertEqual(result, None)

    def test_None(self):
        """ test for 1 item
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test2(self):
        """
        negative
        """
        with self.assertRaises(TypeError):
            max_integer(-1)

    def conv_integer(self):
        """
        conversion cases
        """
        list = ["husjklsd", "sdjhklduhjiklsf;d"]
        self.assertEqual(max_integer(list), 365)

    def test_false_integer(self):
        """
        false test
        """
        list = [1, 2, 3, 4]
        self.assertFalse(max_integer(list) == 2)

    def max_begin(self):
        """
        max at the beginning
        """
        result = max_integer([4, 1, 2])
        self.assertEqual(result, 4)

    def max_middle(self):
        """
        max in middle
        """
        result = max_integer([1, 4, 2])
        self.assertEqual(result, 4)

    def negative_number(self):
        """
        negative in the list
        """
        result = max_integer([3, -1, 2])
        self.assertEqual(result, 3)

    def all_negative(self):
        """
        all negative
        """
        result = max_integer([-2, -3, -1])
        self.assertEqual(result, None)

    def only_one(self):
        """
        only one element
        """
        result = max_integer([2])
        self.assertEqual(result, 2)

    def list_empty(self):
        """
        list empty
        """
        result = max_integer([])
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 1, 2]), 3)
        self.assertEqual(max_integer([2, 3, 1]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-3, -1, -2]), -1)
        self.assertEqual(max_integer([-2, -3, -1]), -1)

    def test_floats(self):
        self.assertEqual(max_integer([1.0, 2.0, 3.0]), 3.0)
        self.assertEqual(max_integer([3.0, 1.0, 2.0]), 3.0)
        self.assertEqual(max_integer([2.0, 3.0, 1.0]), 3.0)

    def test_strings(self):
        self.assertRaises(TypeError, max_integer, ["a", "b", "c"])

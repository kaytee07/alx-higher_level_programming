#!/usr/bin/python3
"""unittest for max_integer that accept a list as input"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """fuction that find the max integer from a string"""

    def test_unordered_list(self):
        """test with unordered list of integers"""
        unordered_list = [3, 4, 5, 6]
        self.assertEqual(max_integer(unordered_list), 6)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered_list = [3, 4, 5, 6]
        self.assertEqual(max_integer(ordered_list), 6)

    def test_max_at_begginning(self):
        """Test list that has it max at the beiginning"""
        test_list = [10, 8, 7, 6]
        self.assertEqual(max_integer(test_list), 10)

    def test_ints_and_floats(self):
        """Test a list made up of integers and floats"""
        list_ints_and_floats = [1.53, 2.5, -9, 11, 6]
        self.assertEqual(max_integer(list_ints_and_floats), 11)

    def test_one_element_list(self):
        """Test list that has just one element"""
        one_elem = [12]
        self.assertEqual(max_integer(one_elem), 12)

    def test_string(self):
        """Test when arg is a string"""
        stng = "kaytee"
        self.assertEqual(max_integer(stng), 'y')

    def test_floats(self):
        """Test list made of floats."""
        floats = [2.54, 6.1, -8.124, 1.2, 6.0]
        self.assertEqual(max_integer(floats), 6.1)

    def test_list_of_strings(self):
        """Test list made of strings."""
        strs = ["kaytee", "is", "his", "alias"]
        self.assertEqual(max_integer(strs), "kaytee")

    def test_empty_string(self):
        """Test if the string is empty"""
        self.assertEqual(max_integer(""), None)

    if __name__ == "__main__":
        unittest.main()

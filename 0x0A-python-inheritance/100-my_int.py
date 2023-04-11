#!/usr/bin/python3
"""Defines a class called MyInt that inherits from int"""


class MyInt(int):
    """reverse the int operators != and =="""

    def __eq__(self, value):
        """reassign == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Oreassign != operator with == behavior."""
        return self.real == value

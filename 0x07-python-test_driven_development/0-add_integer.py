#!/usr/bin/python3
"""this is a script that adds to integers passed to it"""


def add_integer(a, b=98):
    """this function accept two arguments and adds them"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)

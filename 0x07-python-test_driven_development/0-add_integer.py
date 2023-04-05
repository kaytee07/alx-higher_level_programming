#!/usr/bin/python3
"""this is a script that adds to integers passed to it"""


def add_integer(a, b=98):
    """
    Adds two integers.

    :param a: An integer or a float.
    :param b: An integer or a float. Defaults to 98.
    :return: The sum of a and b, as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, float):
        a = int(a)
   
    return a + b

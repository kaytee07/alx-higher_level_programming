#!/usr/bin/python
"""this program print all atribute and methods of an object"""


def lookup(obj):
    """
    return all the attribute and methods of a class in a list
    Args:
        obj: this is the class whose methods and attr are returned
    """
    return (dir(obj))

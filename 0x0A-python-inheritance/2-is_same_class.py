#!/usr/bin/python3
"""
return true if object is an instance of class otherwise
False
"""


def is_same_class(obj, a_class):
    """
    takes an object and a class and checks if the object
    is an instance of the class
    """
    return type(obj) == a_class

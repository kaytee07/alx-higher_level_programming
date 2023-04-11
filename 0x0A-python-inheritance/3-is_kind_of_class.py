#!/usr/bin/python3
"""
return true if object is an instance of, or inherited from
the specified class otherwise false
"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is an instance of a_class or obj
    is an instance of a class that inherited from a_class
    """

    if type(obj) == a_class or issubclass(type(obj), a_class):
        return True
    else:
        return False

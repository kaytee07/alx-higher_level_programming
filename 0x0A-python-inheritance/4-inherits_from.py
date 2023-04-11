#!/usr/bin/python3
"""check if object is an instance if a class
that inherited from a specfied class directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance
    of a class that inherited
    directly or indirectly from a
    class and False if otherwise

    :param obj: The object to check
    :param a_class: The class to check against
    :return: True if obj is an instance of a subclass
    of a_class, and False if otherwise

    """

    return a_class in type(obj).__bases__

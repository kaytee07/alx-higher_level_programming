#!/usr/bin/python3
"""print magic string"""


def magic_string():
    """print magic string"""
    if not hasattr(magic_string, 'counter'):
        magic_string.counter = 1
    else:
        magic_string.counter += 1

    result = "BestSchool" * magic_string.counter
    return result

#!/usr/bin/python3
"""project on adding integers"""
def add_integer(a, b=98):
    """accept twi integers and adds them"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

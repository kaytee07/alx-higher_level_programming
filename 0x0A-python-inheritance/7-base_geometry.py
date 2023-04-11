#!/usr/bin/python3
"""Geometry class"""


class BaseGeometry:
    """raises an en exception when the function printed"""
    def area(self):
        """the area of a geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate values"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

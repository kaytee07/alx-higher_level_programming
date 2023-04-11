#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""class rectangle that inherit from Base Geometry"""


class Rectangle(BaseGeometry):
    """private assign width and height"""
    def __init__(self, width, height):
        """constructor for rectangle"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

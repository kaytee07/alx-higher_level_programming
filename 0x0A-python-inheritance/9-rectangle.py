#!/usr/bin/python3
"""class rectangle that inherit from Base Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """private assign width and height"""
    def __init__(self, width, height):
        """constructor for rectangle"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """compute and return the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print the string representation of the rectangle"""
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"

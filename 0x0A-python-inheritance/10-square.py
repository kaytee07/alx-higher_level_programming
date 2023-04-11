#!/usr/bin/python3
"""
a class square that inherit from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square compute the area of a square
    inherit Rectangle which is it parent class
    """
    def __init__(self, size):
        """
        this is the constructor that set the size of the square

        :params size: this is the size of the square
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

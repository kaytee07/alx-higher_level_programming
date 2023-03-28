#!/usr/bin/python3
"""square py with optional variables"""


class Square:
    """class square defines a squae"""
    def __init__(self, size=0):
        """
        assign size to priv variable and raise excption if needed
        Args:
             size: size of the square              
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the area of a square"""
        return self.__size ** 2

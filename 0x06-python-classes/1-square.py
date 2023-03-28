#!/usr/bin/python3
""" class square defines private instance size """


class Square:
    """assign input to private instance variable size"""
    def __init__(self, size):
        """ assigns size to __size"""
        if not isinstance(size, int):
            print("input should be an int")
        elif size < 0:
            print("input should be a number")
        self.__size = size

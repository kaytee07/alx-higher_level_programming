#!/usr/bin/python3
"""task that defines a rectangle"""


class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    """this is a class rectangle"""
    def __init__(self, width=0, height=0):
        """a constructor that set instance attribue height and width"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the class this is a setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of the class instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the triangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the triangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            TypeError("rect_2 must be an instance of Reactangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        string += str(self.print_symbol)
        print(string)
        return '\n'.join([string * self.__width for x in range(self.__height)])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

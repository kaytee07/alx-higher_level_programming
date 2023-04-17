#!/usr/bin/python3
"""
a rectangle class that inherit from the base
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherit it base from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        this is the construvtor that set various cvalues when
        creating an instance of the Rectangle class
        Args:
             width: this is the width of the rectangle
             height: this is the height of the rectangle
             x: this is value x
             y: this is the value of y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """this is a getter method that get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        this is a setter method that set the value of width
        Args:
             value: this is the value to assign to the
             width private variable
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """this is a getter method that get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        this is a setter method that set the value of height
        Args:
             value: this is the value to assign to the
             height private variable
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """this is a getter method that get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        this is a setter method that set the value of x
        Args:
             value: this is the value to assign to the
             x private variable
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """this is a getter method that get the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        this is a setter method that set the value of y
        Args:
             value: this is the value to assign to the
             y private variable
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """this methods print the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """
        this method print height and width of the rectangle
        with #
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update attribute using kwargs and args"""
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """return dictionary representation of rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """print the user friendly decription of the class"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

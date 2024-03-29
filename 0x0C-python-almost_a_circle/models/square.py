#!/usr/bin/python3
"""this is a class square that inherit from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square inherit from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return the value assigned to size"""
        return self.width

    @size.setter
    def size(self, value):
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
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attribute"""
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        def to_dictionary(self):
            """
            Returns the dictionary representation of the rectangle
            """
            return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }

    def __str__(self):
        """print a human representaion of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

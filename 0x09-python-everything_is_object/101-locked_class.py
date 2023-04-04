#!/usr/bin/python3
"""locked class"""


class LockedClass:
    def __init__(self):
        self.__locked = False

    def __setattr__(self, attr, value):
        if self.__locked and attr != "first_name":
            raise AttributeError("New instance attributes cannot be created")
        else:
            self.__dict__[attr] = value

    def __getattr__(self, attr):
        if attr not in self.__dict__:
            raise AttributeError(f"'{self.__class__.__name__}' ")
        return self.__dict__[attr]

    def lock(self):
        self.__locked = True

    def unlock(self):
        self.__locked = False

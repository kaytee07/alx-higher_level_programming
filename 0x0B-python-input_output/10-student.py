#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance with a first name,
        last name, and age

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the
        Student instance

        Args:
            attrs (list): A list of strings representing the
        attribute names
            to include in the dictionary representation. If
        the list is empty or
            not provided, all attributes are included.

        Returns:
            dict: A dictionary representation of the Student
        instance.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

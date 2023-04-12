#!/usr/bin/python3
"""
This module defines a function for reading and printing the cont
"""


def read_file(filename: str = "") -> None:
    """
    Opens the specified UTF8-encoded text file and prints its
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

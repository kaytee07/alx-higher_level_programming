#!/usr/bin/python3
"""
This module defines a function for reading and printing the cont
"""


def print_file_contents(filename: str = "") -> None:
    """
    Opens the specified UTF8-encoded text file and prints its
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

#!/usr/bin/python3
"""
This module defines a function for appending a string to a
UTF8-encoded text file
"""


def append_to_file(filename: str = "", text: str = "") -> int:
    """
    Opens the specified UTF8-encoded text file and
    appends the given text to the end of the file.

    Returns the number of characters written to the file.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)

#!/usr/bin/python3
"""
This module defines a function for writing a
string to a UTF8-encoded text file
"""


def write_to_file(filename: str = "", text: str = "") -> int:
    """
    Opens the specified UTF8-encoded text file and writes the
    given text to it.

    Returns the number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)

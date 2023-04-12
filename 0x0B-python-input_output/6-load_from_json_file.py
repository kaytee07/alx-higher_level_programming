#!/usr/bin/python3
"""
This module defines a function for creating a
Python object from a JSON file
"""

import json


def load_from_json_file(filename: str) -> object:
    """Reads a JSON file and creates a Python object.

    Args:
        filename: The name of the file to load the JSON data from.

    Returns:
        A Python object representing the JSON data.
    """
    with open(filename, mode="r") as file:
        return json.load(file)

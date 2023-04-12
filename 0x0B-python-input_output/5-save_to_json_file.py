#!/usr/bin/python3
"""
This module defines a function for saving a Python object
 to a JSON file"""

import json


def save_to_json_file(my_obj: object, filename: str) -> None:
    """Converts the specified Python object to a JSON 
    string and writes it to a file.

    Args:
        my_obj: The Python object to be saved.
        filename: The name of the file to save the JSON data to.
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)

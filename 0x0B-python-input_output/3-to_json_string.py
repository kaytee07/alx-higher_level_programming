#!/usr/bin/python3
"""
This module defines a function for converting a Python
object to a JSON string
"""
import json


def to_json_string(my_obj) -> str:
    """
    Converts the specified Python object to a JSON string.

    Returns the resulting JSON string.
    """
    return json.dumps(my_obj)

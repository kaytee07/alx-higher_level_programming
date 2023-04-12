#!/usr/bin/python3
"""
This module defines a function for serializing Python
objects to JSON
"""


def class_to_json(obj):
    """
    Serialize a Python object to a JSON-formatted string.

    Args:
        obj: A simple data structure consisting of primitive
    data types
             (e.g., str, int, float, list, dict).

    Returns:
        A JSON-formatted string representing the serialized object.
    """
    return obj.__dict__

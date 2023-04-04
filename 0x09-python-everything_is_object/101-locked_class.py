#!/usr/bin/python3
"""locked class"""


class LockedClass:
    """prevent user from istantiationg locked class"""
    __slots__ = ["first_name"]

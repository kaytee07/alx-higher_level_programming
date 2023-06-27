#!/usr/bin/python3
"""Finds the peak in the unsorted integers list"""


def find_peak(list_of_integers):
    """Finds the peak in list_of_integers"""

    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None

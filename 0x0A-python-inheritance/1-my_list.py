#!/usr/bin/python3
"""a class with a function that print sorted list"""


class MyList(list):
    """inherit list and has a methof that print out sorted list"""
    def print_sorted(self):
        print(sorted(self))

#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("This is a type error.")
    except TypeError as e:
        raise e        

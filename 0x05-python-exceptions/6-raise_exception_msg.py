#!/usr/bin/python3
def raise_exception_msg(message=""):
    if not message:
        message = "This is a name error."
    raise NameError(message)

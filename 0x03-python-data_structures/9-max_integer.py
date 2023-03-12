#!/bin/usr/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    largest_number = my_list[0]
    for i in my_list[1:]:
        if i > largest_number:
            largest_number = i
    return largest_number

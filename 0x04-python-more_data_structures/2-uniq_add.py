#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    new_list = set(my_list)
    for x in new_list:
        total += x
    return total

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx > -1 and idx < len(my_list):
        for i in my_list:
            new_list.append(i)
        new_list[idx] = element
        return new_list
    else:
        return my_list

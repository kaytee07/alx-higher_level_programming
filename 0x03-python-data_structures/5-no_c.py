#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    for i in my_string:
        if (i == 'c' or i == 'C'):
            continue
        else:
            new_list.append(i)
    return "".join(str(x) for x in new_list)

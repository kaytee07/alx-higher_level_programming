def replace_in_list(my_list, idx, element):
    if (idx > -1 and idx < len(my_list)):
        my_list[idx] = element
        return my_list
    else:
        return my_list

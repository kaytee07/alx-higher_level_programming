#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = 0
    weight_sum = 0
    for score, weight in my_list:
        total += score * weight
        weight_sum += weight
    return total / weight_sum

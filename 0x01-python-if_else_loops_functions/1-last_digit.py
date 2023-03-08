#!/usr/bin/python3
import random


def lastdigit(num):
    last_digit_unsigned = abs(num) % 10
    if (num < 0):
        return -last_digit_unsigned
    else:
        return last_digit_unsigned


number = random.randint(-10000, 10000)
lastdig = lastdigit(number)
const = "Last digit of {} is {} and is".format(number, lastdig)
if lastdig == 0:
    print("{} 0".format(const))
elif lastdig > 5:
    print("{} greater than 5".format(const))
elif lastdig < 6 and number != 0:
    print("{} less than 6 and not 0".format(const))

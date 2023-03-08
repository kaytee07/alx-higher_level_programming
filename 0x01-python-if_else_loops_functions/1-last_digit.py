#!/usr/bin/python3
import random

def lastdigit(num):
    last_digit_unsigned = abs(num)%10
    if (num < 0):
        return -last_digit_unsigned
    else:
        return last_digit_unsigned

number = random.randint(-10000, 10000)
if lastdigit(number) == 0:
    print("Last digit of {} is {} and is 0".format(number,lastdigit(number)))
elif lastdigit(number) > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,lastdigit(number)))
elif lastdigit(number) < 6 and number != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,lastdigit(number)))


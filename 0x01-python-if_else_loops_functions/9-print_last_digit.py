#!/usr/bin/python3
def print_last_digit(number):
    last_unsigned_digit = abs(number) % 10
    print(last_unsigned_digit, end="")
    return last_unsigned_digit

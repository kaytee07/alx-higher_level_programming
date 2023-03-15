#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return None
    roman_list = []
    total = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for char in roman_string:
        if char in roman:
            roman_list.append(roman.get(char))
    for i in range(len(roman_list)):
        current_value = roman_list[i]
        next_value = roman_list[i+1] if i+1 < len(roman_list) else 0
        if current_value < next_value:
            total -= current_value
        else:
            total += current_value
    return total

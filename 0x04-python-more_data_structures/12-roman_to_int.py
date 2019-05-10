#!/usr/bin/python3
def roman_to_int(roman_string):
    count = 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for iter1 in roman_string:
        for k, v in dict.items():
            if iter1 == k:
                count += v
    return (count)

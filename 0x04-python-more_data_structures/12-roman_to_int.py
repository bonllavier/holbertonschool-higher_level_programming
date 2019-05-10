#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) != str) or roman_string is None:
        return 0
    count = 0
    tmp = 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for iter1 in roman_string:
        if tmp >= int(dict.get(iter1)) and tmp != 0:
            count += int(dict.get(iter1))
        elif tmp < int(dict.get(iter1)) and tmp != 0:
            count = count + ((int(dict.get(iter1)) - tmp) - tmp)
        elif tmp == 0:
            count += int(dict.get(iter1))
        tmp = int(dict.get(iter1))
    return (count)

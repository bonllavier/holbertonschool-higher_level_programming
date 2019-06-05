#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    print number lines
    """
    line_number = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_number += 1
    return line_number

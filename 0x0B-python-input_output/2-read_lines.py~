#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    read_lines
    """
    line_number = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_number += 1
            if line_number <= nb_lines and nb_lines > 0:
                print(line, end="")
            elif nb_lines <= 0:
                print(line, end="")
            else:
                break

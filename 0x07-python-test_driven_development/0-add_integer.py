#!/usr/bin/python3

"""
function 0-add_integer
adds two integers
module "0-add_integer"
"""


def add_integer(a, b=98):
    """adds two numbers
    >>> add_integer(4, 3)
    7
    >>> add_integer(5, 5)
    10
    """
    fnum = 0
    if type(a) is int or type(a) is float:
        fnum += int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        fnum += int(b)
    else:
        raise TypeError("b must be an integer")
    return fnum

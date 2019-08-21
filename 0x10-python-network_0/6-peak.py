#!/usr/bin/python3
"""
module
"""


def find_peak(list_of_integers):
    """method
    """
    tmp_num = 0
    if len(list_of_integers) > 0:
        for iter in list_of_integers:
            if iter > tmp_num:
                tmp_num = iter
        return(tmp_num)
    else:
        pass

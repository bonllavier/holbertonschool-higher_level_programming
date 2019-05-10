#!/usr/bin/python3
def common_elements(set_1, set_2):
    for iter1 in set_1:
        for iter2 in set_2:
            if iter1 == iter2:
                return iter1

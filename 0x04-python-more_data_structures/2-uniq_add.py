#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for iter1 in set(my_list):
        sum += iter1
    return sum

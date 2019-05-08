#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    tam = len(my_list)
    if tam > 0:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))

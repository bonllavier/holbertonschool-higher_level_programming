#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    new_dict.update(a_dictionary)
    for k, v in new_dict.items():
        d1 = {k: (v * 2)}
        new_dict.update(d1)
    return new_dict

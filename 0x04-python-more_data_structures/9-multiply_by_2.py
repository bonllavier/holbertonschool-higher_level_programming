#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    new_dict.update(a_dictionary)
    print(new_dict)
    for k, v in a_dictionary.items():
        d1 = {k: v * 2}
        new_dict.update(d1)
    return new_dict

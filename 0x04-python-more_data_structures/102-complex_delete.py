#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dic_tmp = []
    for k, v in a_dictionary.items():
        if v == value:
            dic_tmp.append(k)
    for x in dic_tmp:
        del a_dictionary[x]
    return a_dictionary

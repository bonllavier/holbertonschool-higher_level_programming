#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and a_dictionary:
        x = sorted(a_dictionary, key=(lambda key: a_dictionary[key]),
                   reverse=1)
        return (x[0])
    else:
        return None

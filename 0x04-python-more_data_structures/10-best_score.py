#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    x = sorted(a_dictionary, key=(lambda key: a_dictionary[key]), reverse=True)
    return(x[0])

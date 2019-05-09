#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for iter1 in range(len(my_list)):
        if my_list[iter1] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[iter1])
    return new_list

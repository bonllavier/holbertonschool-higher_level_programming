#!/usr/bin/python3
def element_at(my_list, idx):
    tam = len(my_list)
    if idx < 0 or idx >= tam or idx == 0:
        return None
    else:
        return my_list[idx]

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    for iter1 in range(0, x):
        try:
            print(my_list[iter1], end='')
            cont += 1
        except (IndexError):
            pass
    print("")
    return cont

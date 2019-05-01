#!/usr/bin/python3
def remove_char_at(str, n):
    strtmp = ""
    cont = 0
    for c in str:
        if cont == n:
            pass
        else:
            strtmp += c
        cont += 1
    return strtmp

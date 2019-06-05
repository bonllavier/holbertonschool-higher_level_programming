#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    append
    """
    chara = len(text)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
    return chara

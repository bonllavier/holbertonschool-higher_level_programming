#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    write to file
    """
    chara = len(text)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return chara

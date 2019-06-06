#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """
    append after
    """
    with open(filename, 'r+', encoding='utf-8') as f:
        listtmp = []
        for line in f:
            listtmp.append(line)
            if search_string in line:
                listtmp.append(new_string)
        f.seek(0)
        for line in listtmp:
            f.write(line)

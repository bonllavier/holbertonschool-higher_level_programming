#!/usr/bin/python3
charend = ", "
for i in range(0, 100):
    if i < 10:
        print("{}{}".format(0, i), end=charend)
    else:
        if i == 99:
            charend = ""
        print(i, end=charend)

#!/usr/bin/python3
strtmp = ""
for i in reversed(range(97, 123)):
    if (i % 2) == 0:
        strtmp += chr(i)
    else:
        strtmp += chr(i-32)
print("{}".format(strtmp), end="")

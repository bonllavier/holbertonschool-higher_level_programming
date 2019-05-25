#!/usr/bin/python3
"""
module "5-text_indentation"
"""


def text_indentation(text):
    """
    print text with new line in a predefined arguments
    >>> text_indentation(text)
    text
    """
    strf = text
    ver = 0
    ver2 = 0
    cont2 = 0
    str2 = text
    if type(text) is str:
        str2 = str2[::-1]
        if text[len(text) - 1] is ' ':
            for iter in str2:
                if iter is ' ' and ver2 is 0:
                    cont2 += 1
                if iter != " ":
                    ver2 = 1
            strf = str2[cont2:len(str2)]
            strf = strf[::-1]
        for iter in strf:
            if iter is ' ' and ver is 0:
                pass
            else:
                print(iter, end="")
                ver = 1
            if iter is '.' or iter is '?' or iter is ':':
                print("\n")
                ver = 0
    else:
        raise TypeError("text must be a string")

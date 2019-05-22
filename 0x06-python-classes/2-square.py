#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            size += 0
        except TypeError:
            raise TypeError("size must be an integer")
        try:
            if (int(size) < 0):
                raise ValueError
        except ValueError:
            raise ValueError("size must be >= 0")
        self.__size = size

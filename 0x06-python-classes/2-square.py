#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            size += 1
        except TypeError:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        size -=1
        self.__size = size

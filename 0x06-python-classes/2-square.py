#!/usr/bin/python3
class Square():
    """class square.
    Attributes:
        __size: size of square.
    """
    def __init__(self, size=0):
        """Initialization, only allowed type int > 0."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (int(size) < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

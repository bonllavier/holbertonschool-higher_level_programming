#!/usr/bin/python3
class Square():
    """class square.
    Attributes:
        __size: size of square.
    """
    def __init__(self, size=0):
        """Initialization, only allowed type int > 0."""
        try:
            size + 2
        except TypeError:
            raise TypeError("size must be an integer")
        try:
            if (int(size) < 0):
                raise ValueError
            self.__size = size
        except ValueError:
            raise ValueError("size must be >= 0")

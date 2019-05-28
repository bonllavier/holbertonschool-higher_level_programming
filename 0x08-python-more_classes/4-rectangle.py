#!/usr/bin/python3
"""
module "4-rectangle"
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        init method
        no example
        """
        if type(width) == int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        if type(height) == int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
        width getter
        """
        return self.width

    @property
    def height(self):
        """
        height getter
        """
        return self.height

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
        get area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        get perimeter
        """
        if (self.__height) == 0 or (self.__width) == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """
        print rectangle
        """
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        else:
            for iter1 in range(self.__height):
                for iter2 in range(self.__width):
                    str += "#"
                if iter1 != (self.__height - 1):
                    str += "\n"
        return str

    def __repr__(self):
        str1 = "Rectangle("
        return str1 + str(self.__width) + ", " + str(self.__height) + ')'

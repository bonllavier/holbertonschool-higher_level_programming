#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """
    class rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        cosntructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        get width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set width
        """
        if (type(value) == int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        get height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set height
        """
        if (type(value) == int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """
        get x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        set x
        """
        if (type(value) == int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """
        get y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        set y
        """
        if (type(value) == int):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """
        get area
        """
        return self.__width * self.__height

    def display(self):
        """
        display
        """
        strtmp = ""
        if self.__width == 0 or self.__height == 0:
            return strtmp
        else:
            strtmp += "\n" * self.__y
            for iter1 in range(self.__height):
                for iter3 in range(0, self.__x):
                    strtmp += " "
                for iter2 in range(self.__width):
                    strtmp += "#"
                if iter1 != (self.__height - 1):
                    strtmp += "\n"
        print(strtmp)

    def __str__(self):
        """
        str
        """
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id, self.__x, self.__y,
                                                 self.__width, self.__height))

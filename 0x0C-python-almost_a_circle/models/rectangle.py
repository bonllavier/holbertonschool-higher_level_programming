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
        self.__width = value

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
        self.__height = value

    @property
    def x(self):
        """
        get x
        """
        return self.__x

    @height.setter
    def x(self, value):
        """
        set x
        """
        self.__x = value

    @property
    def y(self):
        """
        get y
        """
        return self.__y

    @height.setter
    def y(self, value):
        """
        set y
        """
        self.__y = value

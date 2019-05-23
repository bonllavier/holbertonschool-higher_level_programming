#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if len(position) == 2:
            if type(position[0]) != int\
               or type(position[1]) != int or type(position) != tuple:
                raise TypeError("position must be a tuple of \
2 positive integers")
            if type(position[0]) is int and type(position[1]) is int:
                if int(position[0]) < 0 or int(position[1]) < 0:
                    raise TypeError("position must be a tuple of \
2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if len(value) == 2:
            if value[0] < 0 or value[1] < 0 or type(value[0]) != int or\
               type(value[1]) != int or type(value) != tuple:
                raise TypeError("position must be a tuple of \
2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        str_tmp = ""
        if self.__size == 0:
            str_tmp += ""
        else:
            str_tmp += "\n" * self.__position[1]
            for iter in range(0, self.__size):
                for iter3 in range(0, self.__position[0]):
                    str_tmp += " "
                for iter2 in range(0, self.__size):
                    str_tmp += "#"
                if iter != self.__size - 1:
                    str_tmp += "\n"
        return str_tmp

    def __str__(self):
        return self.my_print()

#!/usr/bin/python3
class BaseGeometry:
    """
    base class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) == int:
            if value > 0:
                pass
            else:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))


class Rectangle(BaseGeometry):
    """
    reactangle
    """
    def __init__(self, width, height):
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

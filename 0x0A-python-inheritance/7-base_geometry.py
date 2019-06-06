#!/usr/bin/python3
class BaseGeometry:
    """
    base geom
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

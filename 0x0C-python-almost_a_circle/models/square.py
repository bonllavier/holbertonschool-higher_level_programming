#!/usr/bin/python3
"""
module square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    module square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor methos
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """
        getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        str
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x, self.y,
                                              self.width))

    def update(self, *args, **kwargs):
        """
        update method
        """
        if args:
            tmp_list = ["id", "size", "x", "y"]
            for v in range(len(args)):
                setattr(self, tmp_list[v], args[v])
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

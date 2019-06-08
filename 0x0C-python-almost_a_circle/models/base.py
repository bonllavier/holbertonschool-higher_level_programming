#!/usr/bin/python3
class Base:
    """
    module base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor method
        """
        if(id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

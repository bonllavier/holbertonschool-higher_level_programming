#!/usr/bin/python3
"""
module base
"""
import json
import os.path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        json to string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save
        """
        tmp_list = []
        if list_objs is not None:
            for item in list_objs:
                tmp_list.append(item.to_dictionary())

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            file.write(cls.to_json_string(tmp_list))

    @staticmethod
    def from_json_string(json_string):
        """
        from json to string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        """
        if cls.__name__ == "Rectangle":
            txt = cls(1, 1)
        elif cls.__name__ == "Square":
            txt = cls(1)
        cls.update(txt, **dictionary)
        return txt

    @classmethod
    def load_from_file(cls):
        """
        class to create a rectangle object
        """
        new_list = []
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, "r") as read_file:
                new_list = cls.from_json_string(read_file.read())
            for i, j in enumerate(new_list):
                new_list[i] = cls.create(**new_list[i])
        else:
            pass
        return new_list

#!/usr/bin/python3


class MyInt(int):
    """
    miint
    """
    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)

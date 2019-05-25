#!/usr/bin/python3
"""
module "3-say_my_name"
"""


def say_my_name(first_name, last_name=""):
    """
    validate and print names
    say_my_name("juan", "bonilla")
    My name is juan bonilla
    """
    if type(first_name) is str:
        if type(last_name) is str:
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")

#!/usr/bin/python3
""" Base Module """


class Base:
    """
    Base Model
    Args:
        __nb_objects (int): The bumber of instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

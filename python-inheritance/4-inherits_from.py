#!/usr/bin/python3
""" inherits_from module """


def inherits_from(obj, a_class):
    """ check if object is an instance of a class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

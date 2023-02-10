#!/usr/bin/python3
""" is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """ Check if a obj and inherited class-checking function """
    if isinstance(obj, a_class):
        return True
    return False

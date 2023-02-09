#!/usr/bin/python3
""" Module is_same_class """


def is_same_class(obj, a_class):
    """ 
    return true/false if 
    the object is exactly an instance
    """
    if type(obj) == a_class:
        return True
    return False

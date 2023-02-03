#!/usr/bin/python3
"""
Module print name
"""


def say_my_name(first_name, last_name=""):
    """
    print name and last name
    Args:
        first_name (str): first name
        last_name (str): last name
    Raise:
        TypeError: if first or last name is not string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
"""
Add integer or float
>>> add_integer(1, 4)
5
"""


def  add_integer(a, b=98):
    """
    Add two integer "a" and "b"
    Args:
        a (int or float): first value
        b (int or float): second value
    Return:
        Sum "a" and "b"
    """
    if type(a) not in[int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

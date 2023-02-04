#!/usr/bin/python3
"""
Print Square Module
"""


def print_square(size):
    """
    Print square
    Args:
        Size (int): size of square
    Raise:
        TypeError: size is not int
        TypeError: size less than 0
        TypeError: size is float and less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        print("#" * size)

#!/usr/bin/python3
""" Module Square """


class Square:
    """ Square Class
    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0):
        """
        Initialize Methode

        Args:
            size (int): Size of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

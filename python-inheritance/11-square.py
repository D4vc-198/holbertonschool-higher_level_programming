#!/usr/bin/python3
""" Square module #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ represent Square """

    def __init__(self, size):
        """
        Initialize a new Square

        Args:
            Size (int): size of a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

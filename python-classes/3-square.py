#!/usr/bin/python3
""" Module Square """


class Square:
    """ Square Class
    Attributes:
        Size (int): Size of Square
    """
    def __init__(self, size=0):
        """
        Initialize the square
            Args:
                size (int): size of square
            Raises:
            TypeError: if size is not int
            ValueError: size less than 0
        """
        if type(size) != int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method calculate area
        Return:
            Square area
        """
        return self.__size * self.__size

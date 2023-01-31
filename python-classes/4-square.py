#!/usr/bin/python3
""" Module Square """


class Square:
    """ Square Class
    Attributes:
        size (int): size of square
    """

    def __init__(self, size=0):
        """
        Method initialize
        Args:
            size (int): size of square
        """

        self.__size = size

    @property
    def size(self):
        """
        Getter of size
        Return:
            size of square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size
        Args:
            Size (int): size of square
        Raises:
            TypeError: size is not int
            ValueError: size less than 0
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Method to calculate area
        Return:
            Area square
        """

        return self.__size * self.__size

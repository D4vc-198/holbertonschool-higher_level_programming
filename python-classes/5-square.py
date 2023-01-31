#!/usr/bin/python3
""" Module Square """


class Square:
    """
    Square Class
    Args:
        size (int): size of square
    """
    def __init__(self, size=0):
        """
        Initialize methode
        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter of size
        Args:
            size (int): size of square
        Return:
            size (int): return size of squre
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size
        Args:
            size (int): size of square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate Area of square
        Args:
            size (int): size of square
        Returns:
            Area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print "#"
        Args:
            size (int): size of square
        """
        if self.__size == 0:
            print()
        else:
            for n in range(self.__size):
                print("#" * self.__size)

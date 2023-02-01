#!/usr/bin/python3
""" Module Square """


class Square:
    """ Class Square
    Args:
        size (int): size of square
        position (tuple): postion of square in 2D space
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize Methode
        Args:
            size (int): size of square
            position (tuple): postion of square in 2D space
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter of position
        Returns:
            position: postion of square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter of position
        Args:
            position: postion of square in 2D space
        """
        if value[0] < 0 or type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0 or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Area methode
        Args:
            size (int): size of square
        Return:
            Area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print methode
        Args:
            Size (int): size of square
            position (tuple): postion of square in 2D space
        """
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for x in range(0, self.__size):
                print(" "*self.__position[0], end='')
                print("#"*self.__size)

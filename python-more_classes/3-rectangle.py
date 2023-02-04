#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Rectangle representation
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    """

    def __init__(self, width=0, height=0):
        """
        initialize a new Rectangle
        Args:
            witdh (int): width of a rectangle
            height (int): height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be a integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be a integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        data = []
        for n in range(0, self.__height):
            [data.append("#")for j in range(self.__width)]
            if n != self.__height - 1:
                data.append("\n")
        return ("".join(data))

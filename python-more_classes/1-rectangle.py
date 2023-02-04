#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Represent rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle
        Args:
            width (int): width of rectangle
            height (int): heinght of rectangle
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__witdh = value

    @property
    def height(self):
        """Get height with rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


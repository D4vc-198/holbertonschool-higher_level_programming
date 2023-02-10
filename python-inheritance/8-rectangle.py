#!/usr/bin/python3
""" Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ represent Rectangle """
    def __init__(self, width, height):
        """
        Initialize a new Rectangle

        Args:
            width (int): width of a rectangle
            height (int): heigth of a rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Represent Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new Square """
        super().__init__(size, size, x, y, id)

    """ Size """
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

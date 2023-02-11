#!/usr/bin/python3
""" Studen Module """


class Student:

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new student
        Args:
            first_name (str): first name student
            last_name (str): last name student
            age (int): age student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

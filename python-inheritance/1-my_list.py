#!/usr/bin/python3
""" MyList module """


class MyList(list):
    """ MyList class """
    def print_sorted(self):
        sorted_list = self[:]
        """ print sorted list"""
        print(sorted_list.sort())

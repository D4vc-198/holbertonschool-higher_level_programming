#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list != None:
        my_list.reverse()
        for n in range(0, len(my_list)):
            print("{:d}".format(my_list[n]))

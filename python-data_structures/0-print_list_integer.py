#!/usr/bin/python3
def print_list_integer(my_list=[]):
    sizeList = len(my_list)
    for n in range(0, sizeList):
        print("{}".format(my_list[n]))

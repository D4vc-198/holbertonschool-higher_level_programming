#!/usr/bin/python3
def max_integer(my_list=[]):
    maxInt = 0
    i = 0
    size = len(my_list)
    while i < size:
        if my_list[i] > maxInt:
            maxInt = my_list[i]
        i += 1

    return maxInt

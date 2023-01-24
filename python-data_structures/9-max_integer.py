#!/usr/bin/python3
def max_integer(my_list=[]):
    maxInt = my_list[0]
    i = 0
    if my_list == []:
        return None
    while i < len(my_list):
        if my_list[i] > maxInt:
            maxInt = my_list[i]
        i += 1
    return (maxInt)

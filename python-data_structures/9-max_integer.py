#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    i = 0
    maxInt = my_list[0]
    while i < len(my_list) - 1:
        if my_list[i] > maxInt:
            maxInt = my_list[i]
        i += 1
    return (maxInt)

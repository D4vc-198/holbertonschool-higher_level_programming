#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    num = list(set(my_list))
    for n in num:
        x += n
    return x

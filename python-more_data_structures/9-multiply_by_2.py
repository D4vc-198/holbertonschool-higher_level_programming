#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()
    for n in new_d.keys():
        new_d[n] = new_d[n] * 2
    return new_d

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copyOfList = my_list[:]
    copyOfList[idx] = element

    if idx > 0 or idx < len(my_list) - 1:
        return copyOfList
    else:
        return copyOfList

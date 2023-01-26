#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for i, n in zip(set_1, set_2):
        if n == i:
            common.append(n)
    return common

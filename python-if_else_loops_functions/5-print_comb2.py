#!/usr/bin/python3
for n in range(0, 100):
    if n <= 9:
        print("0{}".format(n), end=', ')
    else:
        if n <= 98:
            print("{}".format(n), end = ', ')
        else:
            print("{}".format(n), end='')


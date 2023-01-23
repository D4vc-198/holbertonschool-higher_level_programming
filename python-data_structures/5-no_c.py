#!/usr/bin/python3
def no_c(my_string):
    string = list(my_string)
    for n in range(0, len(string)):
        if string[n] == 'C' or string[n] == 'c':
            string[n] = ''
    my_string = "".join(string)
    return my_string

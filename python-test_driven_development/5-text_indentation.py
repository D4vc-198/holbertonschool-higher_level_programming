#!/usr/bin/python3
"""
    Text Indention module
    """


def text_indentation(text):
    """
    print text
    2 new lines after each of these characters: ., ? and :
    Args:
        text (str): text
    Raise
        TypeError: when text is not str
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

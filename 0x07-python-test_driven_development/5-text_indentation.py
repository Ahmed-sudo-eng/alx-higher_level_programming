#!/usr/bin/python3
"""
This module contain a function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """This function prints a text with 2 new lines after
    each of characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    p = 0
    q = 0
    while p < len(text):
        if text[p] == '.' or text[p] == '?' or text[p] == ':':
            print(text[q:p+1].strip())
            print()
            q = p + 1
        p += 1

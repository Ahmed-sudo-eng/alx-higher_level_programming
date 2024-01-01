#!/usr/bin/python3
"""
This module contains the function "write_file" which writes a string to
a text file and return the number of characters written
"""


def write_file(filename="", text=""):
    """ This function writes a text to file and return the n of c's written """
    with open(filename, mode='w', encoding='utf-8') as f_obj:
        wc = f_obj.write(text)
    return wc

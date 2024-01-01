#!/usr/bin/python3
"""
This module contains the function "read_file" that reads atext file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """ This function reads a file and prints it to stdout """
    with open(filename, mode='r', encoding='utf-8') as f_obj:
        content = f_obj.read()
        print(content, end='')

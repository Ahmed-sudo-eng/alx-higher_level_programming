#!/usr/bin/python3
"""
This module contains the function "append_write" which append a string at the
end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Append a string at the end of a text file and returns num of add ch """
    with open(filename, mode='a', encoding='utf-8') as f_obj:
        ac = f_obj.write(text)
    return ac

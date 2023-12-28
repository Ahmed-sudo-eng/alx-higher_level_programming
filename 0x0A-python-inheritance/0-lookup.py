#!/usr/bin/python3
"""
This module contains a function "lookup" that is used to list the attributes
and methods of an object
"""


def lookup(obj):
    """ This function returns a list of available attributes and methods """
    return dir(obj)

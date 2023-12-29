#!/usr/bin/python3
"""
Thid module contains "add_attribute" function that adds a new attribute to an
object if it's possible
"""


def add_attribute(obj, attribute, value):
    """ This function adds a new attribute to an object if possible """
    setattr(obj, attribute, value)

#!/usr/bin/python3
"""
This module contains the "save_to_json_file" function which writes an Object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file using a JSON representation """
    with open(filename, mode='w', encoding='utf-8') as f_obj:
        json.dump(my_obj, f_obj)

#!/usr/bin/python3
"""
This module contains a function "load_from_json_file" which creates an object
from a "JSON" file
"""
import json


def load_from_json_file(filename):
    """ Creates an Object from a JSON file """
    with open(filename, mode='a', encoding='utf-8') as f_obj:
        obj = json.load(f_obj)
        return obj

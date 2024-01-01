#!/usr/bin/python3
"""
This module contains the "to_json_string" function which returns the JSON
representation of an object
"""
import json


def to_json_string(my_obj):
    """ Returns the JSON representaion of an object """
    return json.dumps(my_obj)

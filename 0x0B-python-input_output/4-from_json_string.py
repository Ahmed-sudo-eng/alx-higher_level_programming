#!/usr/bin/python3
"""
This module contains the "from_json_string" which returns an object
(Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON string """
    return json.loads(my_str)

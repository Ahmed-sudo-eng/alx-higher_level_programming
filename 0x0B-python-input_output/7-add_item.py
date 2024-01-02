#!/usr/bin/python3
"""
This module contains a function "load_from_json_file" which creates an object
from a "JSON" file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
old_list = load_from_json_file('add_item.json')
"""
for item in old_list:
    my_list.append(item)
for arg in sys.argv:
    if (arg == sys.argv[0]):
        pass
    else:
        my_list.append(arg)

save_to_json_file(my_list, 'add_item.json')
"""

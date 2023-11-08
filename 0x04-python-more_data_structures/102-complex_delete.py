#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for k, v in a_dictionary.items():
        if value == v:
            keys.append(k)
    i = 0
    while i < len(keys):
        del a_dictionary[keys.pop()]
    return a_dictionary

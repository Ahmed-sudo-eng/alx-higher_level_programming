#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    cycles = new_list.count(search)
    i = 0
    while i < cycles:
        idx = new_list.index(search)
        del new_list[idx]
        new_list.insert(idx, replace)
        i += 1
    return new_list

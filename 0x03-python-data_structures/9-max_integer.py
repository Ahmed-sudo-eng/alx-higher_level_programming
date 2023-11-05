#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = 0
    while i < (len(my_list) - 1):
        if my_list[i] > my_list[i+1]:
            tmp = my_list[i+1]
            my_list[i+1] = my_list[i]
            my_list[i] = tmp
        i += 1
    max_value = my_list[len(my_list) - 1]
    return max_value

#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    dominator = sum(list(map(lambda t: t[0] * t[1], my_list)))
    nominator = 0
    for t in my_list:
        nominator += t[1]
    return dominator / nominator

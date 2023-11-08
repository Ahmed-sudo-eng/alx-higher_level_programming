#!/usr/bin/python3
def uniq_add(my_list=[]):
    tmp_list = []
    result = 0
    for i in my_list:
        if i in tmp_list:
            pass
        else:
            result += i
        tmp_list.append(i)
    return result

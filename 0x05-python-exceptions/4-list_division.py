#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    q_list = []
    i = 0
    while i < list_length:
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
            quotient = 0
        except TypeError:
            print('wrong type')
            quotient = 0
        except IndexError:
            print('out of range')
            quotient = 0
        finally:
            q_list.append(quotient)
        i += 1
    return q_list

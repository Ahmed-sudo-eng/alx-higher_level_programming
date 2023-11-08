#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    b_score = 0
    for score in a_dictionary.values():
        if score > b_score:
            b_score = score
    for key, value in a_dictionary.items():
        if value == b_score:
            return key

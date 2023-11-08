#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    best = a_dictionary[ret]
    for key, value in a_dictionary.items():
        if value > best:
            big = value
            ret = key
    return ret

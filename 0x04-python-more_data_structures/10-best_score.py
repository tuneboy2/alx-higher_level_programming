#!/usr/bin/python3
def best_score(a_dictionary):
    '''turns a key with the biggest integer value'''
    if a_dictionary:
        best = 0
        for key, value in a_dictionary.items():
            if value > best:
                name = key
                best = value
        return name

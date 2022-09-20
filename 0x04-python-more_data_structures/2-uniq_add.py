#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''Add  all unique integers in a list (only once for each integer)'''
    uniq = set(my_list)
    total = 0
    for no in uniq:
        total += no
    return total

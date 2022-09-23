#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''Replaces all occurrences of an element by another in a new list'''
    new = list(map(lambda x: replace if search == x else x, my_list))
    return new

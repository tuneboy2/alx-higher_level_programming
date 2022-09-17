#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    '''Replace an element of a list at a specific position

        if idx is negative:
            return unmodified list

        if idx is out of range (> of number of element in my_list):
            return unmodified lsit
    '''
    if idx < 0 or idx >= len(my_list):
        return my_list

    for i in range(len(my_list)):
        if i == idx:
            my_list[i] = element
            return my_list

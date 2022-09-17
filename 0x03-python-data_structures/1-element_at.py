#!/usr/bin/python3

def element_at(my_list, idx):
    '''Retrieve an Element from a List

        If idx is negative:
            return none

        idx is out of range (> of number of element in my_list):
            return none
    '''
    if idx < 0 or idx >= len(my_list):
        return

    for i in range(len(my_list)):
        if i == idx:
            return my_list[i]

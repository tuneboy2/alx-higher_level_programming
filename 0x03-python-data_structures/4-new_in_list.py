#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''Replaces an element in a list at a specific position without modifying
       the original list.


        if idx is negative:
            return a copy of the original list

        If idx is out of range (> of number of element in my_list):
            return a copy of the original list
    '''

    list_cpy = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return list_cpy

    for i in range(len(my_list)):
        if i == idx:
            list_cpy[i] = element
            return list_cpy

#!/usr/bin/python3

def max_integer(my_list=[]):
    '''Finds the biggest integer of a list.

        If the list is empty:
            return None
    '''

    if my_list:
        maxima = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > maxima:
                maxima = my_list[i]
    else:
        return None

    return maxima

#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''Finds all multiples of 2 in a list.

        Return a new list with True or False, depending on whether the integer
        at the same position in the original list is a multiple of 2
    '''
    new = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new.append(True)
        else:
            new.append(False)

    return new

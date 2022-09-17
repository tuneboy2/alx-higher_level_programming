#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    '''Prints all integers of a list in reverse mode one integer per line'''

    if my_list is None:
        return

    j = len(my_list)
    list_cpy = my_list[:]

    for i in range(j):
        my_list[i] = list_cpy[j - 1]
        j -= 1
        print("{:d}".format(my_list[i]))

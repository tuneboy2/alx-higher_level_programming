#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''
    A function that prints the first x elements of a list and only integers'''
    a = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            a += 1
        except(TypeError, ValueError):
            None
        except IndexError:
            raise
    print()
    return a

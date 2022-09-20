#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''Prints a dictionary by ordered keys'''
    for row in sorted(a_dictionary):
        for key, item in a_dictionary.items():
            if key == row:
                print("{}: {}".format(key, item))

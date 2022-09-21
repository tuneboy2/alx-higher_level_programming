#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''Deletes keys with a specific value in a dictionary

        If the value doesn’t exist, the dictionary won’t change
    '''
    new = [key for key, item in a_dictionary.items() if item == value]
    for no in range(len(new)):
        del(a_dictionary[new[no]])
    return a_dictionary

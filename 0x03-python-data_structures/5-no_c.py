#!/usr/bin/python3

def no_c(my_string):
    '''Removes all characters c and C from a string.'''

    if my_string is None:
        return

    new = list(my_string)

    i = 0
    for ch in my_string:
        if ch == 'c' or ch == 'C':
            new[i:i + 1] = ''
            continue
        i += 1

    return ''.join(new)

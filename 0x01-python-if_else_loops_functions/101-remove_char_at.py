#!/usr/bin/python3
# Author - Oladapo Olatunbosun

def remove_char_at(st, n):
    string = st[:]
    string = list(string)
    if n > len(string) or n < 0:
        string = ''.join(string)
    else:
        string[n] = ""
        string = ''.join(string)
    return string

# Author - bamidele Adefolaju
"""
def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
    """

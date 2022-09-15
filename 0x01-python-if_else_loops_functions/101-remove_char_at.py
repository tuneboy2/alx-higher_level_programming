#!/usr/bin/python3
def remove_char_at(st, n):
    string = st[:]
    string = list(string)
    if n > len(string) or n < 0:
        string = ''.join(string)
    else:
        string[n] = ""
        string = ''.join(string)
    return string

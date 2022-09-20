#!/usr/bin/python3
# Author - Oladapo Olatunbosun

""" The ord() function returns the number representing the unicode code of a
specified character.

The chr() function returns the character that represents the specified unicode.

Prints the alphabetical letters in lowercase, not fillowed by a new line """
for c in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(c)), end='')

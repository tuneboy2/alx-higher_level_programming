#!/usr/bin/python3
# Author - Oladapo Olatunbosun

for c in range(ord('a'), ord('z') + 1):
    if (c != ord('q')) and (c != ord('e')):
        print("{}".format(chr(c)), end='')

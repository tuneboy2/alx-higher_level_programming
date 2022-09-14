#!/usr/bin/python3
# Author - Oladapo Olatunbosun

""" Prints numbers from 0 to 99 """
for no in range(100):
    if no == 99:
        print("{}".format(no))
        break
    print("{}, ".format(no), end='')

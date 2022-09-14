#!/usr/bin/python3
# Author - Oladapo Olatunbosun

for number in range(10):
    for no in range(number + 1, 10):
        if number == 10 - 2:
            print("{}{}".format(number, no))
        else:
            print("{}{}".format(number, no), end=', ')

#!/usr/bin/python3
# Author - Oladapo Olatunbosun

""" Prints whether the number stored in the variable number is positive or negative """
import random
number = random.randint(-10, 10)
if number < 0:
    print(number, 'is negative')
elif number > 0:
    print("{} is positive".format(number))
else:
    print(f'{number} is zero')

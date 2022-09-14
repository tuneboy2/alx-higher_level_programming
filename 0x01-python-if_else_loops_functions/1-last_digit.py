#!/usr/bin/python3
# Author - Oladapo Olatunbosun

""" Prints the last digit of the number stored in the variable number """
import random
number = random.randint(-10000, 10000)
no = abs(number) % 10
if number < 0:
    no = -no

if no > 5:
    print(f"Last digit of {number} is {no} and is greater than 5")
elif no == 0:
    print("Last digit of {} is 0 and is 0".format(no))
else:
    print(f"Last digit of {number} is {no} and is less than 6 and not 0")

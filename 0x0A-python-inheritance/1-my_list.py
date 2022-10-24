#!/usr/bin/python3
""" Module defining a class Mylist"""


class MyList(list):
    """ A class Mylist that inherits the mrthods of its Superclass 'list'"""
    def print_sorted(self):
        """ prints the list in a sorted ascending order"""
        print(sorted(self)

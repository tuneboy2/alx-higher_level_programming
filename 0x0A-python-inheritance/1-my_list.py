#!/usr/bin/python3
""" Module defining a class Mylist"""


class MyList(list):
    """ A class Mylist that inherits the mrthods of its Superclass 'list'"""
    def printed_sorted(self):
        """ prints the list in a sorted ascending order"""
        new = self.copy()
        new.sort()
        print(new)

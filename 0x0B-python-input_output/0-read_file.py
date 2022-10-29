#!/usr/bin/python3
""" Defines a Function that reads a File """


def read_file(filename=""):
    """ Reads a File """
    with open(filename, encoding="utf-8") as readFile:
        print(readFile.read(), end='')

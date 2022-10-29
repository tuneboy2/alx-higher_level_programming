#!/usr/bin/python3
""" Defines a Function that Appends to a File"""


def append_write(filename="", text=""):
    """ Appends a Text to a File, It creates a new file if filename does not exist

    Args:
        filenane (str): The nane of the File
        text (str): Text to be appended
    """
    with open(filename, mode="a", encoding="utf-8") as File:
        return File.write(text)

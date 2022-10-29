#!/usr/bin/python3
""" Defines a Write Function"""


def write_file(filename="", text=""):
    """ Writes a text into a File

    Args:
        filename (str): The name of the File.
        text (str): The string to be inserted in the File
    """
    with open(filename, mode="w", encoding="utf-8") as File:
        return File.write(text)

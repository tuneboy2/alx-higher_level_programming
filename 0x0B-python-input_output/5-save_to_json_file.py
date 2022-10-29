#!/usr/bin/python3
""" Defines a function that serializes an object into a file"""


import json


def save_to_json_file(my_obj, filename):
    """ Converts an Object to Json string and saves it in a file

    Args:
        my_obj: Object to be converted
        filename: File JSON string is saved to
    """
    with open(filename, mode="w", encoding="utf-8") as File:
        json.dump(my_obj, File)

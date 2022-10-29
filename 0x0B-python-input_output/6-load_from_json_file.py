#!/usr/bin/python3
""" Defines a Function that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """ Creates an object from q JSON file

    Args:
        filename: The json file
    """
    with open(filename, encoding="utf-8") as File:
        return json.load(File)

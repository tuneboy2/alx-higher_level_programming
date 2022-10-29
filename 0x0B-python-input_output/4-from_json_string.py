#!/usr/bin/python3
""" Defines a Function for Deserializing"""


import json


def from_json_string(my_str):
    """ Converts a JSON string to an object

    Args:
        my_str: json string to be converted
    """
    return json.loads(my_str)

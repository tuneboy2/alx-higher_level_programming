#!/usr/bin/python3
""" Defines a Function that serializes an object"""


import json


def to_json_string(my_obj):
    """ Converts an object to JSON string

    Args:
        my_obj: object to be converyed
    """
    return json.dumps(my_obj)

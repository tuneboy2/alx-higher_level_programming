#!/usr/bin/python3
""" Defines a Function that serializes an object"""


import json


def to_json_string(my_obj):
    return json.dumps(my_obj)

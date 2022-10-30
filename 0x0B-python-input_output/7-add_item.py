#!/usr/bin/python3
""" Defines a Module that adds all arguments of the python list, and
    saves in a file """


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
new = []
try:
    old = load_from_json_file(filename)
    for i in range(1, len(sys.argv)):
        old.append(sys.argv[i])

    save_to_json_file(old, filename)
except Exception:
    save_to_json_file(new, filename)

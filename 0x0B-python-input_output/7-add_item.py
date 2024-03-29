#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
arguments = sys.argv[1:]

if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(arguments)
save_to_json_file(my_list, filename)

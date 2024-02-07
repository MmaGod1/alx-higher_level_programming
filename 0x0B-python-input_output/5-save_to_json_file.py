#!/usr/bin/python3
"""Defines a JSON function that writes to a file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)

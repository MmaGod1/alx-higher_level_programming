#!/usr/bin/python3
"""Defines a JSON function tha reads a file."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as file:
        return json.load(file)

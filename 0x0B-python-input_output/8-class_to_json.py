#!/usr/bin/python3
"""Defines a Python JSON serialization of an object function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__

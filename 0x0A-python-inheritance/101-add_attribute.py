#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        attribute: The name of the attribute to add.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")

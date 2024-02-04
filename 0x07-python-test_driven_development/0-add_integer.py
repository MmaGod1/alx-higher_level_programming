#!/usr/bin/python3
"""Defines an additive function"""


def add_integer(a, b=98):

    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    # Cast a and b to integers if they are floats
    return (int(a) + int(b))

#!/usr/bin/python3
"""Defines a function to print the name with the specified full name"""


def say_my_name(first_name, last_name=""):
    """
    Print the name with the specified first and last name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed. Defaults to "".

    Returns:
        None

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # Print the name
    print("My name is {} {}".format(first_name, last_name))

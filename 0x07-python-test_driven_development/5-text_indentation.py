#!/usr/bin/python3
"""Defines a function to print text with indentation."""


def text_indentation(text):
    """
    Print text with indentation.

    Args:
        text (str): The text to be printed.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define characters to split the text
    split_chars = ['.', '?', ':']

    # Initialize an empty line
    new_line = ""

    # Print text with indentation
    for char in text:
        new_line += char
        if char in split_chars:
            print(new_line.strip())
            print()
            # Reset the line
            new_line = ""

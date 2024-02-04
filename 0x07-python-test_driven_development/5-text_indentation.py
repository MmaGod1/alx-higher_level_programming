#!/usr/bin/python3
"""Defines a function to print text with indentation."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if type(text) is not str:
        raise TypeError("Input must be a string")

    index = 0

    # Skip leading spaces
    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end='')

        if text[index] in ['.', '?', ':']:
            print('\n\n', end='')
        elif text[index] == '\n':
            # Ensure no space at the beginning of the line after newline
            print("", end='')
        index += 1

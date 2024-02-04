#!/usr/bin/python3
"""Defines a function to print text with indentation."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0

    while index < len(text):
        # Skip leading spaces
        while index < len(text) and text[index] == ' ':
            index += 1

        # Check if we've reached the end of the text
        if index == len(text):
            break

        print(text[index], end='')

        # Check for newline or specified punctuation marks
        if text[index] in ['.', '?', ':']:
            print('\n\n', end='')
            index += 1
        elif text[index] == '\n':
            print("", end='')
            index += 1
        else:
            index += 1

#!/usr/bin/python3
"""Defines a function to print text with indentation."""


def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define characters to split the text
    split_chars = ['.', '?', ':']

    # Iterate through the text
    for char in text:
        # Print characters without space at the beginning
        if char != ' ':
            print(char, end='')
        
        # Print newline if the character is a split character
        if char in split_chars:
            print('\n')
        elif char == '\n':
            # Ensure no space at the beginning of the line after newline
            print("", end='')

# Test the function
text = "This is a test. Hello, how are you? I'm fine, thank you."
text_indentation(text)

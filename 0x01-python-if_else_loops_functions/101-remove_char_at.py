#!/usr/bin/python3
def remove_char_at(s, n):
    new_string = ""
    for i in range(len(s)):
        if i != n:
            new_string += s[i]
    return new_string

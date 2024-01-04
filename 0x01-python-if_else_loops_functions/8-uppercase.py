#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            new_string += chr(ord(s[i]) - (ord('a') - ord('A')))
        else:
            new_string += s[i]
        print("{}".format(new_string), end='')

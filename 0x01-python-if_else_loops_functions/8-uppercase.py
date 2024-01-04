#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in range(len(str)):
        if 'a' <= str[i] <= 'z':
            new_string += chr(ord(str[i]) - (ord('a') - ord('A')))
        else:
            new_string += str[i]
        print("{}".format(new_string))

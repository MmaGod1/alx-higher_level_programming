#!/usr/bin/python3
"""
sends a POST request to a URL with an email parameter, displays the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    req = {'email': email}
    response = requests.post(url, data=req)
    print(response.text)

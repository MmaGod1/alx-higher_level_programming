#!/usr/bin/python3
"""
This module uses the GitHub API to display the user's
id using Basic Authentication with a personal access token.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    headers = {'Authorization': f'token {token}'}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        user_id = data.get('id')
        print(user_id)
    else:
        print(None)

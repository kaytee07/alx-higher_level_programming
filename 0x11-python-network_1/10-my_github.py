#!/usr/bin/python3
"""
script takes credentials and uses API to display id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

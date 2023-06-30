#!/usr/bin/python3
"""
python script that takes in a URL, sends a request to the URL 
and displays the body of the response
"""


import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf8'))
    except HTTPError as e:
        print('Error code:', e.code)

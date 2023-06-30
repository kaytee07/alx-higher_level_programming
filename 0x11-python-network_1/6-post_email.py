#!/usr/bin/python3
"""send a post request with email pareams and print body"""

import requests
import sys

if __name__ == '__main__':
    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print('Your email is:', res)

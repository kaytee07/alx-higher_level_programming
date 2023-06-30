#!/usr/bin/python3
""" send request and retrieve X-Request-Id"""

import requests
import sys

if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))

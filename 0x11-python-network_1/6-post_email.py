#!/usr/bin/python3
"""send a post request with email pareams and print body"""

import requests
import sys

value = sys.argv[2]
url = sys.argv[1]
res = requests.post(url, data={'key': value})
print(res)

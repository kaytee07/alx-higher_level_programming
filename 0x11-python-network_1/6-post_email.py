#!/usr/bin/python3
"""send a post request with email pareams and print body"""

import requests
import sys

url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}
res = requests.post(url, data=data)
print(res.text)

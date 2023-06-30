#!/usr/bin/python3
"""Get the value of X-Request-Id from header"""


import sys
import urllib.request

if not sys.argv[1]:
    print('<Usage>: Enter URL')
with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.getheader("X-Request-Id")
print(x_request_id)

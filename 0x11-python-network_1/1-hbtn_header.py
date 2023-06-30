#!/usr/bin/python3
"""Get the value of X-Request-Id from header"""
import sys
import urllib.request


url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    x_request_id = response.getheader("X-Request-Id")
print(x_request_id)

#!/usr/bin/python3
"""pass email as POST parameter to url and display body"""


import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    mail = sys.argv[2]
    body = {'email': mail}
    params = urllib.parse.urlencode(body).encode('ascii')
    req = urllib.request.Request(url, body)
    with urllib.request.urlopen(req) as response:
        res = response.read().decode('utf-8')
    print(res)

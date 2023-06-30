#!/usr/bin/python3
"""write pythn script that fetches response from url"""


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
utf8 = html.decode("utf-8")
print("Body response:")
print("\t- type:", type(html))
print("\t- content:", html)
print("\t- utf8 content:", utf8)

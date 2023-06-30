#!/usr/bin/python3
"""
script send letter parameter tohttp://0.0.0.0:5000/search_user
"""
import sys
import requests

if __name__ == "__main__":
    args = "" if len(sys.argv) == 1 else sys.argv[1]
    params = {"q": args}

    req = requests.post("http://0.0.0.0:5000/search_user", data=params)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

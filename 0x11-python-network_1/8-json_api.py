#!/usr/bin/python3
"""
a script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {'q': q}
    req = requests.post(url, data=data)
    try:
        json_req = req.json()
        if 'id' in json_req and 'name' in json_req:
            print("[{}] {}".format(json_req['id'], json_req['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

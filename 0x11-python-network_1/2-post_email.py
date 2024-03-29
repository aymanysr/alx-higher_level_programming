#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the URL with the email as a parameter,
and finally displays the body of the response.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

#!/bin/bash
# This script takes in a URL, sends a GET request to the URL using curl, and displays the body of the response for a 200 status code only
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q 200 && curl -sL "$1"


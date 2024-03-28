#!/bin/bash
# This script takes in a URL, sends a GET request to the URL using curl, and displays the body of the response for a 200 status code only

curl -s -X GET "$1" -D - | awk 'NR==1 {if ($2 == 200) print} NR>1'


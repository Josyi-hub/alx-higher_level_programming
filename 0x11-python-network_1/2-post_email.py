#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded
in utf-8)
"""

import sys
import urllib.request as request
import urllib.parse as parse

url = sys.argv[1]
email = sys.argv[2]
values = {'email': email}

data = parse.urlencode(values)
data = data.encode('ascii')
req = request.Request(url, data)

with request.urlopen(req) as response:
    print(response.read().decode('utf-8'))

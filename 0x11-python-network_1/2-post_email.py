#!/usr/bin/python3
# task2
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
values = {'email': sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode())

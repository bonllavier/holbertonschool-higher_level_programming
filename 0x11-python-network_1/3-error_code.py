#!/usr/bin/python3
# task3
import urllib.request
import sys

if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

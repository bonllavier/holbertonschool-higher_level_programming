#!/usr/bin/python3
# task4
import requests
import sys

if __name__ == '__main__':
    if sys.argv[1] is not None:
        r = requests.get(sys.argv[1])
        print(r.headers.get('X-Request-Id'))

#!/usr/bin/python3
# task6
import requests
import sys

if __name__ == '__main__':
    value = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=value)
    print(r.text)

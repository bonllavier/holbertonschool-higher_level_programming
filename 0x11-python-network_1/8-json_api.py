#!/usr/bin/python3
# task4
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    value = {'q': q}
    req = requests.post(url, data=value)
    try:
        if not req.json():
            print("No result")
        else:
            print("[{}] {}".format(
                req.json().get('id'),
                req.json().get('name')))
    except ValueError:
        print("Not a valid JSON")

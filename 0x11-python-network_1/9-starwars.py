#!/usr/bin/python3
# task8
import sys
import requests

if __name__ == '__main__':
    url1 = 'https://swapi.co/api/people/?search=' + str(sys.argv[1])
    req = requests.get(url1)
    try:
        print("Number of results: {}".format(req.json().get('count')))
        for item in req.json().get('results'):
            print(item.get('name'))
    except ValueError:
        print("Not a valid JSON")

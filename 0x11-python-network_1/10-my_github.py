#!/usr/bin/python3
# task 10
import sys
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = str(sys.argv[1])
    passw = sys.argv[2]
    req = requests.get(url, auth=(user, passw))
    print(req.json().get('id'))

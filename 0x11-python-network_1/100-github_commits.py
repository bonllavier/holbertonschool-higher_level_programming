#!/usr/bin/python3
# task adavance 11
import sys
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    req = requests.get(url)
    content = req.json()
    cont = 0
    for item in content:
        if cont < 10:
            print(item['sha'] + ': ' + item['commit']['author']['name'])
            cont += 1

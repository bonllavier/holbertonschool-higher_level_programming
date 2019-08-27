#!/usr/bin/python3
# task4
import requests

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(
        type(r.text), r.text))

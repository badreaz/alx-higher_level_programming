#!/usr/bin/python3
""" sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response """

from urllib import request
from sys import argv


if __name__ == '__main__':
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        header = dict(response.headers).get("X-Request-Id")
        print(header)

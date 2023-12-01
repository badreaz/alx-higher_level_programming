#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8) """

from urllib import request
from urllib import parse
from sys import argv


if __name__ == '__main__':
    email = {"email": argv[2]}
    data = parse.urlencode(email).encode("ascii")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)

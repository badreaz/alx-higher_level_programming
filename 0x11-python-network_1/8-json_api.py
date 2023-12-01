#!/usr/bin/python3
""" takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a paramete """

import requests
from sys import argv


if __name__ == '__main__':
    if (len(argv) == 1):
        q = ""
    else:
        q = argv[2]
    value = {"q": q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        result = r.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except ValueError:
        print("Not a valid JSON")

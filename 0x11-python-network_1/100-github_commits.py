#!/usr/bin/python3
""" solve the challenge """

import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(argv[2], argv[1]))
    dic = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(dic[i].get("sha"), dic[i]
                                  .get("commit").get("author").get("name")))
    except IndexError:
        pass

#!/usr/bin/python3
""" reads stdin line by line and computes metrics """
import sys


size = 0
lnum = 1
vcodes = ['200', '301', '400', '401', '403', '404', '405', '500']
codes = {}

try:
    for line in sys.stdin:
        if lnum == 10:
            print("File size: {}".format(size))
            for k in sorted(codes):
                print("{}: {}".format(k, codes[k]))
            lnum = 1
        else:
            lnum += 1

        line = line.split()

        try:
            size += int(line[-1])
        except (IndexError, ValueError):
            pass

        try:
            if line[-2] in vcodes:
                if not codes.get(line[-2]):
                    codes[line[-2]] = 1
                else:
                    codes[line[-2]] += 1
        except IndexError:
            pass

    print("File size: {}".format(size))
    for key in sorted(codes):
        print("{}: {}".format(key, codes[key]))

except KeyboardInterrupt:
    print("File size: {}".format(size))
    for k in sorted(codes):
        print("{}: {}".format(k, codes[k]))
    raise

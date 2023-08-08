#!/usr/bin/python3
for i in range(100):
    print("{}{:02d}".format(", " if i > 0 else "", i), end="")
print()

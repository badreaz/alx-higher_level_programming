#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        print(f"{value} is not an integer")
        return False

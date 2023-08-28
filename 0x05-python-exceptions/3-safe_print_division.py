#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ans = a / b
    except ZeroDivisionError:
        ans = None
    finally:
        print("Inside result: {:d}".format(ans))
        return ans

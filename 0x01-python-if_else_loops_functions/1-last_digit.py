#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 0
if number < 0:
    number = number * -1
    sign = 1

if number % 10 > 5:
    print(f"Last digit of {number} is {"-" if sign == 1}{number % 10} "
    "and is greater than 5")
elif number % 10 == 0:
    print(f"Last digit of {number} is 0 and is 0")
else:
    print(f"Last digit of {number} is {"-" if sign == 1}{number % 10} "
    "and is less than 6 and not 0")


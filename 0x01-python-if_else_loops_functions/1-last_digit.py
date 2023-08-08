#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = last * -1

if number % 10 > 5:
    print(f"Last digit of {number:d} is {last:d} and is greater than 5")
elif number % 10 == 0:
    print(f"Last digit of {number:d} is 0 and is 0")
else:
    print(f"Last digit of {number} is {last:d} and is less than 6 and not 0")

#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    values = []
    roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    if not roman_string or type(roman_string) != str:
        return 0
    for c in roman_string:
        values.append(roman_int[c])
    for i in range(len(values) - 1):
        if values[i] >= values[i + 1]:
            num += values[i]
        else:
            num -= values[i]
    num += values[-1]
    return num

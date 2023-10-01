#!/usr/bin/python3
""" text_indentation definition module """


def text_indentation(text):
    """ prints a text with 2 new lines after each
    of these characters '.', '?' and ':'
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for c in text:
        if c in ['.', '?', ':']:
            result += c + "\n\n"
            space = False
        elif c == ' ' and space:
            result += c
        elif c != ' ':
            result += c
            space = True
    print(result.strip(), end='')

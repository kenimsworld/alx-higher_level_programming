#!/usr/bin/python3
"""
Contains the function "append_write"
"""


def append_write(filename="", text=""):
    """function that appends a string to a text file and return the number
    of characters added"""
    with open(filename, 'a', encoding='utf=8') as fil:
        return fil.write(text)

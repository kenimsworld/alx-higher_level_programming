#!/usr/bin/python3
"""
Contains the function that writes to a file
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file and return the number
    of characters written"""
    with open(filename, 'w', encoding='utf=8') as fil:
        return fil.write(text)

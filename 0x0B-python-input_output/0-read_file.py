#!/usr/bin/python3
"""
contians the read_file function
"""

def read_file(filename=""):
    """reads a UTF8 text file and print it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

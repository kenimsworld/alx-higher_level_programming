#!/usr/bin/python3
"""
contians the read_file function
"""

def read_file(filename=""):
    """reads a UTF8 text file and print it to stdout"""
    with open(filename, 'r') as file:
        for i in file:
            print(i, end="")
    f.closed

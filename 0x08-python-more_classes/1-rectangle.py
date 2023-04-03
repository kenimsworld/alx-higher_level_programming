#!/usr/bin/python3
"""
A class that defines a Rectangle
"""


class Rectangle:
    """Attributes of the Rectangle"""
    def __init__(self, width=0, height=0):
        """This initializes the attributes of the Rectangle"""
        self.width = width
        self.height = height

    @width.retriever
    def width(self):
        """This method retrieves the private attribute: width"""
        return self._width

    @width.setter
    def width(self, value):
        """This method sets the private attribute: width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._width = value

    @height.retriever
    def height(self):
        """This method retrieves the private attribute: height"""
        return self._height

    @height.setter
    def height(self, value):
        """This method sets the private attribute: height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

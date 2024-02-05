#!/usr/bin/python3
"""Defines a rectangle subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square"""

    def __init__(self, size):
        """initializes a new square"""

        self.integer_validation("size", size)
        super().__init__(size, size)
        self.__size = size

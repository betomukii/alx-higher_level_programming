#!/usr/bin/python3
"""this module defines a rectangle subclass square"""
Rectangle = __import__('9-rectangle'). Rectangle


class Square(Rectangle):
    """represent a square"""

    def __init__(self, size):
        """initializes a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

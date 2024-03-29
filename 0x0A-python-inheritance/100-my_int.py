#!/usr/bin/python3
"""A module that defines a class MyInt that inherits from int"""


class MyInt(int):
    """invert int operators == and !="""

    def __eq__(self, value):
        """Override == operator with != behaviour"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behaviour"""
        return self.real == value

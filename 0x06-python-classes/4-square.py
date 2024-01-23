#!/usr/bin/python3

"""a module that defines a square """

class Square:
    """ a class rep square """

    def __init__(self, size=0):
        """initializing the square class
        args:
            size: rep the size of the square defined
        raises:
            TypeError: if the size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    self.__size = size

    @property
    def size(self):
        """retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must ba an integer")
        if value < 0:
            raise VlueError("size must be >= 0")
        self.__size = value

    def arae(self):
        """
        calculate area of the square
        Returns: the square of the size
        """


        return (self.__size ** 2)



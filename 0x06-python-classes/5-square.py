#!/usr/bin/python3

"""a module defining square """


class Square:
    """a class repr square """

    def __init__(self, size=0):
        """initializing square class
        Args:
        size: repr the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @prperty
    def size(self):
        """retrieves size of square """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise Vlue Error("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculate area of the square
        returns: the square of the size
        """

        return (self.__size ** 2)

    def my_print(self):
        """print the square in #"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)

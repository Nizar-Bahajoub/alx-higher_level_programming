#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Defines a square

    Attributes:
        __size (int): private instance size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initiation of the class
        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retreive size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size"""
        if type(value) is int:
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set position"""
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        self.__position = value
                    else:
                        raise ValueError("position must be a tuple of 2 positive integers")
                else:
                    raise TypeError("position must be a tuple of 2 positive integers")
            else:
                raise IndexError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integer")

    def area(self):
        """Area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

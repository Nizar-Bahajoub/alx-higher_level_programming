#!/usr/bin/python3
import math


class MagicClass:
    def __init__(self, radius):
        self.__radius = None
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return (self.__radius * 2 * math.pi)

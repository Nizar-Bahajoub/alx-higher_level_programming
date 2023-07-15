#!/usr/bin/pyhton3
"""BaseGeometry Class"""


class BaseGeometry:
    """Not Defined"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """Initialization a new Rec

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validtor("height", height)
        self.__height = height

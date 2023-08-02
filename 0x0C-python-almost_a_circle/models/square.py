#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialisation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string format"""
        my_list = "[" + str(self.__class__.__name__) + "]"
        my_list += " (" + str(self.id) + ") " + str(self.x) + "/" + str(self.y)
        my_list += " - " + str(self.width)
        return (my_list)

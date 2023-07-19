#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict representaion of Student"""
        if (type(attrs) == list and
                all(type(a) == str for a in attrs)):
            return ({att: getattr(self, att) for att in attrs
                    if sattr(self, att)})
        return (self.__dict__)

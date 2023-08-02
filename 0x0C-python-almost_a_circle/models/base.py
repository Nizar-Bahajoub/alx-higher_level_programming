#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """Base Class definition

    Attributes:
        nb_objects (private): the number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        list_to_dic = []
        filename = "{}.json".format(cls.__name__)

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_to_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_to_dic)

        with open(filename, "w") as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dum = cls(10, 10)
        else:
            dum = cls(10)
        dum.update(**dictionary)
        return (dum)

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

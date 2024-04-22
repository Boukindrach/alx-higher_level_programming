#!/usr/bin/python3

"""Defines a base model class."""
import json


class Base:
    """Represents the base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries or list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return ("[]")

    @classmethod
    def save_to_file(cls, list_objs):

        filename = cls.__name__ + ".json"

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

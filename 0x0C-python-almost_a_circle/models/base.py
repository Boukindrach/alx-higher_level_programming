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

    def from_json_string(json_string):
        """Return the deserialization of a JSON string."""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                out = cls(1, 1)
        else:
            out = cls(1)
        out.update(**dictionary)
        return out

    @classmethod
    def load_from_file(cls):

        filename = "{}.json".format(cls.__name__)

        try:
            with open (filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                list_instances = []
                
                for i in list_dicts:
                    list_instances.append(cls.create(**i))
                return list_instances
        except FileNotFoundError:
            return []

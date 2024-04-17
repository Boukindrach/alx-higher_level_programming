#!/usr/bin/python3

"""Defines a Student class."""


class Student:
    """Represent a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert the Student instance to a dictionary.

        Args:
            attrs (list, optional): List of attributes to include in the dictionary.
        
        Returns:
            dict: A dictionary representation of the student's attributes.
        """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Update the Student instance with attributes from a dictionary.

        Args:
            json (dict): A dictionary containing attribute key/value pairs.
        """
        for key, value in json.items():
            setattr(self, key, value)

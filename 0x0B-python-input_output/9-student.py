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

    def to_json(self):
        """Convert the Student instance to a dictionary.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return self.__dict__

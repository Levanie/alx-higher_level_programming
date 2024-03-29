#!/usr/bin/python3
"""contains the class "student" """

class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a student instance with specified attributes"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributesvof the student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass

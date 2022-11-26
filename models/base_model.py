#!/usr/bin/python3
"""This is the base(mdoel) class for the project"""


from datetime import datetime
from uuid import uuid4


class BaseModel(object):
    """
    Sets attributes and methods
    required by the base model
    Attributes
        __init__(self, *args, **kwargs)
        __str__(self)
        save(self)
        to_dict(self)
    """

    def __init__(self):
        """Initializes the base model"""
        self.id = str(uuid4)
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):

        """Returns the string user
            readable format of
            an object
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

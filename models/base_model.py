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
    
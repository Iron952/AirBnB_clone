# This is a Base class where all other classes inherit from, we import uuid for random IDs and datetime 
import uuid
from datetime import datetime


class BaseModel:
    """
    This is the base class that defines all common attributes/Methods for other classes
    Attr: id - string
         created_at - datetime asigned when the instance is created
         updated_at - datetime asigned when the instance is updated
    """
    name = str()
    my_number = int()
    id = str(uuid.uuid4())
    created_at = str(datetime.now())
    updated_at = str(datetime.now())


    def __init__(self):
        pass

    """
    Function __str__ prints the readable format of the object
    :param : self
    :return : string with class name , id and __dict__
    """
    def __str__(self):
        return '[BaseModel] ({}) {}'.format(self.id, self.__dict__)

    """
    This Function save() - Updates the updated variable
    :param : self object
    """
    def save(self):
        self.updated_at = str(datetime.now())

    """
    This Fucntion to_dict() - Returns a dictionary of the instance
    :param : self object
    """
    def to_dict(self):
        return {
            'my_number': self.my_number,
            'name': self.name,
            '__class__': 'BaseModel',
            'updated_at':self.updated_at,
            'id': self.id,
            'created_at': self.created_at
        }

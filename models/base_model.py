#!/usr/bin/python3^M

from uuid import uuid4
from datetime import datetime

class BaseModel:
   
	def __init__(self):
		"""make a random UUID in this case uuid4: Generate a random UUID"""
		self.id = str(uuid4())
		"""created_at: datetime - assign with the current datetime when an instance is created"""
		self.created_at = datetime.today()
		"""updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object"""
		self.updated_at = datetime.today()
	
	""" __str__: should print: [<class name>] (<self.id>) <self.__dict__>"""
	def __str__(self):
		return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

	def save(self):
		"""save(self): updates the public instance attribute updated_at with the current datetime"""
		return self.updated_at

	def to_dict(self):
		""" returns a dictionary containing all keys/values of __dict__ of the instance:"""
		
		dic = self.__dict__
		dic['__class__'] = cls.__name__
		dic['created_at'] = self.created_at.isoformat()
		dic['updated_at'] = self.updated_at.isoformat()
		return dic
		"""
		* by using self.__dict__, only instance attributes set will be returned 
		* a key __class__ must be added to this dictionary with the class name of the object
		* created_at and updated_at must be converted to string object in ISO format
		** format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
		** you can use isoformat() of datetime object
		* This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
		"""
		
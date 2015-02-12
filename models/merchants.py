import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

from base import BaseModel
from peewee import *

class Merchants(BaseModel):
	id = PrimaryKeyField()
	mid = TextField(unique = True)
	name = TextField()

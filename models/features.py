import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

from base import BaseModel
from comments import Comments
from peewee import *

class Features(BaseModel):
	id = PrimaryKeyField()
	commentId = ForeignKeyField(Comments)
	type = CharField()
	feature = CharField()
	frequency = IntegerField()

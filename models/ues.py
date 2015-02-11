import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

from base import BaseModel
from comments import Comments
from merchants import Merchants
from peewee import *

class UEs(BaseModel):
	id = PrimaryKeyField()
	commentId = ForeignKeyField(Comments)
	merchantId = ForeignKeyField(Merchants)
	UE = CharField()
	frequency = IntegerField()

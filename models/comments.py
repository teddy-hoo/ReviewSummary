import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

from base import BaseModel
from merchants import Merchants
from peewee import *

class Comments(BaseModel):
	id = PrimaryKeyField()
	merchantId = ForeignKeyField(Merchants)
	raw = TextField()
	clean = TextField()
	segmented = TextField()
	posed = TextField()
	mergedNouns = TextField()
